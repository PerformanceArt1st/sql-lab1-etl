from src.get_dataset import get_dataset
from src.load_data_to_db import load_data_to_db
from src.fill_structured_table import fill_structured_table
from datetime import date

def etl():
    """Верхнеуровневая функция без входных параметров."""
    print("🚀 Starting ETL pipeline...")
    
    print("📦 Step 1: Generating synthetic dataset...")
    df = get_dataset(n_rows=1500)
    
    print("📥 Step 2: Loading raw data to unstructured table...")
    load_data_to_db(df)
    
    print("🔄 Step 3: Transforming anomalies & loading to structured table...")
    # Период по умолчанию (можно менять внутри, но etl() остаётся без параметров)
    fill_structured_table(start_date=date(2023, 1, 1), end_date=date(2023, 12, 31))
    
    print("🎉 ETL pipeline finished successfully.")