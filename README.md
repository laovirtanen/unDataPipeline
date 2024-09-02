Data Warehouse Project for Health Indicators Analysis
Overview
This portfolio / learning project demonstrates the development and management of a data warehouse for analyzing health indicators using Python and Amazon Redshift. The project showcases the full ETL (Extract, Transform, Load) process, including data cleaning, transformation, and loading into a data warehouse. It also includes designing a robust data model and schema to support efficient querying and analysis.

Project Objectives
Build a data warehouse on Amazon Redshift to store health indicator data.
Implement ETL processes to clean, transform, and load data from CSV files.
Design a star schema with dimension and fact tables to facilitate efficient data analysis.
Provide SQL queries for analyzing data and gaining insights.
Technologies Used
Python: For scripting data transformations and handling data operations.
Pandas: For data manipulation and cleaning.
Amazon Redshift: A fully managed data warehouse service used for storing and querying data.
Boto3: AWS SDK for Python, used to interact with Redshift.
SQL: For querying the data warehouse and performing data analysis.
Data Sources
S3 Bucket for storing the data

![Screenshot 2024-09-02 175745](https://github.com/user-attachments/assets/7fb3b78b-b8f2-41bf-b855-f816f645263c)


Data Model and Schema
The data warehouse is designed using a star schema to optimize for query performance and ease of analysis. The schema includes several dimension tables (Dim_Country, Dim_Series, Dim_Time) and a central fact table (Fact_HealthIndicators).


Tables
Dim_Country: Contains unique identifiers and names for countries or regions.
Dim_Series: Contains unique identifiers and descriptions for different health indicator series.
Dim_Time: Contains unique identifiers for different years.
Fact_HealthIndicators: Contains the health indicator data, linked to the dimension tables by foreign keys.

![Screenshot 2024-08-30 122726](https://github.com/user-attachments/assets/06319bd6-e4eb-4cd8-83e7-09b1f8cdfa4f)

Also a few more tables were created for learning purposes. These can be found from data_folder.


Data Loading Process
For this project, we decided to use the Redshift Serverless Query Editor V2 to load data directly from Amazon S3 into the data warehouse. This decision was made to keep the process simple and focused on demonstrating the basics of data warehousing.

Rationale for Using Query Editor V2
The Redshift Query Editor V2 provides a straightforward, manual approach to loading data into Amazon Redshift.
![Screenshot 2024-09-02 182701](https://github.com/user-attachments/assets/8d30a891-568f-4569-a58e-1912446f11cc)

