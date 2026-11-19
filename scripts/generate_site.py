#!/usr/bin/env python3
"""Generate static HTML pages for Free Unit Converter."""
from __future__ import annotations

import json
import os
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
SITE = "https://free-unit-converter.web-free.site"

ADS_JSON = {
    "site": SITE,
    "siteId": 6199237,
    "category": "Other",
    "units": {
        "popunder": {
            "id": 32266172,
            "script": "https://abscloud.org/1/d663f3e7cf615faaef43e82ad9998a89",
        },
        "native": {
            "id": 32266173,
            "script": "https://bauval.org/21/4cf21c450d84c873f155031633436df2",
            "container": "container-4cf21c450d84c873f155031633436df2",
        },
        "smartlink": {
            "id": 32266174,
            "url": "https://araplhn.org/4/96e688032e9c4620f919b84092a1ca49",
        },
        "socialBar": {
            "id": 32266175,
            "script": "https://bauval.org/14/2a9bb1ed5ab3ca36577a0c4f8288d3fd",
        },
        "banner728x90": {
            "id": 32266176,
            "key": "dbca6215ee53e3c32b13519ff8dbe67c",
            "width": 728,
            "height": 90,
            "src": "https://bauval.org/22/dbca6215ee53e3c32b13519ff8dbe67c",
        },
        "banner468x60": {
            "id": 32266177,
            "key": "6df9e4dcd1b7ffe213239b9f339c517c",
            "width": 468,
            "height": 60,
            "src": "https://bauval.org/22/6df9e4dcd1b7ffe213239b9f339c517c",
        },
        "banner320x50": {
            "id": 32266178,
            "key": "1fbeac751a7ab02213e2043bf4d93396",
            "width": 320,
            "height": 50,
            "src": "https://bauval.org/22/1fbeac751a7ab02213e2043bf4d93396",
        },
        "banner300x250": {
            "id": 32266179,
            "key": "eed27850ddceec31f60a45b6e20112e7",
            "width": 300,
            "height": 250,
            "src": "https://bauval.org/22/eed27850ddceec31f60a45b6e20112e7",
        },
        "banner160x600": {
            "id": 32266180,
            "key": "112cadf7ce20ad62c230952218822899",
            "width": 160,
            "height": 600,
            "src": "https://bauval.org/22/112cadf7ce20ad62c230952218822899",
        },
        "banner160x300": {
            "id": 32266181,
            "key": "b13409dfc8bcfabf898743e1654a6664",
            "width": 160,
            "height": 300,
            "src": "https://bauval.org/22/b13409dfc8bcfabf898743e1654a6664",
        },
    },
}

