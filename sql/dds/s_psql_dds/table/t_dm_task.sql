CREATE TABLE IF NOT EXISTS s_psql_dds.t_dm_task (
    id INT,
    event_date DATE,
    category_id INT,
    region_id INT,
    customer_age INT,
    income DECIMAL(10,2),
    transaction_amount DECIMAL(10,2),
    rating DECIMAL(2,1),
    is_premium BOOLEAN,
    notes TEXT,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id, event_date)
);