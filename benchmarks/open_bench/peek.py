"""Print the tool calls and errors of one or more opencode JSON streams."""
import json, sys
for f in sys.argv[1:]:
    n = 0
    print("==", f)
    for l in open(f, errors="replace"):
        try:
            e = json.loads(l)
        except Exception:
            continue
        n += 1
        p = e.get("part") or {}
        if p.get("type") == "tool":
            st = p.get("state") or {}
            print("  ", p.get("tool"), json.dumps(st.get("input"))[:140], st.get("status"),
                  (st.get("output") or st.get("error") or "")[:160].replace("\n", " | ") if p.get("tool") == "bash" or st.get("status") == "error" else "")
        elif e.get("type") == "error":
            print("  ERR", json.dumps(e.get("error"))[:300])
    print("   events:", n)
