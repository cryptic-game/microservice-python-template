from unittest import TestCase

from mock.mock_loader import mock
from resources import endpoints


class TestWallet(TestCase):
    def setUp(self):
        mock.reset_mocks()

    def test__user_endpoint__echo(self):
        expected_result = {"message": "hello world", "user": "user-uuid"}
        actual_result = endpoints.echo({"message": "hello world"}, "user-uuid")

        self.assertEqual(expected_result, actual_result)

    def test__ms_endpoint__info(self):
        expected_result = {"message": "hello world", "microservice": "test-ms"}
        actual_result = endpoints.info({"message": "hello world"}, "test-ms")

        self.assertEqual(expected_result, actual_result)

    def test__ms_endpoint__delete_user(self):
        expected_result = {"success": True}
        actual_result = endpoints.delete_user({"user": "user-123"}, "server")

        self.assertEqual(expected_result, actual_result)
