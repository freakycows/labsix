import math

current_results = 0.0
number_calc = 0
sum_calc = 0.0
menu_selection = -2
#These are to help set-up the calculations for later
#number_calc and sum_calc are specifically for 7

while menu_selection != 0:
    print('Current Result: ', current_results)
    print('''\nCalculator Menu
    ---------------
    0. Exit Program
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exponentiation
    6. Logarithm
    7. Display Average''')

    menu_selection = int(input('\nEnter Menu Selection: '))

    while menu_selection == 7:
        if current_results == 0:
            print('\nError: No calculations yet to average!')
        else:
            print(f"Sum of calculations: {round(sum_calc, 2)}")
            print(f"Number of calculations: {number_calc}")
            print(f"Average of calculations: {round(sum_calc / number_calc, 2)}")
#I used information from https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python#:~:text=Use%20the%20ceil()%20function,and%20print%20the%20resultant%20number.
#to round the Average of calculations
        menu_selection = int(input("\nEnter Menu Selection: "))
#Adding another menu_selection makes the user have to input a valid number since 7 cannot be the first number inputted

    if menu_selection == 0:
        break

    while menu_selection < 0:
        print('Error: Invalid selection!')
        menu_selection = int(input("\nEnter Menu Selection: "))
    if menu_selection == 0:
        break

    while menu_selection > 7:
        print('Error: Invalid selection!')
        menu_selection = int(input("\nEnter Menu Selection: "))
    if menu_selection == 0:
        break
#If the user inputs a negative number or a number greater than 7 it will make them enter a valid number

    first_operand = float(input('Enter first operand: '))
    second_operand = float(input('Enter second operand: '))

    if menu_selection == 1:
        current_results = first_operand + second_operand
        number_calc += 1
        sum_calc += current_results
#I figured out how to find the average by using "number_calc += 1" from Zybooks Ch 3.13

    elif menu_selection == 2:
        current_results = first_operand - second_operand
        number_calc += 1
        sum_calc += current_results

    elif menu_selection == 3:
        current_results = first_operand * second_operand
        number_calc += 1
        sum_calc += current_results

    elif menu_selection == 4:
        current_results = first_operand / second_operand
        number_calc += 1
        sum_calc += current_results

    elif menu_selection == 5:
        current_results = pow(first_operand, second_operand)
        number_calc += 1
        sum_calc += current_results

    elif menu_selection == 6:
        current_results = math.log(second_operand, first_operand)
        number_calc += 1
        sum_calc += current_results
#I have organized the scientific calculator functions in order while also making sure the number_calc and sum_calc
#add up so that 7 can properly calculate the average

    elif menu_selection == 0:
        break
#I added another menu_selection == 0 to this block because otherwise it would ask for more operands

print('\nThanks for using this calculator. Goodbye!')
