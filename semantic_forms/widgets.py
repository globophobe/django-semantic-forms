from typing import Any, Optional

from django import forms
from django.urls import NoReverseMatch, reverse


class SemanticMixin:
    """Semantic mixin."""

    class Media:
        css = {"all": ["semantic_forms/unsemantic.css"]}


class SemanticSelectMixin(SemanticMixin):
    """Semantic select mixin."""

    template_name = "semantic_forms/forms/widgets/select.html"

    class Media:
        js = ["semantic_forms/semanticDropdown.js"]


class SemanticSelect(SemanticSelectMixin, forms.Select):
    """Semantic select."""


class SemanticSelectMultiple(SemanticSelectMixin, forms.SelectMultiple):
    """Semantic select multiple."""


class SemanticCheckboxMixin(SemanticMixin):
    """Semantic checkbox mixin."""

    class Media:
        js = ["semantic_forms/semanticCheckbox.js"]


class SemanticCheckboxInput(SemanticCheckboxMixin, forms.CheckboxInput):
    """Semantic checkbox input."""

    template_name = "semantic_forms/forms/widgets/checkbox.html"


class SemanticCheckboxSelectMultiple(
    SemanticCheckboxMixin, forms.CheckboxSelectMultiple
):
    """Semantic checkbox select multiple."""

    template_name = "semantic_forms/forms/widgets/checkbox_select.html"
    option_template_name = "semantic_forms/forms/widgets/checkbox_option.html"


class SemanticCalendarMixin(SemanticMixin):
    """Semantic calendar mixin."""

    @property
    def media(self) -> forms.Media:
        """Media."""
        js = ["semantic_forms/semanticCalendar.js"]
        try:
            url = reverse("javascript-catalog")
        except NoReverseMatch:
            try:
                url = reverse("admin:jsi18n")
            except NoReverseMatch:
                js.append("semantic_forms/semanticUntranslatedCalendar.js")
            else:
                js.append(url)
                js.append("semantic_forms/semanticTranslatedCalendar.js")
        else:
            js.append(url)
            js.append("semantic_forms/semanticTranslatedCalendar.js")
        return forms.Media(js=js)


class SemanticDateTimeInput(SemanticCalendarMixin, forms.DateTimeInput):
    """Semantic date time input."""

    template_name = "semantic_forms/forms/widgets/datetime.html"

    def __init__(
        self, attrs: Optional[dict] = None, format: Optional[str] = None
    ) -> None:
        """Initialize."""
        super().__init__(attrs)
        self.format = format or "%Y-%m-%d %H:%M"


class SemanticDateInput(SemanticCalendarMixin, forms.DateInput):
    """Semantic date input."""

    template_name = "semantic_forms/forms/widgets/date.html"

    def __init__(
        self, attrs: Optional[dict] = None, format: Optional[str] = None
    ) -> None:
        """Initialize."""
        super().__init__(attrs)
        self.format = format or "%Y-%m-%d"


class SemanticTimeInput(SemanticCalendarMixin, forms.TimeInput):
    """Semantic time input."""

    template_name = "semantic_forms/forms/widgets/time.html"


class SemanticEmailInput(SemanticMixin, forms.EmailInput):
    """Semantic email input."""

    # TODO
    # template_name = "semantic_forms/forms/widgets/email.html"


class SemanticFileInput(SemanticMixin, forms.ClearableFileInput):
    """Semantic file input."""

    template_name = "semantic_forms/forms/widgets/clearable_file_input.html"


class SemanticImageInput(SemanticFileInput):
    """Semantic image input."""


class SemanticClearableFileInput(SemanticMixin, forms.ClearableFileInput):
    """Semantic clearable file input."""

    template_name = "semantic_forms/forms/widgets/clearable_file_input.html"


class SemanticNumberInput(SemanticMixin, forms.NumberInput):
    """Semantic number input."""


class SemanticPasswordInput(SemanticMixin, forms.NumberInput):
    """Semantic password input."""


class SemanticRadioSelect(SemanticMixin, forms.RadioSelect):
    """Semantic radio select."""

    template_name = "semantic_forms/forms/widgets/radio.html"
    option_template_name = "semantic_forms/forms/widgets/radio_option.html"


class SemanticTextarea(SemanticMixin, forms.Textarea):
    """Semantic textara."""

    template_name = "semantic_forms/forms/widgets/textarea.html"


class SemanticTextInput(SemanticMixin, forms.TextInput):
    """Semantic text input."""

    template_name = "semantic_forms/forms/widgets/text.html"


class SemanticURLInput(SemanticMixin, forms.URLInput):
    """Semantic URL input."""

    template_name = "semantic_forms/forms/widgets/url.html"


class RangeWidget(forms.MultiWidget):
    """Range widget."""

    def decompress(self, value: Any) -> list:
        """Decompress."""
        if value:
            return [value.start, value.stop]
        return [None, None]


class SemanticDateRangeWidget(RangeWidget):
    """Semantic date range widget."""

    def __init__(self, attrs: Optional[dict] = None) -> None:
        """Initialize."""
        widgets = [SemanticDateInput, SemanticDateInput]
        super().__init__(widgets, attrs)


class SemanticTimeRangeWidget(RangeWidget):
    """Semantic time range widget."""

    def __init__(self, attrs: Optional[dict] = None) -> None:
        """Initialize."""
        widgets = [SemanticTimeInput(), SemanticTimeInput()]
        super().__init__(widgets, attrs)
