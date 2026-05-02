CREATE TABLE IF NOT EXISTS s_psql_dds.t_dim_category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);

INSERT INTO s_psql_dds.t_dim_category (name)
SELECT DISTINCT category 
FROM s_psql_dds.t_sql_source_structured 
WHERE category IS NOT NULL
ON CONFLICT (name) DO NOTHING;