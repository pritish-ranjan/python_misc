# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_expenses = [
    {"January": 2200},
    {"February": 2350},
    {"March": 2000},
    {"April": 2130},
    {"May": 2190}]

print(monthly_expenses[1]["February"])

diff_jan_feb = monthly_expenses[1]["February"] - monthly_expenses[0]["January"]
print("The difference between two months is " + str(diff_jan_feb)) 

total_expense_first_quarter = monthly_expenses[0]["January"] + monthly_expenses[1]["February"] + monthly_expenses[2]["March"]

print("The expense for the first quarter is " + str(total_expense_first_quarter))

def check_expense(amount):
    for i in range(len(monthly_expenses)):
        for j in monthly_expenses[i]:
            if monthly_expenses[i][j] == amount:
                
                print("The month with 2000 expense is " + j)
                return True
    return False

res = check_expense(2000)
print("Did I soend 2000 in any month? " + str(res))

monthly_expenses.insert(5, {"June": 1800})

print(monthly_expenses)

monthly_expenses[3] = {"April": 1930}

print(monthly_expenses)