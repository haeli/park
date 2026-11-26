# Sphinx configuration for Hae-Li Park's homepage
# Build locally:  sphinx-build -b html . _build/html

project = "Hae-Li Park"
author = "Hae-Li Park"
copyright = "2026, Hae-Li Park"

extensions = ["myst_parser"]
myst_enable_extensions = ["colon_fence", "deflist", "attrs_inline"]

source_suffix = {".md": "markdown"}
exclude_patterns = ["_build", "README.md", ".github", "Thumbs.db", ".DS_Store"]

# -- HTML output -------------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_title = "Hae-Li Park"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = False

# No left sidebar on any page (the site is small; the top menu is enough)
html_sidebars = {"**": []}

html_theme_options = {
    "navbar_align": "content",
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "secondary_sidebar_items": ["page-toc"],
    "show_prev_next": False,
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version", "theme-version"],
    # Add profile links here when you have them, e.g. Google Scholar, ORCID, GitHub:
    # "icon_links": [
    #     {"name": "Google Scholar", "url": "https://scholar.google.com/citations?user=XXXX",
    #      "icon": "fa-brands fa-google-scholar"},
    #     {"name": "ORCID", "url": "https://orcid.org/0000-0000-0000-0000",
    #      "icon": "fa-brands fa-orcid"},
    #     {"name": "GitHub", "url": "https://github.com/USERNAME",
    #      "icon": "fa-brands fa-github"},
    # ],
}
