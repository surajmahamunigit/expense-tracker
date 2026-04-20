from typing import List, Dict
from file_handler import save_expense
from utils import is_valid_amount, is_valid_category, is_valid_description

def add_expense(expenses: List[Dict]) -> None:
    """Add new expense to the expense list"""


    amount= input("Enter the amount: ")
    if not is_valid_amount(amount):
        return add_expense(expenses)

    category=input("Enter the category: ").strip().lower()
    if not is_valid_category(category):
        return add_expense(expenses)

    description=input("Enter the description: ").strip().lower()
    if not is_valid_description:
        return add_expense()

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

    total_exp=sum(float(expense['amount']) for expense in expenses)
    print(f"Total expenses: {total_exp}")


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
        else:
            print("Please enter a valid category")


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

            option=input("Enter the update:\n 1. Category\n 2. Amount\n 3. Description\n")
            update_value=input("Enter the update: ").strip().lower()
            if option == "1":
                if len(update_value)>0:
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
                if len(update_value)>0:
                    expense['description']=update_value
                else:
                    print("Please enter a valid description")
                    update_expense(expenses)

            save_expense(expenses)
            print("Successfully updated expense")
    return







