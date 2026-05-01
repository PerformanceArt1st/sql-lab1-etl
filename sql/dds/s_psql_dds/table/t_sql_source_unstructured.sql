-- 1. Создаём схему
CREATE SCHEMA IF NOT EXISTS s_psql_dds;

-- 2. Создаём таблицу для "грязных" данных внутри этой схемы
CREATE TABLE IF NOT EXISTS s_psql_dds.t_sql_source_unstructured (
    id VARCHAR,
    event_date VARCHAR,
    category VARCHAR,
    region VARCHAR,
    customer_age VARCHAR,
    income VARCHAR,
    transaction_amount VARCHAR,
    rating VARCHAR,
    is_premium VARCHAR,
    notes VARCHAR
);