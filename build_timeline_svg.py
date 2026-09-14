import os

def generate_timeline_svg(theme='dark'):
    is_dark = (theme == 'dark')
    
    # Theme colors
    line_color = '#38BDF8' if is_dark else '#0284C7'
    branch_line = 'rgba(56,189,248,0.4)' if is_dark else 'rgba(2,132,199,0.4)'
    
    year_color = '#38BDF8' if is_dark else '#0284C7'
    title_color = '#F8FAFC' if is_dark else '#0F172A'
    sub_title_color = '#94A3B8' if is_dark else '#475569'
    branch_label_color = '#A78BFA' if is_dark else '#6D28D9'
    text_content_color = '#CBD5E1' if is_dark else '#334155'
    
    pink = '#EC4899' if is_dark else '#DB2777'
    emerald = '#10B981' if is_dark else '#059669'

    font_mono = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
    font_sans = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 370" width="100%" height="100%" font-family="{font_sans}">
  <style>
    .year-tag {{ font-family: {font_mono}; font-size: 13px; font-weight: 800; fill: {year_color}; letter-spacing: 0.5px; }}
    .node-title {{ font-family: {font_sans}; font-size: 14px; font-weight: 700; fill: {title_color}; }}
    .node-sub {{ font-family: {font_sans}; font-size: 13px; font-weight: 500; fill: {sub_title_color}; }}
    .branch-key {{ font-family: {font_mono}; font-size: 12px; font-weight: 700; fill: {branch_label_color}; }}
    .branch-val {{ font-family: {font_sans}; font-size: 12.5px; font-weight: 500; fill: {text_content_color}; }}
    
    @keyframes pulseNode {{
      0%, 100% {{ r: 6px; opacity: 0.9; }}
      50% {{ r: 9px; opacity: 1; }}
    }}
    .glowing-node {{
      animation: pulseNode 3s ease-in-out infinite;
    }}
  </style>

  <!-- Vertical Timeline Backbone Line -->
  <line x1="28" y1="28" x2="28" y2="340" stroke="{line_color}" stroke-width="2.5" stroke-dasharray="6 3" opacity="0.8"/>

  <!-- NODE 1: 2021 -->
  <g transform="translate(28, 30)">
    <circle cx="0" cy="0" r="7" fill="{year_color}"/>
    <circle cx="0" cy="0" r="11" fill="none" stroke="{year_color}" stroke-width="1.5" opacity="0.5"/>
    <text x="24" y="4" class="year-tag">2021  |  SSLC Graduation</text>
    <text x="240" y="4" class="node-sub">— Navabharath International School (94%)</text>
  </g>

  <!-- NODE 2: 2023 -->
  <g transform="translate(28, 95)">
    <circle cx="0" cy="0" r="7" fill="{year_color}"/>
    <circle cx="0" cy="0" r="11" fill="none" stroke="{year_color}" stroke-width="1.5" opacity="0.5"/>
    <text x="24" y="4" class="year-tag">2023  |  HSC Graduation</text>
    <text x="240" y="4" class="node-sub">— Navabharath International School (78%)</text>
  </g>

  <!-- NODE 3: 2023 ➔ PRESENT -->
  <g transform="translate(28, 160)">
    <circle cx="0" cy="0" r="8" fill="{emerald}" class="glowing-node"/>
    <circle cx="0" cy="0" r="13" fill="none" stroke="{emerald}" stroke-width="1.5" opacity="0.6"/>
    <text x="24" y="4" class="year-tag" fill="{emerald}">2023 ➔ PRESENT  |  B.E. Electronics &amp; Communication Engineering</text>
    <text x="560" y="4" class="node-sub" fill="{pink}">@ SNS College (CGPA: 8.8)</text>
  </g>

  <!-- SUB BRANCHES FOR CURRENT FOCUS -->
  <g transform="translate(28, 160)">
    <!-- Branch Lines -->
    <path d="M 16, 25 L 36, 25" stroke="{branch_line}" stroke-width="1.5"/>
    <path d="M 16, 50 L 36, 50" stroke="{branch_line}" stroke-width="1.5"/>
    <path d="M 16, 75 L 36, 75" stroke="{branch_line}" stroke-width="1.5"/>
    <path d="M 16, 100 L 36, 100" stroke="{branch_line}" stroke-width="1.5"/>
    <line x1="16" y1="15" x2="16" y2="100" stroke="{branch_line}" stroke-width="1.5"/>

    <!-- Branch Items -->
    <g transform="translate(44, 29)">
      <text x="0" y="0" class="branch-key">🔭 ./working_on</text>
      <text x="135" y="0" class="branch-val">➔  AI/GenAI Solutions, Data Analytics, AWS Cloud &amp; IoT Hardware</text>
    </g>

    <g transform="translate(44, 54)">
      <text x="0" y="0" class="branch-key">👯 ./collaborate</text>
      <text x="135" y="0" class="branch-val">➔  ML Applications, IoT System Prototyping, n8n Workflow Automation</text>
    </g>

    <g transform="translate(44, 79)">
      <text x="0" y="0" class="branch-key">🤝 ./explore</text>
      <text x="135" y="0" class="branch-val">➔  Multi-Cloud Architectures, LLM Orchestration, Computer Vision</text>
    </g>

    <g transform="translate(44, 104)">
      <text x="0" y="0" class="branch-key">🌱 ./learning</text>
      <text x="135" y="0" class="branch-val">➔  Generative AI Agent Design, AWS Solution Architecture &amp; BI</text>
    </g>
  </g>

  <!-- NODE 4: 2026 & BEYOND -->
  <g transform="translate(28, 335)">
    <circle cx="0" cy="0" r="7" fill="{pink}"/>
    <circle cx="0" cy="0" r="11" fill="none" stroke="{pink}" stroke-width="1.5" opacity="0.5"/>
    <text x="24" y="4" class="year-tag" fill="{pink}">2026 &amp; BEYOND  |  Leadership &amp; Technical Innovation</text>
    <text x="440" y="4" class="node-sub">— CEO @ DotEco, Tech Host &amp; Speaker</text>
  </g>
</svg>"""
    return svg

with open('timeline-dark.svg', 'w', encoding='utf-8') as f:
    f.write(generate_timeline_svg('dark'))

with open('timeline-light.svg', 'w', encoding='utf-8') as f:
    f.write(generate_timeline_svg('light'))

print('Generated Valid SVG Timeline Flowchart successfully.')
