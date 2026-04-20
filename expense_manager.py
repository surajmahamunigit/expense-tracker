from typing import List, Dict
from file_handler import save_expense

def add_expense(expenses: List[Dict]) -> None:
    """Add new expense to the expense list"""

    try:
        amount= float(input("Enter the amount: ").strip())
    except ValueError:
        print("Please enter a numeric value")
        return
    category=input("Enter the category: ").strip().lower()
    description=input("Enter the description: ").strip().lower()

    if amount<=0:
        print("Please enter a numeric value")
        return
    if not category:
        print("Please enter right category")
        return
    if not description:
        print("Please enter right description")
        return

    # construct a dict
    expense={"amount":amount,"category":category,"description":description}

    # add to the expenses list
    expenses.append(expense)
    print("Successfully added new expense")

    save_expense(expenses)


def view_expenses(expenses: List[Dict]) -> None:
    """Display all the expenses"""

    if not expenses:
        print("No expenses added")
        return

    sorted_expenses = sorted(expenses, key=lambda x: x['category'].lower())
    print("Expenses:\n")
    for expense in sorted_expenses:
        print(f"Category: {expense['category']}")
        print(f"Amount: {expense['amount']}")
        print(f"Description: {expense['description']}\n")


def total_expenses(expenses: List[Dict]) -> None:

    if not expenses:
        print("No expenses found.")
        return

    total_exp=sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: {total_exp:.2f}")


def filter_by_category(expenses: List[Dict]) ->  None:
    """Filter expenses by the category"""

    category = input("Enter the category:").strip().lower()

    list_expenses=[
       expense for expense in expenses if expense['category'].lower()==category
    ]

    # if list of expenses is empty
    if not list_expenses:
        print("No expense found.")
        return

    print(f"All the expenses found in {category} category:\n")
    for expense in list_expenses:
        print(f"Category: {expense['category']}")
        print(f"Amount: {expense['amount']}")
        print(f"Description: {expense['description']}\n")


def delete_expense(expenses: List[Dict]) -> None:
    """Delete expense from the expense list"""

    try:
        category=input("Enter the category you want to delete: ").strip().lower()
    except ValueError:
        print("Please enter the right category")
        return

    for expense in expenses:
        if expense["category"]==category:
            expenses.remove(expense)
            print("Successfully deleted expense")
            save_expense(expenses)


def update_expense(expenses: List[Dict]) -> None:
    """Update expense from the expense list"""

    try:
        category=input("Enter the expense category you want to update: ").strip().lower()
    except ValueError:
        print("Please enter the right category")
        return

    for expense in expenses:
        if expense["category"]==category:

            print("Previous expense:\n")
            print(f"Category: {expense['category']}")
            print(f"Amount: {expense['amount']}")
            print(f"Description: {expense["description"]}")

            option=input("Enter the update:\n 1. Category\n 2. Amount\n 3. Description")
            update_value=input("Enter the update: ").strip().lower()
            if option == "1":
                if update_value.isalpha():
                    expense['category']=update_value
                else:
                    print("Please enter a valid category")
                    update_expense(expenses)
            elif option == "2":
                if update_value.isdigit():
                    expense['amount']=update_value
                else:
                    print("Please enter a valid amount")
                    update_expense(expenses)
            elif option == "3":
                if update_value.isalphanum():
                    expense['description']=update_value
                else:
                    print("Please enter a valid description")
                    update_expense(expenses)

            print("Successfully updated expense")

    print("Failed to update expense. Try again")
    return






