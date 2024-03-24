from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .forms import SemanticKitchenSinkForm

try:
    from django.utils.translation import gettext_lazy as _  # Django >= 4
except ImportError:
    from django.utils.translation import ugettext_lazy as _

BASIC_TEMPLATE = """{% extends "semantic_forms/base.html" %}

{% block extrahead %}{{ form.media }}{% endblock %}

{% block content %}
<form class="ui form{% if errors %} error{% endif %}" action="/" method="post" novalidate>
    {% csrf_token %}{{ form }}
</form>
{% endblock %}"""


def semantic_forms_kitchen_sink(request: HttpResponse) -> HttpResponse:
    """Semantic forms kitchen sink."""
    if request.method == "POST":
        form = SemanticKitchenSinkForm(request.POST)
        if form.is_valid():
            messages.success(request, _("Thank you for your submission."))
    else:
        form = SemanticKitchenSinkForm()
    return render(
        request,
        "semantic_forms/demo/kitchen_sink.html",
        {"form": form, "basic_template": BASIC_TEMPLATE},
    )
