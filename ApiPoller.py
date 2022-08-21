import requests
import asyncio
import aiohttp

class ApiPoller:
    def __init__(self):
        self.url = 'https://httpbin.org/'
        self.headers = {
            'Content-Type': 'application/json'
        }

    def process(self):
        pass

    def get_json(self):
        endpoint = 'json'
        self.call_api(self.url + endpoint)
        pass

    def get_json_loop(self):
        endpoint = 'json'
        self.call_api_with_loop(self.url + endpoint)

    def get_json_async(self):
        endpoint = 'json'
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(self.call_api_async(self.url + endpoint))

    def run_delay(self, delay):
        endpoint = f'delay/{delay}'
        self.call_api(self.url + endpoint)

    def call_api(self, url):
        requests.request('GET', url, params=None, headers=self.headers)
        
    def call_api_with_loop(self, url):
        print('Starting Loop')
        for _ in range(1, 101):
            requests.request('GET', url, params=None, headers=self.headers)
        print('Exit loop')
    
    async def call_api_async(self, url):
        print('Entering async')

        tasks = []
        async with aiohttp.ClientSession() as session:
            for _ in range(1, 101):
                tasks.append(session.get(url, headers=self.headers))
            
            responses = await asyncio.gather(*tasks)

        for response in responses:
            data = await response.json()
            print(data)

        print('Exiting async')


