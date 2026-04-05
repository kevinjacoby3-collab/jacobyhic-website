#!/usr/bin/env python3
"""Light top bar, nav, footer — WordPress-matching styles across all HTML files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TOP_MIN = (
    ".top-bar{font-size:0.85rem;padding:0;border-bottom:1px solid #2A4545}"
    ".top-bar-split{display:flex;width:100%;align-items:stretch;flex-wrap:wrap}"
    ".top-bar-left{flex:1 1 50%;min-width:min(100%,280px);background:#3D5A5A;color:#FFFFFF;padding:0.65rem 1.25rem;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.5}"
    ".top-bar-left a{color:#FFFFFF;font-weight:600;text-decoration:underline}"
    ".top-bar-left a:hover{color:#E8F0ED}"
    ".top-bar-right{flex:1 1 50%;min-width:min(100%,280px);background:#E8F0ED;color:#60A18B;padding:0.65rem 1.25rem;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.5}"
    ".top-bar .serving-text{color:#60A18B;font-weight:700}"
)

TOP_MIN_OLD_LIGHT = (
    ".top-bar{background:#E8F0ED;color:#4A4845;font-size:0.85rem;padding:0.6rem 0;border-bottom:1px solid #D1CFC9}"
    ".top-bar .container{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem}"
    ".top-bar a{color:#60A18B;font-weight:600}.top-bar a:hover{color:#4E8A75}"
    ".top-bar .serving-text{color:#60A18B;font-weight:700}"
)

NAV_MIN = (
    "nav{background:#FFFFFF;padding:1rem 0;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,0.08);border-bottom:1px solid #E8E6E1}"
    ".nav-inner{display:flex;align-items:center;justify-content:space-between;gap:2rem}"
    ".nav-logo img{height:55px;width:auto}"
    ".nav-links{display:flex;align-items:center;gap:0.5rem}"
    ".nav-links a{color:#2D2B28;font-size:0.95rem;font-weight:600;padding:0.5rem 1rem;border-radius:6px;transition:all 0.2s}"
    ".nav-links a:hover{color:#60A18B}"
    ".nav-links a.active{color:#60A18B}"
    ".nav-links .nav-dropdown-toggle{color:#2D2B28;font-size:0.95rem;font-weight:600;padding:0.5rem 1rem;border-radius:6px;transition:all 0.2s;background:none;border:none;font-family:inherit;cursor:pointer}"
    ".nav-links .nav-dropdown-toggle:hover{color:#60A18B}"
    ".nav-cta{background:#60A18B!important;color:#FFFFFF!important;font-weight:700;font-size:0.85rem;padding:0.85rem 2rem!important;border-radius:50px;transition:all 0.2s;white-space:nowrap;text-transform:uppercase;letter-spacing:0.05em}"
    ".nav-cta:hover{background:#4E8A75!important;transform:translateY(-1px)}"
    ".nav-facebook{display:flex;align-items:center;margin-left:1rem}"
    ".nav-facebook:hover svg{fill:#60A18B}"
    ".nav-hamburger{display:none;background:none;border:none;cursor:pointer;padding:0.5rem}"
    ".nav-hamburger span{display:block;width:24px;height:2px;background:#2D2B28;margin:5px 0;border-radius:2px;transition:all 0.3s}"
    ".nav-mobile-menu{display:none;background:#FFFFFF;padding:1rem 1.5rem 1.5rem;flex-direction:column;gap:0.25rem;border-bottom:1px solid #E8E6E1}"
    ".nav-mobile-menu.open{display:flex}"
    ".nav-mobile-menu a{color:#2D2B28;padding:0.75rem 1rem;border-radius:8px;font-size:1rem;font-weight:500}"
    ".nav-mobile-menu a:hover{background:#F7F7F5}"
    ".nav-mobile-group-label{font-size:0.72rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#8A8780;padding:0.6rem 1rem 0.2rem;display:block}"
)

DROP_MIN = (
    ".nav-dropdown{position:relative}.nav-dropdown-toggle{cursor:pointer}"
    ".nav-dropdown-menu{display:none;position:absolute;top:100%;left:0;background:#FFFFFF;border-radius:8px;padding:0.5rem 0;min-width:220px;box-shadow:0 8px 25px rgba(0,0,0,0.12);border:1px solid #E8E6E1;z-index:200}"
    ".nav-dropdown:hover .nav-dropdown-menu,.nav-dropdown:focus-within .nav-dropdown-menu{display:block}"
    ".nav-dropdown-menu a{display:block;padding:0.6rem 1.25rem;color:#2D2B28;font-size:0.9rem;white-space:nowrap}"
    ".nav-dropdown-menu a:hover{background:#F7F7F5;color:#60A18B}"
    ".nav-dropdown-menu a.active{color:#60A18B;font-weight:600}"
    ".nav-mobile-menu a.active{color:#60A18B;background:#F7F7F5}"
    ".nav-mobile-menu .btn-teal.active,.nav-mobile-menu .btn-gold.active{box-shadow:inset 0 0 0 2px rgba(96,161,139,0.35)}"
)

FOOT_MIN = (
    "footer{background:#FFFFFF;color:#4A4845;padding:4rem 0 0;border-top:1px solid #E8E6E1}"
    ".footer-grid{display:grid;grid-template-columns:1.2fr 1.5fr 1fr 1fr;gap:3rem;align-items:start}"
    ".footer-brand img{height:55px;width:auto;margin-bottom:1.5rem}"
    ".footer-brand-address{font-size:0.9rem;color:#60A18B;line-height:1.6;margin-bottom:1rem}"
    ".footer-brand-address a{color:#60A18B}"
    ".footer-brand-phone{font-size:0.9rem;margin-bottom:0.25rem}"
    ".footer-brand-phone strong{color:#2D2B28}"
    ".footer-brand-phone a{color:#2D2B28}"
    ".footer-brand-email a{color:#60A18B;font-weight:600;font-size:0.9rem}"
    ".footer-review-title{font-family:var(--font-display);font-weight:700;font-size:1.1rem;color:#2D2B28;margin:1.25rem 0 0.75rem}"
    ".footer-social-icons{display:flex;gap:1rem;align-items:center}"
    ".footer-social-icons a{color:#8A8780;font-size:1.2rem;transition:color 0.2s}"
    ".footer-social-icons a:hover{color:#60A18B}"
    ".footer-title{font-family:var(--font-display);font-weight:700;font-size:1.1rem;color:#60A18B;margin-bottom:1rem}"
    ".footer-serving-text{font-size:0.9rem;color:#6B6966;line-height:1.7;margin-bottom:1rem}"
    ".footer-areas-list{font-size:0.9rem;color:#4A4845;line-height:1.8}"
    ".footer-areas-list a{color:#60A18B}"
    ".footer-areas-list a:hover{text-decoration:underline}"
    ".footer-links{display:flex;flex-direction:column;gap:0.6rem}"
    ".footer-links a{color:#6B6966;font-size:0.9rem;transition:color 0.2s}"
    ".footer-links a:hover{color:#60A18B}"
    ".footer-cta-btn{display:inline-block;background:#60A18B;color:#FFFFFF;font-weight:700;font-size:0.85rem;padding:0.85rem 2rem;border-radius:50px;text-transform:uppercase;letter-spacing:0.05em;transition:all 0.2s;margin-top:1rem}"
    ".footer-cta-btn:hover{background:#4E8A75}"
    ".footer-bottom{border-top:1px solid #E8E6E1;margin-top:3rem;padding:1.5rem 0;display:flex;justify-content:space-between;align-items:center;font-size:0.8rem;color:#8A8780;flex-wrap:wrap;gap:0.5rem}"
    ".footer-bottom a{color:#8A8780}"
    ".footer-bottom a:hover{color:#60A18B}"
)

FB_MIN = '<a href="https://facebook.com/jacobyhomeimprovementsllc" target="_blank" rel="noopener" class="nav-facebook" aria-label="Facebook"><svg width="24" height="24" viewBox="0 0 24 24" fill="#2D2B28"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>'

FB_PRETTY = """      <a href="https://facebook.com/jacobyhomeimprovementsllc" target="_blank" rel="noopener" class="nav-facebook" aria-label="Facebook">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="#2D2B28"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>
      </a>
