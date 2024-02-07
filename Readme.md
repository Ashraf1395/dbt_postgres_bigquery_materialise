# Transforming Taxi Trip Data into Insights

Welcome to our Analytics Engineering project where we leverage the power of dbt to transform raw taxi trip data into actionable insights. In this project, we'll walk you through the process of loading, transforming, and visualizing taxi trip data, culminating in user-friendly dashboards for analysis.

-   ![Architecture](./images/GCP%20horizontal%20framework%20(1).png)

## Data & Tools

### Datasets:
- Green & Yellow Taxi Data (2019-2020)
- FHV Data (2019)
- Taxi Zone Lookup

### Storage:
- Cloud Storage (GCS) or Postgres (optional)

### Transformation:
- dbt Cloud or dbt Core (local setup)

### Visualization:
- Looker & Metabase

## Project Flow

### Data Loading:
Upload data to GCS or Postgres using orchestration tools (optional).
I have used Mage as the orchestration tool and the pipelines used
are in folder : [API_to_GCS_to_Bigquery](./API_to_GCS_to_Bigquery/).
For detailed implementation of mage you can check my complete etl prjoect on [mage](https://github.com/Ashraf1395/Mage-GCP-Postgres-pipelline).

### Transformation:

1. **Staging Models**: Create views in dbt for initial data cleaning and preparation.
    
    <img src="./images/staging_models_lineage.png" alt="staging_models_lineage">

2. **Core Models**: Build dimension and fact tables in dbt to represent key business metrics.
    
    <img src="./images/core_models_lineage.png" alt="core_models_lineage">

### Testing & Documentation:
Ensure data quality and clarity with dbt tests and model documentation.

```bash

    dbt test
    dbt docs generate

```


### Deployment:
Schedule model runs in production environments for continuous updates.

### Visualization:
Build dashboards in Looker & Metabase to explore and analyze the transformed data.

## Key Models & Features

### Dimension table:
- **dimension_zones**: Built from Taxi Zone Lookup data.

    ```bash

    dbt seed --full-refresh
    
    ```
    To refresh the dimension_zones.

    <img src="./images/dimension_zones_lineage.png" alt="dimension_zones_lineage" width="50%">

### Fact tables:
- **fact_trips**: Joins yellow & green taxi data with dimension_zones for comprehensive trip analysis.
    
    ```bash

    dbt run --select fact_trips
    
    ```
    
    <img src="./images/fact_trips_lineage.png" alt="fact_trips_lineage" width="50%">

- **fact_fhv_trips**: Analyzes FHV trip data with dimension_zones.

    ```bash
    dbt run --select fact_fhv_trips
    
    ```

   <img src="./images/fact_fhv_trips_lineage.png" alt="fact_fhv_trips_lineage" width="50%">

- **dm_monthly_zone_revenue**: Aggregates monthly revenue by zone from fact_trips.
   
   ```bash
    dbt run --select dm_monthly_zone_revenue
    
    ```

   <img src="./images/monlty_revenue_zone_lineage.png" alt="monlty_revenue_zone_lineage" width="50%">

### Other Features:
- **Macros & Packages**: Reusable code snippets and dependencies for efficient development.
- **Testing**: dbt tests ensure data quality and model functionality.
- **Documentation**: Clear documentation for each model aids understanding and maintenance.
- **Deployment**: Production environment with scheduled runs for automatic data updates.

## Dashboards

Looker & Metabase dashboards will be built to answer key questions:
- Total Taxi rides
- Total Fare Amount
- Top Locations
- Heatmap for top pickup times
- Left passengers
- All filtered by service type

## Next Steps

1. Implement Looker & Metabase dashboards based on the mentioned questions.
2. Customize and refine dashboards for specific user needs.
3. Explore additional metrics and visualizations for deeper insights.

## Conclusion

This project demonstrates how data transformation and visualization can unlock valuable insights from raw data. By leveraging dbt and other tools, we can empower data-driven decision making and improve business performance.

For detailed instructions on running models and other commands, refer to the following sections:

- **Model Execution**:
  - Run individual models: `dbt run --select <model_name>`
  - Run all models at once: `dbt run`
- **Dimension Zones Model**:
  - Run with seed data: `dbt seed`
  - Update with full refresh: `dbt seed --full-refresh`
- **Dependencies Installation**:
  - Install dependencies: `dbt deps`
- **Testing**:
  - Run tests: `dbt test`
- **Build**:
  - Build all: `dbt build`
  - Build with select model: `dbt build --select +fact_trips`
- **Documentation Generation**:
  - Generate documentation: `dbt docs generate`

For deployment and scheduling, refer to your dbt Cloud environment or set up production environments locally.

Finally, utilize the transformed tables in BigQuery to create insightful dashboards using Looker and Metabase.

Enjoy exploring your data and discovering new insights!
