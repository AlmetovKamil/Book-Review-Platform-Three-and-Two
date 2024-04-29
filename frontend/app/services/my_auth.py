import httpx


class MyAuth(httpx.Auth):
    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
        request.headers["Authorization"] = self.token
        yield request


client = httpx.Client()