"""

NAV_MEDIA = "@media(max-width:768px){.nav-links{display:none}.nav-hamburger{display:block}}"


def footer_html(img_prefix: str) -> str:
    return f"""<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="{img_prefix}Jacoby-MainLogo.png" alt="Jacoby Home Improvements" />
        <div class="footer-brand-address">
          <a href="https://maps.app.goo.gl/SaB46UcR3EDMEUkH6" target="_blank">1642 Suzanne Drive<br>West Chester, Pennsylvania 19380</a>
        </div>
        <div class="footer-brand-phone"><strong>Phone:</strong> <a href="tel:+14849479097">(484) 947-9097</a></div>
        <div class="footer-brand-email"><a href="mailto:jacobyhomeimprovements@gmail.com">Send Us an Email</a></div>
        <div class="footer-review-title">Leave Us a Review</div>
        <div class="footer-social-icons">
          <a href="http://g.page/r/CdWXsDVRB3EwEAI/review" target="_blank" rel="noopener" aria-label="Google">G</a>
          <a href="https://facebook.com/jacobyhomeimprovementsllc/reviews" target="_blank" rel="noopener" aria-label="Facebook">f</a>
          <a href="http://yelp.com/" target="_blank" rel="noopener" aria-label="Yelp">Y</a>
        </div>
      </div>
      <div>
        <div class="footer-title">Proudly Serving West Chester and Beyond</div>
        <div class="footer-serving-text">Jacoby Home Improvements LLC is proud to serve West Chester, PA, and the surrounding communities. If your town isn't listed, don't worry—just give us a call to see if we can bring our services to your area!</div>
      </div>
      <div>
        <div class="footer-areas-list">
          We're your go-to kitchen and bathroom remodeling contractor in:<br><br>
          West Chester<br>
          <a href="/areas/phoenixville.html">Phoenixville</a><br>
          <a href="/areas/downingtown.html">Downingtown</a><br>
          <a href="/areas/exton.html">Exton</a><br>
          <a href="/areas/chester-springs.html">Chester Springs</a><br>
          <a href="/areas/malvern.html">Malvern</a><br>
          Frazer<br>
          <a href="/areas/coatesville.html">Coatesville</a><br>
          <a href="/areas/kennett-square.html">Kennett Square</a><br>
          Paoli<br>
          Devon<br>
          West Grove<br>
          Unionville<br>
          <a href="/areas/glen-mills.html">Glen Mills</a>
        </div>
      </div>
      <div>
        <a href="/contact.html" class="footer-cta-btn">Request an Estimate</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Jacoby Home Improvements LLC. All rights reserved.</span>
      <div>
        <a href="/privacy-policy.html">Privacy Policy</a> &nbsp;
        <a href="/terms.html">Terms & Conditions</a>
      </div>
    </div>
  </div>
