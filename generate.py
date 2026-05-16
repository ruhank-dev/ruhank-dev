#!/usr/bin/env python3
"""
ruhan-k-dev GitHub Profile SVG Generator
Generates animated SVGs for the profile README.
Run locally or via GitHub Actions.
"""

import os
import math
import random

random.seed(42)
OUT = "assets"
os.makedirs(OUT, exist_ok=True)

# ─────────────────────────────────────────────
# HERO SVG — particle animation forming RUHAN-K-DEV
# Uses CSS @keyframes (works in GitHub SVG renderer)
# ─────────────────────────────────────────────
def gen_hero():
    W, H = 900, 300
    CX, CY = 450, 140

    # Letter point masks
    def letter_pts(ch, ox, oy, lw=50, lh=70, step=5):
        pts = []
        if ch == 'R':
            for y in range(0, lh, step): pts.append((ox+4, oy+y))
            for x in range(4, lw-8, step): pts.append((ox+x, oy))
            for x in range(4, lw-8, step): pts.append((ox+x, oy+lh//2))
            for y in range(0, lh//2, step): pts.append((ox+lw-6, oy+y))
            for i in range(0, lh//2+1, step): pts.append((ox+8+i//2, oy+lh//2+i))
        elif ch == 'U':
            for y in range(0, lh-8, step): pts.append((ox+4, oy+y))
            for y in range(0, lh-8, step): pts.append((ox+lw-4, oy+y))
            for x in range(4, lw-3, step): pts.append((ox+x, oy+lh-4))
        elif ch == 'H':
            for y in range(0, lh, step): pts.append((ox+4, oy+y))
            for y in range(0, lh, step): pts.append((ox+lw-4, oy+y))
            for x in range(4, lw-3, step): pts.append((ox+x, oy+lh//2))
        elif ch == 'A':
            for i in range(0, lh+1, step):
                pts.append((ox+4+i*((lw//2-4)/lh), oy+lh-i))
                pts.append((ox+lw-4-i*((lw//2-4)/lh), oy+lh-i))
            for x in range(int(lw*.25), int(lw*.75), step):
                pts.append((ox+x, oy+lh//2))
        elif ch == 'N':
            for y in range(0, lh, step): pts.append((ox+4, oy+y))
            for y in range(0, lh, step): pts.append((ox+lw-4, oy+y))
            for i in range(0, lh+1, step):
                pts.append((ox+4+i*(lw-8)/lh, oy+i))
        elif ch == '-':
            for x in range(8, lw-7, step): pts.append((ox+x, oy+lh//2))
        elif ch == 'K':
            for y in range(0, lh, step): pts.append((ox+4, oy+y))
            for i in range(0, lh//2+1, step):
                pts.append((ox+4+i*(lw-8)//(lh//2), oy+lh//2-i))
                pts.append((ox+4+i*(lw-8)//(lh//2), oy+lh//2+i))
        elif ch == 'D':
            for y in range(0, lh, step): pts.append((ox+4, oy+y))
            for x in range(4, lw-8, step): pts.append((ox+x, oy))
            for x in range(4, lw-8, step): pts.append((ox+x, oy+lh-1))
            for y in range(0, lh, step): pts.append((ox+lw-4, oy+y))
        elif ch == 'E':
            for y in range(0, lh, step): pts.append((ox+4, oy+y))
            for x in range(4, lw-4, step): pts.append((ox+x, oy))
            for x in range(4, lw-4, step): pts.append((ox+x, oy+lh-1))
            for x in range(4, int(lw*.75), step): pts.append((ox+x, oy+lh//2))
        elif ch == 'V':
            for i in range(0, lh+1, step):
                pts.append((ox+4+i*(lw//2-4)/lh, oy+i))
                pts.append((ox+lw-4-i*(lw//2-4)/lh, oy+i))
        return pts

    text = 'RUHAN-K-DEV'
    LW = 52
    sx0 = CX - (len(text)*LW)//2
    sy0 = CY - 35

    text_pts = []
    for i, ch in enumerate(text):
        text_pts.extend(letter_pts(ch, sx0+i*LW, sy0, lw=LW-2, lh=70, step=5))

    # dedupe
    seen = set()
    pts = []
    for p in text_pts:
        k = (int(p[0]), int(p[1]))
        if k not in seen and 5 < p[0] < W-5 and 5 < p[1] < H-5:
            seen.add(k)
            pts.append(k)

    # Cycle: 0-5s form, 5-8s hold, 8-11s dust L→R, 11-13s scatter, 13-16s reform → 16s total
    T = 16
    circles = []
    for i, (tx, ty) in enumerate(pts):
        angle = random.uniform(0, 2*math.pi)
        dist  = random.uniform(120, 380)
        scx   = CX + math.cos(angle)*dist
        scy   = CY + math.sin(angle)*dist
        # dust destination
        dx = tx + random.uniform(80, 300)
        dy = ty + random.uniform(-50, 50)
        # L→R wave
        norm  = (tx - sx0) / (len(text)*LW)
        td0   = 8 + norm*2          # 8..10s
        td1   = td0 + 1.5           # dust done
        tr    = 13                   # reform start

        def f(t): return f"{t/T:.3f}"

        # keyTimes and values for cx, cy, opacity, r
        kt = f"0;0.01;{f(5)};{f(7.9)};{f(td0)};{f(td1)};{f(tr)};1"

        cx_v  = f"{scx:.1f};{scx:.1f};{tx};{tx};{tx};{dx:.1f};{scx:.1f};{scx:.1f}"
        cy_v  = f"{scy:.1f};{scy:.1f};{ty};{ty};{ty};{dy:.1f};{scy:.1f};{scy:.1f}"
        op_v  = "0.1;0.1;0.92;0.92;0.88;0;0;0.1"
        r_v   = "0.8;0.8;1;1;1;0.3;0.8;0.8"
        begin = f"{random.uniform(0,0.8):.2f}s"

        circles.append(
            f'<circle r="1" fill="#fff">'
            f'<animate attributeName="cx" values="{cx_v}" keyTimes="{kt}" dur="{T}s" repeatCount="indefinite" begin="{begin}"/>'
            f'<animate attributeName="cy" values="{cy_v}" keyTimes="{kt}" dur="{T}s" repeatCount="indefinite" begin="{begin}"/>'
            f'<animate attributeName="opacity" values="{op_v}" keyTimes="{kt}" dur="{T}s" repeatCount="indefinite" begin="{begin}"/>'
            f'<animate attributeName="r" values="{r_v}" keyTimes="{kt}" dur="{T}s" repeatCount="indefinite" begin="{begin}"/>'
            f'</circle>'
        )

    # Ambient dots
    ambient = []
    for _ in range(30):
        ax = random.randint(20, W-20)
        ay = random.randint(20, H-20)
        ar = random.uniform(0.5, 1.2)
        ad = random.uniform(3, 7)
        ao = random.uniform(0.1, 0.4)
        ambient.append(
            f'<circle cx="{ax}" cy="{ay}" r="{ar:.1f}" fill="#fff" opacity="{ao:.2f}">'
            f'<animate attributeName="opacity" values="{ao:.2f};{ao*2:.2f};{ao:.2f}" dur="{ad:.1f}s" repeatCount="indefinite"/>'
            f'</circle>'
        )

    title_kt = f"0;{5/T:.3f};{5.1/T:.3f};{7.9/T:.3f};{8/T:.3f};1"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <style>
      .sub {{ font-family: Arial,sans-serif; font-size:11px; fill:#aaa; text-anchor:middle; letter-spacing:4px; }}
      .loc {{ font-family: Arial,sans-serif; font-size:10px; fill:#555; text-anchor:middle; letter-spacing:3px; }}
      .gh  {{ font-family: Arial,sans-serif; font-size:9px;  fill:#333; text-anchor:middle; letter-spacing:5px; }}
      .corner {{ stroke:#222; stroke-width:1; fill:none; }}
    </style>
  </defs>

  <rect width="{W}" height="{H}" fill="#000"/>

  <!-- ambient stars -->
  {"".join(ambient)}

  <!-- particles -->
  {"".join(circles)}

  <!-- title: fades in when solid (5s→8s in 16s cycle) -->
  <text font-family="Impact,Arial Black,sans-serif" font-size="90" fill="#fff"
        letter-spacing="10" text-anchor="middle" x="{CX}" y="{CY+28}">
    RUHAN-K-DEV
    <animate attributeName="opacity"
      values="0;0;0.95;0.95;0;0"
      keyTimes="{title_kt}"
      dur="{T}s" repeatCount="indefinite"/>
  </text>

  <!-- corner marks -->
  <polyline class="corner" points="14,30 14,12 32,12"/>
  <polyline class="corner" points="868,12 886,12 886,30"/>
  <polyline class="corner" points="14,270 14,288 32,288"/>
  <polyline class="corner" points="868,288 886,288 886,270"/>

  <!-- subtitle always visible -->
  <line x1="160" y1="{CY+55}" x2="740" y2="{CY+55}" stroke="#1e1e1e" stroke-width="1"/>
  <text class="gh"  x="{CX}" y="20">GITHUB.COM / RUHAN-K-DEV</text>
  <text class="sub" x="{CX}" y="{CY+80}">SOFTWARE ENGINEER  ·  AI ENGINEER  ·  SYSTEMS PROGRAMMER</text>
  <text class="loc" x="{CX}" y="{CY+104}">FAST NUCES  ·  ISLAMABAD, PK  ·  BSCS 2027</text>
</svg>'''

    with open(f"{OUT}/hero.svg", "w") as f:
        f.write(svg)
    print(f"✓ hero.svg  ({len(pts)} particles)")


# ─────────────────────────────────────────────
# KEYBOARD SVG
# ─────────────────────────────────────────────
def gen_keyboard():
    W, H = 900, 260

    # Flash animation classes
    flash_css = ""
    for i in range(1, 12):
        d = 1.5 + i * 0.4
        delay = round((i * 0.37) % 2.5, 2)
        flash_css += f"""
      .fa{i} {{ animation: flash {d:.1f}s {delay:.2f}s steps(1) infinite; }}"""

    css = f"""
      .k  {{ fill:#111; stroke:#1a1a1a; stroke-width:1; }}
      .sk {{ fill:#1c1c1c; stroke:#555; stroke-width:1; }}
      .sl {{ font-family:Arial,sans-serif; font-size:9px; font-weight:bold; fill:#fff;
             text-anchor:middle; dominant-baseline:middle; }}
      .sec-title {{ font-family:Arial,sans-serif; font-size:11px; font-weight:bold;
                   fill:#fff; text-anchor:middle; letter-spacing:4px; }}
      {flash_css}
      @keyframes flash {{
        0%,80%,100% {{ fill:#111; stroke:#1a1a1a; }}
        81%          {{ fill:#1c1c1c; stroke:#2a2a2a; }}
        84%          {{ fill:#111; stroke:#1a1a1a; }}
      }}
      @keyframes spulse {{
        0%,100% {{ opacity:0.85; }}
        50%     {{ opacity:1; }}
      }}
      .sp {{ animation: spulse 2.5s ease-in-out infinite; }}"""

    # Build rows using flex-proportional approach
    # Board: x=28, inner width=844, padding=12 each side → usable=820
    # Gap between keys = 4px
    # Row proportions: total units per row

    def make_row(keys, y, board_x=40, board_w=820, gap=4):
        """keys = list of (units, is_skill, char_or_None, flash_class)"""
        total_units = sum(k[0] for k in keys)
        total_gap   = gap * (len(keys) - 1)
        px_per_unit = (board_w - total_gap) / total_units
        elems = []
        x = board_x
        for units, is_skill, char, fclass in keys:
            kw = round(units * px_per_unit)
            kx = round(x)
            if is_skill:
                elems.append(f'<g class="sp"><rect class="sk" x="{kx}" y="{y}" width="{kw}" height="38" rx="5"/>')
                elems.append(f'<text class="sl" x="{kx+kw//2}" y="{y+19}">{char}</text></g>')
            else:
                elems.append(f'<rect class="k {fclass}" x="{kx}" y="{y}" width="{kw}" height="38" rx="5"/>')
            x += kw + gap
        return "\n  ".join(elems)

    fa = lambda i: f"fa{i}"

    # Row 1: num row (14 keys: 13×1u + bksp×2u = 15u)
    # AI/ML starts at index 1
    r1_keys = []
    r1_keys.append((1, False, None, fa(1)))   # `
    for i, ch in enumerate('AI/ML'):
        r1_keys.append((1, True, ch, ''))
    for i in range(8):
        r1_keys.append((1, False, None, fa(i%11+1)))
    r1_keys.append((2, False, None, fa(3)))   # bksp

    # Row 2: tab(1.5) + FullStack(9 keys) + 4 normal + no enter
    r2_keys = [(1.5, False, None, fa(2))]
    for ch in 'FullStack':
        r2_keys.append((1, True, ch, ''))
    for i in range(5):
        r2_keys.append((1, False, None, fa(i%11+1)))
    r2_keys.append((1.5, False, None, fa(5)))

    # Row 3: caps(1.75) + Networking(10 keys) + 1 normal + enter(2.25)
    r3_keys = [(1.75, False, None, fa(7))]
    for ch in 'Networking':
        r3_keys.append((1, True, ch, ''))
    r3_keys.append((1, False, None, fa(4)))
    r3_keys.append((2.25, False, None, fa(9)))

    # Row 4: lshift(2.25) + Compiler(8 keys) + 2 normal + rshift(2.75)
    r4_keys = [(2.25, False, None, fa(2))]
    for ch in 'Compiler':
        r4_keys.append((1, True, ch, ''))
    for i in range(2):
        r4_keys.append((1, False, None, fa(i%11+3)))
    r4_keys.append((2.75, False, None, fa(6)))

    # Row 5: bottom
    r5_keys = [(1.25,False,None,fa(8)),(1.25,False,None,fa(10)),(1.25,False,None,fa(11)),
               (6.25,False,None,fa(1)),(1.25,False,None,fa(5)),(1.25,False,None,fa(7)),
               (1.25,False,None,fa(9))]

    rows_svg = "\n  ".join([
        make_row(r1_keys, 52),
        make_row(r2_keys, 98),
        make_row(r3_keys, 144),
        make_row(r4_keys, 190),
        make_row(r5_keys, 228, board_w=820),
    ])

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs><style>{css}
  </style></defs>

  <rect width="{W}" height="{H}" fill="#000"/>

  <line x1="30" y1="16" x2="370" y2="16" stroke="#333" stroke-width="1"/>
  <text class="sec-title" x="450" y="21">EXPERTISE</text>
  <line x1="530" y1="16" x2="870" y2="16" stroke="#333" stroke-width="1"/>

  <rect x="28" y="36" width="844" height="210" rx="12" fill="#0c0c0c" stroke="#1c1c1c" stroke-width="1"/>

  {rows_svg}
</svg>'''

    with open(f"{OUT}/keyboard.svg", "w") as f:
        f.write(svg)
    print("✓ keyboard.svg")


# ─────────────────────────────────────────────
# PROJECTS SVG
# ─────────────────────────────────────────────
def gen_projects():
    W, H = 900, 370

    projects = [
        ("01", "GPU Computing",    "Video Analytics Engine",
         "Real-time KLT optical flow tracking parallelized\nacross GPU cores. Live motion vector extraction.",
         ["C++","CUDA","OpenACC","OpenCV"]),
        ("02", "AI · Full Stack",  "Property CRM",
         "AI-powered lead management with NVIDIA\nNemotron 3, socket events and RBAC.",
         ["Next.js","MongoDB","Socket.io","NVIDIA AI"]),
        ("03", "Civic Tech",       "Civanta",
         "Geo-tagged civic issue reporting with full-stack\nrouting, interactive maps, real-time updates.",
         ["React","Spring Boot","Leaflet.js"]),
        ("04", "Compiler Design",  "Compiler + Parser",
         "Full pipeline — Lexer → LL(1) → SLR(1)/LR(1)\n→ JSON to XML translator, from scratch.",
         ["C++","Flex","Yacc","Bison"]),
    ]

    card_w = 420
    cards_svg = []
    positions = [(30,34),(454,34),(30,207),(454,207)]

    for (num, tag, name, desc, stack), (cx, cy) in zip(projects, positions):
        cw = card_w
        ch = 168
        # holo number
        cards_svg.append(f'''
  <rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" fill="#000" stroke="#1c1c1c" stroke-width="1"/>
  <text x="{cx+cw-14}" y="{cy+ch-10}" font-family="Impact,Arial Black,sans-serif" font-size="72"
        fill="none" stroke="rgba(255,255,255,0.32)" stroke-width="1"
        text-anchor="end" dominant-baseline="auto">
    {num}
    <animate attributeName="stroke" values="rgba(255,255,255,0.22);rgba(180,220,255,0.48);rgba(255,255,255,0.22)"
      dur="4s" repeatCount="indefinite"/>
  </text>
  <text x="{cx+16}" y="{cy+22}" font-family="Arial,sans-serif" font-size="8" font-weight="bold"
        fill="#666" letter-spacing="3">{tag.upper()}</text>
  <text x="{cx+16}" y="{cy+46}" font-family="Arial,sans-serif" font-size="14" font-weight="bold"
        fill="#eee">{name}</text>''')
        # desc lines
        for li, line in enumerate(desc.split('\n')):
            cards_svg.append(
                f'  <text x="{cx+16}" y="{cy+66+li*14}" font-family="Arial,sans-serif" '
                f'font-size="10" fill="#666">{line}</text>'
            )
        # stack tags
        sx = cx+16
        for tag_item in stack:
            tw = len(tag_item)*6+12
            cards_svg.append(
                f'  <rect x="{sx}" y="{cy+ch-30}" width="{tw}" height="16" rx="2" fill="none" stroke="#222" stroke-width="1"/>'
                f'  <text x="{sx+tw//2}" y="{cy+ch-19}" font-family="Arial,sans-serif" font-size="8"'
                f'        font-weight="bold" fill="#555" text-anchor="middle" letter-spacing="1">{tag_item.upper()}</text>'
            )
            sx += tw + 6

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="#000"/>

  <line x1="30" y1="18" x2="310" y2="18" stroke="#333" stroke-width="1"/>
  <text x="450" y="23" font-family="Arial,sans-serif" font-size="11" font-weight="bold"
        fill="#fff" text-anchor="middle" letter-spacing="4">FEATURED PROJECTS</text>
  <line x1="590" y1="18" x2="870" y2="18" stroke="#333" stroke-width="1"/>

  <line x1="450" y1="34" x2="450" y2="376" stroke="#1a1a1a" stroke-width="1"/>
  <line x1="30"  y1="206" x2="870" y2="206" stroke="#1a1a1a" stroke-width="1"/>

  {"".join(cards_svg)}
</svg>'''

    with open(f"{OUT}/projects.svg", "w") as f:
        f.write(svg)
    print("✓ projects.svg")


# ─────────────────────────────────────────────
# ABOUT SVG
# ─────────────────────────────────────────────
def gen_about():
    W, H = 900, 240

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs><style>
    .ak {{ font-family:Arial,sans-serif; font-size:10px; fill:#555; }}
    .av {{ font-family:Arial,sans-serif; font-size:10px; fill:#bbb; }}
    .at {{ font-family:Arial,sans-serif; font-size:9px;  fill:#444; font-weight:bold; letter-spacing:3px; }}
    .st {{ font-family:Arial,sans-serif; font-size:11px; fill:#fff; font-weight:bold; text-anchor:middle; letter-spacing:4px; }}
    .ct {{ font-family:Arial,sans-serif; font-size:10px; fill:#666; font-weight:bold; text-anchor:middle; letter-spacing:2px; }}
  </style></defs>

  <rect width="{W}" height="{H}" fill="#000"/>

  <!-- section header -->
  <line x1="30" y1="16" x2="395" y2="16" stroke="#333" stroke-width="1"/>
  <text class="st" x="450" y="21">ABOUT</text>
  <line x1="505" y1="16" x2="870" y2="16" stroke="#333" stroke-width="1"/>

  <line x1="450" y1="30" x2="450" y2="175" stroke="#1a1a1a" stroke-width="1"/>

  <!-- LEFT -->
  <text class="at" x="46" y="48">EDUCATION</text>
  <line x1="46" y1="52" x2="420" y2="52" stroke="#111" stroke-width="1"/>
  <text class="ak" x="46" y="70">University</text><text class="av" x="418" y="70" text-anchor="end">FAST NUCES</text>
  <line x1="46" y1="75" x2="420" y2="75" stroke="#0d0d0d" stroke-width="1"/>
  <text class="ak" x="46" y="93">Degree</text><text class="av" x="418" y="93" text-anchor="end">BS Computer Science</text>
  <line x1="46" y1="98" x2="420" y2="98" stroke="#0d0d0d" stroke-width="1"/>
  <text class="ak" x="46" y="116">Expected</text><text class="av" x="418" y="116" text-anchor="end">2027</text>
  <line x1="46" y1="121" x2="420" y2="121" stroke="#0d0d0d" stroke-width="1"/>
  <text class="ak" x="46" y="139">A-Levels</text><text class="av" x="418" y="139" text-anchor="end">PAEC Science School</text>

  <!-- RIGHT -->
  <text class="at" x="466" y="48">INFO</text>
  <line x1="466" y1="52" x2="870" y2="52" stroke="#111" stroke-width="1"/>
  <text class="ak" x="466" y="70">Location</text><text class="av" x="868" y="70" text-anchor="end">Islamabad, PK</text>
  <line x1="466" y1="75" x2="870" y2="75" stroke="#0d0d0d" stroke-width="1"/>
  <text class="ak" x="466" y="93">Email</text><text class="av" x="868" y="93" text-anchor="end">ruhan.k.dev@gmail.com</text>
  <line x1="466" y1="98" x2="870" y2="98" stroke="#0d0d0d" stroke-width="1"/>
  <text class="ak" x="466" y="116">Focus</text><text class="av" x="868" y="116" text-anchor="end">AI · Systems · Fullstack</text>
  <line x1="466" y1="121" x2="870" y2="121" stroke="#0d0d0d" stroke-width="1"/>
  <text class="ak" x="466" y="139">Status</text><text class="av" x="868" y="139" text-anchor="end">Open to opportunities</text>

  <!-- Connect -->
  <line x1="30" y1="178" x2="365" y2="178" stroke="#333" stroke-width="1"/>
  <text class="st" x="450" y="183">CONNECT</text>
  <line x1="535" y1="178" x2="870" y2="178" stroke="#333" stroke-width="1"/>

  <a href="mailto:ruhan.k.dev@gmail.com">
    <rect x="30" y="196" width="415" height="38" rx="2" fill="#000" stroke="#252525" stroke-width="1"/>
    <text class="ct" x="237" y="220">&#9993;  ruhan.k.dev@gmail.com</text>
  </a>
  <a href="https://www.linkedin.com/in/ruhan-kamran-b99007372/">
    <rect x="455" y="196" width="415" height="38" rx="2" fill="#000" stroke="#252525" stroke-width="1"/>
    <text class="ct" x="662" y="220">in  linkedin.com/in/ruhan-kamran</text>
  </a>
</svg>'''

    with open(f"{OUT}/about.svg", "w") as f:
        f.write(svg)
    print("✓ about.svg")


if __name__ == "__main__":
    gen_hero()
    gen_keyboard()
    gen_projects()
    gen_about()
    print("\nAll SVGs generated in ./assets/")


# ─────────────────────────────────────────────
# BELT SVG — scrolling tech icons
# ─────────────────────────────────────────────
def gen_belt():
    items = [
        ("python",     "PYTHON",  "python/python-original"),
        ("cplusplus",  "C++",     "cplusplus/cplusplus-original"),
        ("react",      "REACT",   "react/react-original"),
        ("nextjs",     "NEXT.JS", "nextjs/nextjs-original"),
        ("docker",     "DOCKER",  "docker/docker-original"),
        ("linux",      "LINUX",   "linux/linux-original"),
        ("git",        "GIT",     "git/git-original"),
        ("mongodb",    "MONGODB", "mongodb/mongodb-original"),
        ("java",       "JAVA",    "java/java-original"),
        ("javascript", "JS",      "javascript/javascript-original"),
    ]
    base = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons"
    pitch = 96

    def item(x, label, path):
        url = f"{base}/{path}.svg"
        return (f'<g transform="translate({x},4)">'
                f'<rect width="84" height="80" rx="2" fill="#000" stroke="#1e1e1e" stroke-width="1"/>'
                f'<image href="{url}" x="29" y="10" width="26" height="26"/>'
                f'<text x="42" y="60" font-family="Arial,sans-serif" font-size="7" font-weight="bold" '
                f'fill="#444" text-anchor="middle" letter-spacing="1">{label}</text>'
                f'</g>')

    set1 = "".join(item(6 + i*pitch, lab, path) for i, (_, lab, path) in enumerate(items))
    set2 = "".join(item(6 + (len(items)*pitch) + i*pitch, lab, path) for i, (_, lab, path) in enumerate(items))
    total = len(items) * pitch

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="88" viewBox="0 0 900 88">
  <defs>
    <style>.bg{{animation:scroll {total/32:.0f}s linear infinite}}
    @keyframes scroll{{from{{transform:translateX(0)}}to{{transform:translateX(-{total}px)}}}}</style>
    <linearGradient id="fl" x1="0" x2="1"><stop offset="0%" stop-color="#000"/><stop offset="100%" stop-color="#000" stop-opacity="0"/></linearGradient>
    <linearGradient id="fr" x1="0" x2="1"><stop offset="0%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000"/></linearGradient>
    <clipPath id="c"><rect width="900" height="88"/></clipPath>
  </defs>
  <rect width="900" height="88" fill="#000"/>
  <line x1="0" y1="0" x2="900" y2="0" stroke="#2a2a2a" stroke-width="1"/>
  <line x1="0" y1="87" x2="900" y2="87" stroke="#2a2a2a" stroke-width="1"/>
  <g clip-path="url(#c)"><g class="bg">{set1}{set2}</g></g>
  <rect x="0" y="0" width="70" height="88" fill="url(#fl)"/>
  <rect x="830" y="0" width="70" height="88" fill="url(#fr)"/>
</svg>'''

    with open(f"{OUT}/belt.svg", "w") as f:
        f.write(svg)
    print("✓ belt.svg")


# regenerate all including belt
if __name__ == "__main__":
    gen_hero()
    gen_keyboard()
    gen_projects()
    gen_about()
    gen_belt()
    print("\nAll SVGs generated in ./assets/")
