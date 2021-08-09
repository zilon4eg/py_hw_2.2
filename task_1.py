import requests
from pprint import pprint

def sorted_dict(dict):
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get, reverse=True)
    for key in sorted_keys:
        sorted_dict[key] = dict[key]
    return sorted_dict

def sorted_super_heroes_by_intelligence(access_token, super_heroes):
    base_url = 'https://superheroapi.com/api/'

    super_heroes_intelligence = {}
    for super_hero in super_heroes:
        response = requests.get(f'{base_url}{access_token}/search/{super_hero}')
        id = response.json()['results'][0]['id']
        powerstats = requests.get(f'{base_url}{access_token}/{id}/powerstats')
        intelligence = int(powerstats.json()['intelligence'])
        super_heroes_intelligence[super_hero] = intelligence
    sorted_super_heroes_intelligence = sorted_dict(super_heroes_intelligence)

    print('Было у отца три сына:')
    for id, element in enumerate(sorted_super_heroes_intelligence, 1):
        if id == 1:
            print(f'Старший умный был детина - {element}:{sorted_super_heroes_intelligence[element]}')
        elif id == 2:
            print(f'Средний был и так и сяк - {element}:{sorted_super_heroes_intelligence[element]}')
        else:
            print(f'Младший вовсе был дурак - {element}:{sorted_super_heroes_intelligence[element]}')


access_token = '2619421814940190'
super_heroes = ['Hulk', 'Captain America', 'Thanos']

sorted_super_heroes_by_intelligence(access_token, super_heroes)