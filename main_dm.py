from src.fill_dm_table import fill_dm_table
from src.transfer_to_mysql import transfer_to_mysql
from datetime import date

if __name__ == "__main__":
    print("🚀 Starting Lab 2: DWH & Data Mart Pipeline...")
    
    # 1. Формируем витрину в PostgreSQL
    fill_dm_table(start_dt=date(2023, 1, 1), end_dt=date(2023, 12, 31))
    
    # 2. Перекладываем в MySQL
    transfer_to_mysql()
    
    print("🎉 Lab 2 pipeline finished successfully.")