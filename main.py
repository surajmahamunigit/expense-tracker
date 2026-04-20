from file_handler import load_expense, save_expense
from expense_manager import add_expense, view_expenses, total_expenses, filter_by_category

expenses = []



def display_menu():
    print("\nWelcome to Expense Tracker\n")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total expenses")
    print("4. Filter by Category")
    print("4. Exit")


def main():
    """Main function"""

    # Load all the expenses at the start of the application
    expenses=load_expense()

    while True:

        display_menu()

        option= input("Enter your choice: ")

        if option == "1":
            add_expense(expenses)
        elif option == "2":
            view_expenses(expenses)
        elif option == "3":
            total_expenses(expenses)
        elif option == "4":
            filter_by_category(expenses)

if __name__ == "__main__":
    main()



