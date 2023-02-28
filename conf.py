# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'wradlib'
copyright = '2023, Wradlib Community'
author = 'Wradlib Developers'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'ablog',
    'sphinx_comments',
    'sphinx_design',
    'sphinx_copybutton',
]

# sphinx-copybutton configurations
copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: '
copybutton_prompt_is_regexp = True

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_logo = "_static/wradlib_logo.svg.png"

html_context = {
    "github_url": "https://github.com",  # or your GitHub Enterprise site
    "github_user": "wradlib",
    "github_repo": "wradlib.github.io",
    "github_version": "main",
}

# Add some more theme Options
html_theme_options = {
    "external_links": [
        {
            "url": "https://docs.wradlib.org",
            "name": "Docs",
        },
    ],
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "favicon.ico",
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "favicon.png",
        },
    ],
    "icon_links": [
        {
            "name": "Discourse",
            "url": "https://openradar.discourse.group/tag/wradlib",
            "icon": "fab fa-discourse",
        },
    ],
    'github_url': 'https://github.com/wradlib/wradlib.github.io',
    "header_links_before_dropdown": 5,
    "show_toc_level": 1,
    'search_bar_text': 'Search this site... ',
    "navbar_align": "left",
    "navbar_end": ["icon-links.html"],
    "use_edit_page_button": True,
}

# rediraffe_redirects = 'redirects.txt'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
    "blog": [
        "postcard.html",
        "tagcloud.html",
        "categories.html",
        "authors.html",
        "languages.html",
        "archives.html",
    ],
    "posts/*/*": [
        "postcard.html",
        "tagcloud.html",
        "categories.html",
        "authors.html",
        "languages.html",
        "archives.html",
    ]
}


blog_baseurl = 'wradlib.org'
blog_title = 'An Open Source Library for Weather Radar Data Processing'
blog_path = 'blog'
fontawesome_included = True
blog_post_pattern = 'posts/*/*'
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image', 'dollarmath']
myst_url_schemes = ['http', 'https', 'mailto']

# Temporarily stored as off until we fix it
nb_execution_mode = 'off'

# disable for now, until we know hot to only allow it for blog-posts
# comments_config = {
#     'utterances': {'repo': 'wradlib/wradlib.github.io',
#                    #'optional': 'config',
#                    'label': '💬 comment'},
# }