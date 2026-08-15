import snowflake.connector
import pandas as pd

print("Starting CSV Load to Snowflake...")

# 1. Snowflake Connection
conn = snowflake.connector.connect(
    user='arvind',
    password='Your-passwword',
    account='en89759.ap-southeast-7.aws',
    warehouse='COMPUTE_WH',
    database='AUTODATA',
    schema='AUTO_DATA',
    role='ACCOUNTADMIN'
)
print("Connection Success!")

# 2. Read CSV File
csv_path = r'C:\Snowflake-Project\salesPune.csv'
df = pd.read_csv(csv_path)
print("\nCSV Data:")
print(df)

# 3. Create Table
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS SALESPUNE")
cur.execute("""
    CREATE TABLE SALESPUNE (
        ORDER_ID NUMBER,
        CUSTOMER_NAME VARCHAR(100),
        AMOUNT NUMBER(10,2),
        ORDER_DATE DATE
    )
""")
print("\nSALES Table Created!")

# 4. Insert Data into Snowflake
for index, row in df.iterrows():
    cur.execute("INSERT INTO SALESPUNE VALUES (%s, %s, %s, %s)",
        (row['ORDER_ID'], row['CUSTOMER_NAME'], row['AMOUNT'], row['ORDER_DATE'])
    )
conn.commit()
print("Data Inserted Successfully!")

# 5. Verify Data
cur.execute("SELECT * FROM SALESPUNE")
results = cur.fetchall()
print("\nFinal Data in Snowflake:")
for r in results:
    print(r)

cur.close()
conn.close()
print("\nProcess Complete!")