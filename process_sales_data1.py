
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# ✅ Create Spark session
spark = SparkSession.builder.appName("SalesAnalytics").getOrCreate()

# ✅ Use correct relative path (from project root)
input_path = "sales_data1.csv"
output_path = "../Output/"

# ✅ Read the CSV file
df = spark.read.csv(input_path, header=True, inferSchema=True)

# ✅ Data transformation
df = df.withColumn("total_amount", col("quantity") * col("unit_price"))

df_grouped = df.groupBy("product").agg(
    sum("quantity").alias("total_quantity"),
    sum("total_amount").alias("total_sales")
)

df_grouped.show()

# ✅ Write output
df_grouped.coalesce(1).write.mode("overwrite").option("header", "true").csv(output_path)

print("✅ PySpark job completed successfully. Check Output/ folder.")
