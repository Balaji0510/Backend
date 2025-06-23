from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SalesDataProcessor").getOrCreate()

df = spark.read.csv("Data/sample_sales.csv", header=True, inferSchema=True)

df = df.withColumn("total", df["quantity"] * df["price"])

df.groupBy("product").sum("total")

# Save output
df.write.mode("overwrite").option("header", "true").csv("Output/transformed_sales.csv")

spark.stop()