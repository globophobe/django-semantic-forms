$(document).ready(function () {
  const hasJavascriptCatalog = false;

  $(".ui.calendar.datetime")
    .not("[name*=__prefix__]")
    .each(function () {
      $(this).calendar(getCalendarOptions("datetime", hasJavascriptCatalog));
    });

  $(".ui.calendar.date")
    .not("[name*=__prefix__]")
    .each(function () {
      $(this).calendar(getCalendarOptions("date", hasJavascriptCatalog));
    });

  $(".ui.calendar.time")
    .not("[name*=__prefix__]")
    .each(function () {
      $(this).calendar(getCalendarOptions("time", hasJavascriptCatalog));
    });
});
