def expense_tracker(expenses):
    total = 0
    highest_expense = expenses[0]
    lowest_expense = expenses[0]
    average_expense = 0
    for expense in expenses:
        if expense > highest_expense:
            highest_expense = expense
        elif expense < lowest_expense:
            lowest_expense = expense
        total += expense
        average_expense += expense
    average_expense /= len(expenses)

    return total, highest_expense, lowest_expense, average_expense 