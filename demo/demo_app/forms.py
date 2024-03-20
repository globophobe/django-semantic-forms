from django.db import models

from semantic_forms import SemanticForm
from semantic_forms.fields import (
    SemanticCharField,
    SemanticCheckboxField,
    SemanticCheckboxMultipleChoiceField,
    SemanticChoiceField,
    SemanticDateField,
    SemanticDateTimeField,
    SemanticMultipleChoiceField,
    SemanticRadioChoiceField,
    SemanticTextareaField,
    SemanticTimeField,
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


class SemanticKitchenSinkForm(SemanticForm):
    """Semantic kitchen sink form"""

    char_field = SemanticCharField(label=_("Char"), help_text=_("Helpful text"))
    datetime_field = SemanticDateTimeField(
        label=_("Datetime"), help_text=_("Helpful text")
    )
    date_field = SemanticDateField(label=_("Date"), help_text=_("Helpful text"))
    time_field = SemanticTimeField(label=_("Time"), help_text=_("Helpful text"))
    text_field = SemanticTextareaField(label=_("Text"), help_text=_("Helpful text"))
    checkbox_field = SemanticCheckboxField(
        label=_("Checkbox"), help_text=_("Helpful text")
    )
    radio_field = SemanticRadioChoiceField(
        label=_("Radio"),
        help_text=_("Helpful text"),
        choices=Colors.choices,
    )
    checkbox_select_field = SemanticCheckboxMultipleChoiceField(
        label=_("Checkbox select"),
        help_text=_("Helpful text"),
        choices=Colors.choices,
    )
    select_field = SemanticChoiceField(
        label=_("Select"), help_text=_("Helpful text"), choices=Colors.choices
    )
    select_muliple_field = SemanticMultipleChoiceField(
        label=_("Select multiple"),
        help_text=_("Helpful text"),
        choices=Colors.choices,
    )
