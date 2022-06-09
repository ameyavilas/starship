import requests

# Global variable to append all page result into single list
startship_list = []
films_list = []


def get_response(url):
    json_data = requests.get(url).json()
    return json_data


def get_starship_result(url):
    starship_result = get_response(url)
    startship_list.extend(starship_result['results'])
    if starship_result['next'] is not None:
        get_starship_result(starship_result['next'])


def get_film_result(url):
    film_result = get_response(url)
    films_list.extend(film_result['results'])
    if film_result['next'] is not None:
        print(film_result['next'])
        get_film_result(film_result['next'])

# Exercise 1
def all_ships_in_return_of_jedi():
    starships_in_return_of_jedi = [films['starships'] for films in films_list if films['title'] == 'Return of the Jedi']
    starships_return_of_jedi = [starships['name'] for starships in startship_list if starships['url'] in starships_in_return_of_jedi[0]]
    return starships_return_of_jedi

# Exercise 2
def all_ships_hyperdrive_rating_condition():
    starships_hyper_drive = [starships['name'] for starships in startship_list if starships['hyperdrive_rating'] != "unknown" and float(starships['hyperdrive_rating']) >= 1.0]
    return starships_hyper_drive

# Exercise 3
def all_ships_with_crew_condition():
    starships_crew_condition = [starships['name'] for starships in startship_list if (starships['crew'] != "unknown" and "-" not in str(starships['crew'])) and (int(starships['crew'].replace(",", "")) > 3 and int(starships['crew'].replace(",", "")) < 100)]
    return starships_crew_condition


if __name__ == '__main__':
    get_starship_result("https://swapi.dev/api/starships/")
    get_film_result("https://swapi.dev/api/films/")
    print("Exercise 1 result")
    print(all_ships_in_return_of_jedi())   # Exercise 1 result
    print("Exercise 2 result") 
    print(all_ships_hyperdrive_rating_condition())   # Exercise 2 result
    print("Exercise 3 result")
    print(all_ships_with_crew_condition())  # Exercise 3 result
