#!/usr/bin/env python3
"""Generate self-contained profile SVGs. Python standard library only."""
from html import escape
from pathlib import Path
from random import Random

ROOT = Path(__file__).resolve().parents[1] / "assets"
BG, PANEL, CYAN, PINK, WHITE, MUTED = "#090b16", "#101525", "#56f4ff", "#ff4fa3", "#eff6ff", "#9caec7"


def text(x, y, value, size=14, color=MUTED, extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" {extra}>{escape(value)}</text>'


def svg(name, width, height, title, body, defs=""):
    ROOT.mkdir(exist_ok=True)
    (ROOT / name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<defs><style>text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',monospace}} .display{{font-family:Arial,Helvetica,sans-serif;font-weight:800}}</style>{defs}</defs>
{body}
</svg>\n''')


def banner():
    rng = Random(101)
    rain = []
    for i in range(48):
        x = i * 21 + 6
        duration, delay = rng.uniform(7, 14), rng.uniform(-16, 0)
        chars = "".join(rng.choice("01{}[]<>/GO+=:アイウエカキクケコ") for _ in range(18))
        stream = "".join(text(x, j * 20, ch, 13, PINK if i % 7 == 0 else CYAN,
                              f'opacity="{0.10 + j * 0.032:.3f}"') for j, ch in enumerate(chars))
        rain.append(f'<g class="rain" style="animation-duration:{duration:.2f}s;animation-delay:{delay:.2f}s;--rest:{rng.randrange(-300, 100)}px">{stream}</g>')
    defs = f'''
<linearGradient id="edge"><stop stop-color="{CYAN}"/><stop offset=".6" stop-color="#7b70ff"/><stop offset="1" stop-color="{PINK}"/></linearGradient>
<linearGradient id="veil"><stop stop-color="{BG}" stop-opacity=".93"/><stop offset=".62" stop-color="{BG}" stop-opacity=".8"/><stop offset="1" stop-color="{BG}" stop-opacity=".22"/></linearGradient>
<radialGradient id="aura"><stop stop-color="#213f60" stop-opacity=".55"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#536686" stroke-opacity=".12"/></pattern>
<clipPath id="bounds"><rect x="1" y="1" width="958" height="378" rx="5"/></clipPath>
<style>
@keyframes rainfall{{from{{transform:translateY(-370px)}}to{{transform:translateY(400px)}}}}
@keyframes orbit{{to{{transform:rotate(360deg)}}}}
@keyframes signal{{0%,100%{{opacity:.4}}50%{{opacity:1}}}}
.rain{{animation:rainfall linear infinite;transform:translateY(var(--rest))}}
.orbit{{transform-origin:790px 183px;animation:orbit 36s linear infinite}}
.signal{{animation:signal 4s ease-in-out infinite}}
@media(prefers-reduced-motion:reduce){{.rain,.orbit,.signal{{animation:none}}}}
</style>'''
    body = f'<rect width="960" height="380" rx="6" fill="{BG}"/>'
    body += '<g clip-path="url(#bounds)"><rect width="960" height="380" fill="url(#grid)"/>'
    body += "".join(rain)
    body += '<rect width="960" height="380" fill="url(#veil)"/><ellipse cx="790" cy="183" rx="220" ry="205" fill="url(#aura)"/>'
    body += f'<path d="M650 93H702L724 71H899M650 273H703L725 295H914" fill="none" stroke="{CYAN}" opacity=".25"/>'
    body += f'<circle cx="790" cy="183" r="94" fill="none" stroke="{CYAN}" stroke-opacity=".18"/>'
    body += f'<circle class="orbit" cx="790" cy="183" r="107" fill="none" stroke="{PINK}" stroke-width="2" stroke-dasharray="66 32 3 120 32 420"/>'
    body += f'<path d="M731 119H834L850 135V231L834 247H731L715 231V135Z" fill="{PANEL}" stroke="{CYAN}" stroke-opacity=".6"/>'
    body += text(781, 201, "Go", 65, CYAN, 'class="display" text-anchor="middle" font-style="italic"')
    body += text(782, 227, "BACKEND CORE", 10, MUTED, 'text-anchor="middle" letter-spacing="2"')
    body += f'<path d="M691 168H713M685 183H713M695 198H713" stroke="{CYAN}" stroke-width="3"/>'
    body += text(40, 40, "VLBL / SOFTWARE ENGINEERING", 12, CYAN, 'letter-spacing="2"')
    body += f'<circle class="signal" cx="771" cy="35" r="3" fill="{CYAN}"/>'
    body += text(785, 40, "HCMC, VIETNAM", 12, MUTED)
    body += text(40, 110, "BACKEND SYSTEMS. REAL-WORLD PRODUCTS.", 12, MUTED, 'letter-spacing="1.5"')
    body += text(38, 185, "VU LE BAO", 68, WHITE, 'class="display" letter-spacing="-2"')
    body += text(38, 255, "LONG", 78, WHITE, 'class="display" letter-spacing="-2"')
    body += text(266, 255, ".", 78, PINK, 'class="display"')
    body += f'<path d="M42 278H94" stroke="{PINK}" stroke-width="3"/>'
    body += text(110, 284, "Go Backend & Full-Stack Engineer", 18, CYAN)
    body += f'<path d="M40 316H920" stroke="#263147"/>'
    body += text(40, 349, "Go / gRPC / Real-time / AI", 13, WHITE)
    body += text(920, 349, "IDEA → API → PRODUCTION", 12, MUTED, 'text-anchor="end"')
    body += '</g><rect x=".5" y=".5" width="959" height="379" rx="6" fill="none" stroke="#2c3450"/><path d="M1 1H959" stroke="url(#edge)" stroke-width="2"/>'
    svg("cyberpunk-banner.svg", 960, 380, "Vu Le Bao Long — Go Backend & Full-Stack Engineer. Animated cyan and magenta matrix rain.", body, defs)
    still = '<style>.rain,.orbit,.signal{animation:none!important}</style>'
    svg("cyberpunk-banner-static.svg", 960, 380, "Vu Le Bao Long — Go Backend & Full-Stack Engineer", body, defs + still)
    mobile = f'<rect width="480" height="360" rx="6" fill="{BG}"/>'
    mobile += '<g clip-path="url(#mobile-bounds)"><rect width="480" height="360" fill="url(#grid)"/>' + "".join(rain[:24])
    mobile += '<rect width="480" height="360" fill="url(#veil)"/>'
    mobile += text(24, 37, "VLBL / SOFTWARE ENGINEERING", 11, CYAN, 'letter-spacing="1"')
    mobile += text(24, 85, "GO BACKEND & FULL-STACK ENGINEER", 13, CYAN)
    mobile += text(22, 160, "VU LE BAO", 65, WHITE, 'class="display" letter-spacing="-2"')
    mobile += text(22, 234, "LONG.", 78, WHITE, 'class="display" letter-spacing="-2"')
    mobile += f'<path d="M24 258H78" stroke="{PINK}" stroke-width="3"/>'
    mobile += text(24, 293, "Go / gRPC / Real-time / AI", 16, WHITE)
    mobile += text(24, 331, "HO CHI MINH CITY, VIETNAM", 12, MUTED, 'letter-spacing="1"')
    mobile += '</g><rect x=".5" y=".5" width="479" height="359" rx="6" fill="none" stroke="#2c3450"/><path d="M1 1H479" stroke="url(#edge)" stroke-width="2"/>'
    svg("cyberpunk-banner-mobile.svg", 480, 360, "Vu Le Bao Long — Go Backend & Full-Stack Engineer", mobile,
        defs + '<clipPath id="mobile-bounds"><rect width="480" height="360" rx="6"/></clipPath>')
    svg("cyberpunk-banner-mobile-static.svg", 480, 360, "Vu Le Bao Long — Go Backend & Full-Stack Engineer", mobile,
        defs + '<clipPath id="mobile-bounds"><rect width="480" height="360" rx="6"/></clipPath>' + still)


def section(name, index, title, subtitle):
    body = f'<rect width="960" height="62" rx="4" fill="{BG}"/><path d="M0 1H960" stroke="#27334b"/><path d="M0 1H88" stroke="{CYAN}" stroke-width="2"/>'
    body += text(20, 39, index, 15, PINK)
    body += text(66, 40, title, 22, WHITE, 'class="display" letter-spacing="1"')
    body += text(938, 38, subtitle, 11, MUTED, 'text-anchor="end" letter-spacing="1"')
    svg(f"section-{name}.svg", 960, 62, title, body)
    mobile = f'<rect width="480" height="62" rx="4" fill="{BG}"/><path d="M0 1H480" stroke="#27334b"/><path d="M0 1H64" stroke="{CYAN}" stroke-width="2"/>'
    mobile += text(18, 39, index, 15, PINK) + text(60, 40, title, 22, WHITE, 'class="display" letter-spacing="1"')
    svg(f"section-{name}-mobile.svg", 480, 62, title, mobile)


def project(name, title, category, accent, nodes):
    body = f'<rect width="460" height="144" rx="4" fill="{BG}"/><path d="M0 1H460" stroke="{accent}" stroke-width="2"/>'
    body += text(22, 29, category, 10, accent, 'letter-spacing="1.4"')
    body += text(20, 70, title, 35 if len(title) < 17 else 29, WHITE, 'class="display"')
    for i, node in enumerate(nodes):
        x = 22 + i * 146
        body += f'<rect x="{x}" y="96" width="124" height="28" rx="3" fill="{PANEL}" stroke="#28364b"/>'
        body += text(x + 62, 114, node, 10, MUTED, 'text-anchor="middle"')
        if i < 2:
            body += f'<path d="M{x+125} 110h19m-4-3 4 3-4 3" fill="none" stroke="{accent}"/>'
    svg(f"project-{name}.svg", 460, 144, f"{title} — {category}", body)


def contact(name, label, accent):
    body = f'<rect x=".5" y=".5" width="143" height="35" rx="3" fill="{PANEL}" stroke="#34405b"/><path d="M1 1H33" stroke="{accent}" stroke-width="2"/>'
    body += text(72, 23, label, 12, WHITE, 'text-anchor="middle" letter-spacing="1"')
    svg(f"link-{name}.svg", 144, 36, label, body)


if __name__ == "__main__":
    banner()
    for args in [("about", "01", "ENGINEER PROFILE", "GO AT THE CORE"),
                 ("projects", "02", "SELECTED WORK", "PRODUCTS + OPEN SOURCE"),
                 ("stack", "03", "TECH STACK", "BUILD / SHIP / OPERATE"),
                 ("activity", "04", "CONTRIBUTION SIGNAL", "GITHUB ACTIVITY")]:
        section(*args)
    project("predix", "PrediX", "GO / MICROSERVICES", CYAN, ["REST / gRPC", "GO SERVICES", "DATA + RAG"])
    project("megapro", "MegaPro", "GO / AI + REAL-TIME", PINK, ["KNOWLEDGE", "GO + RAG", "STREAMING"])
    project("deploy-kit", "deploy-kit", "GO / DEVELOPER TOOLING", CYAN, ["YAML CONFIG", "DOCKER BUILD", "SSH DEPLOY"])
    project("observability", "observability-stack", "INFRA / CONTAINER LOGGING", PINK, ["ALLOY", "LOKI", "GRAFANA"])
    for args in [("portfolio", "PORTFOLIO ↗", CYAN), ("email", "EMAIL ↗", PINK),
                 ("linkedin", "LINKEDIN ↗", CYAN), ("resume", "RESUME ↗", PINK)]:
        contact(*args)
    svg("footer.svg", 960, 86, "Let's build something that works in the real world.",
        f'<rect width="960" height="86" rx="4" fill="{BG}"/><path d="M0 0H960" stroke="#303752"/>'
        + text(480, 38, "LET’S BUILD SOMETHING THAT WORKS IN THE REAL WORLD.", 17, WHITE, 'text-anchor="middle" class="display"')
        + text(480, 64, "vulebaolong.com  /  Go. Systems. Product.", 12, CYAN, 'text-anchor="middle"'))
