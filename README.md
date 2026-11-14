# Free Unit Converter

Browser-based unit converter for [free-unit-converter.web-free.site](https://free-unit-converter.web-free.site): **17 categories**, **200+ units**, bidirectional conversion, and a custom-factor tab. All math runs **client-side** in your browser.

Based on the MIT-licensed [yovaraj-collab/unit-converter](https://github.com/yovaraj-collab/unit-converter) by Yovaraj Karunakaran. Part of the [web-free.site](https://web-free.site) free tools collection.

## Stack

- Static HTML/CSS/JS in `public/`
- Cloudflare Workers static assets (`wrangler.toml`, **not deployed from this agent**)
- Regenerate inner pages: `python3 scripts/generate_site.py`

## Develop locally

```bash
python3 -m http.server 8765 --directory public
```

Open http://127.0.0.1:8765/

## License

MIT — see [LICENSE](LICENSE). Upstream credit in site footer and `/about/`.