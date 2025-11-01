# src/expense_tracker.py
# Simple Personal Expense Tracker (CSV + pandas)
# Created by Apurva Bhoyar

import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "expenses.csv"

def load_data():
    """Load CSV data into a DataFrame"""
    return pd.read_csv(DATA_PATH, parse_dates=["date"])

def add_expense(date, category, amount, notes=""):
    df = load_data()
    new = {"date": pd.to_datetime(date), "category": category, "amount": float(amount), "notes": notes}
    df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)
    print("Expense added.")

def summary_by_month():
    df = load_data()
    df['month'] = df['date'].dt.to_period('M')
    summary = df.groupby('month')['amount'].agg(total='sum', average='mean', count='count').reset_index()
    print(summary.to_string(index=False))

if __name__ == "__main__":
    print("Personal Expense Tracker — commands: add / summary")
    cmd = input("Enter command: ").strip().lower()
    if cmd == "add":
        d = input("date (YYYY-MM-DD): ")
        c = input("category: ")
        a = input("amount: ")
        n = input("notes (optional): ")
        add_expense(d, c, a, n)
    elif cmd == "summary":
        summary_by_month()
    else:
        print("Unknown command. Use 'add' or 'summary'.")
