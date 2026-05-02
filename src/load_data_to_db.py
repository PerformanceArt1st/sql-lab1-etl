import psycopg2
from psycopg2.extras import execute_values
from config import DB_CONFIG

def load_data_to_db(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    cur.execute("TRUNCATE TABLE s_psql_dds.t_sql_source_unstructured;")
    
    # Приводим всё к строке и заменяем NaN/None на пустую строку для VARCHAR
    df = df.astype(str).replace('nan', '').replace('None', '')
    tuples = [tuple(x) for x in df.values]
    cols = ','.join(df.columns)
    
    query = f"INSERT INTO s_psql_dds.t_sql_source_unstructured ({cols}) VALUES %s"
    execute_values(cur, query, tuples, page_size=500)
    
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Loaded {len(df)} rows into t_sql_source_unstructured")