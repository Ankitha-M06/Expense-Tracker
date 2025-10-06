expenses = []

def add_expense(amount, desc):
    expenses.append({"amount": amount, "desc": desc})
    return "Expense added."

def view_expenses():
    return expenses

def delete_expense(index):
    if 0 <= index < len(expenses):
        return expenses.pop(index)
    return "Invalid index."

# Example usage
if __name__ == "__main__":
    add_expense(500, "Groceries")
    add_expense(1200, "Rent")
    print(view_expenses())
