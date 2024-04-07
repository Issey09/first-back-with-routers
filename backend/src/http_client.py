import aiohttp

class HttpClient():
    def __init__(self, main_url):
        self.session = aiohttp.ClientSession(
            base_url=main_url
        )


class AsyncHttpClient(HttpClient):
    async def create_user(self):
        async with self.session.get('/create_user/') as resp:
            data = await resp.json()
            return data


