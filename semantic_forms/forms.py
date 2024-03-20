from django import forms


class SemanticFormMixin:
    """Semantic form mixin."""

    template_name = "semantic_forms/forms/semantic_form.html"


class SemanticForm(SemanticFormMixin, forms.Form):
    """Semantic form."""


class SemanticModelForm(SemanticFormMixin, forms.ModelForm):
    """Semantic model form."""
