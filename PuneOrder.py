import pandas as pd
import snowflake.connector

# 1. Snowflake Connection
conn = snowflake.connector.connect(
    user='arvind',
    password='Your Password',
    account='en89759.ap-southeast-7.aws',
    warehouse='COMPUTE_WH',
    database='AUTODATA',
    schema='AUTO_DATA',
    role='ACCOUNTADMIN'
)
cur = conn.cursor()

# 2. Read CSV
csv_path = r'C:\Python-Snowflake-Project\PuneOrder.csv'
df = pd.read_csv(csv_path)
df['order_date']=pd.to_datetime(df['order_date'],format='%d-%m-%Y')
print(df)
print("CSV Loaded Successfully!")

# 3. Create Table
cur.execute("DROP TABLE IF EXISTS PUNEORDER")
cur.execute("""
CREATE TABLE IF NOT EXISTS PUNEORDER(
    order_id INT,
    customer_name VARCHAR(100),
    product VARCHAR(100),
    quantity INT,
    price FLOAT,
    order_date DATE,
    region VARCHAR(50)
)
""")
print("\nPUNEORDER Table Created!")
# 4. Insert Data into Snowflake
for index, row in df.iterrows():
    cur.execute(
        "INSERT INTO PUNEORDER(order_id, customer_name, product, quantity, price, order_date, region) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (row['order_id'], row['customer_name'], row['product'], row['quantity'], row['price'], row['order_date'], row['region'])
    )

conn.commit()
print("Data Inserted Successfully!")

# 5. Verify Data
cur.execute("SELECT * FROM PUNEORDER")
results = cur.fetchall()
print("\nFinal Data in Snowflake:")
for r in results:
    print(r)

cur.close()
conn.close()