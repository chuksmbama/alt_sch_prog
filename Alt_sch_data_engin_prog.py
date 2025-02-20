import uuid
from datetime import datetime, timezone


class Expense:
    # Represents an indiviual expense with a unique ID, title, amount and timestamps
    def __init__(self, title: str, amount: float):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow().replace(tzinfo=timezone.utc)
        self.updated_at = self.created_at

    def update(self, title: str = None, amount: float = None):
        # Updates the expense title and amount
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)

    def to_dict(self):
        # Converts the expense object into a dictionary format
        return {
            'id': self.id,
            'Title': self.title,
            'Amount': self.amount,
            'Created_at': self.created_at.isoformat(),
            'Updated_at': self.updated_at.isoformat()
        }


class ExpenseDatabase:
    # Manages a collection of expense objects
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
    # Adds an expense to the database

    def remove_expense(self, expense_id: str):
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]
    # Removes an expense from the database using its ID

    def get_expense_by_id(self, expense_id: str):
        # Retrieves an expense by its unique ID
        for exp in self.expenses:
            if exp.id == expense_id:
                return exp
        return None

    def get_expense_by_title(self, title: str):
        # Retrieves a list of expenses matching the given title
        return [exp for exp in self.expenses if exp.title.lower() == title.lower()]

    def to_dict(self):
        # Returns all expenses in a dictionary format
        return [exp.to_dict() for exp in self.expenses]


def main():
    db = ExpenseDatabase()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Remove Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter expense title: ")
            amount = float(input("Enter expense amount: "))
            expense = Expense(title, amount)
            db.add_expense(expense)
            print("Expense added successfully!\n")

        elif choice == '2':
            if not db.expenses:
                print("No expenses recorded.\n")
            else:
                for exp in db.to_dict():
                    print(exp)

        elif choice == '3':
            expense_id = input("Enter the expense ID to remove: ")
            db.remove_expense(expense_id)
            print("Expense removed if ID was found.\n")

        elif choice == '4':
            print("Exiting...\n")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
