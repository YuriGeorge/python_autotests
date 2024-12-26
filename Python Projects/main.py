import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '322d486aa8513fc06ab0dd0d8bb9244a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "ein_yuhrer@mail.ru",
    "password": "Iloveqa111"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_putin = {
    "pokemon_id": "169772",
    "name": "chitaez",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "169772"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers_confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_putin = requests.put(url = f'{URL}/pokemons', headers = HEADER, json =  body_putin)
print(response_putin.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)            