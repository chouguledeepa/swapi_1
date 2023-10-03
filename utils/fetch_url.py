import requests
import random
import pprint
from typing import List
import logging

# logging configration
logging.basicConfig(
    filename='example.log',
    encoding='utf-8',
    level=logging.DEBUG
)


def mylogger(func):
    def wrapper(*url, **kwargs):
        try:
            logging.info(f'there are hitting url - {url}')
            result_ = func(url)
            logging.info(f'success -{result_.status_code}')
        except Exception:
            logging.error(f'there are issue fetch details')
        return result_

    return wrapper


@mylogger
def hit_url(url):
    return requests.get(url)


def fetch_data(urls: List) -> List:
    """
    fetching data
    :param urls:
    :return:
    """
    data = []
    for url in urls:
        res = requests.get(url)
        data.append(res.json())
    return data
