# Module 3
#   Programming Assignment 4
#     Prob-2.py

# <Stephen Guild>

'''
input: Input for a name, hourly wage, and hours. Also add modifiers
    for overtime, tax rate, and medical insurance.
process: calculate the wages from input. Overtime is calculated
    over 40 hours. Tax is 20% of all wages and insurance is 10%
    of all wages
output:name, regular wages, overtime wages, total wages, tax
    withholding, insurance withholding, and take home pay
'''

def main():
    #name input
    name=(input("Enter Name- "))
    print()
    #hourly wage input
    hourlyWage=(eval(input("input Hourly Wage- ")))
    print()
    #hours input
    hours=(eval(input("input hours- ")))
    print()
    #if statement if hours are over 40.
    if hours > 40:
        overtimeWage=hourlyWage*1.5
    #calculation for total wages
    wage=hourlyWage*hours
    if hours> 40:
        wage=hourlyWage*40+(overtimeWage*(hours-40))
    #calculation for Tax
    tax=wage*0.2
    #calculation for insurance
    medInsure=wage*0.1
    #final calculation for take home pay
    netWage=wage-(tax+medInsure)
    print("\nname:",name)
    print("\nhourly wage:",hourlyWage)
    print("\novertime wages:",overtimeWage)
    print("\ntotal wages:",wage)
    print("\ntax withholding:",tax)
    print("\ninsurance withholding:",medInsure)
    print("\ntake home pay:",netWage)

main()