</footer>"""


TOP_BAR_HTML_MIN = (
    '<div class="top-bar"><div class="top-bar-split"><div class="top-bar-left">'
    "Contact Us Today! Call us <a href=\"tel:+14849479097\">(484) 947-9097</a> or "
    '<a href="mailto:jacobyhomeimprovements@gmail.com">email us</a>.</div>'
    '<div class="top-bar-right"><span class="serving-text">Serving West Chester & Surrounding Areas</span></div></div></div>'
)

TOP_BAR_HTML_PRETTY = """  <div class="top-bar">
    <div class="top-bar-split">
      <div class="top-bar-left">
        Contact Us Today! Call us <a href="tel:+14849479097">(484) 947-9097</a> or <a href="mailto:jacobyhomeimprovements@gmail.com">email us</a>.
      </div>
      <div class="top-bar-right">
        <span class="serving-text">Serving West Chester & Surrounding Areas</span>
      </div>
    </div>
  </div>"""


def serving_html(t: str, *, pretty: bool = False) -> str:
    if "top-bar-split" in t:
        return t
    repl = TOP_BAR_HTML_PRETTY if pretty else TOP_BAR_HTML_MIN
    t = re.sub(
        r'<div class="top-bar">\s*<div class="container">[\s\S]*?</div>\s*</div>',
        repl,
        t,
        count=1,
    )
    return t


def nav_text(t: str) -> str:
    t = t.replace('class="nav-cta">Free Estimate</a>', 'class="nav-cta">REQUEST AN ESTIMATE</a>')
    t = t.replace('class="nav-cta active">Free Estimate</a>', 'class="nav-cta active">REQUEST AN ESTIMATE</a>')
    t = re.sub(
        r'(<a href="/contact\.html"[^>]*>)Get a Free Estimate(</a>)',
        r"\1REQUEST AN ESTIMATE\2",
        t,
    )
    return t


def insert_fb(t: str) -> str:
    if 'class="nav-facebook"' in t:
        return t
    if "</div>\n      <button class=\"nav-hamburger\"" in t:
        return t.replace(
            "</div>\n      <button class=\"nav-hamburger\"",
            "</div>\n" + FB_PRETTY + "      <button class=\"nav-hamburger\"",
            1,
        )
    if "</div>\n    <button class=\"nav-hamburger\"" in t:
        return t.replace(
            "</div>\n    <button class=\"nav-hamburger\"",
            "</div>\n    " + FB_MIN + "\n    <button class=\"nav-hamburger\"",
            1,
        )
    if "</div><button class=\"nav-hamburger\"" in t:
        return t.replace(
            "</div><button class=\"nav-hamburger\"",
            "</div>" + FB_MIN + "<button class=\"nav-hamburger\"",
            1,
        )
    raise RuntimeError("nav-facebook insert failed")


def patch_css_common(t: str) -> str:
    if re.search(r"\.top-bar\{background:var\(--navy-dark\)", t):
        t = re.sub(
            r"\.top-bar\{background:var\(--navy-dark\)[\s\S]*?(?=\s*nav\{)",
            TOP_MIN + "\n    ",
            t,
            count=1,
        )
    if re.search(r"nav\{background:var\(--navy\)", t):
        t = re.sub(
            r"nav\{background:var\(--navy\)[\s\S]*?@media\(max-width:768px\)\{\.nav-links\{display:none\}\.nav-hamburger\{display:block\}\}",
            NAV_MIN + NAV_MEDIA,
            t,
            count=1,
        )

    def foot_sub(m: re.Match[str]) -> str:
        return FOOT_MIN + "@media(max-width:768px){.footer-grid{grid-template-columns:1fr 1fr;gap:2rem}}@media(max-width:480px){.footer-grid{grid-template-columns:1fr}}"

    if re.search(r"footer\{background:var\(--navy-dark\)", t):
        t2, n = re.subn(
            r"footer\{background:var\(--navy-dark\)[\s\S]*?@media\(max-width:480px\)\{\.footer-grid\{grid-template-columns:1fr\}\}",
            foot_sub,
            t,
            count=1,
        )
        if n:
            t = t2
        else:
            t3, n2 = re.subn(
                r"footer\{background:var\(--navy-dark\)[\s\S]*?@media\(max-width:480px\)\{\.footer-grid\{grid-template-columns:1fr\}\}",
                lambda m: FOOT_MIN
                + "@media(max-width:768px){.footer-grid{grid-template-columns:1fr 1fr;gap:2rem}.blog-post .featured-img{height:280px}}@media(max-width:480px){.footer-grid{grid-template-columns:1fr}}",
                t,
                count=1,
            )
            if n2:
                t = t3

    if re.search(r"\.nav-dropdown\{position:relative\}", t) and "nav-dropdown-menu{background:#FFFFFF" not in t.replace(
        " ", ""
    ):
        t = re.sub(
            r"\.nav-dropdown\{position:relative\}[\s\S]*?(?=</style>)",
            DROP_MIN + "\n",
            t,
            count=1,
        )
    if TOP_MIN_OLD_LIGHT in t:
        t = t.replace(TOP_MIN_OLD_LIGHT, TOP_MIN)
    return t


def process_file(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    img_p = "../" if rel.parts[0] in ("blog", "areas") else ""

    pretty_top = path.parent == ROOT and path.name in ("index.html", "kitchen-remodeling.html")
    t = serving_html(t, pretty=pretty_top)
    t = nav_text(t)
    t = re.sub(r"<footer>[\s\S]*?</footer>", footer_html(img_p), t, count=1)
    t = insert_fb(t)

    if path.name == "index.html" and path.parent == ROOT:
        t = patch_index_css(t)
    else:
        t = patch_css_common(t)

    path.write_text(t, encoding="utf-8")


def patch_index_css(t: str) -> str:
    """index.html has a different CSS section order (trust bar before footer rules)."""
    top_new = """    /* ===== TOP BAR ===== */
    .top-bar {
      font-size: 0.85rem;
      padding: 0;
      border-bottom: 1px solid #2A4545;
    }
    .top-bar-split {
      display: flex;
      width: 100%;
      align-items: stretch;
      flex-wrap: wrap;
    }
    .top-bar-left {
      flex: 1 1 50%;
      min-width: min(100%, 280px);
      background: #3D5A5A;
      color: #FFFFFF;
      padding: 0.65rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      line-height: 1.5;
    }
    .top-bar-left a {
      color: #FFFFFF;
      font-weight: 600;
      text-decoration: underline;
    }
    .top-bar-left a:hover {
      color: #E8F0ED;
    }
    .top-bar-right {
      flex: 1 1 50%;
      min-width: min(100%, 280px);
      background: #E8F0ED;
      color: #60A18B;
      padding: 0.65rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      line-height: 1.5;
    }
    .top-bar .serving-text {
      color: #60A18B;
      font-weight: 700;
    }
