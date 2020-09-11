#THIS PROGRAM ALLOWS THE USER TO ACCESS TWO DIFFERENT FINANCIAL CALCULATIONS: AN INVESTMENT
#CALCULATOR AND HOME LOAN REPAYMENT CALCULATOR.
import math

print("Choose either 'inverstment' or 'bond' from the menu below to proceed:\n")
print("investment   -   to calculate the amount of interest you'll earn on interest")
print("bond         -   to calculate the amount you'll have to pay on a home loan\n")

calculation = input("Enter your choice:(Investment/Bond)\n")
uppercase_calculation = calculation.upper()

#INVESTMENT CALCULATOR
if(uppercase_calculation == "INVESTMENT"):
    deposit = float(input("How much are you depositing? E.g 1000\n"))
    interest = float(input("What is the interest rate on your investment? E.g 7\n"))
    years = int(input("How many years are you planning on investing? E.g. 12\n"))
    interest_type = input("What interest is your inverstment?(Compound/Simple)\n")
    uppercase_interest_type = interest_type.upper()

    if(uppercase_interest_type == "COMPOUND"):
        r = interest/100
        total_amount = round((deposit*math.pow((1+r),years)),2)
        print(f"Your investment would be R{total_amount}")

    elif(uppercase_interest_type == "SIMPLE"):
        r = interest/100
        total_amount1 = round((deposit*(1 + (r * years))),2)
        print(f"Your investment would be R{total_amount1}")
    else:
        print("Please enter your choice correctly")

#BOND CALCULATOR
else:
    if(uppercase_calculation == "BOND"):
        present_value = float(input("How much is the that you buying? E.g 100000\n"))
        interest_rate = float(input("What is the interest rate? E.g. 7\n"))
        months = int(input("How many months are you planning on paying the house? E.g. 120\n"))
        i = (interest_rate/100)/12
        monthly_repayments = round(((i*present_value)/(1 - math.pow((1 + i),-months))),2)
        print(f"Your monthly repayments are going to be R{monthly_repayments}")

    else:
        print("Please enter your choice correctly")


