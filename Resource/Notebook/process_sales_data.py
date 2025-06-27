from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

def process_sales_data(df):
    return df.groupBy("Product").agg(sum("Sales").alias("Total_Sales"))

if __name__ == "__main__":
    spark = SparkSession.builder.appName("SalesProcessing").getOrCreate()
    input_df = spark.read.csv("Data/sales_data.csv", header=True, inferSchema=True)
    output_df = process_sales_data(input_df)
    output_df.coalesce(1).write.csv("Output/transformed_sales.csv", header=True, mode="overwrite")
    spark.stop()
