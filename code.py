def main():
    # Check current balance
    salary = get_int("What's your salary? ")
    percent_expense = get_int("What's the percent for expense? ")
    expense = expenses(salary, percent_expense)
    cost = get_int("How much is it? $")

    amount = percent(cost, expense)
    print(f"This item cost you {amount}% of your expenses of ${expense}")

    buy_item(cost, expense)
    # If Y, minus from expenses

# Calculate the percentage of input value
def percent(cost, expense):
    return int((cost / expense) * 100)

# Calculate expense
def expenses(salary, percent_expense):
    return int(salary * (percent_expense / 100))

# Calculate after buying
def buy_item(cost, expense):
    purchase = input("You sure? Y/N? ").upper()
    if purchase == "Y":
        update = int(expense - cost)
        print(f"You spent ${cost}, left with ${update}.")

    else:
        print(f"Good, save that ${cost}.")


# get_int for exception handling
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
