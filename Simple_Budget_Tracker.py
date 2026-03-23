# Simple Budget Tracker
# This script helps track monthly budget and expenses

def main():
    # Ask for total monthly budget
    try:
        budget = float(input("Enter your total monthly budget: LKR "))
    except ValueError:
        print("Invalid input. Please enter a valid number for budget.")
        return

    # Initialize remaining balance
    remaining_balance = budget

    # Ask for expenses (enter 'done' to finish)
    expenses = []
    i = 1
    while True:
        user_input = input(f"Enter expense {i} (or 'done' to finish): LKR ")
        if user_input.lower() == 'done':
            break
        try:
            expense = float(user_input)
            expenses.append(expense)
            remaining_balance -= expense
            print(f"Remaining Balance: LKR {remaining_balance:.2f}")
            if remaining_balance < 500:
                print("Warning: Low Funds")
            i += 1
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")
            continue

    # Calculate total expenses
    total_expenses = sum(expenses)

    # remaining_balance is already calculated

    # Display results
    print(f"\nTotal Budget: LKR {budget:.2f}")
    print(f"Total Expenses: LKR {total_expenses:.2f}")
    print(f"Remaining Balance: LKR {remaining_balance:.2f}")

    if remaining_balance < 0:
        print("Warning: You have exceeded your budget!")
    elif remaining_balance == 0:
        print("You have used up your entire budget.")
    else:
        print("You are within your budget.")

    if remaining_balance <= 500:
        print("Warning: Low Funds")


if __name__ == "__main__":
    main()