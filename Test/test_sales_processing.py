import pytest
from pyspark.sql import SparkSession
from Resource.Notebook.process_sales_data import process_sales_data  # You may need to modularize this

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").appName("TestSession").getOrCreate()

def test_sales_aggregation(spark):
    data = [
        ("2024-01-01", "A", 100),
        ("2024-01-01", "B", 200),
        ("2024-01-02", "A", 150),
        ("2024-01-02", "C", 300)
    ]
    columns = ["Date", "Product", "Sales"]

    df = spark.createDataFrame(data, columns)
    
    result_df = process_sales_data(df)  # You need to refactor your script to have this as a function

    result = {row["Product"]: row["Total_Sales"] for row in result_df.collect()}
    assert result["A"] == 250
    assert result["B"] == 200
    assert result["C"] == 300
