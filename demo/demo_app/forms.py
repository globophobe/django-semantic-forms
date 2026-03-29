from django.db import models
from django.utils.safestring import mark_safe

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

    char_field = SemanticCharField(
        label=_("Char"),
        help_text=mark_safe(
            "<pre><code>char_field = SemanticCharField()</code></pre>"
        ),
    )
    datetime_field = SemanticDateTimeField(
        label=_("Datetime"),
        help_text=mark_safe(
            "<pre><code>datetime_field = SemanticDateTimeField()</code></pre>"
        ),
    )
    date_field = SemanticDateField(
        label=_("Date"),
        help_text=mark_safe(
            "<pre><code>date_field = SemanticDateField()</code></pre>"
        ),
    )
    time_field = SemanticTimeField(
        label=_("Time"),
        help_text=mark_safe(
            "<pre><code>time_field = SemanticTimeField()</code></pre>"
        ),
    )
    textarea_field = SemanticTextareaField(
        label=_("Text"),
        help_text=mark_safe(
            "<pre><code>textarea_field = SemanticTextareaField()</code></pre>"
        ),
    )
    checkbox_field = SemanticCheckboxField(
        label=_("Checkbox"),
        help_text=mark_safe(
            "<pre><code>checkbox_field = SemanticCheckboxField()</code></pre>"
        ),
    )
    radio_field = SemanticRadioChoiceField(
        label=_("Radio"),
        help_text=mark_safe(
            "<pre><code>radio_field = SemanticRadioChoiceField()</code></pre>"
        ),
        choices=Colors.choices,
    )
    checkbox_select_field = SemanticCheckboxMultipleChoiceField(
        label=_("Checkbox select"),
        help_text=mark_safe(
            "<pre><code>checkbox_select_field = SemanticCheckboxMultipleChoiceField()</code></pre>"
        ),
        choices=Colors.choices,
    )
    select_field = SemanticChoiceField(
        label=_("Select"),
        help_text=mark_safe(
            "<pre><code>select_field = SemanticChoiceField()</code></pre>"
        ),
        choices=Colors.choices,
    )
    select_muliple_field = SemanticMultipleChoiceField(
        label=_("Select multiple"),
        help_text=mark_safe(
            "<pre><code>select_multiple_field = SemanticMultipleChoiceField()</code></pre>"
        ),
        choices=Colors.choices,
    )
