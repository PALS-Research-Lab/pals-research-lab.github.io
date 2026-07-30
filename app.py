"""Local preview server for the built Jekyll site.

Serves the contents of _site/ with pretty-URL resolution (/people ->
people/index.html). This does NOT build the site -- run `bundle exec jekyll
build` first. Intended for local preview only; the real site is served by
GitHub Pages.
"""

import os

from flask import Flask, abort, send_from_directory
from werkzeug.utils import safe_join

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_site")
SITE_ROOT = os.path.realpath(SITE)

app = Flask(__name__)


def _resolve(rel):
    """Return the real path of `rel` inside _site, or None if it escapes.

    safe_join rejects absolute paths (including Windows drive letters such as
    "C:/Windows/win.ini"), alternate separators, and ".." segments. The realpath
    containment check below additionally covers symlinks, which safe_join does
    not follow.
    """
    candidate = safe_join(SITE, rel)
    if candidate is None:
        return None

    resolved = os.path.realpath(candidate)
    if resolved != SITE_ROOT and not resolved.startswith(SITE_ROOT + os.sep):
        return None

    return resolved if os.path.isfile(resolved) else None


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    """Serve Jekyll's _site, including pretty URL folders (people/index.html)."""
    if not path or path == ".":
        candidates = ["index.html"]
    else:
        candidates = [path, path + ".html", path + "/index.html"]

    for rel in candidates:
        full = _resolve(rel)
        if full is not None:
            return send_from_directory(
                os.path.dirname(full), os.path.basename(full)
            )

    abort(404)


if __name__ == "__main__":
    # Bind to loopback only, and keep the Werkzeug debugger (which exposes an
    # interactive code-execution console) off unless explicitly requested.
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=os.environ.get("FLASK_DEBUG") == "1",
    )
