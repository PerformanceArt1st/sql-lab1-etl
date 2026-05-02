CREATE TABLE IF NOT EXISTS s_psql_dds.t_dim_region (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);

INSERT INTO s_psql_dds.t_dim_region (name)
SELECT DISTINCT region 
FROM s_psql_dds.t_sql_source_structured 
WHERE region IS NOT NULL
ON CONFLICT (name) DO NOTHING;