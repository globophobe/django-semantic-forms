function semanticChooser() {
  var $ = (window.django && window.django.jQuery) || window.jQuery || window.$;

  if (!$) {
    return;
  }

  $(".semantic-autocomplete")
    .not(".initialized")
    .not("[name*=__prefix__]")
    .each(function () {
      // Reverse lookup id from hidden input, if any.
      var $select = $(this);
      var id = $select.attr("id");
      var optionValue = $("#" + id + "-value").val();
      if (optionValue) {
        const reverseUrl = $select.data("ajax-url");
        const lookupUrl =
          reverseUrl.substring(0, reverseUrl.length - 1) +
          "-reverse/?id=" +
          optionValue;
        fetch(lookupUrl)
          .then((response) => response.json())
          .then((data) => {
            var { results } = data;
            if (results && results.length) {
              results.forEach(({ id, text }) => {
                $select.append(new Option(text, id));
              });
            }
          });
      }
      // Initialize dropdown.
      var url = $select.data("ajax-url") + "?term={query}";
      var app_label = $select.data("app-label");
      if (app_label) {
        url += "&app_label=" + app_label;
      }
      var model_name = $select.data("model-name");
      if (model_name) {
        url += "&model_name=" + model_name;
      }
      var field_name = $select.data("field-name");
      if (field_name) {
        url += "&field_name=" + field_name;
      }
      $select.dropdown({
        apiSettings: {
          url: url,
          onResponse: function (response) {
            response.results = response.results.map((result) => {
              return Object.assign(
                { value: result.id, name: result.name || result.text },
                result,
              );
            });
            return response;
          },
          cache: false,
        },
        clearable: true,
        fullTextSearch: true,
        forceSelection: false,
        saveRemoteData: false,
      });
      $select.addClass("initialized");
    });
}
