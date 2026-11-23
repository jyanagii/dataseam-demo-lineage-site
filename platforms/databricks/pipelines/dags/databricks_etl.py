from datetime import datetime
from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from airflow.providers.databricks.operators.databricks_sql import (
    DatabricksCopyIntoOperator,
    DatabricksSqlOperator,
)

with DAG(dag_id="databricks_daily", start_date=datetime(2026, 1, 1), schedule="@daily") as dag:
    copy_raw = DatabricksCopyIntoOperator(
        task_id="copy_raw_orders",
        catalog="acme_prod",
        schema="raw",
        table_name="orders",
        file_location="s3://acme-landing/orders/",
        file_format="PARQUET",
    )
    agg_sql = DatabricksSqlOperator(
        task_id="refresh_summary",
        catalog="acme_prod",
        schema="mart",
        sql="INSERT INTO exec_summary SELECT order_date, total_amount FROM analytics.daily_sales",
    )
    run_job = DatabricksSubmitRunOperator(
        task_id="submit_kpi_job",
        json={
            "tasks": [
                {
                    "task_key": "build_kpi",
                    "sql_task": {
                        "query": "INSERT INTO acme_prod.mart.kpi_rollup SELECT * FROM acme_prod.mart.exec_summary"
                    },
                }
            ]
        },
    )
    copy_raw >> agg_sql >> run_job
