CREATE OR REPLACE FUNCTION s_psql_dds.fn_dm_data_load(start_dt DATE, end_dt DATE)
RETURNS VOID AS $$
BEGIN
    DELETE FROM s_psql_dds.t_dm_task 
    WHERE event_date BETWEEN start_dt AND end_dt;

    INSERT INTO s_psql_dds.t_dm_task (
        id, event_date, category_id, region_id, customer_age, income,
        transaction_amount, rating, is_premium, notes
    )
    SELECT 
        s.id, s.event_date, c.id, r.id, s.customer_age, s.income,
        s.transaction_amount, s.rating, s.is_premium, s.notes
    FROM s_psql_dds.t_sql_source_structured s
    LEFT JOIN s_psql_dds.t_dim_category c ON s.category = c.name
    LEFT JOIN s_psql_dds.t_dim_region r ON s.region = r.name
    WHERE s.event_date BETWEEN start_dt AND end_dt;
END;
$$ LANGUAGE plpgsql;