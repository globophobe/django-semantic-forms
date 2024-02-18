from django import forms

from .widgets import (
    SemanticDateInput,
    SemanticDateTimeInput,
    SemanticSelect,
    SemanticSelectMultiple,
    SemanticTimeInput,
)


class SemanticDateTimeField(forms.DateTimeField):
    """Semantic date time field"""

    widget = SemanticDateTimeInput


class SemanticDateField(forms.DateField):
    """Semantic date field"""

    widget = SemanticDateInput


class SemanticTimeField(forms.TimeField):
    """Semantic time field"""

    widget = SemanticTimeInput


class SemanticChoiceField(forms.ChoiceField):
    """Semantic choice field"""

    widget = SemanticSelect


class SemanticTypedChoiceField(forms.TypedChoiceField):
    """Semantic typed choice field"""

    widget = SemanticSelect


class SemanticModelChoiceField(forms.ModelChoiceField):
    """Semantic model choice field"""

    widget = SemanticSelect


class SemanticMultipleChoiceField(forms.MultipleChoiceField):
    """Semantic multiple choice field"""

    widget = SemanticSelectMultiple


class SemanticTypedMultipleChoiceField(forms.TypedMultipleChoiceField):
    """Semantic typed multiple choice field"""

    widget = SemanticSelectMultiple


class SemanticModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    """Semantic model multiple choice field"""

    widget = SemanticSelectMultiple
