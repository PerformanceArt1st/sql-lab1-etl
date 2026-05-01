import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def get_dataset(n_rows: int = 1000) -> pd.DataFrame:
    # Генерация базовых данных
    base_dates = [(datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d") for _ in range(n_rows)]
    
    # "Ломаем" ~5% дат для имитации аномалий
    for i in random.sample(range(n_rows), int(n_rows * 0.05)):
        base_dates[i] = random.choice(["invalid", "2023/12/01", "", "32-01-2023"])

    data = {
        "id": [str(i) for i in range(1, n_rows + 1)],
        "event_date": base_dates,
        "category": [random.choice(["electronics", "clothing", "food", "electronics ", "FOOD", None]) for _ in range(n_rows)],
        "region": [random.choice(["north", "south", "east", "west", "  North "]) for _ in range(n_rows)],
        "customer_age": [str(random.randint(15, 130)) for _ in range(n_rows)],
        "income": [str(round(random.uniform(20000, 150000), 2)) for _ in range(n_rows)],
        "transaction_amount": [str(round(random.uniform(5, 5000), 2)) for _ in range(n_rows)],
        "rating": [str(round(random.uniform(0.5, 6.0), 1)) for _ in range(n_rows)],
        "is_premium": [random.choice(["Yes", "no", "1", "False", "да", ""]) for _ in range(n_rows)],
        "notes": [f"Note {i}" if random.random() > 0.1 else "" for i in range(n_rows)]
    }

    # Добавляем аномалии в числовые поля
    for i in random.sample(range(n_rows), int(n_rows * 0.03)):
        data["customer_age"][i] = random.choice(["N/A", "-5", "abc"])
    for i in random.sample(range(n_rows), int(n_rows * 0.03)):
        data["income"][i] = random.choice(["-5000", "high", ""])
    for i in random.sample(range(n_rows), int(n_rows * 0.03)):
        data["transaction_amount"][i] = random.choice(["-100", "0", "N/A"])

    df = pd.DataFrame(data)
    return df