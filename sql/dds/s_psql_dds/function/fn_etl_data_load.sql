-- Чистка аномалий и загрузка в структурированную таблицу. Только SQL/PLpgSQL
CREATE OR REPLACE FUNCTION s_psql_dds.fn_etl_data_load(start_date DATE, end_date DATE)
RETURNS VOID AS $$
BEGIN
    -- Удаляем старые данные за период для реализации Type 1 (overwrite)
    DELETE FROM s_psql_dds.t_sql_source_structured
    WHERE event_date BETWEEN start_date AND end_date;

    INSERT INTO s_psql_dds.t_sql_source_structured (
        id, event_date, category, region, customer_age, income,
        transaction_amount, rating, is_premium, notes
    )
    SELECT
        NULLIF(TRIM(id), '')::INT,
        -- Безопасное приведение даты: только валидный ISO-формат
        CASE WHEN event_date ~ '^\d{4}-\d{2}-\d{2}$' THEN event_date::DATE ELSE NULL END,
        NULLIF(TRIM(LOWER(category)), ''),
        NULLIF(TRIM(UPPER(region)), ''),
        -- Возраст: только числа от 18 до 100
        CASE WHEN customer_age ~ '^\d+$' AND customer_age::INT BETWEEN 18 AND 100 THEN customer_age::INT ELSE NULL END,
        -- Доход: только неотрицательные числа
        CASE WHEN income ~ '^\d+(\.\d+)?$' AND income::DECIMAL >= 0 THEN income::DECIMAL ELSE NULL END,
        -- Сумма транзакции: только положительные числа
        CASE WHEN transaction_amount ~ '^\d+(\.\d+)?$' AND transaction_amount::DECIMAL > 0 THEN transaction_amount::DECIMAL ELSE NULL END,
        -- Рейтинг: от 1.0 до 5.0 с шагом 0.1
        CASE WHEN rating ~ '^\d+(\.\d)?$' AND rating::DECIMAL BETWEEN 1.0 AND 5.0 THEN rating::DECIMAL ELSE NULL END,
        -- Булев флаг: нормализация разных вариантов написания
        CASE
            WHEN LOWER(TRIM(is_premium)) IN ('yes', 'true', '1', 'да', 'y') THEN TRUE
            WHEN LOWER(TRIM(is_premium)) IN ('no', 'false', '0', 'нет', 'n') THEN FALSE
            ELSE NULL
        END,
        NULLIF(TRIM(notes), '')
    FROM s_psql_dds.t_sql_source_unstructured
    WHERE event_date ~ '^\d{4}-\d{2}-\d{2}$'
      AND event_date::DATE BETWEEN start_date AND end_date
      AND id IS NOT NULL;
END;
$$ LANGUAGE plpgsql;