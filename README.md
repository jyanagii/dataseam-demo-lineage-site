# dataseam-demo-lineage-site

Aggregate lineage site and PR Impact Check repository for the DataSeam multi-repo demo.

## Repositories in this demo
- `jyanagii/dataseam-demo-dbt-core`: Upstream dbt models + dbt Semantic Layer
- `jyanagii/dataseam-demo-dbt-mart`: Downstream dbt models reading `core.*` as sources
- `jyanagii/dataseam-demo-bi-airflow`: Airflow DAGs, LookML, Metabase export, Tableau workbook
- `jyanagii/dataseam-demo-lineage-site`: This repository (`dataseam.yml`, site build, PR impact check)

## Additional warehouse platform demos
- `platforms/snowflake/`: Snowflake dbt project, `snowflake_operators` Airflow DAG, and Snowflake access history export
- `platforms/databricks/`: Databricks dbt project, `databricks_operators` Airflow DAG, and Databricks table lineage export
