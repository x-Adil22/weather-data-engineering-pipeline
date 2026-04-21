# Weather Data Engineering Pipeline

## Overview

This project demonstrates an end-to-end data engineering pipeline that extracts real-time weather data from an API, processes it, and loads it into a PostgreSQL database using Apache Airflow for orchestration.

---

## Architecture

API → Extract → Transform → Load → PostgreSQL → Airflow Scheduling

---

## Tech Stack

* Python (Pandas, Requests)
* Apache Airflow
* PostgreSQL
* Docker

---

## Features

* Automated ETL pipeline using Airflow DAGs
* Incremental data loading (no duplicates)
* Data validation and cleaning
* Containerized environment using Docker
* Modular code structure (extract, transform, load)

---

## 📸 Screenshots

### Airflow DAG Execution

![DAG] (<Screenshot 2026-04-21 at 7.19.43 PM.png>)

### Successful Pipeline Logs

![Logs] (<Screenshot 2026-04-21 at 7.20.40 PM.png>)

### Data Stored in PostgreSQL

![DB] (<Screenshot 2026-04-21 at 7.24.01 PM.png>)

---

##  How to Run

### 1. Clone the repository

git clone https://github.com/-Adil22/data-engineering-pipeline.git

### 2. Navigate to project

cd data-engineering-pipeline

### 3. Start Docker containers

docker-compose up

### 4. Open Airflow UI

http://localhost:8080
Username: admin
Password: admin

### 5. Trigger DAG

Run the "weather_pipeline" DAG from the Airflow UI

---

## Output

* Clean structured weather data stored in PostgreSQL
* Automated daily pipeline execution

---

## Learnings

* Built a production-style ETL pipeline
* Understood Airflow orchestration and DAG design
* Learned Docker-based environment setup
* Implemented real-world data engineering practices

---

## Future Improvements

* Add logging and monitoring
* Implement retry and alerting system
* Extend to streaming pipeline using Kafka
* Store data in cloud warehouse (BigQuery/Redshift)

---

## Author

Adil
