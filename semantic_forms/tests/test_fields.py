from django.test import SimpleTestCase

from semantic_forms.fields import (
    SemanticCharField,
    SemanticCheckboxField,
    SemanticCheckboxMultipleChoiceField,
    SemanticChoiceField,
    SemanticDateField,
    SemanticDateTimeField,
    SemanticFileField,
    SemanticMultipleChoiceField,
    SemanticRadioChoiceField,
    SemanticTextareaField,
    SemanticTimeField,
)
from semantic_forms.widgets import (
    SemanticCheckboxInput,
    SemanticCheckboxSelectMultiple,
    SemanticDateInput,
    SemanticDateTimeInput,
    SemanticFileInput,
    SemanticRadioSelect,
    SemanticSelect,
    SemanticSelectMultiple,
    SemanticTextarea,
    SemanticTextInput,
    SemanticTimeInput,
)


class SemanticFieldTests(SimpleTestCase):
    def test_checkbox_field_defaults(self):
        field = SemanticCheckboxField()

        self.assertFalse(field.required)
        self.assertEqual(field.label_suffix, "")
        self.assertIsInstance(field.widget, SemanticCheckboxInput)

    def test_checkbox_field_preserves_explicit_required_and_label_suffix(self):
        field = SemanticCheckboxField(required=True, label_suffix="?")

        self.assertTrue(field.required)
        self.assertEqual(field.label_suffix, "?")

    def test_field_classes_use_semantic_widgets(self):
        cases = [
            (SemanticCharField, SemanticTextInput),
            (SemanticTextareaField, SemanticTextarea),
            (SemanticDateTimeField, SemanticDateTimeInput),
            (SemanticDateField, SemanticDateInput),
            (SemanticTimeField, SemanticTimeInput),
            (SemanticCheckboxMultipleChoiceField, SemanticCheckboxSelectMultiple),
            (SemanticRadioChoiceField, SemanticRadioSelect),
            (SemanticChoiceField, SemanticSelect),
            (SemanticMultipleChoiceField, SemanticSelectMultiple),
            (SemanticFileField, SemanticFileInput),
        ]

        for field_class, widget_class in cases:
            with self.subTest(field_class=field_class.__name__):
                self.assertIsInstance(field_class().widget, widget_class)
