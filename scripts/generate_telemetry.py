import datetime
import os
import sys

def generate_svg(repo_count=38, timestamp=None):
    if timestamp is None:
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    svg = f"""<svg width="800" height="200" viewBox="0 0 800 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="200" rx="8" fill="#0d1117" stroke="#30363d" stroke-width="1"/>
  
  <!-- Header Bar -->
  <rect x="0" y="0" width="800" height="36" rx="8" fill="#161b22"/>
  <rect x="0" y="28" width="800" height="8" fill="#161b22"/>
  <line x1="0" y1="36" x2="800" y2="36" stroke="#30363d" stroke-width="1"/>
  
  <!-- Terminal Indicators -->
  <circle cx="20" cy="18" r="4.5" fill="#f85149"/>
  <circle cx="36" cy="18" r="4.5" fill="#e3b341"/>
  <circle cx="52" cy="18" r="4.5" fill="#2ea043"/>
  <text x="75" y="22" fill="#8b949e" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="12" font-weight="600">HOST_TELEMETRY // RUNTIME_STATUS: ACTIVE</text>
  <text x="780" y="22" text-anchor="end" fill="#58a6ff" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11">SYNC: {timestamp}</text>

  <!-- Metric Column 1: Core Metrics -->
  <g transform="translate(30, 60)">
    <text x="0" y="0" fill="#8b949e" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" letter-spacing="1">ENGINEERING PROFILE</text>
    <text x="0" y="24" fill="#c9d1d9" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13">Primary Focus: <tspan fill="#58a6ff" font-weight="600">Cybersecurity &amp; Distributed Systems</tspan></text>
    <text x="0" y="48" fill="#c9d1d9" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13">Primary Stack: <tspan fill="#7ee787">Python 3.11+, TypeScript, Node, Bun, Linux</tspan></text>
    <text x="0" y="72" fill="#c9d1d9" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13">Public Repositories: <tspan fill="#d2a8ff" font-weight="600">{repo_count}</tspan></text>
    <text x="0" y="96" fill="#c9d1d9" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13">Commit Authentication: <tspan fill="#3fb950" font-weight="600">SSH ed25519 (Cryptographically Signed)</tspan></text>
  </g>

  <!-- Metric Column 2: System Invariants -->
  <g transform="translate(490, 60)">
    <text x="0" y="0" fill="#8b949e" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" letter-spacing="1">SYSTEM INVARIANTS</text>
    
    <rect x="0" y="14" width="280" height="24" rx="4" fill="#161b22" stroke="#30363d" stroke-width="1"/>
    <text x="12" y="30" fill="#8b949e" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11">Architecture: <tspan fill="#79c0ff">Defensive by Default</tspan></text>
    
    <rect x="0" y="44" width="280" height="24" rx="4" fill="#161b22" stroke="#30363d" stroke-width="1"/>
    <text x="12" y="60" fill="#8b949e" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11">Type Discipline: <tspan fill="#7ee787">Strict Null Safety (Zod/Mypy)</tspan></text>
    
    <rect x="0" y="74" width="280" height="24" rx="4" fill="#161b22" stroke="#30363d" stroke-width="1"/>
    <text x="12" y="90" fill="#8b949e" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11">CI Invariants: <tspan fill="#ffa657">Deterministic Pipelines</tspan></text>
  </g>

  <!-- Bottom Terminal Status Bar -->
  <line x1="30" y1="172" x2="770" y2="172" stroke="#21262d" stroke-width="1"/>
  <text x="30" y="188" fill="#484f58" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10">PIPELINE: GITHUB_ACTIONS // RUNTIME: CONTAINERIZED // SECRET_SCANNING: ENFORCED</text>
  <text x="770" y="188" text-anchor="end" fill="#3fb950" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="10">● ALL CHECKS PASSING</text>
</svg>
"""
    return svg

def main():
    repo_count = 38
    # If GH_TOKEN or GITHUB_TOKEN is present, fetch actual count
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        try:
            import urllib.request
            import json
            req = urllib.request.Request(
                "https://api.github.com/users/parth2024-tech",
                headers={"Authorization": f"Bearer {token}", "User-Agent": "telemetry-sync"}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                repo_count = data.get("public_repos", repo_count)
        except Exception as e:
            print(f"Warning: could not fetch live count, using default: {e}", file=sys.stderr)

    svg_content = generate_svg(repo_count=repo_count)
    os.makedirs("assets", exist_ok=True)
    with open("assets/telemetry.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Telemetry SVG generated at assets/telemetry.svg")

if __name__ == "__main__":
    main()
