from django import forms

from .widgets import (
    SemanticCheckboxInput,
    SemanticCheckboxSelectMultiple,
    SemanticDateInput,
    SemanticDateTimeInput,
    SemanticFileInput,
    SemanticRadioSelect,
    SemanticSelect,
    SemanticSelectMultiple,
    SemanticTextarea,
    SemanticTextInput,
    SemanticTimeInput,
)


class SemanticCharField(forms.CharField):
    """Semantic char field."""

    widget = SemanticTextInput


class SemanticTextareaField(forms.CharField):
    """Semantic textarea field."""

    widget = SemanticTextarea


class SemanticDateTimeField(forms.DateTimeField):
    """Semantic date time field."""

    widget = SemanticDateTimeInput


class SemanticDateField(forms.DateField):
    """Semantic date field."""

    widget = SemanticDateInput


class SemanticTimeField(forms.TimeField):
    """Semantic time field."""

    widget = SemanticTimeInput


class SemanticCheckboxField(forms.BooleanField):
    """Semantic checkbox field."""

    widget = SemanticCheckboxInput

    def __init__(self, *args, **kwargs) -> None:
        """Initialize."""
        super().__init__(*args, **kwargs)
        if not kwargs.get("label_suffix"):
            self.label_suffix = ""
        if not kwargs.get("required"):
            self.required = False


class SemanticCheckboxMultipleChoiceField(forms.MultipleChoiceField):
    """Semantic checkbox multiple choice field."""

    widget = SemanticCheckboxSelectMultiple


class SemanticRadioChoiceField(forms.ChoiceField):
    """Semantic radio choice field."""

    widget = SemanticRadioSelect


class SemanticChoiceField(forms.ChoiceField):
    """Semantic choice field."""

    widget = SemanticSelect


class SemanticTypedChoiceField(forms.TypedChoiceField):
    """Semantic typed choice field."""

    widget = SemanticSelect


class SemanticModelChoiceField(forms.ModelChoiceField):
    """Semantic model choice field."""

    widget = SemanticSelect


class SemanticMultipleChoiceField(forms.MultipleChoiceField):
    """Semantic multiple choice field."""

    widget = SemanticSelectMultiple


class SemanticTypedMultipleChoiceField(forms.TypedMultipleChoiceField):
    """Semantic typed multiple choice field."""

    widget = SemanticSelectMultiple


class SemanticModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    """Semantic model multiple choice field."""

    widget = SemanticSelectMultiple


class SemanticFileField(forms.FileField):
    """Semantic file field."""

    widget = SemanticFileInput
