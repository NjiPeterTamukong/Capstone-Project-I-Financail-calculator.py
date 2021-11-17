import math  # this to import all math function

# this variable aim at choosing either investment or bond, and .lower() to minimize user error of divers character size
choice_calculation = input("'investment' or 'bond' from the menu below to proceed:" "\n"
                             "investment   -to calculate the amount of interest you will earn upon investing" "\n"
                             "bond         -to calculate the amount you will have to pay on a home loan" "\n").lower()
print(choice_calculation)   # to print the choice type

# if investment is the users choice;
# consider the money deposited, interest rate, the duration and interest type from user
if choice_calculation == "investment":
    investment = int(float(input("Enter the amount of money deposited:  ")))
    interest_rate = float(input("enter interest rate, NB;should the format '8' and not 8%:  "))/100
    year = int(input("Enter number of years:  "))

    # user should enter either simple or compound
    interest_type = input("Enter either 'simple' or 'compound' interest""\n")

    # if simple, consider the calculation for simple interest
    if interest_type == 'simple':
        total_interest = investment * (1 + interest_rate * year)

        # print out the total interest of the user
        print("the simple interest for the years is : ""\n", total_interest)

    # else if compound, consider the calculations for compound,
    else:
        total_interest = investment * (math.pow((1 + interest_rate),year))

        # print the result of total interest of the user
        print(round(total_interest, 2))

# if bond is the user choice_calculation:
# the value of the house, interest rate, duration will be consider for this calculation
elif choice_calculation == "bond":
    house_value = float(input("the value of the house:  "))
    interest_rate = float(input("enter interest rate, NB; it should take the format '8' not 8%:  "))/100/12
    number_of_months = int((input("enter the number of months to repay the bond, for example 120:  ")))

    # consider the formula for calculating bond below
    repayment = (interest_rate * house_value)/(1 - ((1 +interest_rate)**(-number_of_months)))

    # display users monthly repayment amount
    print(round(repayment, 2))


