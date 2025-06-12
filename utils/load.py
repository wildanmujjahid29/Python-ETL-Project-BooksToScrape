import pandas as pd
import os
import mysql.connector

def save_to_csv(df, filename='data/books_bersih.csv'):
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to CSV: {filename}")


def save_to_mysql(df, table_name='buku_data', db_config=None):
    if db_config is None:
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'load_buku'
        }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create table if not exists (otomatis dari kolom df)
        columns = ', '.join([f"{col} TEXT" for col in df.columns])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")

        # Insert data
        for _, row in df.iterrows():
            placeholders = ', '.join(['%s'] * len(row))
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(insert_query, tuple(row))

        conn.commit()
        print(f"✅ Data saved to MySQL table `{table_name}` in database `load_buku`.")
    
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

