#Matthew McKinley Financial Calculator

#Calculates how long it will take to save for a goal
def goal():
    totalGoal = float(input("What would you like the goal to be? :"))
    weekorMonth = str(input("Would you like to deposit Weekly or Monthly? (W/M)")).upper()
    if weekorMonth == "W":
        WoM = "week"
    elif weekorMonth == "M":
        WoM = "month"

    howMuch = float(input("How much money would you like to deposit every week/month? :"))
    howLong = totalGoal/howMuch
    print(f"It will take {howLong:.2f} weeks to reach your goal! \n \n \n")
    runAgain()

#Calculates compound interest
def compIntCalc():
    start = float(input("How much money are you starting with?"))
    rate = float(input("What is the rate of interest? (Percentage Anually)"))
    compound = float(input("How many times will it compound anually?"))
    years  = float(input("How many years are you going to leave it?"))
    rate = float(rate/100)
#Calculating based off of the inputs
    rateCompound = 1 + (rate / compound)
    compTime = compound * years
    rateCompCompYear = rateCompound**compTime
    total2 = start * rateCompCompYear
    total2 = float(total2)
    print(f"You will end up with {total2:.2f} dollars! \n \n \n")
    runAgain()
    
#Allocates a budget based off of the income
def budgetAlloc():
    budget = float(input("What is your monthly income?"))
    needs = float(budget*.5)
    wants = float(budget*.3)
    saving = float(budget*.2)
    print(f"You should put {needs:.2f} dollars toward things you need, {wants:.2f} dollars toward things you want, and {saving:.2f} dollars toward saving up for something, out of your total {budget:.2f} budget! \n \n \n")
    runAgain()


#Finds sale price of something after a discount
def salePriceCalc():
    price = float(input("What is the price of the item you are buying? :"))
    discount = float(input("What is the percentage discount of that item? :"))
    newPrice = price * (1 - (discount/100))
    print(f"With this discount, you only have to pay {newPrice:.2f} dollars! \n \n \n")
    runAgain()

#Finds the tip based off of the price and the percent you are going to tip
def tipCalc():
    price = float(input("What is the price of the item that you are finding the tip for? :"))
    tip = float(input("How much are you going to tip (percent) :"))
    tip2 = float(1 + (tip/100))
    totalPrice = price * tip2
    print(f"You will have to pay {totalPrice:.2f} dollars total! \n \n \n")
    runAgain()

#defining the main function
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


def runAgain():
    again = str(input("Would you like to run it again? (Y/N)"))
    if again == "Y":
        main()
    elif again == "N":
        exit()
    else:
        print("You didn't put a Y or an N \n")
        runAgain()

#calling the main function so that it actually runs
main()