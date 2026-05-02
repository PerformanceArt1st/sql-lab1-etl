import psycopg2
from config import DB_CONFIG
from datetime import date

def fill_structured_table(start_date: date = date(2023, 1, 1), end_date: date = date(2023, 12, 31)):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # 1. Очищаем таблицу перед новой загрузкой, чтобы избежать ошибок UniqueViolation
    cur.execute("TRUNCATE TABLE s_psql_dds.t_sql_source_structured CASCADE;")

    # Запуск SQL-процедуры трансформации
    cur.execute("SELECT s_psql_dds.fn_etl_data_load(%s, %s)", (start_date, end_date))
    
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Transformed & loaded data for period: {start_date} to {end_date}")