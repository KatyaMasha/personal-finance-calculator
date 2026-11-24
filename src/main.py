import storage
import finance

def show_menu():
    print("\n=== Калькулятор личных финансов ===")
    print("1. Добавить операцию")
    print("2. Показать все операции")
    print("3. Показать баланс")
    print("0. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            finance.add_operation()
        elif choice == "2":
            storage.show_operations()
        elif choice == "3":
            storage.show_balance()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()