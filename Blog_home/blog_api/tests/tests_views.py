import unittest

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from blog.models import Note

class TestNoteListCreateAPIView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="Test@Test.ru")

    def test_list_objects(self):
        url = "/notes/"
        resp = self.client.get(url)

        expected_status_code = status.HTTP_200_OK
        self.assertEqual(expected_status_code, resp.status_code)

        response_data = resp.data
        expected_data = []
        self.assertEqual(expected_data, response_data)

        Note.objects.create(title="tests", author_id=1)

        resp = self.client.get(url)
        expected_status_code = status.HTTP_200_OK
        self.assertEqual(expected_status_code, resp.status_code)

        response_data = resp.data
        self.assertEqual(1, len(response_data))

    @unittest.skip("Еще не готово")
    def test_create_object(self):
        new_title = "test_title"
        data = {
            "title": new_title,
            "author": "1"
        }
        url = "/notes/"
        resp = self.client.post(url, json=data)
        self.assertEqual(status.HTTP_201_CREATED, resp.status_code)
        Note.objects.get(title=new_title)




