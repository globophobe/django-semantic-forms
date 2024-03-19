from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .forms import DemoForm

try:
    from django.utils.translation import gettext_lazy as _  # Django >= 4
except ImportError:
    from django.utils.translation import ugettext_lazy as _


def semantic_form_demo(request: HttpResponse) -> HttpResponse:
    """Semantic form demo"""
    if request.method == "POST":
        form = DemoForm(request.POST)
        if form.is_valid():
            messages.success(request, _("Thank you for your submission."))
    else:
        form = DemoForm()
    return render(request, "semantic_forms.html", {"form": form})
