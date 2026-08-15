# This is a sample Python script.
from unittest import result

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import snowflake.connector
import pandas as pd

print("Browsen")

conn = snowflake.connector.connect(
    user='arvindpune',
    password='Patilarvind@123',
    account='en89759.ap-southeast-7.aws',
    warehouse='COMPUTE_WH',
    database='AUTODATA',
    schema='AUTO_DATA',
    role='ACCOUNTADMIN'
)

print("Connection Success!")
cur = conn.cursor()
cur.execute("SELECT current_version()")
#print(cur.fetchone())

cur = conn.cursor()
# 1. Data read
cur.execute("SELECT * FROM TEST_TABLE")
results=cur.fetchall()
for r in results:
    print(r)

#print("Data in Table:", cur.fetchall())

cur.close()
conn.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
