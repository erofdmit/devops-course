# dags/my_complex_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def compute_sum(**kwargs):
    total = sum(range(1, 101))
    print(f"Сумма чисел от 1 до 100: {total}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'my_complex_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Пример DAG, состоящий из нескольких шагов: запуск, вычисление и завершение'
) as dag:
    
    start_task = BashOperator(
        task_id='start',
        bash_command='echo "Запуск DAG"'
    )

    compute_task = PythonOperator(
        task_id='compute_sum',
        python_callable=compute_sum,
        provide_context=True
    )

    finish_task = BashOperator(
        task_id='finish',
        bash_command='echo "DAG завершён успешно"'
    )

    start_task >> compute_task >> finish_task
