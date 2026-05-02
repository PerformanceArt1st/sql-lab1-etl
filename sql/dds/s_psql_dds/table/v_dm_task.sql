CREATE OR REPLACE VIEW s_psql_dds.v_dm_task AS
SELECT 
    id, event_date, category_id, region_id, customer_age, income,
    transaction_amount, rating, is_premium, notes, loaded_at
FROM s_psql_dds.t_dm_task;