import sqlite3
import pandas as pd

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

df = pd.read_csv("Job opportunities.csv")

print("Перші 5 рядків CSV:")
print(df.head())

print("\nНазви колонок:")
print(df.columns)

df.to_sql("jobs", conn, if_exists="replace", index=False)

print("\nДані завантажено у таблицю jobs")

print("\nПерші 10 вакансій:")

query = """
SELECT *
FROM jobs
LIMIT 10;
"""

result = pd.read_sql(query, conn)
print(result)

print("\nВакансії з навичкою SQL:")

query = """
SELECT *
FROM jobs
WHERE "Required Skills" LIKE '%SQL%';
"""

result = pd.read_sql(query, conn)
print(result)

print("\nУнікальні Location та Company:")

query = """
SELECT DISTINCT Location, Company
FROM jobs;
"""

result = pd.read_sql(query, conn)
print(result)

print("\nСередня зарплата за Experience Level:")

query = """
SELECT "Experience Level",
AVG(CAST(substr("Salary Range",1,5) AS INTEGER)) as avg_salary
FROM jobs
GROUP BY "Experience Level";
"""

result = pd.read_sql(query, conn)
print(result)

print("\nКількість вакансій за Experience Level:")

query = """
SELECT "Experience Level",
COUNT(*) as total_jobs
FROM jobs
GROUP BY "Experience Level";
"""

result = pd.read_sql(query, conn)
print(result)

print("\nМінімальна та максимальна зарплата:")

query = """
SELECT
MIN(CAST(substr("Salary Range",1,5) AS INTEGER)) as min_salary,
MAX(CAST(substr("Salary Range",1,5) AS INTEGER)) as max_salary
FROM jobs;
"""

result = pd.read_sql(query, conn)
print(result)

print("\nКількість вакансій у кожній індустрії (зарплата > 50000):")

query = """
SELECT Industry,
COUNT(*) as jobs_count
FROM jobs
WHERE CAST(substr("Salary Range",1,5) AS INTEGER) > 50000
GROUP BY Industry;
"""

result = pd.read_sql(query, conn)
print(result)

print("\nСередня зарплата для кожної індустрії:")

query = """
SELECT Industry,
AVG(CAST(substr("Salary Range",1,5) AS INTEGER)) as avg_salary
FROM jobs
GROUP BY Industry;
"""

result = pd.read_sql(query, conn)
print(result)

print("\nКількість вакансій за Location та Experience Level:")

query = """
SELECT Location, "Experience Level",
COUNT(*) as total
FROM jobs
GROUP BY Location, "Experience Level";
"""

result = pd.read_sql(query, conn)
print(result)

print("\nКількість вакансій за Industry та Job Type:")

query = """
SELECT Industry, "Job Type",
COUNT(*) as total
FROM jobs
GROUP BY Industry, "Job Type";
"""

result = pd.read_sql(query, conn)
print(result)

print("\nСередня зарплата за Location і Experience Level:")

query = """
SELECT Location, "Experience Level",
AVG(CAST(substr("Salary Range",1,5) AS INTEGER)) as avg_salary
FROM jobs
GROUP BY Location, "Experience Level";
"""

result = pd.read_sql(query, conn)
print(result)

print("\n5 вакансій з найвищою зарплатою:")

query = """
SELECT *
FROM jobs
ORDER BY CAST(substr("Salary Range",1,5) AS INTEGER) DESC
LIMIT 5;
"""

result = pd.read_sql(query, conn)
print(result)

print("\nКомпанії з найбільшою кількістю вакансій у 2023:")

query = """
SELECT Company,
COUNT(*) as jobs_count
FROM jobs
WHERE "Posting Date" LIKE '2023%'
GROUP BY Company
ORDER BY jobs_count DESC;
"""

result = pd.read_sql(query, conn)
print(result)

conn.close()