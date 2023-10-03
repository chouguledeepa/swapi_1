import requests

from utils.randgn import produce_char

start = 1
stop = 15

obj =produce_char()
characters = []

characters.append(next(obj))

if __name__=="__main__":
    print(__name__)

    home_url = "https://swapi.dev"
    relative = "api/people/{0}"

    for num_ in characters:
        absolute_url = home_url + relative.format(num_)
        print(f"fetching Details : -{absolute_url} => \n")
        response = requests.get(absolute_url)
        response= response.json()
        print(response)
        print()
        print("@@@@@"*30)
        print()