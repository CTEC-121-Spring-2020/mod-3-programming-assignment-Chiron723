# Module 3
#   Programming Assignment 4
#     Prob-1.py

# <Stephen>
'''
input: Subtotal
process: Calculate shipping cost. Cost is $2.99 for totals less than $10.00
    and zero otherwise.
output: Return Shipping cost.
'''

def shippingCost(orderSubTotal):
    shippingCost = 2.99
    #Added the if statement for greater than $10.00.
    if orderSubTotal >= 10.00:
        shippingCost = 0.00


    return shippingCost

def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    
    #added test for shipping cost over 10.00.
    print("Shipping cost if subtotal >= 10.00\t", shippingCost(10.00))

if __name__ == "__main__":
    unitTest()