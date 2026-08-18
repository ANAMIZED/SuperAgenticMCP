# Web control plane

Server OS convention: control-plane assets live under `web/`.

The interactive hero demo currently ships at the repository root as
[`../superagenticmcp.html`](../superagenticmcp.html) so zero-install previews
and existing links keep working.

When the live board is implemented, prefer serving from this directory
(e.g. `web/board.html` or static assets behind the `:7420` board process).
