# Module 3
#   Programming Assignment 4
#     Prob-5.py

# <YOUR NAME>

def main():
    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print("\nA TypeError has occured\n")
    except:
        print("\nUnkown Exception has occured\n")

main()