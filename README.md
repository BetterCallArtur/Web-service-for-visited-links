# Web-сервис для учета посещенных ресурсов

## Требования
- Python 3
- Flask
- SQLAlchemy

## Установка и запуск
1. Установите зависимости: `pip install -r requirements.txt`
2. Запустите сервис: `python app.py`

## Тестирование 
Запустите тесты: `python test_app.py`

## Контейнеризация (по желанию)
Если вы хотите использовать Docker:

1. Соберите Docker образ: `docker build -t название-образа .`
2. Запустите контейнер: `docker run -p 5000:5000 название-образа`

Приложение будет доступно по адресу [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Эндпоинты

### Добавление посещенных ссылок
Описание: Этот эндпоинт принимает список посещенных ссылок от работника и фиксирует их в базе данных. Время посещения ссылок считается временем принятия запроса сервисом.

### Пример запроса: 
{
 "links": [
 "https://ya.ru/",
 "https://ya.ru/search/?text=мемы+с+котиками",
 "https://sber.ru",
 "https://stackoverflow.com/questions/65724760/how-it-is"
 ] }

### Пример ответа: 
 {
 "status": "ok"
}


## Пример запроса в Python: 
import requests

url_visited_links = "http://127.0.0.1:5000/visited_links"
data_visited_links = {
    "links": [
        "https://ya.ru/",
        "https://ya.ru/search/?text=мемы+с+котиками",
        "https://sber.ru",
        "https://stackoverflow.com/questions/65724760/how-it-is"
    ]
}

response_visited_links = requests.post(url_visited_links, json=data_visited_links)

if response_visited_links.status_code == 200:
    print("Ссылки успешно добавлены!")
else:
    print("Ошибка при добавлении ссылок:", response_visited_links.json()["status"])
    


### Получение списка уникальных посещенных доменов в заданном временном интервале
Описание: Этот эндпоинт предоставляет возможность получить список уникальных доменов, которые были посещены в указанном временном интервале.

URL: `GET /visited_domains?from=1545221231&to=1545217638


### Параметры запроса
- `from` (integer): С какого времени в формате Unix timestamp.
- `to` (integer): По какое время в формате Unix timestamp.

### Пример запроса через Bash:
curl -X GET "http://127.0.0.1:5000/visited_domains?from=1545221231&to=1545217638"

### Пример ответа: 
{
  "domains": [
    "ya.ru",
    "sber.ru",
    "stackoverflow.com"
  ],
  "status": "ok"
}

### Пример запроса в Python: 
import requests

url_visited_domains = "http://127.0.0.1:5000/visited_domains"
params_visited_domains = {
    "from": 1545221231,
    "to": 1545217638
}

response_visited_domains = requests.get(url_visited_domains, params=params_visited_domains)

if response_visited_domains.status_code == 200:
    unique_domains = response_visited_domains.json()["domains"]
    print("Уникальные домены:", unique_domains)
else:
    print("Ошибка при получении уникальных доменов:", response_visited_domains.json()["status"])

### Пример запроса через браузер: 
Откройте веб-браузер и введите следующий URL, заменив параметры from и to на необходимые значения:
http://127.0.0.1:5000/visited_domains?from=1545221231&to=1545217638

### Пример ответа:
{
  "domains": [
    "ya.ru",
    "sber.ru",
    "stackoverflow.com"
  ],
  "status": "ok"
}


### Примечание
- Сервис использует SQLite в качестве базы данных. Вы можете изменить строку подключения в файле `app.py` по своим требованиям.
- Файл базы данных (`visited_links.db`) будет создан автоматически при первом запуске.



