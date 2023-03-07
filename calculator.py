first_operand = float(input("Enter first operand: "))
second_operand = float(input("Enter second operand: "))
#I used Zybooks Chapter 2.4 for help with floating-point numbers

print('''Calculator Menu 
--------------- 
1. Addition 
2. Subtraction 
3. Multiplication 
4. Division ''')

operation = int(input('\nWhich operation do you want to perform? '))

if operation == 1:
    print('\nThe result of the operation is ', first_operand + second_operand, '.', ' Goodbye!',  sep='')
elif operation == 2:
    print('\nThe result of the operation is ', first_operand - second_operand, '.', ' Goodbye!', sep='')
elif operation == 3:
    print('\nThe result of the operation is ', first_operand * second_operand, '.', ' Goodbye!', sep='')
elif operation == 4:
    print('\nThe result of the operation is ', first_operand / second_operand, '.', ' Goodbye!', sep='')
else:
    print('\nError: Invalid selection! Terminating program.')
'''I used https://www.programiz.com/python-programming/if-elif-else to learn about indenting the print statements as 
well as else statements.
I used advice from the user "synthphreak" in the reddit thread below to connect the period to the variable using sep=.
https://www.reddit.com/r/learnpython/comments/owl7o7/how_can_i_add_a_period_at_the_end_of_a_print/'''