PAGES = [
    {
        "path": "index.html",
        "lang": "en",
        "category": None,
        "title": "Free Unit Converter — 17 categories, 200+ units, instant & private",
        "description": "Convert length, mass, temperature, volume, area, speed and more. Free Unit Converter runs entirely in your browser — no signup, works offline.",
        "h1": "Free Unit Converter",
        "intro": "Instant, bidirectional conversions across 17 categories and 200+ units. Everything runs client-side in your browser.",
        "faq_extra": [],
    },
    {
        "path": "length/index.html",
        "lang": "en",
        "category": "Distance",
        "title": "Length & Distance Converter — meters, feet, miles, km",
        "description": "Convert meters to feet, kilometers to miles, inches to cm and more. Free online length and distance unit converter.",
        "h1": "Length & distance converter",
        "intro": "Convert between meters, feet, miles, kilometers, inches, yards, nautical miles, light-years, and dozens of other length units.",
    },
    {
        "path": "mass/index.html",
        "lang": "en",
        "category": "Mass",
        "title": "Mass & Weight Converter — kg, lb, oz, metric tons",
        "description": "Convert kilograms to pounds, grams to ounces, stones, tons and more with Free Unit Converter.",
        "h1": "Mass converter",
        "intro": "Switch between kilograms, pounds, ounces, grams, stones, metric tons and other mass units instantly.",
    },
    {
        "path": "temperature/index.html",
        "lang": "en",
        "category": "Temperature",
        "title": "Temperature Converter — Celsius, Fahrenheit, Kelvin",
        "description": "Convert °C to °F, Fahrenheit to Celsius, Kelvin and Rankine with exact formulas. Handles negative values correctly.",
        "h1": "Temperature converter",
        "intro": "Exact non-linear conversions between Celsius, Fahrenheit, Kelvin, Rankine, Réaumur and more.",
    },
    {
        "path": "volume/index.html",
        "lang": "en",
        "category": "Volume",
        "title": "Volume Converter — liters, gallons, cups, cubic meters",
        "description": "Convert liters to gallons, ml to fl oz, cubic feet to cubic meters and other volume units online for free.",
        "h1": "Volume converter",
        "intro": "Liters, gallons, cups, cubic meters, barrels and other liquid volume units in one tool.",
    },
    {
        "path": "area/index.html",
        "lang": "en",
        "category": "Area",
        "title": "Area Converter — square meters, acres, hectares",
        "description": "Convert square feet to square meters, acres to hectares, and other area units with Free Unit Converter.",
        "h1": "Area converter",
        "intro": "Square meters, acres, hectares, square feet and more — all through a common base unit.",
    },
    {
        "path": "speed/index.html",
        "lang": "en",
        "category": "Speed",
        "title": "Speed Converter — mph, km/h, knots, m/s",
        "description": "Convert miles per hour to km/h, knots to m/s, and other speed units. Free browser-based converter.",
        "h1": "Speed converter",
        "intro": "Miles per hour, kilometers per hour, knots, meters per second and Mach number.",
    },
    {
        "path": "convert-kilometers-to-miles/index.html",
        "lang": "en",
        "category": "Distance",
        "initial_in": 11,
        "initial_out": 16,
        "title": "Kilometers to Miles Converter (km to mi)",
        "description": "Convert kilometers to miles and miles to kilometers with one click. Accurate km↔mi conversion, free and private.",
        "h1": "Kilometers to miles",
        "intro": "Type a distance in kilometers or miles — the other field updates instantly. Swap units with one click.",
    },
    {
        "path": "how-to/index.html",
        "lang": "en",
        "category": None,
        "content_only": True,
        "title": "How to use Free Unit Converter",
        "description": "Step-by-step guide to converting units online with Free Unit Converter — categories, swap, precision, and custom factors.",
        "h1": "How to convert units",
    },
    {
        "path": "faq/index.html",
        "lang": "en",
        "category": None,
        "content_only": True,
        "title": "FAQ — Free Unit Converter",
        "description": "Answers about accuracy, offline use, privacy, supported categories, and temperature conversion on Free Unit Converter.",
        "h1": "Frequently asked questions",
    },
    {
        "path": "about/index.html",
        "lang": "en",
        "category": None,
        "content_only": True,
        "title": "About Free Unit Converter",
        "description": "About this free browser-based unit converter, open-source base, license, and credits.",
        "h1": "About",
    },
    {
        "path": "privacy/index.html",
        "lang": "en",
        "category": None,
        "content_only": True,
        "title": "Privacy Policy — Free Unit Converter",
        "description": "Privacy policy for Free Unit Converter: client-side processing, cookies, advertising, and contact.",
        "h1": "Privacy policy",
    },
    {
        "path": "terms/index.html",
        "lang": "en",
        "category": None,
        "content_only": True,
        "title": "Terms of Use — Free Unit Converter",
        "description": "Terms of use for the Free Unit Converter website.",
        "h1": "Terms of use",
    },
    {
        "path": "contact/index.html",
        "lang": "en",
        "category": None,
        "content_only": True,
        "title": "Contact — Free Unit Converter",
        "description": "Contact and feedback for Free Unit Converter via the web-free.site hub.",
        "h1": "Contact",
    },
    {
        "path": "how-to-convert-celsius-to-fahrenheit/index.html",
        "lang": "en",
        "category": None,
        "content_only": True,
        "title": "How to convert Celsius to Fahrenheit",
        "description": "Use the standard Celsius-Fahrenheit formulas and convert temperatures in your browser with Free Unit Converter, including values below zero.",
        "h1": "How to convert Celsius to Fahrenheit",
    },
    {
        "path": "how-to-convert-pounds-to-kilograms/index.html",
        "lang": "en",
        "category": None,
        "content_only": True,
        "title": "How to convert pounds to kilograms",
        "description": "Convert pounds (lb) to kilograms (kg) and back with the standard factor, using Free Unit Converter in your browser.",
        "h1": "How to convert pounds to kilograms",
    },
    {
        "path": "fr/index.html",
        "lang": "fr",
        "category": None,
        "title": "Convertisseur d'unités gratuit — 17 catégories, 200+ unités",
        "description": "Convertissez longueur, masse, température, volume et plus. Outil gratuit dans le navigateur, sans inscription.",
        "h1": "Convertisseur d'unités gratuit",
        "intro": "Conversions bidirectionnelles instantanées dans 17 catégories. Tout s'exécute localement dans votre navigateur.",
        "fr_ui": True,
    },
]


