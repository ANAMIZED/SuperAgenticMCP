(function () {
  "use strict";
  var W = window.ANAMIZEDWebMCP;
  var logEl = document.getElementById("webmcp-log");
  var statusEl = document.getElementById("webmcp-status");
  var rackView = document.getElementById("rack-view");
  var RACK = [];
  function paint() { if (rackView) rackView.textContent = JSON.stringify(RACK, null, 2); }
  var tools = [
    { name: "status", description: "Page-board health and rack count. Read-only.", inputSchema: { type: "object", properties: {} }, annotations: { readOnlyHint: true },
      execute: async function () { return { name: "superagenticmcp", surface: "webmcp-board", version: "0.2.0", status: "ok", rack_count: RACK.length, note: "Page board is not the stdio MCP process." }; } },
    { name: "list_rack", description: "List MCP servers on this page board.", inputSchema: { type: "object", properties: {} }, annotations: { readOnlyHint: true },
      execute: async function () { return { servers: RACK.slice(), count: RACK.length }; } },
    { name: "rack_add", description: "Register a server on the in-page rack. Requires confirmation.", inputSchema: { type: "object", properties: { name: { type: "string" }, command: { type: "string" }, notes: { type: "string" } }, required: ["name", "command"] }, annotations: { readOnlyHint: false },
      execute: async function (params) {
        var name = String((params && params.name) || "").trim();
        var command = String((params && params.command) || "").trim();
        if (!W.confirmWrite("Add " + name + " to the in-page rack?")) return { cancelled: true };
        var entry = { name: name, command: command, notes: (params && params.notes) || "" };
        RACK = RACK.filter(function (s) { return s.name !== name; });
        RACK.push(entry); paint(); W.log(logEl, "rack_add " + name);
        return { status: "ok", server: entry, count: RACK.length };
      } },
    { name: "rack_remove", description: "Remove one in-page rack entry. Requires confirmation.", inputSchema: { type: "object", properties: { name: { type: "string" } }, required: ["name"] }, annotations: { readOnlyHint: false },
      execute: async function (params) {
        var name = params && params.name;
        if (!W.confirmWrite("Remove " + name + " from the in-page rack?")) return { cancelled: true };
        var before = RACK.length;
        RACK = RACK.filter(function (s) { return s.name !== name; });
        paint();
        if (RACK.length === before) return { error: "server not on rack: " + name };
        W.log(logEl, "rack_remove " + name);
        return { status: "removed", name: name, count: RACK.length };
      } },
    { name: "route_task", description: "Plan a task against the in-page rack. Stub — does not execute downstream tools.", inputSchema: { type: "object", properties: { task: { type: "string" }, preferred_server: { type: "string" } }, required: ["task"] }, annotations: { readOnlyHint: true },
      execute: async function (params) {
        var names = RACK.map(function (s) { return s.name; });
        var preferred = params && params.preferred_server;
        var chosen = names.indexOf(preferred) >= 0 ? preferred : names[0] || null;
        return { task: params.task, candidates: names, chosen: chosen, executed: false, note: "Planner stub — no downstream MCP calls." };
      } }
  ];
  var btn = document.getElementById("rack-add-btn");
  if (btn) btn.addEventListener("click", function () {
    var name = document.getElementById("rack-name").value.trim();
    var command = document.getElementById("rack-cmd").value.trim();
    if (!name || !command) return;
    RACK = RACK.filter(function (s) { return s.name !== name; });
    RACK.push({ name: name, command: command, notes: "ui" });
    paint();
  });
  async function boot() {
    statusEl.textContent = W.supported() ? "WebMCP available — board tools registered" : "WebMCP API not in this browser.";
    W.log(logEl, "registered " + JSON.stringify(await W.registerAll(tools)));
    paint();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
