"""Open-weights models for the pi harness, served by vLLM on Modal.

    modal deploy pi_harness/modal_vllm.py

Two OpenAI-compatible endpoints, one H100 each, scaled to zero after 10 idle
minutes:

  qwen   Qwen/Qwen3.8-27B-FP8    27.8B dense, the "small model" arm (<50B)
  gptoss openai/gpt-oss-120b     117B MoE, the "large model" arm

Every request needs the bearer key in pi-agent/vllm_key (created on first
deploy, gitignored); pi reads it through models.json (`!cat ...`). Serving
flags follow the vLLM recipes: the reasoning parser keeps the thinking out of
message.content, and the tool-call parser turns the model's native tool
syntax into OpenAI tool_calls, which pi needs.
"""

import secrets
import subprocess
from pathlib import Path

import modal

KEY_FILE = Path(__file__).resolve().parent / "pi-agent" / "vllm_key"
if not KEY_FILE.is_file():
    KEY_FILE.parent.mkdir(parents=True, exist_ok=True)
    KEY_FILE.write_text(secrets.token_urlsafe(32))
    KEY_FILE.chmod(0o600)

VLLM = "0.30.0"
image = (
    modal.Image.from_registry("nvidia/cuda:12.9.1-devel-ubuntu22.04", add_python="3.12")
    .entrypoint([])
    .uv_pip_install(f"vllm=={VLLM}", "huggingface_hub[hf_transfer]", "transformers>=5.8.0")
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1", "VLLM_USE_V1": "1"})
)
hf_cache = modal.Volume.from_name("huggingface-cache", create_if_missing=True)
vllm_cache = modal.Volume.from_name("vllm-cache", create_if_missing=True)
key = modal.Secret.from_dict({"VLLM_API_KEY": KEY_FILE.read_text().strip()})

app = modal.App("ale-pi-harness-vllm")

COMMON = dict(
    image=image,
    gpu="H100",
    scaledown_window=10 * 60,
    timeout=24 * 60 * 60,
    volumes={"/root/.cache/huggingface": hf_cache, "/root/.cache/vllm": vllm_cache},
    secrets=[key],
)


def _serve(model: str, extra: list[str]) -> None:
    cmd = ["vllm", "serve", model, "--host", "0.0.0.0", "--port", "8000",
           "--enable-prefix-caching", "--enable-auto-tool-choice",
           # vLLM defaults to 1024 sequences; Qwen3.8's linear-attention (Mamba)
           # cache has room for ~855, so startup fails. Agents need at most ~16.
           "--max-num-seqs", "32", *extra]
    # The key comes from the secret's environment, not argv.
    subprocess.Popen(" ".join(cmd) + ' --api-key "$VLLM_API_KEY"', shell=True)


# Four agents per GPU and up to three GPUs: one H100 gave nine agents about
# 24 tokens/s each, so a plain-arm answer took 15-30 minutes.
@app.function(**COMMON, max_containers=3)
@modal.concurrent(max_inputs=4)
@modal.web_server(port=8000, startup_timeout=30 * 60)
def qwen():
    _serve("Qwen/Qwen3.8-27B-FP8", [
        "--served-model-name", "qwen3.8-27b",
        "--max-model-len", "262144", "--kv-cache-dtype", "fp8",
        "--language-model-only",
        "--reasoning-parser", "qwen3", "--tool-call-parser", "qwen3_xml",
        # The checkpoint's own multi-token-prediction head (vLLM recipe).
        "--speculative-config", "'{\"method\":\"mtp\",\"num_speculative_tokens\":3}'",
    ])


@app.function(**COMMON)
@modal.concurrent(max_inputs=16)
@modal.web_server(port=8000, startup_timeout=30 * 60)
def gptoss():
    _serve("openai/gpt-oss-120b", [
        "--served-model-name", "gpt-oss-120b",
        "--max-model-len", "131072",
        "--reasoning-parser", "openai_gptoss", "--tool-call-parser", "openai",
    ])
