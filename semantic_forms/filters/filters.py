from django import forms
from django.utils.translation import gettext_lazy as _
from django_filters.conf import settings
from django_filters.fields import (
    ChoiceField,
    ChoiceIterator,
    ChoiceIteratorMixin,
    ModelChoiceField,
    ModelMultipleChoiceField,
    MultipleChoiceField,
)
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
    SemanticDateField,
    SemanticDateTimeField,
    SemanticTimeField,
)
from semantic_forms.widgets import SemanticSelect, SemanticSelectMultiple

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


class SemanticFilterChoiceField(ChoiceField):
    """Semantic filter choice field."""

    widget = SemanticSelect


class SemanticFilterMultipleChoiceField(MultipleChoiceField):
    """Semantic filter multiple choice field."""

    widget = SemanticSelectMultiple


class SemanticFilterTypedChoiceField(ChoiceIteratorMixin, forms.TypedChoiceField):
    """Semantic filter typed choice field."""

    iterator = ChoiceIterator
    widget = SemanticSelect

    def __init__(self, *args, **kwargs):
        self.empty_label = kwargs.pop("empty_label", settings.EMPTY_CHOICE_LABEL)
        super().__init__(*args, **kwargs)


class SemanticFilterTypedMultipleChoiceField(
    ChoiceIteratorMixin, forms.TypedMultipleChoiceField
):
    """Semantic filter typed multiple choice field."""

    iterator = ChoiceIterator
    widget = SemanticSelectMultiple

    def __init__(self, *args, **kwargs):
        self.empty_label = None
        super().__init__(*args, **kwargs)


class SemanticFilterModelChoiceField(ModelChoiceField):
    """Semantic filter model choice field."""

    widget = SemanticSelect


class SemanticFilterModelMultipleChoiceField(ModelMultipleChoiceField):
    """Semantic filter model multiple choice field."""

    widget = SemanticSelectMultiple


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

    field_class = SemanticFilterChoiceField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("empty_label", "")
        super().__init__(*args, **kwargs)


class SemanticMultipleChoiceFilter(MultipleChoiceFilter):
    """Semantic multiple choice filter."""

    field_class = SemanticFilterMultipleChoiceField


class SemanticTypedChoiceFilter(TypedChoiceFilter):
    """Semantic typed choice filter."""

    field_class = SemanticFilterTypedChoiceField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("empty_label", "")
        super().__init__(*args, **kwargs)


class SemanticTypedMultipleChoiceFilter(TypedMultipleChoiceFilter):
    """Semantic typed multiple choice filter."""

    field_class = SemanticFilterTypedMultipleChoiceField


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

    field_class = SemanticFilterChoiceField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("empty_label", "")
        super().__init__(*args, **kwargs)


class SemanticMultipleAllValuesFilter(AllValuesMultipleFilter):
    """Semantic multiple all values filter."""

    field_class = SemanticFilterMultipleChoiceField


class SemanticModelChoiceFilter(ModelChoiceFilter):
    """Semantic model choice filter."""

    field_class = SemanticFilterModelChoiceField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("empty_label", "")
        super().__init__(*args, **kwargs)


class SemanticModelMultipleChoiceFilter(ModelMultipleChoiceFilter):
    """Semantic model multiple choice filter."""

    field_class = SemanticFilterModelMultipleChoiceField
