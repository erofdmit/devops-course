# dags/spark_dag.py
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

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
    'spark_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='DAG для выполнения Spark job через SparkSubmitOperator'
) as dag:

    spark_job = SparkSubmitOperator(
        task_id='run_spark_job',
        application='/opt/airflow/spark/lr2.py',
        name='my_spark_job',
        conn_id='spark_local', 
        verbose=True,
        conf={'spark.master': 'spark://spark-master:7077'},
    )

    spark_job
