from django_filters.filters import (
    AllValuesMultipleFilter,
    ChoiceFilter,
    DateFilter,
    DateTimeFilter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter,
    MultipleChoiceFilter,
    TimeFilter,
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


class SemanticTypedChoiceFilter(TypedMultipleChoiceFilter):
    """Semantic typed choice filter."""

    field_class = SemanticTypedChoiceField


class SemanticTypedMultipleChoiceFilter(TypedMultipleChoiceFilter):
    """Semantic typed multiple choice filter."""

    field_class = SemanticTypedMultipleChoiceField


class SemanticMultipleAllValuesFilter(AllValuesMultipleFilter):
    """Semantic multiple all values filter."""

    field_class = SemanticChoiceField


class SemanticModelChoiceFilter(ModelChoiceFilter):
    """Semantic model choice filter."""

    field_class = SemanticModelChoiceField


class SemanticModelMultipleChoiceFilter(ModelMultipleChoiceFilter):
    """Semantic model multiple choice filter."""

    field_class = SemanticModelMultipleChoiceField
