$(document).ready(function () {
  $(".ui.checkbox")
    .not("[name*=__prefix__]")
    .each(function () {
      $(this).checkbox();
    });
});
