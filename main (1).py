---------
# 1️⃣ Introduction
# ---------------------------------------------------------------
# In this lecture, we learned:
# - What is JSON?
# - What is SQL?
# - How to read JSON data in Python
# - How to connect MySQL database with Python
# - How to convert SQL data into Pandas DataFrame
# - How APIs return data (mostly in JSON format)

# ---------------------------------------------------------------
# 2️⃣ What is JSON?
# ---------------------------------------------------------------
# JSON = JavaScript Object Notation
# It is a Universal Data Format.
# Almost all programming languages understand JSON.

# Why JSON is popular?
# - Lightweight
# - Easy to read
# - Used in APIs
# - Language independent
# - Data exchange format between server & client

# Example JSON format:
# {
#   "id": 1,
#   "name": "Krishna",
#   "course": "Machine Learning"
# }

# JSON is mostly used when:
# - Calling APIs
# - Web development
# - Data transfer between applications


# ---------------------------------------------------------------
# 3️⃣ Reading JSON in Python using Pandas
# ---------------------------------------------------------------

# Import pandas
import pandas as pd

# Reading JSON file from local machine
# df = pd.read_json("file_name.json")

# Example:
# df = pd.read_json("recipes.json")
# print(df.head())

# JSON file can also be loaded from URL
# df = pd.read_json("https://example.com/data.json")

# Important Parameters in read_json():
# - encoding
# - lines=True
# - nrows
# - chunksize (for large files)

# Output:
# Data gets converted into a DataFrame automatically.


# ---------------------------------------------------------------
# 4️⃣ What is SQL?
# ---------------------------------------------------------------
# SQL = Structured Query Language
# Used to communicate with databases.
# Used for:
# - Selecting data
# - Filtering data
# - Inserting data
# - Updating data
# - Deleting data

# SQL works directly with databases like:
# - MySQL
# - PostgreSQL
# - SQLite
# - Oracle


# ---------------------------------------------------------------
# 5️⃣ Installing MySQL Connector (Bridge between Python & MySQL)
# ---------------------------------------------------------------

# To connect Python with MySQL:
# pip install mysql-connector-python

# Import connector
import mysql.connector

# Create connection
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="world"
# )

# If connection successful:
# print("Connected Successfully")


# ---------------------------------------------------------------
# 6️⃣ Reading SQL Table into Pandas DataFrame
# ---------------------------------------------------------------

# SQL Query
# query = "SELECT * FROM city"

# Load SQL data into DataFrame
# df = pd.read_sql(query, connection)
# print(df.head())

# Example with filter:
# query = "SELECT * FROM city WHERE CountryCode='IND'"
# df = pd.read_sql(query, connection)

# Example:
# query = "SELECT * FROM country WHERE LifeExpectancy > 60"
# df = pd.read_sql(query, connection)


# ---------------------------------------------------------------
# 7️⃣ Database Setup (Using XAMPP)
# ---------------------------------------------------------------
# Steps:
# 1. Install XAMPP
# 2. Start Apache & MySQL
# 3. Open browser → localhost/phpmyadmin
# 4. Create new database (example: world)
# 5. Import SQL file
# 6. Tables get created (city, country, countrylanguage)


# ---------------------------------------------------------------
# 8️⃣ Important SQL Concepts Used
# ---------------------------------------------------------------
# SELECT * FROM table_name
# WHERE condition
# Greater than (>)
# Filtering using country code
# Retrieving specific columns


# ---------------------------------------------------------------
# 9️⃣ JSON vs SQL
# ---------------------------------------------------------------
# JSON:
# - Used for APIs
# - Data exchange format
# - No strict schema
# - Flexible

# SQL:
# - Structured database
# - Tables & rows
# - Requires queries
# - Used in backend systems


# ---------------------------------------------------------------
# 🔟 API Concept
# ---------------------------------------------------------------
# When you send request to API:
# - Server returns response
# - Response mostly in JSON format

# Example:
# import requests
# response = requests.get("https://api.example.com/data")
# data = response.json()


# ---------------------------------------------------------------
# 1️⃣1️⃣ Key Takeaways
# ---------------------------------------------------------------
# ✔ JSON is universal data format
# ✔ SQL is used for database management
# ✔ Pandas can read both JSON & SQL
# ✔ MySQL connector acts as bridge
# ✔ APIs mostly return JSON


# ===============================================================
# End of Notes
# ===============================================================