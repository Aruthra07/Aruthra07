#!/usr/bin/env python3
"""
Generate ultra-high-contrast theme-aware SVGs for Aruthra S M's GitHub Profile README.
Ensures crisp readability in both Dark and Light GitHub themes.
"""

def generate_hero(theme="dark"):
    is_dark = (theme == "dark")
    bg = "#0B1220" if is_dark else "#FFFFFF"
    panel_bg = "#111827" if is_dark else "#F8FAFC"
    panel_bar = "#172033" if is_dark else "#F1F5F9"
    text_main = "#F8FAFC" if is_dark else "#0F172A"
    text_muted = "#94A3B8" if is_dark else "#475569"
    text_dim = "#64748B" if is_dark else "#64748B"
    border = "rgba(34,211,238,0.4)" if is_dark else "rgba(8,145,178,0.3)"
    cyan = "#22D3EE" if is_dark else "#0891B2"
    violet = "#A78BFA" if is_dark else "#7C3AED"
    emerald = "#10B981" if is_dark else "#059669"
    pink = "#EC4899" if is_dark else "#DB2777"
    pill_bg = "rgba(124,58,237,0.25)" if is_dark else "rgba(124,58,237,0.08)"
    pill_stroke = "rgba(167,139,250,0.4)" if is_dark else "rgba(124,58,237,0.3)"

    w, h = 1180, 200
    font_mono = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
    font_sans = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{font_mono}" role="img" aria-label="Aruthra S M Hero">
  <defs>
    <linearGradient id="line_grad_{theme}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{cyan}" />
      <stop offset="33%" stop-color="{violet}" />
      <stop offset="66%" stop-color="{pink}" />
      <stop offset="100%" stop-color="{emerald}" />
    </linearGradient>
  </defs>

  <!-- Shell -->
  <rect width="{w}" height="{h}" fill="{bg}" rx="14" />
  <rect width="{w-2}" height="{h-2}" x="1" y="1" fill="none" stroke="{border}" stroke-width="1.5" rx="13" />

  <!-- Ambient Grid Line -->
  <line x1="0" y1="100" x2="{w}" y2="100" stroke="{cyan}" stroke-width="0.5" opacity="0.15" />

  <!-- Top Badges -->
  <g transform="translate(35, 20)">
    <rect width="210" height="22" rx="11" fill="{pill_bg}" stroke="{pill_stroke}" />
    <circle cx="14" cy="11" r="3.5" fill="{emerald}">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.8s" repeatCount="indefinite" />
    </circle>
    <text x="26" y="15" font-size="9.5" font-weight="700" fill="{cyan}" letter-spacing="1">DEVELOPER_STATION // ONLINE</text>
  </g>

  <g transform="translate(905, 20)">
    <rect width="240" height="22" rx="11" fill="{pill_bg}" stroke="{pill_stroke}" />
    <circle cx="14" cy="11" r="3.5" fill="{pink}">
      <animate attributeName="opacity" values="1;0.2;1" dur="2.2s" repeatCount="indefinite" />
    </circle>
    <text x="26" y="15" font-size="9.5" font-weight="700" fill="{violet}" letter-spacing="1">ECE @ SNS COLLEGE OF ENG '27</text>
  </g>

  <!-- Main Hero Name -->
  <g transform="translate(35, 88)">
    <text x="0" y="0" font-family="{font_sans}" font-size="44" font-weight="800" fill="{text_main}" letter-spacing="-0.5">
      &lt;<tspan fill="{cyan}">Aruthra S M</tspan>/&gt;
      <tspan fill="{cyan}">_<animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite" /></tspan>
    </text>
    
    <text x="0" y="30" font-family="{font_mono}" font-size="13" font-weight="600" fill="{cyan}" letter-spacing="0.5">
      Technology Enthusiast <tspan fill="{pink}">•</tspan> AI Explorer <tspan fill="{pink}">•</tspan> Community Leader <tspan fill="{pink}">•</tspan> Public Speaker <tspan fill="{pink}">•</tspan> Content Writer <tspan fill="{pink}">•</tspan> Problem Solver
    </text>

    <rect x="0" y="42" width="760" height="3" rx="1.5" fill="url(#line_grad_{theme})">
      <animate attributeName="opacity" values="0.7;1;0.7" dur="3s" repeatCount="indefinite" />
    </rect>
  </g>

  <!-- Footer Tagline -->
  <g transform="translate(35, 178)">
    <text x="0" y="0" font-size="10" fill="{text_dim}">LEARN • BUILD • SHARE • CONNECT</text>
    <text x="1110" y="0" font-size="10" text-anchor="end" fill="{cyan}">https://github.com/Aruthra07</text>
  </g>
