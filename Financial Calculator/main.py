#Matthew McKinley Financial Calculator
"""
How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator 
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator
"""


def goal():
    totalGoal = int(input("What would you like the goal to be? :"))
    weekorMonth = str(input("Would you like to deposit Weekly or Monthly? (W/M)")).upper()
    if weekorMonth == "W":
        WoM = "week"
    elif weekorMonth == "M":
        WoM = "month"
    
    if WoM == "week":
        WoM2 = "weeks"
    elif WoM == "month":
        WoM2 = "months"

    howMuch = int(input("How much money would you like to deposit every week/month?"))
    howLong = totalGoal/howMuch
    print("It will take", howLong, WoM2, "to reach your goal! \n \n \n")
    main()


def compIntCalc():
    start = float(input("How much money are you starting with?"))
    rate = float(input("What is the rate of interest? (Percentage Anually)"))
    compound = float(input("How many times will it compound anually?"))
    years  = int(input("How many years are you going to leave it?"))
    rate = float(rate/100)
    #broke it down further, wasn't working with the other commented formula
    rateCompound = 1 + (rate / compound)
    compTime = compound * years
    rateCompCompYear = rateCompound**compTime
    total2 = start * rateCompCompYear
    #total = start(1 + (rate/compound))**(compound * years)
    total2 = float(total2)
    print("You will end up with", total2, "dollars! \n \n \n")
    main()
    
def budgetAlloc():
    budget = float(input("What is your monthly income?"))
    needs = float(budget*.5)
    wants = float(budget*.3)
    saving = float(budget*.2)
    print("You should put", needs, "dollars toward things you need,", wants, "dollars toward things you want, and", saving, "dollars toward saving up for something, out of your total", budget, "budget! \n \n \n")
    main()



def salePriceCalc():
    price = int(input("What is the price of the item you are buying? :"))
    discount = int(input("What is the percentage discount of that item? :"))
    newPrice = price * (1 - (discount/100))
    print("With this discount, you only have to pay", newPrice, "dollars! \n \n \n")
    main()



def tipCalc():
    price = int(input("What is the price of the item that you are finding the tip for? :"))
    tip = int(input("How much are you going to tip (percent) :"))
    totalPrice = price * (1 + (tip/100))
    print("You will have to pay", totalPrice, "dollars total! \n \n \n")
    main()


def main():
    choice = int(input(" Press 1 to see how long it will take to save for a goal \n Press 2 for a Compound Interest Calculator \n Press 3 for a Budget Allocator \n Press 4 for a Sale Price Calculator \n Press 5 for a Tip Calculator \n :"))
    if choice == 1:
        goal()
    elif choice == 2:
        compIntCalc()
    elif choice == 3:
        budgetAlloc()
    elif choice == 4:
        salePriceCalc()
    elif choice == 5:
        tipCalc()
    else:
        print("You did not input one of the options! Try again.")
        main()

main()