
from modules.ExpenseTracker import ExpenseTracker
from modules.BudgetPlanner import BudgetPlanner
from modules.DataVisualization import Visualization
from modules.Export import Export
from modules.Reminder import Reminder
from utils.CurrencyConverter import CurrencyConverter

def display_menu():
    print("\n--- Finance Manager ---")
    print("1. Log an Expense")
    print("2. View Transactions")
    print("3. Set a Budget")
    print("4. Check Budget Status")
    print("5. Visualize Spending Trends")
    print("6. Export Transactions")
    print("7. Add a Reminder")
    print("8. Convert Currency")
    print("9. Exit")

def main():
    tracker = ExpenseTracker()
    planner = BudgetPlanner()
    visualizer = Visualization()
    exporter = Export()
    reminder_manager = Reminder()
    converter = CurrencyConverter()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category (e.g., Food, Transportation): ")
            amount = float(input("Enter amount: "))
            currency = input("Enter currency (default USD): ") or "USD"
            notes = input("Enter notes (optional): ")
            tracker.log_expense(category, amount, currency, notes)
            print("Expense logged successfully!")

        elif choice == "2":
            print(tracker.view_transactions())

        elif choice == "3":
            category = input("Enter category: ")
            limit = float(input("Enter budget limit: "))
            planner.set_budget(category, limit)
            print(f"Budget set for {category}: {limit}")

        elif choice == "4":
            category = input("Enter category: ")
            spent = float(input("Enter amount spent: "))
            print(planner.check_budget(category, spent))

        elif choice == "5":
            visualizer.plot_spending_trends(tracker.view_transactions())

        elif choice == "6":
            file_name = input("Enter export file name (default: exported_report.xlsx): ") or "exported_report.xlsx"
            exporter.export_to_excel(tracker.view_transactions(), file_name)

        elif choice == "7":
            task = input("Enter reminder task: ")
            date = input("Enter due date (YYYY-MM-DD): ")
            reminder_manager.add_reminder(task, date)
            print("Reminder added!")

        elif choice == "8":
            amount = float(input("Enter amount to convert: "))
            from_currency = input("Enter source currency (default USD): ") or "USD"
            to_currency = input("Enter target currency: ")
            converted_amount = converter.convert(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()