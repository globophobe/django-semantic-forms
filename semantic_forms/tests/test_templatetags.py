from django.test import SimpleTestCase
from django.utils.safestring import mark_safe

from semantic_forms import SemanticForm
from semantic_forms.fields import SemanticCharField, SemanticCheckboxField
from semantic_forms.templatetags.semantic_forms import (
    is_checkbox,
    semantic_error_list,
    semantic_help_text,
)


class ExampleForm(SemanticForm):
    name = SemanticCharField()
    enabled = SemanticCheckboxField()


class HelpTextForm(SemanticForm):
    safe_help = SemanticCharField(
        help_text=mark_safe("<ul><li>Use letters</li></ul>"),
        required=False,
    )
    plain_help = SemanticCharField(
        help_text="<strong>Plain</strong>",
        required=False,
    )


class SemanticTemplateTagTests(SimpleTestCase):
    def test_is_checkbox_detects_semantic_checkbox_widget(self):
        form = ExampleForm()

        self.assertFalse(is_checkbox(form["name"]))
        self.assertTrue(is_checkbox(form["enabled"]))

    def test_semantic_help_text_adds_semantic_list_classes(self):
        html = semantic_help_text(mark_safe("<ul><li>One</li><li>Two</li></ul>"))

        self.assertIn('<ul class="ui bulleted list">', html)
        self.assertEqual(html.count('<li class="item">'), 2)

    def test_semantic_help_text_escapes_plain_html(self):
        html = semantic_help_text("<ul><li>One</li></ul>")

        self.assertIn("&lt;ul&gt;&lt;li&gt;One&lt;/li&gt;&lt;/ul&gt;", html)
        self.assertNotIn("<ul>", html)

    def test_semantic_error_list_uses_semantic_list_classes(self):
        html = semantic_error_list(["One", "Two"])

        self.assertIn('<ul class="ui bulleted list semantic-error-list">', html)
        self.assertEqual(html.count('<li class="item">'), 2)

    def test_semantic_error_list_escapes_errors(self):
        html = semantic_error_list(['<script>alert("x")</script>'])

        self.assertIn("&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;", html)
        self.assertNotIn("<script>", html)


class SemanticFormRenderTests(SimpleTestCase):
    def test_form_rendering_uses_semantic_help_text(self):
        rendered = str(HelpTextForm())

        self.assertIn('class="help semantic-help-text"', rendered)
        self.assertIn('<ul class="ui bulleted list">', rendered)
        self.assertIn('<li class="item">Use letters</li>', rendered)
        self.assertIn("&lt;strong&gt;Plain&lt;/strong&gt;", rendered)
        self.assertNotIn("<strong>Plain</strong>", rendered)

    def test_form_rendering_uses_semantic_error_list(self):
        form = ExampleForm(data={})

        self.assertFalse(form.is_valid())

        rendered = str(form)

        self.assertIn('class="ui bulleted list semantic-error-list"', rendered)
        self.assertIn('<li class="item">', rendered)
