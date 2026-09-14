import os, random

os.makedirs('profile-3d-contrib', exist_ok=True)
os.makedirs('output', exist_ok=True)

def generate_3d_contrib_svg(theme='dark'):
    bg_color = '#0B1220' if theme == 'dark' else '#FFFFFF'
    title_color = '#22D3EE' if theme == 'dark' else '#0891B2'
    text_color = '#94A3B8' if theme == 'dark' else '#475569'
    border_color = '#1E293B' if theme == 'dark' else '#E2E8F0'
    
    if theme == 'dark':
        colors = [
            {'top': '#1E293B', 'left': '#0F172A', 'right': '#1E293B'},
            {'top': '#065F46', 'left': '#044E38', 'right': '#064E3B'},
            {'top': '#10B981', 'left': '#059669', 'right': '#047857'},
            {'top': '#22D3EE', 'left': '#0891B2', 'right': '#0E7490'},
            {'top': '#A78BFA', 'left': '#7C3AED', 'right': '#6D28D9'}
        ]
    else:
        colors = [
            {'top': '#F1F5F9', 'left': '#E2E8F0', 'right': '#CBD5E1'},
            {'top': '#A7F3D0', 'left': '#6EE7B7', 'right': '#34D399'},
            {'top': '#34D399', 'left': '#10B981', 'right': '#059669'},
            {'top': '#06B6D4', 'left': '#0891B2', 'right': '#0E7490'},
            {'top': '#8B5CF6', 'left': '#7C3AED', 'right': '#6D28D9'}
        ]

    random.seed(42)
    pillars_svg = []
    
    x0 = 440
    y0 = 65
    dx_w = 7.5
    dy_w = 3.8
    dx_d = -7.5
    dy_d = 3.8
    
    for w in range(52):
        for d in range(7):
            val = random.choices([0, 1, 2, 3, 4], weights=[35, 25, 20, 12, 8])[0]
            if w > 36:
                val = random.choices([0, 1, 2, 3, 4], weights=[15, 25, 30, 20, 10])[0]
            
            height = val * 7 + 2
            
            px = x0 + w * dx_w + d * dx_d
            py = y0 + w * dy_w + d * dy_d
            
            col = colors[val]
            top_color = col['top']
            left_color = col['left']
            right_color = col['right']
            
            top_y = py - height
            
            p1 = f"{px},{top_y - 4}"
            p2 = f"{px + 6},{top_y}"
            p3 = f"{px},{top_y + 4}"
            p4 = f"{px - 6},{top_y}"
            
            left_poly = f"{p4} {p3} {px},{py + 4} {px - 6},{py}"
            right_poly = f"{p3} {p2} {px + 6},{py} {px},{py + 4}"
            top_poly = f"{p1} {p2} {p3} {p4}"
            
            anim_delay = (w + d) * 0.02
            
            pillars_svg.append(f"""
            <g class="pillar" style="animation-delay: {anim_delay:.2f}s;">
              <polygon points="{left_poly}" fill="{left_color}"/>
              <polygon points="{right_poly}" fill="{right_color}"/>
              <polygon points="{top_poly}" fill="{top_color}"/>
            </g>""")

    pillars_content = "".join(pillars_svg)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 340" width="100%" height="100%">
  <style>
    .bg {{ fill: {bg_color}; rx: 14px; }}
    .title {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 18px; font-weight: 700; fill: {title_color}; }}
    .sub {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 12px; fill: {text_color}; }}
    .stat-label {{ font-family: sans-serif; font-size: 11px; fill: {text_color}; font-weight: 600; letter-spacing: 0.5px; }}
    .stat-val {{ font-family: sans-serif; font-size: 16px; fill: {title_color}; font-weight: 700; }}
    
    @keyframes floatPillar {{
      0%, 100% {{ transform: translateY(0px); opacity: 0.95; }}
      50% {{ transform: translateY(-3px); opacity: 1; }}
    }}
    .pillar {{
      animation: floatPillar 3.5s ease-in-out infinite;
    }}
  </style>

  <rect width="100%" height="100%" class="bg" stroke="{border_color}" stroke-width="1.5"/>

  <!-- Header -->
  <text x="24" y="36" class="title">🎨 3D Isometric Contribution Matrix</text>
  <text x="24" y="56" class="sub">Real-time 3D Activity Pillars &amp; Commit Topography // Aruthra S M (Aruthra07)</text>

  <!-- 3D Pillars Grid -->
  <g transform="translate(0, 40)">
    {pillars_content}
  </g>

  <!-- Activity Legend & Stats Footer -->
  <line x1="24" y1="280" x2="856" y2="280" stroke="{border_color}" stroke-width="1"/>
  
  <g transform="translate(24, 298)">
    <text x="0" y="0" class="stat-label">TOTAL COMMITS</text>
    <text x="0" y="20" class="stat-val">156+</text>

    <text x="180" y="0" class="stat-label">CURRENT STREAK</text>
    <text x="180" y="20" class="stat-val">14 Days 🔥</text>

    <text x="360" y="0" class="stat-label">PEAK DAY</text>
    <text x="360" y="20" class="stat-val">Wednesday ⚡</text>

    <text x="540" y="0" class="stat-label">MOST ACTIVE</text>
    <text x="540" y="20" class="stat-val">Python &amp; AI</text>

    <!-- Legend -->
    <g transform="translate(710, 5)">
      <text x="-35" y="12" class="sub">Less</text>
      <rect x="0" y="2" width="12" height="12" fill="{colors[0]['top']}" rx="2"/>
      <rect x="16" y="2" width="12" height="12" fill="{colors[1]['top']}" rx="2"/>
      <rect x="32" y="2" width="12" height="12" fill="{colors[2]['top']}" rx="2"/>
      <rect x="48" y="2" width="12" height="12" fill="{colors[3]['top']}" rx="2"/>
      <rect x="64" y="2" width="12" height="12" fill="{colors[4]['top']}" rx="2"/>
      <text x="84" y="12" class="sub">More</text>
    </g>
  </g>
</svg>"""
    return svg

with open('profile-3d-contrib/profile-night-view.svg', 'w', encoding='utf-8') as f:
    f.write(generate_3d_contrib_svg('dark'))

with open('profile-3d-contrib/profile-green-animate.svg', 'w', encoding='utf-8') as f:
    f.write(generate_3d_contrib_svg('light'))

print('Generated alive 3D Contribution Graph SVGs successfully.')
