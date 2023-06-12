# Установка и запуск
Для работы необходимо наличие установленных и запущенных программ docker и docker compose.
В файле .env указываются параметры конфигурации приложения.
Для запуска в терминале из корневой папки проекта вызываем команду:
```shell
docker compose up
```

# Примеры
Пример получения 1 вопроса:
```shell
curl --location --request POST 'http://127.0.0.1:8000/quiz?questions_num=1'
```
Пример вывода:
```json
{
  "question_id": 21,
  "question": "On June 18, 1940 Churchill said, \"The battle for France is over\" & this \"is about to begin\"",
  "answer": "the Battle of Britain",
  "date": "2023-05-21T17:35:43"
}
```

# База данных
Для подключения к базе данных необходимо использовать параметры .env из файла. 
Для подключения через клиент psql открываем bash в контейнере:
```shell
docker exec -it <container_id> bash
```
пример:
```shell
docker exec -it e583ee429f81169cd4fd92a5776243ac650ba7cd1ab734db387baf0860a28b3f bash
```
Затем подключаемся к postgres:
```shell
psql --no-readline -U <POSTGRES_USER> -h <HOST> -p <POSTGRES_PORT> -d <POSTGRES_DB_NAME> -W
```
пример:
```shell
psql --no-readline -U postgres -h localhost -p 5432 -d postgres -W
```
Вводим пароль <POSTGRES_PASSWORD> например 'postgres'
