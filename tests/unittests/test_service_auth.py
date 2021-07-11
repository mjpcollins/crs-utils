from src.crs_utils.service_auth import *
from tests.unittests_utils.common import TestInvolvingAuth


class TestServiceAuth(TestInvolvingAuth):

    def test_get_auth_token_when_in_cloud(self):
        os.environ["CLOUD"] = "True"
        expected_token = "TESTTOKENSERVICE2SERVICE"
        actual_token = get_auth_token(self._test_service_url)
        self.assertEqual(expected_token, actual_token)

    def test_get_auth_token_when_in_local(self):
        expected_token = "TESTTOKENLOCAL"
        actual_token = get_auth_token(self._test_service_url)
        self.assertEqual(expected_token, actual_token)

    def test_get_local_auth_token(self):
        expected_token = "TESTTOKENLOCAL"
        actual_token = get_local_auth_token()
        self.assertEqual(expected_token, actual_token)

    def test_get_service_to_service_token(self):
        expected_token = "TESTTOKENSERVICE2SERVICE"
        actual_token = get_service_to_service_token(self._test_service_url)
        self.assertEqual(expected_token, actual_token)
