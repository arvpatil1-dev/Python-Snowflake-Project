# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import snowflake.connector
import pandas as pd

print("Browsen")

conn = snowflake.connector.connect(
    user='arvind',
    password='Your Password',   # हे add करा
    account='en89759.ap-southeast-7.aws',
    warehouse='COMPUTE_WH',
    database='AUTODATA',
    schema='AUTO_DATA',
    role='ACCOUNTADMIN'               # हे add करा
)

print("Connection Success!")
cur = conn.cursor()
cur.execute("SELECT current_version()")
#print(cur.fetchone())

cur = conn.cursor()

# 1. Create Table
cur.execute("CREATE TABLE IF NOT EXISTS TEST_TABLE (ID NUMBER, NAME VARCHAR(50))")

# 2. Data insert
cur.execute("INSERT INTO TEST_TABLE VALUES (2, 'Pratik')")

# 3. Data read
cur.execute("SELECT * FROM TEST_TABLE")
print("Data in Table:", cur.fetchall())

cur.close()
conn.close()

cur.close()
conn.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
