import requests
from pprint import pprint

token = 'AQAAAABObNioAADLW6YcfbMcdkX3riuShOu7u9M'
base_url = 'https://cloud-api.yandex.net:443/'

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""



headers = {
    'accept': 'application/json',
    'authorization': f'OAuth {token}'
}

# response = requests.get(f'{base_url}v1/disk', headers=headers) получение параметров я.диска пользователя

#===(запрос на получение ссылки для загрузки файла)==
response = requests.get(f'{base_url}v1/disk/resources/upload', params={'path': 'data-science.jpg', 'overwrite': 'true'}, headers=headers)
print(response.json())

#===(загрузка файла c ПК на я.диск)==
upload_url = response.json()['href']
response = requests.put(upload_url, files={'file': open('data\data-science.jpg', 'rb')})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
