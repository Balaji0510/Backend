from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# Create a Spark session
spark = SparkSession.builder.appName("SalesProcessing").getOrCreate()

# Read input CSV
df = spark.read.csv("Data/sales_data.csv", header=True, inferSchema=True)

# Group by Product and sum Sales
result = df.groupBy("Product").agg(sum("Sales").alias("Total_Sales"))

# Write output
result.coalesce(1).write.csv("Output/transformed_sales.csv", header=True, mode="overwrite")

spark.stop()
