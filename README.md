# Лабораторная работа 1: Airflow + Docker Compose

## Описание проекта

Этот репозиторий содержит конфигурацию для развертывания Apache Airflow с использованием Docker Compose. Проект включает:

- **Dockerfile**: Определяет кастомный Docker-образ на основе `apache/airflow:2.7.1`. В образ копируются DAG файлы.
- **docker-compose.yml**: Конфигурация для развертывания сервисов:
  - `airflow-init`: Инициализация базы данных Airflow.
  - `scheduler`: Планировщик задач Airflow.
  - `webserver`: Веб-сервер Airflow, доступный по [http://localhost:8080](http://localhost:8080).
  - `postgres`: Сервис базы данных PostgreSQL.
  
  **Примечания:**
  - Используется `LocalExecutor` вместо `CeleryExecutor`.
  - Отключены сервисы: redis, airflow-worker, airflow-triggerer, airflow-cli, flower.
  - Переменная `AIRFLOW__CORE__LOAD_EXAMPLES` установлена в `false` для отключения примеров DAG.

- **dags/my_complex_dag.py**: Пример DAG, содержащий три задачи:
  - `start`: Задача запуска, выводящая сообщение.
  - `compute_sum`: Задача на Python, вычисляющая сумму чисел от 1 до 100.
  - `finish`: Финальная задача, выводящая сообщение о завершении.

## Развертывание

1. Клонируйте репозиторий:
``` git clone <URL репозитория> cd <папка репозитория> ```

2. Запустите Docker Compose:
``` docker-compose up -d ```

3. Проверьте состояние контейнеров:
``` docker ps ```

Должны быть активны два контейнера Airflow (webserver и scheduler) и один контейнер PostgreSQL.

Откройте браузер и перейдите по адресу:
[http://localhost:8080](http://localhost:8080)

## Использование DAG

В веб-интерфейсе Airflow найдите DAG с именем `my_complex_dag`. Вы можете запустить его вручную или дождаться автоматического выполнения по расписанию.

## Дополнительно

При необходимости внесите изменения в файлы конфигурации или DAG для расширения функциональности.
