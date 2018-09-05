import requests
import random


def build_api_call(name):
    prefix = 'https://api.genderize.io/?name='

    return prefix + name


def guess_species(name):
    if not name:
        raise ValueError

    if str.isdigit(name):
        return 'florborg'

    return 'human'


def guess_human_gender(name):
    query = build_api_call(name)

    response = requests.get(query)
    response = response.json()

    return response['gender']


def guess_gender(name):
    if not name:
        raise ValueError

    customer_species = guess_species(name)

    if customer_species == 'human':
        customer_gender = guess_human_gender(name)
    else:
        customer_gender = 'florborg'

    return customer_gender


def get_recommendation(gender):
    recommendations_map = {
        'male': ['Condoms', 'Male-oriented scented shaving foam', 'Die Hard 4', 'Larger than average shoe'],
        'female': ['Bras', 'Flowers', 'Bridgette Jones\' Diary', 'Smaller than average shoe'],
        'florborg': ['Oil', 'CPUs', 'Silver suits', 'Warp Cores']
    }

    return random.choice(recommendations_map[gender])
