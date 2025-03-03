#makes it so that they can't input anything except for letters
"""

def check_input(user_txt):
    return not any(char.isdigit() for char in user_txt)

def hello(name):
    if check_input(name):
        print(f"Hello {name}!")
    else:
        print("Please only input letters")
        user = input("What is your name:\n").strip().capitalize()
        hello(user)

user = input("What is your name:\n").strip().capitalize()
hello(user)

"""

#outer and inner functions
"""
def fun1():
    msg = "This is the outer function"

    def fun2():
        print(msg)

    fun2()
fun1()

#wrapper function exists to protect the other code

"""


#closure functions
"""
def fun(a):
    #outer function remembers the value of a

    def adder(b):
        return a+b
    return adder #return the closure

val = fun(10)
print(val(5))
"""

def end(income):

    def calc(cost, type):
        percent = cost/income * 100
        print(f"Your {type} is ${cost:.2f} and that is {percent:.0f}")
    return calc

def user_input(type):
    return int(input(f"What is your monthly {type}: \n$"))

income = user_input("Income")
rent = user_input("Rent")
utilities = user_input("Utilities")
transportation = user_input("Transportation")

ready = end(income)

ready(rent, "rent")
ready(utilities, "utilities")
ready(transportation, "transportation")