from datetime import datetime
from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.snowflake.transfers.copy_into_snowflake import (
    CopyFromExternalStageToSnowflakeOperator,
)

with DAG(dag_id="snowflake_daily", start_date=datetime(2026, 1, 1), schedule="@daily") as dag:
    load_raw = CopyFromExternalStageToSnowflakeOperator(
        task_id="copy_raw_orders",
        database="ACME_PROD",
        schema="RAW",
        table="ORDERS",
        stage="S3_STAGE",
        file_format="PARQUET_FMT",
    )
    publish_summary = SnowflakeOperator(
        task_id="publish_executive_summary",
        database="ACME_PROD",
        schema="MART",
        sql="INSERT INTO EXEC_SUMMARY SELECT ORDER_DATE, TOTAL_AMOUNT FROM ANALYTICS.DAILY_SALES",
    )
    load_raw >> publish_summary