def banner_iframe(key: str, w: int, h: int, src: str, slot_id: str) -> str:
    return textwrap.dedent(
        f"""
        <div class="ad-slot ad-iframe" id="{slot_id}" aria-hidden="true">
          <iframe title="Advertisement" class="ad-frame" width="{w}" height="{h}" scrolling="no" frameborder="0" sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox" srcdoc="<!DOCTYPE html><html><head><meta charset=&quot;utf-8&quot;><style>html,body{{margin:0;padding:0;overflow:hidden}}</style></head><body><script>atOptions = {{'key':'{key}','format':'iframe','height':{h},'width':{w},'params':{{}}}};</script><script src=&quot;{src}&quot;></script></body></html>"></iframe>
        </div>
        """
    ).strip()


def ads_block() -> str:
    u = ADS_JSON["units"]
    b728 = u["banner728x90"]
    b468 = u["banner468x60"]
    b320 = u["banner320x50"]
    b300 = u["banner300x250"]
def ads_mid() -> str:
    u = ADS_JSON["units"]
    b728 = u["banner728x90"]
    b468 = u["banner468x60"]
    b300 = u["banner300x250"]
    native = u["native"]
    return f"""
        <div class="ad-row ad-mid">{banner_iframe(b728['key'], b728['width'], b728['height'], b728['src'], 'ad-mid-728')}</div>
        <div class="ad-row ad-mid ad-mid-sm">{banner_iframe(b468['key'], b468['width'], b468['height'], b468['src'], 'ad-mid-468')}</div>
        <div class="ad-native">
          <script async="async" data-cfasync="false" src="{native['script']}"></script>
          <div id="{native['container']}"></div>
        </div>
        <div class="ad-row ad-inline">{banner_iframe(b300['key'], b300['width'], b300['height'], b300['src'], 'ad-mid-300')}</div>
    """


def ads_tail() -> str:
    u = ADS_JSON["units"]
    b320 = u["banner320x50"]
    return f'<div class="ad-sticky-mobile">{banner_iframe(b320["key"], b320["width"], b320["height"], b320["src"], "ad-sticky-320")}</div>'


def head_scripts() -> str:
    u = ADS_JSON["units"]
    return f"""
    <script data-cfasync="false" src="{u['popunder']['script']}"></script>
    """


def foot_scripts() -> str:
    u = ADS_JSON["units"]
    return f"""
    <script data-cfasync="false" src="{u['socialBar']['script']}"></script>
    """


def canonical_for(path: str) -> str:
    if path == "index.html":
        return SITE + "/"
    return SITE + "/" + path.replace("index.html", "").rstrip("/") + "/"


def hreflang(path: str, lang: str) -> str:
    en = canonical_for(path) if lang == "en" else SITE + "/"
    fr = SITE + "/fr/" if lang == "fr" else (SITE + "/fr/" if path == "index.html" else "")
    bits = [f'<link rel="canonical" href="{canonical_for(path)}">']
    bits.append(f'<link rel="alternate" hreflang="en" href="{en}">')
    bits.append(f'<link rel="alternate" hreflang="fr" href="{fr}">')
    bits.append(f'<link rel="alternate" hreflang="x-default" href="{en}">')
    return "\n".join(bits)


