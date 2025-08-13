import os
from pyspark.sql import SparkSession

#Extract
spark = SparkSession.builder.appName("Pipeline").getOrCreate()

base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, "data.csv")
df = spark.read.csv(csv_path, header=True, inferSchema=True)

# Transform 
# Filter rows where age is between 20 and 30 (inclusive)
df_filtered = df.filter((df.age >= 20) & (df.age <= 30))

# Load 
df_filtered.show()

# Optionally save to CSV
output_path = os.path.join(base_path, "filtered_data.csv")
df_filtered.write.mode("overwrite").csv(output_path, header=True)
