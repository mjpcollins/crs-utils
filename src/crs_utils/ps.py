import os
import zlib
import json
from google.cloud import pubsub_v1


def get_gcp_project():
    return os.getenv('GCP_PROJECT')


def post_to_pubsub(data, topic, compress=False):
    publisher = pubsub_v1.PublisherClient()
    project = get_gcp_project()
    topic_path = publisher.topic_path(project, topic)
    message = get_pubsub_safe_message(data, compress)
    publisher.publish(topic_path, message)


def get_pubsub_safe_message(data, compress=False):
    if isinstance(data, dict):
        message_str = json.dumps(data)
    else:
        message_str = str(data)
    if compress:
        return compress_str(message_str)
    return message_str.encode('utf-8')


def decompress_json_data(data):
    s = decompress_str(data)
    return json.loads(s)


def compress_str(s):
    s_as_bytes = s.encode('utf-8')
    return zlib.compress(s_as_bytes)


def decompress_str(compressed_s):
    s_as_bytes = zlib.decompress(compressed_s)
    s = s_as_bytes.decode('utf-8')
    return s
