expenses=[2200, 2350,2600,2130, 2190];

#1. In Feb, how many dollars you spent extra compare to January?
feb_extra_expense = expenses[1]-expenses[0]
print('extra dollars spent on Feb compare to Jan is:', feb_extra_expense)
#2. Find out your total expense in first quarter (first three months) of the year.
first_quarter_expense = expenses[1]+expenses[2]+expenses[3]
print('total expense in first quarter:', first_quarter_expense)
#3. Find out if you spent exactly 2000 dollars in any month
print(2000 in expenses, 'has expense of 2000')
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980);
print('Expense for June', expenses[5])
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this
expenses[3]=expenses[3]-200;
print('Updated expense for april:', expenses[3])