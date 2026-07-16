import argparse

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Write a dummy DataFrame to a Delta table.")
parser.add_argument("--table-name", default="dummy_delta_table", help="Delta table name.")
parser.add_argument(
    "--output-path",
    default=None,
    help="Delta output path. Defaults to Tables/<table-name> in the default lakehouse.",
)
parser.add_argument(
    "--mode",
    default="overwrite",
    choices=["overwrite", "append", "ignore", "error"],
    help="Write mode.",
)
args = parser.parse_args()

output_path = args.output_path or f"Tables/{args.table_name}"

# Create Spark session
spark = SparkSession.builder.appName("sjd-demo").getOrCreate()

# Define schema for the dummy DataFrame
schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), True),
    StructField("value", DoubleType(), True),
])

# Create dummy data
data = [
    (1, "alpha", 10.5),
    (2, "beta", 20.0),
    (3, "gamma", 30.75),
    (4, "delta", 40.25),
    (5, "epsilon", 50.0),
]

df = spark.createDataFrame(data, schema)

df.show()

# Write the DataFrame to a Delta table in the default lakehouse
df.write.format("delta").mode(args.mode).save(output_path)

print(f"Successfully wrote {df.count()} rows to Delta at {output_path}")

spark.stop()
