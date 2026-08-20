from pyspark import pipelines as dp

dp.create_streaming_table("sdp_pipelines.`01_silver`.customers_SCD1")

dp.create_auto_cdc_flow(
    target="sdp_pipelines.`01_silver`.customers_SCD1",
    source="sdp_pipelines.`00_bronze`.customers_bronze_raw",
    keys=["customer_id"],
    sequence_by="update_date",
    apply_as_deletes="operation = 'Delete'",
    except_column_list=["operation"],
    stored_as_scd_type=1
)

