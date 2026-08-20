
from pyspark import pipelines as dp
from pyspark.sql import functions as sf

@dp.table(
    name = "sdp_pipelines.00_bronze.customers_bronze_raw"
)
def bronze_raw():
    return spark.readStream.format("cloudFiles") \
                .option("cloudFiles.format", "csv") \
                .option("cloudFiles.inferColumnTypes", "true") \
                .load('/Volumes/sdp_pipelines/00_bronze/scd_files') \
                .withColumn("source_file", sf.col("_metadata.file_path")) \
                .withColumn("ingestion_time", sf.current_timestamp())
                

