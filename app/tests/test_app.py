from importlib import machinery, util
from unittest import TestCase

from mock.mock_loader import mock
from resources import endpoints
from schemes import scheme_echo


def import_app(name: str = "app"):
    return machinery.SourceFileLoader(name, util.find_spec("app").origin).load_module()


class TestApp(TestCase):
    def setUp(self):
        mock.reset_mocks()

    def test__microservice_setup(self):
        app = import_app()

        mock.get_config.assert_called_with()
        self.assertEqual(mock.get_config(), app.config)

        mock.MicroService.assert_called_with("template")
        self.assertEqual(mock.MicroService(), app.m)

        mock.m.get_wrapper.assert_called_with()
        self.assertEqual(mock.m.get_wrapper(), app.wrapper)

    def test__run_as_main(self):
        import_app("__main__")

        mock.wrapper.Base.metadata.create_all.assert_called_with(bind=mock.wrapper.engine)
        mock.m.run.assert_called_with()

    def test__import_as_module(self):
        import_app()

        mock.wrapper.Base.metadata.create_all.assert_not_called()
        mock.m.run.assert_not_called()

    def test__endpoints_available(self):
        app = import_app("__main__")
        elements = [getattr(app, element_name) for element_name in dir(app)]

        registered_user_endpoints = mock.user_endpoints.copy()
        registered_ms_endpoints = mock.ms_endpoints.copy()

        expected_user_endpoints = [(["echo"], scheme_echo, endpoints.echo)]

        expected_ms_endpoints = [(["info"], endpoints.info), (["delete_user"], endpoints.delete_user)]

        for path, requires, func in expected_user_endpoints:
            self.assertIn((path, requires), registered_user_endpoints)
            registered_user_endpoints.remove((path, requires))
            self.assertIn(mock.user_endpoint_handlers[tuple(path)], elements)
            self.assertEqual(func, mock.user_endpoint_handlers[tuple(path)])

        for path, func in expected_ms_endpoints:
            self.assertIn(path, registered_ms_endpoints)
            registered_ms_endpoints.remove(path)
            self.assertIn(mock.ms_endpoint_handlers[tuple(path)], elements)
            self.assertEqual(func, mock.ms_endpoint_handlers[tuple(path)])

        self.assertFalse(registered_user_endpoints)
        self.assertFalse(registered_ms_endpoints)
