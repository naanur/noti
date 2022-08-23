# Сервис рассылки уведомлений

Сервис на django rest framework с celery и flower

1. Скопировать репозиторий с Github:
````
git clone git@github.com:naanur/noti.git
````
2. Перейти в директорию проекта
````
cd noti
````
3. Создать виртуальное окружение:
````
python -m venv venv && venv\Scripts\activate
````
4. В файле .env: ```TOKEN = '<your token>'```

5. Установка зависимостей:
```
pip install -r requirements.txt
```
6. Создать, применить миграции в базу данных и запустить тесты:

```
py manage.py makemigrations
py manage.py migrate
py manage.py test main
```

7. Запустить сервер

```
py manage.py runserver
```

9. Запустить celery

```
celery -A notification_service worker -l info
```

10. Запустить flower

```
celery -A notification_service flower --port=5555
```

***

## Установка проекта с помощью docker-compose

``` 
sudo docker-compose up -d
 ```

***
```http://0.0.0.0:8000/api/``` - api проекта

```http://0.0.0.0:8000/api/clients/``` - клиенты

```http://0.0.0.0:8000/api/mailsends/``` - рассылки

```http://0.0.0.0:8000/api/mailsends/fullinfo/``` - общая статистика по всем рассылкам

```http://0.0.0.0:8000/api/mailsends/<pk>/info/``` - детальная статистика по конкретной рассылке

```http://0.0.0.0:8000/api/messages/``` - сообщения

```http://0.0.0.0:8000/docs/``` - docs проекта

```http://0.0.0.0:5555``` - celery flower

***
