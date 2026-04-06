import pandas as pd  # for arranging the data in files
import os  # to check the file exits

# data file where data stored  .csv file (Comma-Separated Values file) is a simple text file used to store tabular data—like a spreadsheet.
FILENAME = "expenses.csv"
# Each line represents a row.Columns are separated by commas.It’s commonly used for data storage, importing/exporting between Excel, databases, Python, etc.


def load_expenses():  # function
    if os.path.exists(FILENAME):  # check csv file exits
        return pd.read_csv(FILENAME)  # load to panda table
    else:

        # if else return name amount category
        return pd.DataFrame(columns=["Name", "Amount", "Category"])


def save_expenses(df):  # define fn save expenses. df is a table /input to the fn
    # save df to csv ,filename is expenses.cv don;t save row value index=false
    df.to_csv(FILENAME, index=False)


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. View all expenses")
    print("2. Add expense")
    print("3. View total")
    print("4. View by category")
    print("5. Quit")  # shows menu

    choice = input("Choose an option: ")

    # Loads the expenses from the CSV file every time the menu shows. will get latest data
    df = load_expenses()

    if choice == "1":
        if df.empty:
            print("No expenses yet!")
        else:
            print(df)

    elif choice == "2":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: $"))
        category = input("Enter category (food/transport/shopping/other): ")
        new_expense = pd.DataFrame([[name, amount, category]], columns=[

                                   "Name", "Amount", "Category"])
        # Creates a new row with the expense data.
        df = pd.concat([df, new_expense], ignore_index=True)
        save_expenses(df)
        print("Expense added successfully!")

    elif choice == "3":
        if df.empty:
            print("No expenses yet!")
        else:
            # gets amount column adds all the amounts together
            total = df["Amount"].sum()
            # rounding to 2 decimal places — because money always has 2 decimal places!
            print("\nTotal spent: $", round(total, 2))

    elif choice == "4":
        if df.empty:
            print("No expenses yet!")
        else:
            category = input("Enter category to view: ")
            # filters the table to show only that category
            filtered = df[df["Category"] == category]
            if filtered.empty:
                print("No expenses in this category!")
            else:
                print(filtered)
                print("Total:", round(filtered["Amount"].sum(), 2))

    elif choice == "5":
        print("Goodbye!")
        break
