# 📊 Automated Environmental Data ETL Pipeline

## Overview
An end-to-end Python automation script that extracts live REST API data, secures it within a relational database, and transforms it into an interactive, executive-ready visual dashboard. 

This project bridges the gap between backend data engineering and clean visual composition, ensuring data is not just collected, but instantly comprehensible.

## ⚙️ The Architecture (ETL)
* **Extract:** Pulls 7-day rolling climate data via a live REST API using `requests`.
* **Load:** Secures the raw payload locally into a lightweight `sqlite3` relational database.
* **Transform:** Cleans, aggregates, and structures the data using `pandas`.
* **Visualize:** Renders a sleek, dark-mode interactive HTML dashboard using `plotly`, applying core design principles to negative space and color balance.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Database:** SQLite
* **Libraries:** Pandas, Plotly Express, Requests, Selenium
* **Version Control:** Git / GitHub

## 🚀 Business Value
This pipeline eliminates manual CSV downloading and spreadsheet formatting. By automating the data lifecycle, teams can make immediate decisions based on live, beautifully composed interactive charts rather than sifting through raw data tables.