from django import forms, template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from semantic_forms.widgets import SemanticCheckboxInput

register = template.Library()


def _add_tag_classes(tag: str, classes: str) -> str:
    class_attr = 'class="'
    if class_attr in tag:
        return tag.replace(class_attr, f"{class_attr}{classes} ", 1)
    return tag.replace(">", f' class="{classes}">', 1)


def _identity(value: object) -> object:
    return value


@register.filter(name="is_checkbox")
def is_checkbox(field: forms.Field) -> bool:
    """Is the field a checkbox?"""
    return isinstance(field.field.widget, SemanticCheckboxInput)


@register.filter(is_safe=True, needs_autoescape=True)
def semantic_help_text(value: object, autoescape: bool = True):
    """Render generated help text with Semantic UI list classes."""
    if not value:
        return ""

    escaper = conditional_escape if autoescape else _identity
    html = str(escaper(value))
    html = html.replace("<ul>", _add_tag_classes("<ul>", "ui bulleted list"))
    html = html.replace("<li>", _add_tag_classes("<li>", "item"))
    return mark_safe(html)


@register.filter(is_safe=True, needs_autoescape=True)
def semantic_error_list(value: object, autoescape: bool = True):
    """Render Django form errors as a compact Semantic UI error list."""
    if not value:
        return ""

    errors = [value] if isinstance(value, str) else value
    escaper = conditional_escape if autoescape else _identity
    items = "".join(f'<li class="item">{escaper(error)}</li>' for error in errors)
    return mark_safe(f'<ul class="ui bulleted list semantic-error-list">{items}</ul>')
