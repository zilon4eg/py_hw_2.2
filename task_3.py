import requests, time
from datetime import date
from pprint import pprint

def questions_for_two_days():
    site = "stackoverflow.com"
    all_questions = []
    day_today = (int(date.today().strftime('%d')))
    month_today = (int(date.today().strftime('%m')))
    year_today = (int(date.today().strftime('%Y')))
    yesterday = str(time.mktime(time.strptime(f'{day_today}/{month_today}/{year_today}', "%d/%m/%Y")))[:-2]
    day_before_yesterday = str(time.mktime(time.strptime(f'{day_today - 2}/{month_today}/{year_today}', "%d/%m/%Y")))[:-2]

    response = requests.get(f'https://api.stackexchange.com/2.3/questions', params={'tagged': 'Python', 'site': site, 'fromdate': day_before_yesterday, 'todate': yesterday}).json()

    for question in response['items']:
        dict_questions = {}
        dict_questions['question_id'] = question['question_id']
        dict_questions['link'] = question['link']
        dict_questions['tags'] = question['tags']
        all_questions.append(dict_questions)

    print(f'Все вопросы c "stackoverflow.com" за последние два дня, содержащие тэг "Python":')
    for question in all_questions:
        print(question)

questions_for_two_days()