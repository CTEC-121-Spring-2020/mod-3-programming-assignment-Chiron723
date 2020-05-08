# Module 3
#   Programming Assignment 4
#     Prob-3.py

# <YOUR NAME>

def letterGrade(score):
    if score==5:
        grade="A"
    elif score==4:
        grade="B"
    elif score==3:
        grade="C"
    elif score==2:
        grade="D"
    else:
        grade="F"
    print(grade)

    return grade

def unitTest():
    letterGrade(5)
    letterGrade(4)
    letterGrade(3)
    letterGrade(2)
    letterGrade(1)
    letterGrade(0)

if __name__ == "__main__":
    unitTest()