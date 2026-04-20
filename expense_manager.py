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




