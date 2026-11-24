import json
import os

DATA_FILE = "operations.json"

def load_operations():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_all(operations):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(operations, f, ensure_ascii=False, indent=2)

def add_operation(op_type, amount, category, date):
    ops = load_operations()
    ops.append({
        "type": op_type,
        "amount": amount,
        "category": category,
        "date": date,
    })
    save_all(ops)

def show_operations():
    ops = load_operations()
    if not ops:
        print("\nОпераций пока нет.")
        return
    print("\n--- Все операции ---")
    for i, op in enumerate(ops, 1):
        sign = "+" if op["type"] == "доход" else "−"
        print(f"{i}. {op['date']} | {op['category']:<15} | {sign}{op['amount']:.2f}")

def show_balance():
    ops = load_operations()
    income = sum(o["amount"] for o in ops if o["type"] == "доход")
    expense = sum(o["amount"] for o in ops if o["type"] == "расход")
    print(f"\nДоходы:  {income:.2f}")
    print(f"Расходы: {expense:.2f}")
    print(f"Баланс:  {income - expense:.2f}")