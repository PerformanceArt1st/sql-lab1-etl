import psycopg2
from config import DB_CONFIG
from datetime import date

def fill_dm_table(start_dt: date = date(2023, 1, 1), end_dt: date = date(2023, 12, 31)):
    """Запускает SQL-функцию формирования витрины в PostgreSQL"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT s_psql_dds.fn_dm_data_load(%s, %s)", (start_dt, end_dt))
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ DM table filled for period: {start_dt} to {end_dt}")