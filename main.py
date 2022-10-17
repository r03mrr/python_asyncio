from ApiPoller import ApiPoller
from time import perf_counter


def json_loop(poller):
    start_time = perf_counter()
    poller.get_json_loop()
    end_time = perf_counter()
    print(f'JSON LOOP - Run time {end_time - start_time}')


def json_async(poller):
    start_time = perf_counter()
    poller.get_json_async()
    end_time = perf_counter()
    print(f'JSON ASYNC - Run time {end_time - start_time}')


def json_normal(poller):
    start_time = perf_counter()
    poller.get_json()
    end_time = perf_counter()
    print(f'JSON NORMAL - Run time {end_time - start_time}')

if __name__ == '__main__':
    api_poller = ApiPoller()
    json_normal(api_poller)
    json_loop(api_poller)
    json_async(api_poller)
