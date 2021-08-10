import requests

response = requests.get('http://meta.example.stackexchange.com/answers/{/fromdate/1;2;3}/questions')
print(response.text)