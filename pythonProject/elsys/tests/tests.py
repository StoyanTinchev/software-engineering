import unittest

from django.test import TestCase
from elsys.models import Car
from datetime import datetime

from unittest.mock import Mock, patch
from elsys.processors.api_processor import ApiProcessor
import json


class TestCarModel(TestCase):
    def setUp(self):
        # called when test is started
        Car.objects.create(color="red", made=datetime.now(), brand="audi", description="red audi")
        Car.objects.create(color="green", made=datetime.now(), brand="bmw", description="red bmw")

    def tearDown(self):
        # called after tests were run
        pass

    def test_car_is_red(self):
        assert Car.objects.get(brand="audi").color == "red"

    def test_car_is_green(self):
        assert Car.objects.get(brand="bmw").color == "green"


class TestC(TestCase):
    @patch("requests.get")
    def test_call_api(self, mocked_requests):
        data = json.load(open('./elsys/comments.json'))
        mocked_requests.return_value.json = Mock(return_value=data)
        response = ApiProcessor().longest_comment()
        assert response['id'] == 3


# mock test for post_with_longest_title
class TestPostWithLongestTitle(TestCase):
    @patch("requests.get")
    def test_call_api(self, mocked_requests):
        data = json.load(open('./elsys/posts.json'))
        mocked_requests.return_value.json = Mock(return_value=data)
        response = ApiProcessor().post_with_longest_title()
        print(response)
        assert response['id'] == 58


if __name__ == '__main__':
    unittest.main()
