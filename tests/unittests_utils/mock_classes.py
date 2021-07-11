
class FakePipe:

    def read(self):
        return b"TESTTOKENLOCAL"


class FakePopen:

    def __init__(self, args, shell, stdout, stderr):
        self.stdout = stdout


class FakeRequests:

    def get(self, url, headers):
        return FakeResponse(url, headers)

    def post(self, url, json, headers):
        return FakeResponse(url, headers)


class FakeResponse:

    def __init__(self, url, headers):
        self.url = url
        if ("metadata/computeMetadata" in self.url) and (headers == {"Metadata-Flavor": "Google"}):
            self.content = b"TESTTOKENSERVICE2SERVICE"
        elif self.url == "https//www.cloud_run_service_url.com/":
            self.content = b""

