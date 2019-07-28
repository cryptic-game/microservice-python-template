from unittest import TestCase

from mock.mock_loader import mock
from models.template import Template


class TestWalletModel(TestCase):
    def setUp(self):
        mock.reset_mocks()

    def test__model__template__structure(self):
        self.assertEqual("Template", Template.__tablename__)
        self.assertTrue(issubclass(Template, mock.wrapper.Base))
        for col in ["uuid"]:
            self.assertIn(col, dir(Template))

    def test__model__template__serialize(self):
        wallet = Template(uuid="some-uuid")

        expected_result = {"uuid": "some-uuid"}
        serialized = wallet.serialize

        self.assertEqual(expected_result, serialized)

        serialized["uuid"] = "other-uuid"
        self.assertEqual(expected_result, wallet.serialize)

    def test__model__template__create(self):
        actual_result = Template.create()

        self.assertRegex(actual_result.uuid, r"[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}")
        mock.wrapper.session.add.assert_called_with(actual_result)
        mock.wrapper.session.commit.assert_called_with()

    def test__model__wallet__create__different_uuid(self):
        first_element = Template.create().uuid
        second_element = Template.create().uuid
        self.assertNotEqual(first_element, second_element)
