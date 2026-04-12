from unittest.mock import patch

from django import forms
from django.test import SimpleTestCase
from django.urls import NoReverseMatch

from semantic_forms.widgets import (
    RangeWidget,
    SemanticDateInput,
    SemanticDateTimeInput,
)


class SemanticCalendarWidgetTests(SimpleTestCase):
    def test_calendar_media_uses_javascript_catalog_when_available(self):
        media = SemanticDateInput().media

        self.assertEqual(
            media._js,
            [
                "semantic_forms/semanticCalendar.js",
                "/jsi18n/",
                "semantic_forms/semanticTranslatedCalendar.js",
            ],
        )

    def test_calendar_media_falls_back_to_admin_catalog(self):
        with patch(
            "semantic_forms.widgets.reverse",
            side_effect=[NoReverseMatch, "/admin/jsi18n/"],
        ):
            media = SemanticDateInput().media

        self.assertEqual(
            media._js,
            [
                "semantic_forms/semanticCalendar.js",
                "/admin/jsi18n/",
                "semantic_forms/semanticTranslatedCalendar.js",
            ],
        )

    def test_calendar_media_falls_back_to_untranslated_calendar(self):
        with patch("semantic_forms.widgets.reverse", side_effect=NoReverseMatch):
            media = SemanticDateInput().media

        self.assertEqual(
            media._js,
            [
                "semantic_forms/semanticCalendar.js",
                "semantic_forms/semanticUntranslatedCalendar.js",
            ],
        )

    def test_date_and_datetime_inputs_use_default_formats(self):
        self.assertEqual(SemanticDateInput().format, "%Y-%m-%d")
        self.assertEqual(SemanticDateTimeInput().format, "%Y-%m-%d %H:%M")

    def test_range_widget_decompresses_start_and_stop(self):
        widget = RangeWidget(widgets=[forms.TextInput(), forms.TextInput()])

        self.assertEqual(widget.decompress(range(1, 3)), [1, 3])
        self.assertEqual(widget.decompress(None), [None, None])
