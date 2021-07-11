from tests.unittests_utils.common import TestInvolvingAuth
from src.crs_utils.direct import add_token_to_headers


class TestDirect(TestInvolvingAuth):

    def test_add_token_to_headers(self):
        header = {'argument': "no it isn't"}
        expected_header = {'argument': "no it isn't",
                           'Authorization': 'Bearer: TESTTOKENLOCAL'}
        actual_header = add_token_to_headers(self._test_service_url,
                                             header)
        self.assertEqual(expected_header, actual_header)

    def test_add_token_to_headers_no_input(self):
        expected_header = {'Authorization': 'Bearer: TESTTOKENLOCAL'}
        actual_header = add_token_to_headers(self._test_service_url)
        self.assertEqual(expected_header, actual_header)
