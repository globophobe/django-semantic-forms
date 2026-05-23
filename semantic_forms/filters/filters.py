from django.utils.translation import gettext_lazy as _
from django_filters.filters import (
    AllValuesFilter,
    AllValuesMultipleFilter,
    ChoiceFilter,
    DateFilter,
    DateTimeFilter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter,
    MultipleChoiceFilter,
    TimeFilter,
    TypedChoiceFilter,
    TypedMultipleChoiceFilter,
)

from semantic_forms.fields import (
    SemanticChoiceField,
    SemanticDateField,
    SemanticDateTimeField,
    SemanticModelChoiceField,
    SemanticModelMultipleChoiceField,
    SemanticMultipleChoiceField,
    SemanticTimeField,
    SemanticTypedChoiceField,
    SemanticTypedMultipleChoiceField,
)

BOOLEAN_CHOICES = (
    ("true", _("Yes")),
    ("false", _("No")),
)


def coerce_boolean(value):
    """Coerce semantic boolean filter values."""
    if value in (True, "true", "True", "1", 1):
        return True
    if value in (False, "false", "False", "0", 0):
        return False
    return value


class SemanticDateTimeFilter(DateTimeFilter):
    """Semantic datetime filter."""

    field_class = SemanticDateTimeField


class SemanticDateFilter(DateFilter):
    """Semantic date filter."""

    field_class = SemanticDateField


class SemanticTimeFilter(TimeFilter):
    """Semantic time filter."""

    field_class = SemanticTimeField


class SemanticChoiceFilter(ChoiceFilter):
    """Semantic choice filter."""

    field_class = SemanticChoiceField


class SemanticMultipleChoiceFilter(MultipleChoiceFilter):
    """Semantic multiple choice filter."""

    field_class = SemanticMultipleChoiceField


class SemanticTypedChoiceFilter(TypedChoiceFilter):
    """Semantic typed choice filter."""

    field_class = SemanticTypedChoiceField


class SemanticTypedMultipleChoiceFilter(TypedMultipleChoiceFilter):
    """Semantic typed multiple choice filter."""

    field_class = SemanticTypedMultipleChoiceField


class SemanticBooleanFilter(SemanticTypedMultipleChoiceFilter):
    """Semantic boolean filter."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("choices", BOOLEAN_CHOICES)
        kwargs.setdefault("coerce", coerce_boolean)
        kwargs.setdefault("distinct", False)
        super().__init__(*args, **kwargs)

    def is_noop(self, qs, value):
        return {coerce_boolean(item) for item in value} == {True, False}


class SemanticAllValuesFilter(AllValuesFilter):
    """Semantic all values filter."""

    field_class = SemanticChoiceField


class SemanticMultipleAllValuesFilter(AllValuesMultipleFilter):
    """Semantic multiple all values filter."""

    field_class = SemanticMultipleChoiceField


class SemanticModelChoiceFilter(ModelChoiceFilter):
    """Semantic model choice filter."""

    field_class = SemanticModelChoiceField


class SemanticModelMultipleChoiceFilter(ModelMultipleChoiceFilter):
    """Semantic model multiple choice filter."""

    field_class = SemanticModelMultipleChoiceField
