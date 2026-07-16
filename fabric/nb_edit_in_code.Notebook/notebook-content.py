# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a1391ba1-4e9d-4aa6-914f-fb0c8c4d3517",
# META       "default_lakehouse_name": "lh_option1_dev",
# META       "default_lakehouse_workspace_id": "40b5245a-c93d-4182-a1d0-00688539d305",
# META       "known_lakehouses": [
# META         {
# META           "id": "a1391ba1-4e9d-4aa6-914f-fb0c8c4d3517"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import Row
from pyspark.sql.functions import current_timestamp

# Create a simple demo DataFrame
rows = [
    Row(id=1, name="Alice", value=10.5),
    Row(id=2, name="Bob", value=20.0),
    Row(id=3, name="Charlie", value=30.75)
]

df_demo = spark.createDataFrame(rows)

# Add load_timestamp column
df_demo = df_demo.withColumn("load_timestamp", current_timestamp())

# Write to default Lakehouse as a table
# For a schema-enabled Lakehouse, use three-part name like "lh_option1_dev.dbo.demo_table"
# Here we use a simple table name; Fabric will place it under the default Lakehouse

target_table_name = "demo_table"

(df_demo
    .write
    .mode("overwrite")
    .format("delta")
    .saveAsTable(target_table_name)
)

print(f"Wrote {df_demo.count()} rows to table '{target_table_name}' in the default Lakehouse.")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
