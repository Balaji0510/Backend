from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, sum

spark = SparkSession.builder \
    .appName("SalesAnalytics") \
    .getOrCreate()

# Read raw data
df = spark.read.csv("data/sales_data.csv", header=True, inferSchema=True)

# Transform: Add total_amount column
df_transformed = df.withColumn("total_amount", col("quantity") * col("unit_price"))

# Group by product
summary_df = df_transformed.groupBy("product").agg(
    sum("quantity").alias("total_quantity"),
    sum("total_amount").alias("total_sales")
)

# Save to CSV for Power BI
summary_df.coalesce(1).write.mode("overwrite").option("header", "true").csv("output/")