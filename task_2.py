import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        base_url = 'https://cloud-api.yandex.net:443/'
        file_list = os.listdir(os.path.join(os.getcwd(), file_path))

        headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {self.token}'
        }

        for file in file_list:
            #===(запрос на получение ссылки для загрузки файла)==
            response = requests.get(f'{base_url}v1/disk/resources/upload', params={'path': file, 'overwrite': 'true'}, headers=headers)
            #===(загрузка файла c ПК на я.диск)==
            upload_url = response.json()['href']
            response = requests.put(upload_url, files={'file': open(f'{file_path}/{file}', 'rb')})

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь к загружаемому файлу: ')
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
