import requests
import asyncio
import json
from aiohttp import ClientSession


class ApiPoller:
    def __init__(self):
        self.url = 'https://httpbin.org/'
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.calls = 100

    def process(self):
        pass

    def get_json(self):
        endpoint = 'json'
        self.call_api(self.url + endpoint)

    def get_json_loop(self):
        endpoint = 'json'
        self.call_api_with_loop(self.url + endpoint)

    def get_json_async(self):
        endpoint = 'json'
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.call_api_async(self.url + endpoint))

    def run_delay(self, delay):
        endpoint = f'delay/{delay}'
        self.call_api(self.url + endpoint)

    def call_api(self, url):
        requests.request('GET', url, params=None, headers=self.headers)
        
    def call_api_with_loop(self, url):
        print(f'Making {self.calls} requests in a loop')
        for _ in range(1, self.calls+1):
            requests.request('GET', url, params=None, headers=self.headers)
        print('Exit loop')
    
    async def call_api_async(self, url):
        print (f'Making {self.calls} request async')

        tasks = []
        async with ClientSession() as session:
            for _ in range(1, self.calls + 1):
                tasks.append(session.get(url, headers=self.headers))

            responses = await asyncio.gather(*tasks)

        for response in responses:
            data = await response.json()
        print('Exiting async')
