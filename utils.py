def is_valid_amount(value:str) -> bool:
    try:
        return float(value) > 0
    except ValueError:
        print("Please enter a positive amount")
        return False

def is_valid_category(category:str) -> bool:
    if category.isalpha and len(category) > 1:
        return True
    else:
        print("Please enter a valid category")
        return False


def is_valid_description(description:str) -> bool:
    if description.isalnum and len(description) > 3:
        return True
    else:
        print("Please enter a valid description")
        return False