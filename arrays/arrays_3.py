#Create a list of all odd numbers between 1 and a max number. 
#Max number is something you need to take from a user using input() function
max_number= int(input('Enter the maximum number:'))
if max_number > 1:
    odd_numbers=[num for num in range(1, max_number) if num %2 ==1]
    print(odd_numbers)
else:
    print('Entered number cannot be less than 1')