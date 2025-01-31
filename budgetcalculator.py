# Function to get user input for a specific expense category
def get_expense(name):
    while True:
        try:
            expense = float(input(f"Enter your {name} expense: $"))
            if expense < 0:
                print("Expense cannot be negative. Please try again.")
            else:
                return expense
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Function to calculate and display budget details
def budget_calculator():
    print("Welcome to the Budget Calculator!")

    # Get user income
    while True:
        try:
            income = float(input("Enter your total income: $"))
            if income < 0:
                print("Income cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Categories of expenses
    categories = ["Rent", "Utilities", "Groceries", "Transportation", "Entertainment"]

    total_expenses = 0
    expense_details = {}

    # Collect expenses for each category
    for category in categories:
        expense_details[category] = get_expense(category)
        total_expenses += expense_details[category]

    # Calculate remaining balance
    remaining_balance = income - total_expenses

    # Display results
    print("\n--- Budget Summary ---")
    print(f"Income: ${income:.2f}")
    print("Expenses:")
    for category, amount in expense_details.items():
        print(f"  {category}: ${amount:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${remaining_balance:.2f}")

    # Optionally save the results to a file
    save_option = input("\nDo you want to save this budget summary to a file? (yes/no): ").lower()
    if save_option == 'yes':
        with open("budget_summary.txt", "w") as file:
            file.write("--- Budget Summary ---\n")
            file.write(f"Income: ${income:.2f}\n")
            for category, amount in expense_details.items():
                file.write(f"{category}: ${amount:.2f}\n")
            file.write(f"Total Expenses: ${total_expenses:.2f}\n")
            file.write(f"Remaining Balance: ${remaining_balance:.2f}\n")
        print("Budget summary saved to 'budget_summary.txt'.")

# Run the program
if __name__ == "__main__":
    budget_calculator()
