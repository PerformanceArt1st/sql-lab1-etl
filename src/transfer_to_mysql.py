import psycopg2
import pymysql
from config import DB_CONFIG, MYSQL_CONFIG

def transfer_to_mysql():
    """Перекладывает данные из PG-витрины v_dm_task в MySQL"""
    # 1. Читаем из PostgreSQL
    pg_conn = psycopg2.connect(**DB_CONFIG)
    pg_cur = pg_conn.cursor()
    pg_cur.execute("""
        SELECT id, event_date, category_id, region_id, customer_age, income,
               transaction_amount, rating, is_premium, notes, loaded_at
        FROM s_psql_dds.v_dm_task
    """)
    rows = pg_cur.fetchall()
    pg_cur.close()
    pg_conn.close()

    if not rows:
        print("⚠️ Нет данных для перекладки. Сначала запусти fill_dm_table()")
        return

    # 2. Записываем в MySQL
    mysql_conn = pymysql.connect(**MYSQL_CONFIG)
    mysql_cur = mysql_conn.cursor()
    
    # Очищаем целевую таблицу
    mysql_cur.execute("DELETE FROM t_dm_task")
    
    insert_sql = """
        INSERT INTO t_dm_task (id, event_date, category_id, region_id, customer_age, income,
                               transaction_amount, rating, is_premium, notes, loaded_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    mysql_cur.executemany(insert_sql, rows)
    mysql_conn.commit()
    mysql_cur.close()
    mysql_conn.close()
    
    print(f"✅ Transferred {len(rows)} rows to MySQL successfully.")