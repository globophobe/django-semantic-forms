from django.test import SimpleTestCase
from django.urls import reverse


class KitchenSinkViewTests(SimpleTestCase):
    def test_demo_view_renders_semantic_media_once(self):
        response = self.client.get(reverse("semantic-forms-kitchen-sink"))

        self.assertEqual(response.status_code, 200)

        content = response.content.decode()
        catalog_url = reverse("javascript-catalog")

        self.assertEqual(content.count("semantic_forms/semanticDropdown.js"), 1)
        self.assertEqual(content.count("semantic_forms/semanticCheckbox.js"), 1)
        self.assertEqual(content.count("semantic_forms/semanticCalendar.js"), 1)
        self.assertEqual(content.count("semantic_forms/semanticTranslatedCalendar.js"), 1)
        self.assertEqual(content.count(catalog_url), 1)