"""
    nav_new = """    /* ===== NAV ===== */
    nav {
      background: #FFFFFF;
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.08);
      border-bottom: 1px solid #E8E6E1;
    }
    .nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 2rem;
    }
    .nav-logo img {
      height: 55px;
      width: auto;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .nav-links a {
      color: #2D2B28;
      font-size: 0.95rem;
      font-weight: 600;
      padding: 0.5rem 1rem;
      border-radius: 6px;
      transition: all 0.2s;
    }
    .nav-links a:hover {
      color: #60A18B;
    }
    .nav-links a.active {
      color: #60A18B;
    }
    .nav-links .nav-dropdown-toggle {
      color: #2D2B28;
      font-size: 0.95rem;
      font-weight: 600;
      padding: 0.5rem 1rem;
      border-radius: 6px;
      transition: all 0.2s;
      background: none;
      border: none;
      font-family: inherit;
      cursor: pointer;
    }
    .nav-links .nav-dropdown-toggle:hover { color: #60A18B; }
    .nav-cta {
      background: #60A18B !important;
      color: #FFFFFF !important;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.85rem 2rem !important;
      border-radius: 50px;
      transition: all 0.2s;
      white-space: nowrap;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .nav-cta:hover {
      background: #4E8A75 !important;
      transform: translateY(-1px);
    }
    .nav-facebook { display: flex; align-items: center; margin-left: 1rem; }
    .nav-facebook:hover svg { fill: #60A18B; }
    .nav-hamburger {
      display: none;
      background: none;
      border: none;
      cursor: pointer;
      padding: 0.5rem;
    }
    .nav-hamburger span {
      display: block;
      width: 24px;
      height: 2px;
      background: #2D2B28;
      margin: 5px 0;
      border-radius: 2px;
      transition: all 0.3s;
    }
    .nav-mobile-menu {
      display: none;
      background: #FFFFFF;
      padding: 1rem 1.5rem 1.5rem;
      flex-direction: column;
      gap: 0.25rem;
      border-bottom: 1px solid #E8E6E1;
    }
    .nav-mobile-menu.open { display: flex; }
    .nav-mobile-menu a {
      color: #2D2B28;
      padding: 0.75rem 1rem;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: 500;
    }
    .nav-mobile-menu a:hover { background: #F7F7F5; }
    .nav-mobile-group-label {
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #8A8780;
      padding: 0.6rem 1rem 0.2rem;
      display: block;
    }
    @media (max-width: 768px) {
      .nav-links { display: none; }
      .nav-hamburger { display: block; }
    }

    .nav-dropdown { position: relative; }
    .nav-dropdown-toggle { cursor: pointer; }
    .nav-dropdown-menu {
      display: none;
      position: absolute;
      top: 100%;
      left: 0;
      background: #FFFFFF;
      border-radius: 8px;
      padding: 0.5rem 0;
      min-width: 220px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.12);
      border: 1px solid #E8E6E1;
      z-index: 200;
    }
    .nav-dropdown:hover .nav-dropdown-menu,
    .nav-dropdown:focus-within .nav-dropdown-menu { display: block; }
    .nav-dropdown-menu a {
      display: block;
      padding: 0.6rem 1.25rem;
      color: #2D2B28;
      font-size: 0.9rem;
      white-space: nowrap;
    }
    .nav-dropdown-menu a:hover { background: #F7F7F5; color: #60A18B; }
    .nav-mobile-menu a.active { color: #60A18B; background: #F7F7F5; }
"""
    foot_new = """    /* ===== FOOTER ===== */
    footer {
      background: #FFFFFF;
      color: #4A4845;
      padding: 4rem 0 0;
      border-top: 1px solid #E8E6E1;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.2fr 1.5fr 1fr 1fr;
      gap: 3rem;
      align-items: start;
    }
    .footer-brand img {
      height: 55px;
      width: auto;
      margin-bottom: 1.5rem;
    }
    .footer-brand-address {
      font-size: 0.9rem;
      color: #60A18B;
      line-height: 1.6;
      margin-bottom: 1rem;
    }
    .footer-brand-address a { color: #60A18B; }
    .footer-brand-phone { font-size: 0.9rem; margin-bottom: 0.25rem; }
    .footer-brand-phone strong { color: #2D2B28; }
    .footer-brand-phone a { color: #2D2B28; }
    .footer-brand-email a { color: #60A18B; font-weight: 600; font-size: 0.9rem; }
    .footer-review-title {
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.1rem;
      color: #2D2B28;
      margin: 1.25rem 0 0.75rem;
    }
    .footer-social-icons {
      display: flex;
      gap: 1rem;
      align-items: center;
    }
    .footer-social-icons a {
      color: #8A8780;
      font-size: 1.2rem;
      transition: color 0.2s;
    }
    .footer-social-icons a:hover { color: #60A18B; }
    .footer-title {
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.1rem;
      color: #60A18B;
      margin-bottom: 1rem;
    }
    .footer-serving-text {
      font-size: 0.9rem;
      color: #6B6966;
      line-height: 1.7;
      margin-bottom: 1rem;
    }
    .footer-areas-list {
      font-size: 0.9rem;
      color: #4A4845;
      line-height: 1.8;
    }
    .footer-areas-list a { color: #60A18B; }
    .footer-areas-list a:hover { text-decoration: underline; }
    .footer-links {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }
    .footer-links a {
      color: #6B6966;
      font-size: 0.9rem;
      transition: color 0.2s;
    }
    .footer-links a:hover { color: #60A18B; }
    .footer-cta-btn {
      display: inline-block;
      background: #60A18B;
      color: #FFFFFF;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.85rem 2rem;
      border-radius: 50px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      transition: all 0.2s;
      margin-top: 1rem;
    }
    .footer-cta-btn:hover { background: #4E8A75; }
    .footer-bottom {
      border-top: 1px solid #E8E6E1;
      margin-top: 3rem;
      padding: 1.5rem 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      color: #8A8780;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
    .footer-bottom a { color: #8A8780; }
    .footer-bottom a:hover { color: #60A18B; }

    @media (max-width: 768px) {
      .footer-grid { grid-template-columns: 1fr 1fr; gap: 2rem; }
    }
    @media (max-width: 480px) {
      .footer-grid { grid-template-columns: 1fr; }
    }
"""
    t = re.sub(
        r"/\* ===== TOP BAR ===== \*/[\s\S]*?(?=\s*/\* ===== NAV ===== \*/)",
        top_new,
        t,
        count=1,
    )
    t = re.sub(
        r"/\* ===== NAV ===== \*/[\s\S]*?(?=\s*/\* ===== HERO ===== \*/)",
        nav_new,
        t,
        count=1,
    )
    t = re.sub(
        r"/\* ===== FOOTER ===== \*/[\s\S]*?(?=\s*/\* ===== UTILITIES ===== \*/)",
        foot_new,
        t,
        count=1,
    )
    return t


def main() -> None:
    files = sorted(
        list(ROOT.glob("*.html"))
        + list((ROOT / "areas").glob("*.html"))
        + list((ROOT / "blog").glob("*.html"))
    )
    for f in files:
        process_file(f)
    print("OK", len(files))


if __name__ == "__main__":
    main()
