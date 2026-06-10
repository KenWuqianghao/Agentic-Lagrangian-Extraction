const form = document.getElementById("search-form");
const statusEl = document.getElementById("status");
const resultEl = document.getElementById("result");
const runnersEl = document.getElementById("runners");
const metaEl = document.getElementById("meta");
const submitBtn = document.getElementById("submit-btn");

function show(el) {
  el.classList.remove("hidden");
}

function hide(el) {
  el.classList.add("hidden");
}

function setStatus(message, type = "loading") {
  statusEl.textContent = message;
  statusEl.className = `status ${type}`;
  show(statusEl);
}

function paperHtml(paper, heading) {
  const year = paper.published ? paper.published.slice(0, 4) : "—";
  const breakdown = Object.entries(paper.score_breakdown || {})
    .map(([k, v]) => `${k}: ${Number(v).toFixed(3)}`)
    .join(", ");

  const links = [];
  if (paper.abs_url) links.push(`<a href="${paper.abs_url}" target="_blank" rel="noopener">arXiv</a>`);
  if (paper.inspire_id) {
    links.push(
      `<a href="https://inspirehep.net/literature/${paper.inspire_id}" target="_blank" rel="noopener">INSPIRE</a>`
    );
  }

  return `
    ${heading ? `<h2 class="result-title">${heading}</h2>` : ""}
    <p class="paper-title">${escapeHtml(paper.title)}</p>
    <dl>
      <dt>arXiv</dt><dd>${paper.arxiv_id || "—"}</dd>
      <dt>INSPIRE</dt><dd>${paper.inspire_id ?? "—"}</dd>
      <dt>INSPIRE cites</dt><dd>${paper.citation_count}</dd>
      <dt>Year</dt><dd>${year}</dd>
      <dt>Score</dt><dd>${paper.score.toFixed(4)}</dd>
      ${breakdown ? `<dt>Breakdown</dt><dd>${breakdown}</dd>` : ""}
      ${paper.text_path ? `<dt>Text</dt><dd>${escapeHtml(paper.text_path)}</dd>` : ""}
    </dl>
    ${links.length ? `<div class="links">${links.join(" · ")}</div>` : ""}
  `;
}

function escapeHtml(text) {
  return text
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  submitBtn.disabled = true;
  hide(resultEl);
  hide(runnersEl);
  hide(metaEl);
  setStatus("Searching INSPIRE, arXiv, and ADS…");

  const data = new FormData(form);
  const body = {
    model_name: data.get("model_name"),
    keywords: data.get("keywords") || "",
    exclude_keywords: data.get("exclude_keywords") || "",
    authors: data.get("authors") || "",
    exclude_authors: data.get("exclude_authors") || "",
    since: data.get("since") || null,
    until: data.get("until") || null,
    sort: data.get("sort"),
    search_mode: data.get("search_mode"),
    theory_only: data.get("theory_only") === "on",
    use_ads: data.get("use_ads") === "on",
    require_abstract: data.get("require_abstract") === "on",
    abstract_keyword_match: data.get("abstract_keyword_match") === "on",
    semantic_scope: data.get("semantic_scope") || "combined",
    probe_latex_source: data.get("probe_latex_source") === "on",
    runners_up: Number(data.get("runners_up") || 0),
    download_pdfs: data.get("download_pdfs") === "on",
    extract_text: data.get("extract_text") === "on",
  };

  try {
    const response = await fetch("/api/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const payload = await response.json();
    if (!response.ok) {
      throw new Error(payload.detail || "Search failed");
    }

    hide(statusEl);

    if (payload.selected_paper) {
      resultEl.innerHTML = paperHtml(payload.selected_paper, "Selected paper");
      show(resultEl);
    } else {
      setStatus("No suitable paper found.", "error");
    }

    if (payload.runners_up?.length) {
      runnersEl.innerHTML =
        "<h2 class=\"result-title\">Runners-up</h2><ul class=\"runner-list\">" +
        payload.runners_up
          .map(
            (paper, i) =>
              `<li><strong>#${i + 2}</strong> ${escapeHtml(paper.title)} ` +
              `(${paper.arxiv_id || "no arXiv"}, ${paper.citation_count} INSPIRE cites, score ${paper.score.toFixed(3)})</li>`
          )
          .join("") +
        "</ul>";
      show(runnersEl);
    }

    let meta =
      `Pool: ${payload.pool_searched} papers · INSPIRE: ${payload.inspire_hits} · arXiv: ${payload.arxiv_hits} · ADS: ${payload.ads_hits}`;
    if (payload.latex_probe) {
      const lp = payload.latex_probe;
      meta += `<br>LaTeX: available=${lp.available}, format=${lp.format}, main=${lp.main_tex || "—"}`;
    }
    meta += `<br>Audit log: ${escapeHtml(payload.audit_log)}`;
    metaEl.innerHTML = meta;
    show(metaEl);
  } catch (err) {
    setStatus(err.message || "Something went wrong.", "error");
  } finally {
    submitBtn.disabled = false;
  }
});
