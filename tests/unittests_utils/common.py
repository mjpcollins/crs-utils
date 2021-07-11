from unittest import TestCase, mock
from src.crs_utils.service_auth import *
from tests.unittests_utils.mock_classes import *


class TestInvolvingAuth(TestCase):

    def setUp(self):
        self._fake_requests = mock.patch("src.crs_utils.service_auth.requests", FakeRequests())
        self._fake_pipe = mock.patch("src.crs_utils.service_auth.PIPE", FakePipe())
        self._fake_Popen = mock.patch("src.crs_utils.service_auth.Popen", FakePopen)
        self._fake_requests.start()
        self._fake_pipe.start()
        self._fake_Popen.start()
        self._test_service_url = "https//www.cloud_run_service_url.com/"

    def tearDown(self):
        try:
            del os.environ["CLOUD"]
        except KeyError:
            pass
        self._fake_requests.stop()
        self._fake_pipe.stop()
        self._fake_Popen.stop()


