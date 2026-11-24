from storage import add_operation as save_operation

def add_operation():
    """Запрашивает у пользователя данные и сохраняет операцию."""
    print("\n--- Новая операция ---")
    op_type = input("Тип (доход/расход): ").strip().lower()
    if op_type not in ("доход", "расход"):
        print("Ошибка: тип должен быть 'доход' или 'расход'.")
        return
    try:
        amount = float(input("Сумма: ").replace(",", "."))
    except ValueError:
        print("Ошибка: сумма должна быть числом.")
        return
    category = input("Категория: ").strip() or "без категории"
    date = input("Дата (ГГГГ-ММ-ДД): ").strip() or "—"
    save_operation(op_type, amount, category, date)
    print("Операция добавлена!")