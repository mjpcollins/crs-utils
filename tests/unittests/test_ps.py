from unittest import TestCase
from src.crs_utils.ps import *


class TestPS(TestCase):

    def setUp(self):
        self._delete_env_var("GCP_PROJECT")
        self._bytes = b'x\x9c\xabV\xcaH\xcd\xc9\xc9W\xb2RP*\xcf/\xcaIQ\xaa\x05\x009\x99\x06\x17'
        self._test_string = '{"hello": "world"}'
        self._test_dict = {"hello": "world"}

    def tearDown(self):
        self._delete_env_var("GCP_PROJECT")

    def test_get_gcp_project(self):
        os.environ['GCP_PROJECT'] = 'project-123124'
        expected_project = 'project-123124'
        actual_project = get_gcp_project()
        self.assertEqual(expected_project, actual_project)

    def test_compress_str(self):
        actual_bytes = compress_str(self._test_string)
        self.assertEqual(self._bytes, actual_bytes)

    def test_decompress_str(self):
        actual_str = decompress_str(self._bytes)
        self.assertEqual(self._test_string, actual_str)

    def test_decompress_json_data(self):
        actual_json_data = decompress_json_data(self._bytes)
        self.assertEqual(self._test_dict, actual_json_data)

    def test_get_pubsub_safe_message_str(self):
        input_s = 'message to post'
        expected_message = b'message to post'
        actual_message = get_pubsub_safe_message(data=input_s,
                                                 compress=False)
        self.assertEqual(expected_message, actual_message)

    def test_get_pubsub_safe_message_json(self):
        expected_message = b'{"hello": "world"}'
        actual_message = get_pubsub_safe_message(data=self._test_dict,
                                                 compress=False)
        self.assertEqual(expected_message, actual_message)

    def test_get_pubsub_safe_message_json_compressed(self):
        actual_message = get_pubsub_safe_message(data=self._test_dict,
                                                 compress=True)
        self.assertEqual(self._bytes, actual_message)

    @staticmethod
    def _delete_env_var(variable):
        try:
            del os.environ[variable]
        except KeyError:
            pass