def json_ld_webapp(path: str, title: str, description: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Free Unit Converter",
        "url": canonical_for(path),
        "description": description,
        "applicationCategory": "UtilityApplication",
        "operatingSystem": "Any",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "inLanguage": ["en", "fr"],
        "browserRequirements": "Requires JavaScript",
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def json_ld_faq() -> str:
    faqs = [
        ("Is Free Unit Converter really free?", "Yes. Conversions run in your browser with no account and no paid API."),
        ("Does it work offline?", "After the page loads once, unit math works without a network connection."),
        ("How accurate are conversions?", "Linear units use definition-based factors to a base unit; temperature uses exact scale formulas."),
        ("Is my input sent to a server?", "No. Values never leave your device for conversion."),
        ("What categories are supported?", "17 categories including distance, mass, temperature, volume, area, speed, pressure, power, and custom factors."),
    ]
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def nav_links(lang: str) -> str:
    if lang == "fr":
        return """
        <nav class="site-nav" aria-label="Principal">
          <a href="/fr/">Accueil</a>
          <a href="/length/">Distance</a>
          <a href="/mass/">Masse</a>
          <a href="/temperature/">Température</a>
          <a href="/faq/">FAQ</a>
          <a href="/">English</a>
        </nav>
        """
    return """
    <nav class="site-nav" aria-label="Main">
      <a href="/">Home</a>
      <a href="/length/">Length</a>
      <a href="/mass/">Mass</a>
      <a href="/temperature/">Temperature</a>
      <a href="/volume/">Volume</a>
      <a href="/how-to/">How-to</a>
      <a href="/faq/">FAQ</a>
      <a href="/fr/">Français</a>
    </nav>
    """


def footer_html(lang: str) -> str:
    u = ADS_JSON["units"]
    smart = u["smartlink"]["url"]
    if lang == "fr":
        return f"""
        <footer>
          <div class="footer-inner">
            <span class="mark">Convertisseur d'unités gratuit</span>
            <span class="divider" aria-hidden="true"></span>
            <span>17 catégories · 200+ unités · <a href="https://web-free.site">web-free.site</a></span>
            <span>Basé sur le projet MIT de <a href="https://github.com/yovaraj-collab/unit-converter" rel="noopener">Yovaraj Karunakaran</a></span>
            <a class="smartlink" href="{smart}" rel="nofollow sponsored">Ressources</a>
            <span><a href="/about/">À propos</a> · <a href="/privacy/">Confidentialité</a> · <a href="/terms/">Conditions</a></span>
          </div>
        </footer>
        """
    return f"""
    <footer>
      <div class="footer-inner">
        <span class="mark">Free Unit Converter</span>
        <span class="divider" aria-hidden="true"></span>
        <span>17 categories · 200+ units · <a href="https://web-free.site">More free tools at web-free.site</a></span>
        <span>Built on the MIT project by <a href="https://github.com/yovaraj-collab/unit-converter" rel="noopener">Yovaraj Karunakaran</a></span>
        <a class="smartlink" href="{smart}" rel="nofollow sponsored">Resources</a>
        <span><a href="/about/">About</a> · <a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/contact/">Contact</a></span>
      </div>
    </footer>
    """


def converter_shell(lang: str, fr_ui: bool) -> str:
    labels = {
        "tabs": "Unit categories" if not fr_ui else "Catégories d'unités",
        "input": "Input" if not fr_ui else "Entrée",
        "output": "Output" if not fr_ui else "Sortie",
        "swap": "Swap" if not fr_ui else "Inverser",
        "swap_title": "Swap units — reverse the conversion" if not fr_ui else "Inverser les unités",
        "prec": "Precision" if not fr_ui else "Précision",
        "clear": "Clear" if not fr_ui else "Effacer",
        "ready": "Ready" if not fr_ui else "Prêt",
        "custom_hint": "Define your own conversion, then type a value in either box below. It converts both ways."
        if not fr_ui
        else "Définissez votre conversion, puis saisissez une valeur dans l'un des champs.",
    }
    digits = "digits" if not fr_ui else "chiffres"
    return f"""
    <div class="tabs" id="tabs" role="tablist" aria-label="{labels['tabs']}"></div>
    <div class="card" id="converter-card">
      <div class="panel">
        <div class="customdef" id="customdef">
          <div class="row">
            <span>1</span>
            <input type="text" class="field" id="cNameA" value="Widget" aria-label="Unit A">
            <span>=</span>
            <input type="text" class="field num" id="cFactor" value="2.5" inputmode="decimal" aria-label="Factor">
            <input type="text" class="field" id="cNameB" value="Gadget" aria-label="Unit B">
          </div>
          <div class="hint">{labels['custom_hint']}</div>
        </div>
        <div class="lists" id="lists">
          <div class="group">
            <span class="group-label">{labels['input']}</span>
            <div class="listbox" id="listIn" role="listbox" tabindex="0" aria-label="{labels['input']}"></div>
          </div>
          <div class="swapcol">
            <button class="swap" id="btnSwap" title="{labels['swap_title']}" aria-label="{labels['swap_title']}">&#8646;</button>
            <span class="swaplabel">{labels['swap']}</span>
          </div>
          <div class="group">
            <span class="group-label">{labels['output']}</span>
            <div class="listbox" id="listOut" role="listbox" tabindex="0" aria-label="{labels['output']}"></div>
          </div>
        </div>
        <div class="fields">
          <label for="valIn">{labels['input']}</label>
          <input class="field" id="valIn" inputmode="decimal" autocomplete="off" spellcheck="false" placeholder="0">
          <span class="unitname" id="nameIn"></span>
          <label for="valOut">{labels['output']}</label>
          <input class="field" id="valOut" inputmode="decimal" autocomplete="off" spellcheck="false" placeholder="0">
          <span class="unitname" id="nameOut"></span>
        </div>
      </div>
      <div class="toolbar">
        <label for="precSel">{labels['prec']}</label>
        <select id="precSel" aria-label="{labels['prec']}">
          <option value="4">4 {digits}</option>
          <option value="6">6 {digits}</option>
          <option value="8">8 {digits}</option>
          <option value="10" selected>10 {digits}</option>
          <option value="12">12 {digits}</option>
        </select>
        <button class="btn-clear" id="btnClear" type="button">{labels['clear']}</button>
        <div class="status" id="status">{labels['ready']}</div>
      </div>
    </div>
    """


def static_content(page: dict) -> str:
    name = page["path"].split("/")[0]
    if name == "how-to":
        return """
        <article class="prose">
          <ol>
            <li>Choose a category tab (Distance, Mass, Temperature, etc.) or open a dedicated category page from the menu.</li>
            <li>Click the input unit in the left list and the output unit in the right list.</li>
            <li>Type a value in <strong>Input</strong> — the result appears in <strong>Output</strong>, or type in Output to convert backward.</li>
            <li>Use the round <strong>Swap</strong> button to exchange units and values.</li>
            <li>Adjust precision (4–12 significant digits) in the toolbar.</li>
            <li>For bespoke conversions, open <strong>Custom</strong> and set <code>1 A = factor B</code>.</li>
          </ol>
          <p><a href="/">Open the converter</a></p>
        </article>
        """
    if name == "faq":
        return """
        <article class="prose">
          <h2>Is it free?</h2><p>Yes — no account and no subscription.</p>
          <h2>Where is data processed?</h2><p>Entirely in your browser; conversion values are not uploaded.</p>
          <h2>Can I use it offline?</h2><p>After the first load, math works offline.</p>
          <h2>Temperature below zero?</h2><p>Celsius and Fahrenheit negatives are supported via exact formulas.</p>
          <h2>Source code?</h2><p>Based on <a href="https://github.com/yovaraj-collab/unit-converter">yovaraj-collab/unit-converter</a> (MIT).</p>
        </article>
        """
    if name == "about":
        return """
        <article class="prose">
          <p><strong>Free Unit Converter</strong> is a browser-based tool for everyday and technical unit conversions.
          It is a rebranded deployment of the open-source <a href="https://github.com/yovaraj-collab/unit-converter">unit-converter</a>
          project by <strong>Yovaraj Karunakaran</strong> (MIT License).</p>
          <p>Layout and categories were inspired by Josh Madison's classic Convert for Windows.</p>
          <p>Part of the <a href="https://web-free.site">web-free.site</a> collection of free utilities.</p>
        </article>
        """
    if name == "privacy":
        return """
        <article class="prose">
          <p>Conversions are performed locally in your browser. We do not receive the numbers you type.</p>
          <p>Like most free sites, we display advertising (Adsterra). Ad partners may use cookies or similar technologies
          under their own policies. We do not sell personal data.</p>
          <p>Contact: see <a href="/contact/">Contact</a> or <a href="https://web-free.site">web-free.site</a>.</p>
        </article>
        """
    if name == "terms":
        return """
        <article class="prose">
          <p>Use this tool at your own risk. Results are for general reference; verify critical measurements independently.</p>
          <p>Content and software are provided "as is" without warranty. MIT-licensed upstream code remains under its license.</p>
        </article>
        """
    if name == "how-to-convert-celsius-to-fahrenheit":
        return """
        <article class="prose"><p>Celsius and Fahrenheit measure the same thing on different scales. The conversion is a fixed formula, not an exchange rate, so the same math works every time. Free Unit Converter can apply it in the temperature category.</p><ol><li><strong>Open the temperature converter.</strong> Go to Free Unit Converter and choose the temperature category, or open the temperature page.</li><li><strong>Select Celsius and Fahrenheit.</strong> Set the input unit to Celsius and the output unit to Fahrenheit (or the other way around).</li><li><strong>Type the value.</strong> Enter the temperature. Negative values are allowed. The other field updates in the browser.</li><li><strong>Optional: check the formula.</strong> To convert Celsius to Fahrenheit by hand, multiply by 9/5 and add 32. To convert Fahrenheit to Celsius, subtract 32 and multiply by 5/9.</li></ol><h2>A worked example</h2><p>20 C is (20 x 9/5) + 32 = 68 F. 0 C is 32 F, the freezing point of water on these scales. 100 C is 212 F.</p><h2>Precision</h2><p>You can raise or lower the number of significant digits in the toolbar if you need a more or less rounded display. For cooking or weather, a whole number is often enough.</p><p>Convert a temperature on the <a href="/temperature/">temperature page</a> or the <a href="/">main converter</a>.</p></article>
        """
    if name == "how-to-convert-pounds-to-kilograms":
        return """
        <article class="prose"><p>Pounds and kilograms are both units of mass in everyday use. International kits and many official forms use kilograms; some household scales still show pounds. Free Unit Converter can switch between them in the mass category.</p><ol><li><strong>Open the mass converter.</strong> On Free Unit Converter, choose the mass (weight) category or the mass page.</li><li><strong>Select pounds and kilograms.</strong> Set one list to pounds (lb) and the other to kilograms (kg).</li><li><strong>Enter the value and read the result.</strong> Type the number you have. You can also type in the other field to convert in the opposite direction, or use the swap control.</li><li><strong>Optional: the factor.</strong> One international pound is 0.45359237 kilograms by definition. The converter uses standard factors like this rather than a rough guess.</li></ol><h2>Mass versus force</h2><p>In everyday language people say "weight" for both. This tool is converting mass units (lb and kg), which is what bathroom scales and shipping forms usually mean.</p><h2>Stone and ounces</h2><p>If you need stone or ounces as well, pick those units in the same mass category instead of doing a second manual calculation.</p><p>Convert lb and kg on the <a href="/mass/">mass page</a> or <a href="/">Free Unit Converter</a>.</p></article>
        """
    if name == "contact":
        return """
        <article class="prose">
          <p>For feedback about this converter, visit the hub at <a href="https://web-free.site">web-free.site</a>
          where our free tools are listed.</p>
        </article>
        """
    return ""


def fix_render_page(page: dict) -> str:
    """Cleaner render without duplicate main content."""
    path = page["path"]
    lang = page["lang"]
    title = page["title"]
    desc = page["description"]
    h1 = page["h1"]
    fr_ui = page.get("fr_ui", False)
    content_only = page.get("content_only", False)
    cat = page.get("category")
    init_in = page.get("initial_in")
    init_out = page.get("initial_out")

    og = f"""
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{canonical_for(path)}">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    """

    body_class = "lang-fr" if lang == "fr" else "lang-en"
    init_attrs = ""
    if cat:
        init_attrs += f' data-initial-category="{cat}"'
    if init_in is not None:
        init_attrs += f' data-initial-in="{init_in}"'
    if init_out is not None:
        init_attrs += f' data-initial-out="{init_out}"'

    header_title = "Free Unit Converter" if lang == "en" else "Convertisseur d'unités gratuit"

    if path == "faq/index.html":
        ld_extra = json_ld_faq()
    elif path in ("index.html", "fr/index.html"):
        ld_extra = json_ld_faq()
    else:
        ld_extra = ""

    if content_only:
        main_body = f"<h1 class='page-title'>{h1}</h1>{static_content(page)}"
        show_converter = False
    else:
        intro = page.get("intro", "")
        main_body = f"<h1 class='page-title'>{h1}</h1><p class='lede'>{intro}</p>{converter_shell(lang, fr_ui)}"
        show_converter = True

    u = ADS_JSON["units"]
    b728 = u["banner728x90"]
    ad_top = f'<div class="ad-row ad-top">{banner_iframe(b728["key"], b728["width"], b728["height"], b728["src"], "ad-top-728")}</div>'

    b160600 = u["banner160x600"]
    b160300 = u["banner160x300"]
    rail = f"""<aside class="ad-rail" aria-label="Advertisement">
{banner_iframe(b160600['key'], b160600['width'], b160600['height'], b160600['src'], 'ad-rail-160x600')}
{banner_iframe(b160300['key'], b160300['width'], b160300['height'], b160300['src'], 'ad-rail-160x300')}
</aside>"""

    mid = ads_mid() if True else ""
    tail = ads_tail()

    converter_scripts = "<script src=\"/assets/logo-orb.js\" defer></script>"
    if show_converter:
        converter_scripts += "\n<script src=\"/assets/converter.js\" defer></script>"

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{hreflang(path, lang)}
{og}
{json_ld_webapp(path, title, desc)}
{ld_extra}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Allison&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{head_scripts()}
<script src="https://ref.web-free.site/r.js" defer></script>
</head>
<body class="{body_class}"{init_attrs}>
<header>
  <div class="header-inner">
    <canvas id="logoOrb" class="logo-orb" width="144" height="144" aria-hidden="true"></canvas>
    <div class="brand">
      <span class="wordmark">{header_title}</span>
      {nav_links(lang)}
    </div>
  </div>
</header>
{ad_top}
<div class="page-layout">
{rail}
<div class="page-main">
<main>
{main_body}
{mid}
</main>
</div>
</div>
{tail}
{footer_html(lang)}
{foot_scripts()}
{converter_scripts}
</body>
</html>
"""


def sitemap_urls() -> list[str]:
    urls = []
    for p in PAGES:
        urls.append(canonical_for(p["path"]))
    return urls


def main() -> None:
    PUBLIC.mkdir(parents=True, exist_ok=True)
    (PUBLIC / "assets").mkdir(exist_ok=True)
    (PUBLIC / "ads.json").write_text(json.dumps(ADS_JSON, indent=2) + "\n", encoding="utf-8")

    for page in PAGES:
        out = PUBLIC / page["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fix_render_page(page), encoding="utf-8")

    urls = "\n".join(f"  <url><loc>{u}</loc></url>" for u in sitemap_urls())
    (PUBLIC / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n',
        encoding="utf-8",
    )
    (PUBLIC / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n",
        encoding="utf-8",
    )
    print(f"Generated {len(PAGES)} pages under {PUBLIC}")


if __name__ == "__main__":
    main()