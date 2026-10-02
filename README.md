# bc-nexus-docs

Merchant documentation for the **Nexus Sports** BigCommerce theme by
[PapaThemes](https://papathemes.com).

Production URL: <https://tvlgiao.github.io/bc-nexus-docs/>

This is the URL `meta.documentation_url` points at in the theme's `config.json`,
and the page BigCommerce opens during Theme Marketplace review. The PapaThemes
convention is a `bc-<theme>-docs.papathemes.com` subdomain; to move there, add a
DNS record (`CNAME bc-nexus-docs -> tvlgiao.github.io`), add `docs/CNAME`, change
`site_url`, redeploy, and update `meta.documentation_url`.

## Work on it

```bash
pip install mkdocs-material
mkdocs serve            # http://127.0.0.1:8000
mkdocs build --strict   # fails on a broken internal link
mkdocs gh-deploy        # publish to the gh-pages branch
```

## Settings reference

`docs/settings-reference.md` is generated from the theme. Re-run after each theme
release, with the theme repo checked out next to this one:

```bash
python scripts/sinh-tham-chieu.py ../bc-nexus-sport-theme
```
