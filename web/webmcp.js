/**
 * ANAMIZED WebMCP helper. document.modelContext with navigator fallback.
 */
(function (root) {
  "use strict";
  function getModelContext() {
    if (typeof document !== "undefined" && document.modelContext) return document.modelContext;
    if (typeof navigator !== "undefined" && navigator.modelContext) return navigator.modelContext;
    return null;
  }
  function supported() { return Boolean(getModelContext()); }
  async function registerTool(tool) {
    const ctx = getModelContext();
    if (!ctx || typeof ctx.registerTool !== "function") return { ok: false, reason: "webmcp-unavailable" };
    const payload = { name: tool.name, description: tool.description, inputSchema: tool.inputSchema || { type: "object", properties: {} }, execute: tool.execute, annotations: tool.annotations || {} };
    if (tool.title) payload.title = tool.title;
    await ctx.registerTool(payload);
    return { ok: true, name: tool.name };
  }
  async function registerAll(tools) {
    const results = [];
    for (const tool of tools) {
      try { results.push(await registerTool(tool)); }
      catch (err) { results.push({ ok: false, name: tool && tool.name, reason: err instanceof Error ? err.message : String(err) }); }
    }
    return results;
  }
  async function rest(path, options) {
    const opts = options || {};
    const response = await fetch(path, { method: opts.method || "GET", headers: Object.assign({ accept: "application/json" }, opts.body ? { "content-type": "application/json" } : {}, opts.headers || {}), body: opts.body ? JSON.stringify(opts.body) : undefined, credentials: "same-origin" });
    const text = await response.text();
    let data = text;
    try { data = text ? JSON.parse(text) : null; } catch (_err) {}
    if (!response.ok) { const err = new Error("HTTP " + response.status + " " + path); err.status = response.status; err.body = data; throw err; }
    return data;
  }
  function confirmWrite(message) {
    return typeof window !== "undefined" && typeof window.confirm === "function" ? window.confirm(message) : false;
  }
  function log(el, line) {
    if (!el) return;
    el.textContent = "[" + new Date().toISOString().slice(11, 19) + "] " + line + "\n" + el.textContent;
  }
  root.ANAMIZEDWebMCP = { getModelContext: getModelContext, supported: supported, registerTool: registerTool, registerAll: registerAll, rest: rest, confirmWrite: confirmWrite, log: log };
})(typeof window !== "undefined" ? window : globalThis);
