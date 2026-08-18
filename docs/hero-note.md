# Hero demo

The full interactive SuperAgenticMCP design prototype (patch bay, mission console, 3D memory scope, hot-swap rack, install panes) is maintained as the product vision surface.

**Current status:** The OpenGOS-style repo layout is in place. The complete client-side simulation HTML is ready to land as `superagenticmcp.html` in a follow-up commit (large single-file design artifact).

Until then:

```bash
pip install -e ".[dev]"
superagenticmcp-cli status
```

See root `README.md` for surfaces and routing model.
