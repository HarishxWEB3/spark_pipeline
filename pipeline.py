import os
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Pipeline").getOrCreate()

# Get the folder where this script is located
base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, "data.csv")

df = spark.read.csv(csv_path, header=True, inferSchema=True)
df.show()
