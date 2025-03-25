# Описание проекта

Данный репозиторий содержит лабораторные работы по развертыванию Apache Airflow с использованием Docker Compose, а также интеграцию Airflow с Apache Spark.

## Проект демонстрирует

- Развёртывание Airflow с помощью Docker Compose и кастомного Docker-образа.

- Создание и выполнение DAG'ов:
  - **ЛР1**: Простой DAG (`my_complex_dag`), состоящий из последовательных шагов: запуск, вычисление суммы чисел от 1 до 100 и завершение.
  - **ЛР2**: DAG (`spark_dag`) для запуска Spark job через `SparkSubmitOperator`, где Spark job (`lr2.py`) выполняет вычисление суммы чисел от 1 до 100 с использованием PySpark.

- Интеграцию с Apache Spark посредством:
  - Модифицированного `Dockerfile` (копирование директории `spark`, установка пакетов `procps` и `default-jre`, установка библиотеки `apache-airflow-providers-apache-spark`).
  - Дополнительных сервисов в `docker-compose` (`spark-master` и `spark-worker`).

## Структура репозитория

### `Dockerfile`

Кастомный образ на основе `apache/airflow:2.7.1`. В нём:

- Устанавливаются системные пакеты (`procps`, `default-jre`).
- Копируются файлы из директорий `dags` и `spark`.
- Устанавливается провайдер для работы с Apache Spark.

### `docker-compose.yml`

Конфигурация для развертывания следующих сервисов:

- `airflow-init`, `scheduler`, `webserver`: Основные компоненты Airflow (используется `LocalExecutor`).
- `postgres`: СУБД PostgreSQL.
- `spark-master`, `spark-worker`: Сервисы для формирования Spark кластера (Spark WebUI доступен по `http://localhost:4040`).

### `dags/my_complex_dag.py` (ЛР1)

Пример DAG для ЛР1:

- `start`: Bash-задача для вывода сообщения о запуске.
- `compute_sum`: Python-задача, вычисляющая сумму чисел от 1 до 100.
- `finish`: Bash-задача, выводящая сообщение о завершении работы DAG.

### `dags/spark_dag.py`

DAG для ЛР2, который с помощью оператора `SparkSubmitOperator` запускает Spark job.

### `spark/lr2.py`

Скрипт для Spark job, использующий PySpark (`SparkSession`) для вычисления суммы чисел от 1 до 100.

## Лабораторные отчёты

- `lab1.pdf`: Отчёт по ЛР1 (Airflow + Docker Compose).
- `lab2.pdf`: Отчёт по ЛР2 (Интеграция Airflow со Spark).

## Развертывание проекта

Клонируйте репозиторий:

```bash
git clone <URL репозитория>
cd <папка репозитория>
```

Запустите Docker Compose:

```bash
docker-compose up -d
```

После успешного запуска должны быть запущены следующие контейнеры:

- Airflow webserver (доступен по `http://localhost:8080`)
- Airflow scheduler
- PostgreSQL
- Spark master (Spark WebUI — `http://localhost:4040`)
- Spark worker

Проверьте состояние контейнеров:

```bash
docker ps
```

Если контейнеры находятся в состоянии `health: starting`, подождите, пока они перейдут в состояние `healthy`.

## Использование DAG

### DAG для ЛР1: `my_complex_dag`

**Описание:**
Последовательность задач:

- `start`: Вывод сообщения о запуске.
- `compute_sum`: Вычисление суммы чисел от 1 до 100.
- `finish`: Вывод сообщения о завершении.

**Запуск:**
DAG можно запустить вручную через веб-интерфейс Airflow или дождаться автоматического выполнения согласно расписанию (`@daily`).

#### DAG для ЛР2: `spark_dag`

**Описание:**
DAG, использующий оператор `SparkSubmitOperator` для выполнения Spark job.
Spark job (скрипт `lr2.py`) использует PySpark (`SparkSession`) для вычисления суммы чисел от 1 до 100.

**Настройка подключения к Spark:**
В административной панели Airflow необходимо создать новое подключение:

- **Conn Id**: `spark_local` (или иное, соответствующее значению в DAG)
- **Conn Type**: `Spark`
- **Host**: `spark://spark-master`
- **Port**: `7077`

**Запуск:**
Запустите DAG через веб-интерфейс Airflow. При корректной настройке, в Spark WebUI (по `http://localhost:4040`) будут отображаться запущенные задачи и информация о воркере.
