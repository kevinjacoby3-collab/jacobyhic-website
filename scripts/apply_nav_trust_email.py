#!/usr/bin/env python3
"""Trust bar (not index), Services dropdown on all pages, mailto + remove CF email artifacts."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIL = "jacobyhomeimprovements@gmail.com"
MAILTO = f"mailto:{MAIL}"
CF_SCRIPT = '<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>'

DROP_CSS_MIN = (
    ".nav-dropdown{position:relative}"
    ".nav-dropdown-toggle{cursor:pointer;color:rgba(255,255,255,0.85);font-size:0.95rem;font-weight:500;padding:0.5rem 1rem;border-radius:6px;transition:all 0.2s;display:inline-flex;align-items:center;gap:0.25rem;background:none;border:none;font-family:inherit;line-height:inherit}"
    ".nav-dropdown-toggle:hover,.nav-dropdown:focus-within .nav-dropdown-toggle{color:#fff;background:rgba(255,255,255,0.08)}"
    ".nav-dropdown-menu{display:none;position:absolute;top:100%;left:0;min-width:230px;padding:0.4rem 0;background:var(--navy-dark);border-radius:8px;box-shadow:0 12px 32px rgba(0,0,0,0.25);z-index:200;flex-direction:column}"
    ".nav-dropdown:hover .nav-dropdown-menu,.nav-dropdown:focus-within .nav-dropdown-menu{display:flex}"
    ".nav-dropdown-menu a{color:rgba(255,255,255,0.9)!important;padding:0.55rem 1.1rem;border-radius:0;font-weight:500}"
    ".nav-dropdown-menu a:hover{background:rgba(255,255,255,0.08)}"
    ".nav-dropdown-menu a.active{color:#fff!important;background:rgba(255,255,255,0.1)}"
    ".nav-mobile-group-label{font-size:0.72rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:rgba(255,255,255,0.45);padding:0.6rem 1rem 0.2rem;display:block}"
    ".nav-mobile-menu a.active{color:#fff;background:rgba(255,255,255,0.08)}"
    ".nav-mobile-menu .btn-teal.active{box-shadow:inset 0 0 0 2px rgba(255,255,255,0.2)}"
)

DROP_CSS_INDEX = """
    .nav-dropdown { position: relative; }
    .nav-dropdown-toggle {
      cursor: pointer; color: rgba(255,255,255,0.85); font-size: 0.95rem; font-weight: 500;
      padding: 0.5rem 1rem; border-radius: 6px; transition: all 0.2s; display: inline-flex;
      align-items: center; gap: 0.25rem; background: none; border: none; font-family: inherit; line-height: inherit;
    }
    .nav-dropdown-toggle:hover, .nav-dropdown:focus-within .nav-dropdown-toggle {
      color: #fff; background: rgba(255,255,255,0.08);
    }
    .nav-dropdown-menu {
      display: none; position: absolute; top: 100%; left: 0; min-width: 230px; padding: 0.4rem 0;
      background: var(--navy-dark); border-radius: 8px; box-shadow: 0 12px 32px rgba(0,0,0,0.25);
      z-index: 200; flex-direction: column;
    }
    .nav-dropdown:hover .nav-dropdown-menu, .nav-dropdown:focus-within .nav-dropdown-menu { display: flex; }
    .nav-dropdown-menu a { color: rgba(255,255,255,0.9) !important; padding: 0.55rem 1.1rem; border-radius: 0; font-weight: 500; }
    .nav-dropdown-menu a:hover { background: rgba(255,255,255,0.08); }
    .nav-dropdown-menu a.active { color: #fff !important; background: rgba(255,255,255,0.1); }
    .nav-mobile-group-label {
      font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;
      color: rgba(255,255,255,0.45); padding: 0.6rem 1rem 0.2rem; display: block;
    }
    .nav-mobile-menu a.active { color: #fff; background: rgba(255,255,255,0.08); }
"""

TRUST_CSS_MIN = (
    ".trust-bar{background:var(--cream);padding:2.5rem 0;border-top:1px solid var(--gray-200);border-bottom:1px solid var(--gray-200)}"
    ".trust-items{display:flex;justify-content:center;align-items:center;gap:3rem;flex-wrap:wrap}"
    ".trust-items img{height:50px;width:auto;opacity:0.85;transition:opacity 0.2s}"
    ".trust-items img:hover{opacity:1}"
    ".trust-items a{display:block}"
)

NAV_LINKS_RE = re.compile(
    r'<div class="nav-links">\s*'
    r'<a\s+href="/kitchen-remodeling\.html"[^>]*>\s*Kitchen Remodeling\s*</a>\s*'
    r'<a\s+href="/bathroom-remodeling\.html"[^>]*>\s*Bathroom Remodeling\s*</a>\s*'
    r'<a\s+href="/portfolio\.html"[^>]*>\s*Portfolio\s*</a>\s*'
    r'<a\s+href="/blog/"[^>]*>\s*Blog\s*</a>\s*'
    r'<a\s+href="/contact\.html"[^>]*>\s*Free Estimate\s*</a>\s*'
    r"</div>",
    re.DOTALL,
)

NAV_MOBILE_RE = re.compile(
    r'<div class="nav-mobile-menu">\s*'
    r'<a\s+href="/kitchen-remodeling\.html"[^>]*>\s*Kitchen Remodeling\s*</a>\s*'
    r'<a\s+href="/bathroom-remodeling\.html"[^>]*>\s*Bathroom Remodeling\s*</a>\s*'
    r'<a\s+href="/portfolio\.html"[^>]*>\s*Portfolio\s*</a>\s*'
    r'<a\s+href="/blog/"[^>]*>\s*Blog\s*</a>\s*'
    r'<a\s+href="/contact\.html"[^>]*>\s*Get a Free Estimate\s*</a>\s*'
    r"</div>",
    re.DOTALL,
)

CF_ANCHOR_SPAN_RE = re.compile(
    r'<a\s+href="/cdn-cgi/l/email-protection[^"]*">\s*<span class="__cf_email__"[^>]*>.*?</span>\s*</a>',
    re.DOTALL,
)
MAILTO_CF_SPAN_RE = re.compile(
    r'<a\s+href="' + re.escape(MAILTO) + r'">\s*<span class="__cf_email__"[^>]*>.*?</span>\s*</a>',
    re.DOTALL,
)


def ac(on: bool) -> str:
    return ' class="active"' if on else ""


def desktop_inner_min(path: Path) -> str:
    s, par = path.name, path.parent.name
    cta = (
        ' class="nav-cta active"'
        if s == "contact.html"
        else " class=\"nav-cta\""
    )
    return (
        '<div class="nav-dropdown">'
        '<button type="button" class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Services</button>'
        '<div class="nav-dropdown-menu" role="menu">'
        f'<a href="/kitchen-remodeling.html" role="menuitem"{ac(s == "kitchen-remodeling.html")}>Kitchen Remodeling</a>'
        f'<a href="/bathroom-remodeling.html" role="menuitem"{ac(s == "bathroom-remodeling.html")}>Bathroom Remodeling</a>'
        f'<a href="/portfolio.html" role="menuitem"{ac(s == "portfolio.html")}>Portfolio</a>'
        "</div></div>"
        f'<a href="/blog/"{ac(s == "index.html" and par == "blog")}>Blog</a>'
        f'<a href="/contact.html"{cta}>Free Estimate</a>'
    )


def desktop_inner_pretty(path: Path) -> str:
    s, par = path.name, path.parent.name
    line_cta = (
        '        <a href="/contact.html" class="nav-cta active">Free Estimate</a>\n'
        if s == "contact.html"
        else '        <a href="/contact.html" class="nav-cta">Free Estimate</a>\n'
    )
    return (
        "      <div class=\"nav-links\">\n"
        "        <div class=\"nav-dropdown\">\n"
        "          <button type=\"button\" class=\"nav-dropdown-toggle\" aria-expanded=\"false\" aria-haspopup=\"true\">Services</button>\n"
        "          <div class=\"nav-dropdown-menu\" role=\"menu\">\n"
        f"            <a href=\"/kitchen-remodeling.html\" role=\"menuitem\"{ac(s == 'kitchen-remodeling.html')}>Kitchen Remodeling</a>\n"
        f"            <a href=\"/bathroom-remodeling.html\" role=\"menuitem\"{ac(s == 'bathroom-remodeling.html')}>Bathroom Remodeling</a>\n"
        f"            <a href=\"/portfolio.html\" role=\"menuitem\"{ac(s == 'portfolio.html')}>Portfolio</a>\n"
        "          </div>\n"
        "        </div>\n"
        f"        <a href=\"/blog/\"{ac(s == 'index.html' and par == 'blog')}>Blog</a>\n"
        f"{line_cta}"
        "      </div>"
    )


def desktop_inner_index() -> str:
    return (
        "      <div class=\"nav-links\">\n"
        "        <div class=\"nav-dropdown\">\n"
        "          <button type=\"button\" class=\"nav-dropdown-toggle\" aria-expanded=\"false\" aria-haspopup=\"true\">Services</button>\n"
        "          <div class=\"nav-dropdown-menu\" role=\"menu\">\n"
        "            <a href=\"/kitchen-remodeling.html\" role=\"menuitem\">Kitchen Remodeling</a>\n"
        "            <a href=\"/bathroom-remodeling.html\" role=\"menuitem\">Bathroom Remodeling</a>\n"
        "            <a href=\"/portfolio.html\" role=\"menuitem\">Portfolio</a>\n"
        "          </div>\n"
        "        </div>\n"
        "        <a href=\"/blog/\">Blog</a>\n"
        "        <a href=\"/contact.html\" class=\"nav-cta\">Free Estimate</a>\n"
        "      </div>"
    )


def mobile_attrs(path: Path) -> tuple[str, str, str, str]:
    s, par = path.name, path.parent.name
    return (
        ac(s == "kitchen-remodeling.html"),
        ac(s == "bathroom-remodeling.html"),
        ac(s == "portfolio.html"),
        ac(s == "index.html" and par == "blog"),
    )


def mobile_inner_min(path: Path) -> str:
    k, b, p, bl = mobile_attrs(path)
    cta = ' class="btn btn-teal active"' if path.name == "contact.html" else ' class="btn btn-teal"'
    return (
        '<div class="nav-mobile-menu">'
        '<span class="nav-mobile-group-label">Services</span>'
        f'<a href="/kitchen-remodeling.html"{k}>Kitchen Remodeling</a>'
        f'<a href="/bathroom-remodeling.html"{b}>Bathroom Remodeling</a>'
        f'<a href="/portfolio.html"{p}>Portfolio</a>'
        f'<a href="/blog/"{bl}>Blog</a>'
        f'<a href="/contact.html"{cta} style="text-align:center;margin-top:0.5rem;">Get a Free Estimate</a>'
        "</div>"
    )


def mobile_inner_pretty(path: Path, *, onclick: bool, btn_gold: bool) -> str:
    k, b, p, bl = mobile_attrs(path)
    oc = ' onclick="this.parentElement.classList.remove(\'open\')"' if onclick else ""
    cta_cls = "btn btn-gold" if btn_gold else "btn btn-teal"
    extra = " active" if path.name == "contact.html" else ""
    return (
        f'<div class="nav-mobile-menu">\n'
        f'    <span class="nav-mobile-group-label">Services</span>\n'
        f'    <a href="/kitchen-remodeling.html"{oc}{k}>Kitchen Remodeling</a>\n'
        f'    <a href="/bathroom-remodeling.html"{oc}{b}>Bathroom Remodeling</a>\n'
        f'    <a href="/portfolio.html"{oc}{p}>Portfolio</a>\n'
        f'    <a href="/blog/"{oc}{bl}>Blog</a>\n'
        f'    <a href="/contact.html" class="{cta_cls}{extra}" style="text-align:center;margin-top:0.5rem;"'
        f'{oc}>Get a Free Estimate</a>\n'
        f"  </div>"
    )


def mobile_inner_kitchen_page() -> str:
    oc = ' onclick="this.parentElement.classList.remove(\'open\')"'
    return (
        f'<div class="nav-mobile-menu">\n'
        f'    <span class="nav-mobile-group-label">Services</span>\n'
        f'    <a href="/kitchen-remodeling.html"{oc} class="active">Kitchen Remodeling</a>\n'
        f'    <a href="/bathroom-remodeling.html"{oc}>Bathroom Remodeling</a>\n'
        f'    <a href="/portfolio.html"{oc}>Portfolio</a>\n'
        f'    <a href="/blog/"{oc}>Blog</a>\n'
        f'    <a href="/contact.html" class="btn btn-teal" style="text-align:center;margin-top:0.5rem;"'
        f'{oc}>Get a Free Estimate</a>\n'
        f"  </div>"
    )


def trust_block(path: Path) -> str:
    prefix = "../" if path.parent.name in ("blog", "areas") else ""
    return (
        "\n\n  <!-- TRUST BAR -->\n"
        "  <div class=\"trust-bar\">\n"
        "    <div class=\"container\">\n"
        "      <div class=\"trust-items\">\n"
        "        <a href=\"http://g.page/r/CdWXsDVRB3EwEAI/review\" target=\"_blank\" rel=\"noopener\">\n"
        f"          <img src=\"{prefix}images/google-reviews.png\" alt=\"Google Reviews - 5 Stars\" />\n"
        "        </a>\n"
        f"        <img src=\"{prefix}images/fully-licensed.png\" alt=\"Fully Licensed and Insured\" />\n"
        "      </div>\n"
        "    </div>\n"
        "  </div>\n\n"
    )


def fix_emails(html: str) -> str:
    html = re.sub(
        r'href="/cdn-cgi/l/email-protection[^"]*"',
        f'href="{MAILTO}"',
        html,
    )
    html = html.replace(CF_SCRIPT, "")
    html = CF_ANCHOR_SPAN_RE.sub(f'<a href="{MAILTO}">{MAIL}</a>', html)
    html = MAILTO_CF_SPAN_RE.sub(f'<a href="{MAILTO}">{MAIL}</a>', html)
    return html


def inject_css(html: str, chunk: str) -> str:
    return html.replace("</style>", chunk + "\n</style>", 1)


def pretty_nav_pages(path: Path) -> bool:
    """Multiline nav markup (not single-line minified)."""
    if path.parent.name == "areas":
        return True
    if path.parent == ROOT and path.name in (
        "contact.html",
        "portfolio.html",
        "bathroom-remodeling.html",
        "kitchen-remodeling.html",
    ):
        return True
    if path.name == "index.html" and path.parent.name == "blog":
        return True
    return False


def process_file(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    html = fix_emails(html)

    is_home = path.name == "index.html" and path.parent == ROOT

    if not is_home:
        if "trust-bar" not in html:
            html = inject_css(html, TRUST_CSS_MIN)
        if "<!-- TRUST BAR -->" not in html:
            html = html.replace("<footer", trust_block(path) + "<footer", 1)

    if "nav-dropdown{" not in html:
        html = inject_css(html, DROP_CSS_INDEX if is_home else DROP_CSS_MIN)

    if is_home:
        html = html.replace(
            "      <div class=\"nav-links\">\n"
            "        <a href=\"/kitchen-remodeling.html\">Kitchen Remodeling</a>\n"
            "        <a href=\"/bathroom-remodeling.html\">Bathroom Remodeling</a>\n"
            "        <a href=\"/portfolio.html\">Portfolio</a>\n"
            "        <a href=\"/blog/\">Blog</a>\n"
            "        <a href=\"/contact.html\" class=\"nav-cta\">Free Estimate</a>\n"
            "      </div>",
            desktop_inner_index(),
        )
        html = html.replace(
            "  <div class=\"nav-mobile-menu\">\n"
            "    <a href=\"/kitchen-remodeling.html\" onclick=\"this.parentElement.classList.remove('open')\">Kitchen Remodeling</a>\n"
            "    <a href=\"/bathroom-remodeling.html\" onclick=\"this.parentElement.classList.remove('open')\">Bathroom Remodeling</a>\n"
            "    <a href=\"/portfolio.html\" onclick=\"this.parentElement.classList.remove('open')\">Portfolio</a>\n"
            "    <a href=\"/blog/\" onclick=\"this.parentElement.classList.remove('open')\">Blog</a>\n"
            "    <a href=\"/contact.html\" class=\"btn btn-gold\" style=\"text-align:center;margin-top:0.5rem;\" onclick=\"this.parentElement.classList.remove('open')\">Get a Free Estimate</a>\n"
            "  </div>",
            mobile_inner_pretty(path, onclick=True, btn_gold=True),
        )
        path.write_text(html, encoding="utf-8")
        return

    def repl_desktop(_: re.Match[str]) -> str:
        if pretty_nav_pages(path):
            return desktop_inner_pretty(path)
        return "<div class=\"nav-links\">" + desktop_inner_min(path) + "</div>"

    html, n = NAV_LINKS_RE.subn(repl_desktop, html, count=1)
    if n != 1:
        raise SystemExit(f"nav-links replace failed: {path}")

    def repl_mobile(_: re.Match[str]) -> str:
        if path.name == "kitchen-remodeling.html" and path.parent == ROOT:
            return mobile_inner_kitchen_page()
        if pretty_nav_pages(path):
            return mobile_inner_pretty(path, onclick=False, btn_gold=False)
        return mobile_inner_min(path)

    html, n2 = NAV_MOBILE_RE.subn(repl_mobile, html, count=1)
    if n2 != 1:
        raise SystemExit(f"nav-mobile replace failed: {path}")

    path.write_text(html, encoding="utf-8")


def main() -> None:
    files = sorted(
        list(ROOT.glob("*.html"))
        + list((ROOT / "areas").glob("*.html"))
        + list((ROOT / "blog").glob("*.html"))
    )
    for f in files:
        process_file(f)
    print(f"OK: {len(files)} files")


if __name__ == "__main__":
    main()
