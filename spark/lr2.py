# spark/my_script.py
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

# Настройка конфигурации для подключения к Spark мастеру
conf = SparkConf().setAppName("My PySpark App").setMaster("spark://spark-master:7077")
sc = SparkContext(conf=conf)

# Инициализация SparkSession
spark = SparkSession.builder.config(conf=conf).getOrCreate()

# Пример: вычисление суммы чисел от 1 до 100
data = list(range(1, 101))
rdd = sc.parallelize(data)
result = rdd.sum()
print("Сумма чисел от 1 до 100:", result)

# Завершение работы SparkSession
spark.stop()