</svg>'''

def generate_quest(theme="dark"):
    is_dark = (theme == "dark")
    bg = "#0B1220" if is_dark else "#FFFFFF"
    panel_bg = "#111827" if is_dark else "#F8FAFC"
    text_muted = "#94A3B8" if is_dark else "#475569"
    border = "rgba(34,211,238,0.4)" if is_dark else "rgba(8,145,178,0.3)"
    cyan = "#22D3EE" if is_dark else "#0891B2"
    violet = "#A78BFA" if is_dark else "#7C3AED"
    emerald = "#10B981" if is_dark else "#059669"
    pink = "#EC4899" if is_dark else "#DB2777"
    amber = "#F59E0B" if is_dark else "#D97706"

    w, h = 1180, 100
    font_mono = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

    steps = [
      ("COMMIT", "Initial Code Push", cyan),
      ("CONTRIBUTE", "Pull Requests & Issues", violet),
      ("BUILD", "Solving Real Problems", emerald),
      ("LEARN", "Multi-Cloud & GenAI", pink),
      ("REPEAT", "Continuous Evolution", amber)
    ]

    nodes_xml = []
    step_w = 190
    start_x = 35
    gap = 45

    for i, (title, sub, col) in enumerate(steps):
        x = start_x + i * (step_w + gap)
        nodes_xml.append(f'''
        <g transform="translate({x}, 15)">
          <rect width="{step_w}" height="65" rx="8" fill="{panel_bg}" stroke="{col}" stroke-width="1.2" />
          <circle cx="18" cy="20" r="3.5" fill="{col}">
            <animate attributeName="opacity" values="1;0.3;1" dur="{1.5 + i*0.3}s" repeatCount="indefinite" />
          </circle>
          <text x="28" y="24" font-size="11.5" font-weight="700" fill="{col}">{title}</text>
          <text x="14" y="44" font-size="9.5" fill="{text_muted}">{sub}</text>
        </g>
        ''')
        if i < len(steps) - 1:
            arrow_x = x + step_w + 8
            nodes_xml.append(f'''
            <g transform="translate({arrow_x}, 45)">
              <line x1="0" y1="0" x2="28" y2="0" stroke="{cyan}" stroke-width="2" stroke-dasharray="4 2" />
              <polygon points="28,-4 34,0 28,4" fill="{cyan}" />
            </g>
            ''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{font_mono}" role="img" aria-label="Contribution Quest">
  <rect width="{w}" height="{h}" fill="{bg}" rx="12" />
  <rect width="{w-2}" height="{h-2}" x="1" y="1" fill="none" stroke="{border}" stroke-width="1" rx="11" opacity="0.6" />
  {"".join(nodes_xml)}
</svg>'''

def generate_community_map(theme="dark"):
    is_dark = (theme == "dark")
    bg = "#0B1220" if is_dark else "#FFFFFF"
    panel_bg = "#111827" if is_dark else "#F8FAFC"
    border = "rgba(34,211,238,0.4)" if is_dark else "rgba(8,145,178,0.3)"
    cyan = "#22D3EE" if is_dark else "#0891B2"
    violet = "#A78BFA" if is_dark else "#7C3AED"
    emerald = "#10B981" if is_dark else "#059669"
    pink = "#EC4899" if is_dark else "#DB2777"
    amber = "#F59E0B" if is_dark else "#D97706"

    w, h = 1180, 220
    font_mono = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

    cx, cy = 590, 110

    nodes = [
      ("CEO — DotEco", cx - 380, cy - 50, emerald),
      ("Microsoft Learn Enthusiast", cx - 200, cy + 50, cyan),
      ("AWS Learning Community", cx + 200, cy - 50, amber),
      ("Oracle Community", cx + 380, cy + 50, violet),
      ("Public Speaking & Events", cx, cy + 70, pink)
    ]

    lines_xml = []
    nodes_xml = []

    nodes_xml.append(f'''
    <g transform="translate({cx-85}, {cy-25})">
      <rect width="170" height="50" rx="25" fill="{panel_bg}" stroke="{cyan}" stroke-width="2" />
      <text x="85" y="30" text-anchor="middle" font-size="13" font-weight="800" fill="{cyan}">ARUTHRA S M</text>
    </g>
    ''')

    for title, nx, ny, col in nodes:
        lines_xml.append(f'''
        <line x1="{cx}" y1="{cy}" x2="{nx}" y2="{ny}" stroke="{col}" stroke-width="1.5" stroke-dasharray="5 3" opacity="0.7" />
        <circle cx="{nx}" cy="{ny}" r="4" fill="{col}">
          <animate attributeName="r" values="3;6;3" dur="2s" repeatCount="indefinite" />
        </circle>
        ''')
        box_w = len(title) * 7.2 + 26
        nodes_xml.append(f'''
        <g transform="translate({nx - box_w/2}, {ny - 16})">
          <rect width="{box_w}" height="32" rx="16" fill="{panel_bg}" stroke="{col}" stroke-width="1" />
          <text x="{box_w/2}" y="20" text-anchor="middle" font-size="10.5" font-weight="700" fill="{col}">{title}</text>
        </g>
        ''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{font_mono}" role="img" aria-label="Community Connection Map">
  <rect width="{w}" height="{h}" fill="{bg}" rx="12" />
  <rect width="{w-2}" height="{h-2}" x="1" y="1" fill="none" stroke="{border}" stroke-width="1" rx="11" opacity="0.6" />
  {"".join(lines_xml)}
  {"".join(nodes_xml)}
</svg>'''

def main():
    for theme in ("dark", "light"):
        with open(f"{theme}.svg", "w", encoding="utf-8") as f:
            f.write(generate_hero(theme))
        with open(f"quest-{theme}.svg", "w", encoding="utf-8") as f:
            f.write(generate_quest(theme))
        with open(f"community-map-{theme}.svg", "w", encoding="utf-8") as f:
            f.write(generate_community_map(theme))
        print(f"Generated SVGs for {theme}")

if __name__ == "__main__":
    main()
