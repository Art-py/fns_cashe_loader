# FNS cashe loader

short project description

## Оглавление
1) [Установка](README.md#установка)
2) [Запуск Celery на Windows](README.md#запуск-celery-на-windows)

## Установка
[Ссылка на документациюъ](./docs/ru/index.md#установка)

## Запуск Celery на Windows

1. Создайте контейнер с Redis в Docker:
    ```bash
    docker run -d -p 6379:6379 --name myredis redis
    ```

2. Перейдите в папку `src` в консоли.

3. Запустите Celery с помощью команды:
    ```bash
    celery -A django_project.celery worker --loglevel=info -P eventlet
    ```

4. Откройте новую консоль, не закрывая старую, и перейдите в папку `src`.

5. Запустите команду для работы задач, которые вызываются в определённое время:
    ```bash
    celery -A django_project.celery beat --loglevel=debug
    ```
