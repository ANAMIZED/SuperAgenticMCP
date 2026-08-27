# WebMCP on ANAMIZED pages

WebMCP is a **page-level** tool surface for visiting browser agents. It is **not** a replacement for the `superagenticmcp` stdio server.

Page tools live on `web/board.html`. Writes (`rack_add`, `rack_remove`) require `window.confirm`. `route_task` is a planner stub and does not execute downstream tools.

See also the shared contract notes in ANAMIZED/desk `WEBMCP.md`.
