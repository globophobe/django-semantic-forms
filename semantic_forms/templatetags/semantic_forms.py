from django import forms, template

from semantic_forms.widgets import SemanticCheckboxInput

register = template.Library()


@register.filter(name="is_checkbox")
def is_checkbox(field: forms.Field) -> bool:
    """Is the field a checkbox?"""
    return isinstance(field.field.widget, SemanticCheckboxInput)
