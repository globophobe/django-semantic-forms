const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

function loadCalendarModule() {
  const filename = path.join(
    __dirname,
    "..",
    "..",
    "semantic_forms",
    "static",
    "semantic_forms",
    "semanticCalendar.js",
  );
  const source =
    fs.readFileSync(filename, "utf8") +
    "\nmodule.exports = { getCalendarOptions };";

  const context = {
    module: { exports: {} },
    exports: {},
    gettext: (value) => value,
    pgettext: (_context, value) => value,
  };

  vm.createContext(context);
  vm.runInContext(source, context, { filename });

  return context.module.exports;
}

test("calendar formatters match Django datetime strings", () => {
  const { getCalendarOptions } = loadCalendarModule();
  const date = new Date(2026, 3, 9, 5, 20, 0);

  const { formatter } = getCalendarOptions("datetime", false);

  assert.equal(formatter.date(date), "2026-04-09");
  assert.equal(formatter.datetime(date), "2026-04-09 05:20");
  assert.equal(formatter.time(date), "05:20");
});
