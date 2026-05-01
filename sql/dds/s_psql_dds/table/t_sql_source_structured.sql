-- Целевая таблица с правильными типами. Реализует Type 1 историчность (перезапись)
CREATE TABLE IF NOT EXISTS s_psql_dds.t_sql_source_structured (
    id INT PRIMARY KEY,
    event_date DATE,
    category VARCHAR(50),
    region VARCHAR(50),
    customer_age INT,
    income DECIMAL(10,2),
    transaction_amount DECIMAL(10,2),
    rating DECIMAL(2,1),
    is_premium BOOLEAN,
    notes TEXT,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);