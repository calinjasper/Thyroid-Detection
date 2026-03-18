from django.test import TestCase, Client
from django.urls import reverse
from .models import UserImageModel
from PIL import Image
import io

class Deploy8ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('Deploy_8')

    def test_deploy_8_post_request(self):
        # Create a dummy image for testing
        image = Image.new('RGB', (100, 100), color = 'red')
        image_file = io.BytesIO()
        image.save(image_file, 'jpeg')
        image_file.seek(0)

        response = self.client.post(self.url, {'image': image_file})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'output.html')
