(function ($) {
  if (!$) {
    return;
  }

  $(function () {
    const hasJavascriptCatalog = true;

    $(".ui.calendar.datetime")
      .not(".initialized")
      .not("[name*=__prefix__]")
      .each(function () {
        $(this).calendar(getCalendarOptions("datetime", hasJavascriptCatalog));
        $(this).addClass("initialized");
      });

    $(".ui.calendar.date")
      .not(".initialized")
      .not("[name*=__prefix__]")
      .each(function () {
        $(this).calendar(getCalendarOptions("date", hasJavascriptCatalog));
        $(this).addClass("initialized");
      });

    $(".ui.calendar.time")
      .not(".initialized")
      .not("[name*=__prefix__]")
      .each(function () {
        $(this).calendar(getCalendarOptions("time", hasJavascriptCatalog));
        $(this).addClass("initialized");
      });
  });
})((window.django && window.django.jQuery) || window.jQuery || window.$);
