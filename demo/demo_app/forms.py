from django import forms
from django.db import models

from semantic_forms import SemanticForm
from semantic_forms.fields import (
    SemanticChoiceField,
    SemanticDateField,
    SemanticDateTimeField,
    SemanticMultipleChoiceField,
    SemanticTimeField,
)
from semantic_forms.widgets import (
    SemanticCheckboxInput,
    SemanticCheckboxSelectMultiple,
    SemanticRadioSelect,
    SemanticTextarea,
    SemanticTextInput,
)

try:
    from django.utils.translation import gettext_lazy as _  # Django >= 4
except ImportError:
    from django.utils.translation import ugettext_lazy as _


class Colors(models.TextChoices):
    """Colors"""

    red = "red", _("red")
    green = "green", _("green")
    blue = "blue", _("blue")


class DemoForm(SemanticForm):
    """Semantic form"""

    char_field = forms.CharField(
        label=_("Char"),
        widget=SemanticTextInput(),
        help_text=_("Helpful text"),
    )
    datetime_field = SemanticDateTimeField(
        label=_("Datetime"), help_text=_("Helpful text")
    )
    date_field = SemanticDateField(label=_("Date"), help_text=_("Helpful text"))
    time_field = SemanticTimeField(label=_("Time"), help_text=_("Helpful text"))
    text_field = forms.CharField(
        label=_("Text"), widget=SemanticTextarea(), help_text=_("Helpful text")
    )
    checkbox_field = forms.BooleanField(
        label=_("Checkbox"),
        label_suffix="",
        help_text=_("Helpful text"),
        widget=SemanticCheckboxInput(),
        required=False,
    )
    radio_field = forms.ChoiceField(
        label=_("Radio"),
        help_text=_("Helpful text"),
        choices=Colors.choices,
        widget=SemanticRadioSelect(),
    )
    checkbox_select_field = forms.MultipleChoiceField(
        label=_("Checkbox select"),
        help_text=_("Helpful text"),
        choices=Colors.choices,
        widget=SemanticCheckboxSelectMultiple(),
    )
    select_field = SemanticChoiceField(
        label=_("Select"), help_text=_("Helpful text"), choices=Colors.choices
    )
    select_muliple_field = SemanticMultipleChoiceField(
        label=_("Select multiple"),
        help_text=_("Helpful text"),
        choices=Colors.choices,
    )
