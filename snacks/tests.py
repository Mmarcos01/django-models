from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from snacks.models import Snack


class SnackTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com", password="pass")
        self.snack = Snack.objects.create(
            name = 'Chocolate River', purchaser = self.user, description = "chocolaty")

    def test_user_name(self):
        self.assertEqual(f'{self.user}', 'testuser')

    def test_string_representation(self):
        self.assertEqual(str(self.snack.name), 'Chocolate River')

    def test_snack_name(self):
        self.assertEqual(f'{self.snack.name}', 'Chocolate River')

    def test_snack_description(self):
        self.assertEqual(f'{self.snack.description}', 'chocolaty')

    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")
