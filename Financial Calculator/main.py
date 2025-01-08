"""
How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator 
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator
"""

def goal():
    totalGoal = int(input("What would you like the goal to be? :"))
    howMuch = int(input("How much money would you like to deposit every week? :"))
    howLong = print(totalGoal/howMuch)
    print(howLong)


#def compIntCalc():
    
#def budgetAlloc():


def salePriceCalc():
    price = int(input("What is the price of the item you are buying? :"))
    discount = int(input("What is the percentage discount of that item? :"))
    newPrice = price * (1 - (discount/100))
    print(newPrice)



def tipCalc():
    price = int(input("What is the price of the item that you are finding the tip for? :"))
    tip = int(input("How much are you going to tip (percent) :"))
    totalPrice = price * (1 + (tip/100))
    print(totalPrice)



#def main():
