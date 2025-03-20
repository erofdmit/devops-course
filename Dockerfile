# Dockerfile
FROM apache/airflow:2.7.1

# Устанавливаем рабочую директорию по умолчанию для Airflow
WORKDIR /opt/airflow

# Копируем каталог с DAG'ами в директорию образа
COPY dags/ /opt/airflow/dags/
