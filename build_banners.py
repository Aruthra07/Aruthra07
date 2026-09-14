#!/usr/bin/env python3
"""
Generate sleek, frameless dark.svg and light.svg hero banners for Aruthra S M's GitHub Profile README.
No heavy dark/black background rects behind text; clean, transparent-friendly typography and glowing line.
"""

def generate_svg(theme="dark"):
    is_dark = (theme == "dark")
    text_main = "#22D3EE" if is_dark else "#0891B2"
    text_sub = "#F8FAFC" if is_dark else "#0F172A"
    text_muted = "#94A3B8" if is_dark else "#475569"
    cyan = "#22D3EE" if is_dark else "#0891B2"
    violet = "#A78BFA" if is_dark else "#7C3AED"
    emerald = "#10B981" if is_dark else "#059669"
    pink = "#EC4899" if is_dark else "#DB2777"
    pill_bg = "rgba(34,211,238,0.12)" if is_dark else "rgba(8,145,178,0.08)"
    pill_stroke = "rgba(34,211,238,0.4)" if is_dark else "rgba(8,145,178,0.3)"

    w, h = 1180, 180
    font_mono = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
    font_sans = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{font_mono}" role="img" aria-label="Aruthra S M Banner">
  <defs>
    <linearGradient id="grad_line_{theme}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{cyan}" />
      <stop offset="33%" stop-color="{violet}" />
      <stop offset="66%" stop-color="{pink}" />
      <stop offset="100%" stop-color="{emerald}" />
    </linearGradient>
  </defs>

  <!-- TOP STATUS BADGES (Frameless / Light pills) -->
  <g transform="translate(10, 20)">
    <rect width="210" height="24" rx="12" fill="{pill_bg}" stroke="{pill_stroke}" />
    <circle cx="14" cy="12" r="4" fill="{emerald}">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.8s" repeatCount="indefinite" />
    </circle>
    <text x="26" y="16" font-size="10" font-weight="700" fill="{cyan}" letter-spacing="1">DEVELOPER_STATION // ONLINE</text>
  </g>

  <g transform="translate(930, 20)">
    <rect width="240" height="24" rx="12" fill="{pill_bg}" stroke="{pill_stroke}" />
    <circle cx="14" cy="12" r="4" fill="{cyan}">
      <animate attributeName="opacity" values="1;0.2;1" dur="2.2s" repeatCount="indefinite" />
    </circle>
    <text x="26" y="16" font-size="10" font-weight="700" fill="{violet}" letter-spacing="1">ECE @ SNS COLLEGE OF ENG '27</text>
  </g>

  <!-- HERO TITLE & TAGLINE -->
  <g transform="translate(10, 85)">
    <!-- Name -->
    <text x="0" y="0" font-family="{font_sans}" font-size="44" font-weight="800" fill="{text_sub}" letter-spacing="-0.5">
      &lt;<tspan fill="{text_main}">Aruthra S M</tspan>/&gt;
      <tspan fill="{cyan}">
        <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite" />_
      </tspan>
    </text>

    <!-- Roles Subtitle -->
    <text x="0" y="32" font-family="{font_mono}" font-size="13" font-weight="600" fill="{cyan}" letter-spacing="0.5">
      Technology Enthusiast <tspan fill="{pink}">•</tspan> AI Explorer <tspan fill="{pink}">•</tspan> Community Leader <tspan fill="{pink}">•</tspan> Public Speaker <tspan fill="{pink}">•</tspan> Content Writer <tspan fill="{pink}">•</tspan> Problem Solver
    </text>

    <!-- Animated Gradient Divider Line -->
    <rect x="0" y="44" width="760" height="3" fill="url(#grad_line_{theme})" rx="1.5">
      <animate attributeName="width" values="0;760" dur="1.2s" ease="ease-out" fill="freeze" />
    </rect>
  </g>

  <!-- Bottom Info -->
  <g transform="translate(10, 168)">
    <text x="0" y="0" font-size="10" font-weight="600" fill="{text_muted}" letter-spacing="1">LEARN • BUILD • SHARE • CONNECT</text>
    <text x="1160" y="0" text-anchor="end" font-size="10" font-weight="600" fill="{text_muted}">https://github.com/Aruthra07</text>
  </g>
</svg>'''
    return svg

def main():
    with open("dark.svg", "w", encoding="utf-8") as f:
        f.write(generate_svg("dark"))
    with open("light.svg", "w", encoding="utf-8") as f:
        f.write(generate_svg("light"))
    print("Frameless hero banners dark.svg and light.svg generated successfully.")

if __name__ == "__main__":
    main()
