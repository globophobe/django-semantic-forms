from django.test import SimpleTestCase

from semantic_forms import SemanticForm
from semantic_forms.fields import SemanticCharField, SemanticCheckboxField
from semantic_forms.templatetags.semantic_forms import is_checkbox


class ExampleForm(SemanticForm):
    name = SemanticCharField()
    enabled = SemanticCheckboxField()


class SemanticTemplateTagTests(SimpleTestCase):
    def test_is_checkbox_detects_semantic_checkbox_widget(self):
        form = ExampleForm()

        self.assertFalse(is_checkbox(form["name"]))
        self.assertTrue(is_checkbox(form["enabled"]))
