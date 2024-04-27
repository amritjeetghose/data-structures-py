expense_obj={
    'January': 2200,
    'February': 2350,
    'March': 2600,
    'April': 2130,
    'May': 2190
}
#1. In Feb, how many dollars you spent extra compare to January?
feb_extra_expense = expense_obj['February']-expense_obj['January']
print('extra dollars spent on Feb compare to Jan is:', feb_extra_expense)
#2. Find out your total expense in first quarter (first three months) of the year.
first_quarter_expense = expense_obj['January']+expense_obj['February']+expense_obj['March']
print('total expense in first quarter:', first_quarter_expense)
#3. Find out if you spent exactly 2000 dollars in any month
expense_of_2000 = any(expense == 2000 for expense in expense_obj.values())
print(expense_of_2000, 'has expense of 2000')
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense_obj['June']=1980
for month, expense in expense_obj.items():
    print(f"{month}: {expense}")
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this
print('brfore------')
for month, expense in expense_obj.items():
    print(f"{month}: {expense}")
expense_obj['April']=expense_obj['April']-200
print('after------')
for month, expense in expense_obj.items():
    print(f"{month}: {expense}")
