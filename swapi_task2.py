import requests
from typing import List
from pprint import pprint
from typing import Dict, List
from utils.fetch_url import fetch_data
from utils.timing import timeit


@timeit
def get_all_char_names(result: Dict) -> List:
    """
    picks only names in characters data
    :param result:data fetched  from 1 film
    :return:name of character in movie 1
    """
    char_urls = result.get('characters')
    char_data = fetch_data(char_urls) if char_urls else []
    char_names = [char.get('name') for char in char_data if char_data]
    return char_names


@timeit
def get_all_vehicles_name(result: Dict) -> List:
    """
        pick data from vehicles
        :param result:data from first file
        :return:name of vehicles
    """
    v_urls = result.get('vehicles')
    v_data = fetch_data(v_urls) if v_urls else []
    v_names = [vehicle.get('name') for vehicle in v_data if v_data]
    return v_names


if __name__ == "__main__":
    print(__name__)

    url = "https://swapi.dev/api/films/1"
    response = requests.get(url)
    result = response.json()

    char_names = get_all_char_names(result)
    v_names = get_all_vehicles_name(result)

    print(char_names)
    print('####' * 30)
    print(v_names)
