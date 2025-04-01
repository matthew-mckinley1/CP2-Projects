#import csv
import csv

#loads coins from the CSV file and returns them as a dictionary for each country
def load_coins(csv_file):
    coins_by_country = {}

    #opens the csv file in read mode
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)

        #go through each row (each country and its coins) and save as a list
        for row in csv_reader:
            country_name = row[0]
            country_coins = []

            #add each coin and its value for this country
            for i in range(1, len(row), 2):
                coin_name = row[i]
                coin_value = row[i + 1]
                try:
                    coin_value = float(coin_value)  #convert value to float
                except ValueError: #if it can't convert that to a float, prints error that it can't
                    print(f"Can't convert coin value '{coin_value}' to a float!")
                    continue
                country_coins.append((coin_name, coin_value))

            coins_by_country[country_name] = country_coins
    return coins_by_country

#obtains an amount of money from the user
def get_amount(country):
    while True: #keeps running it
        amount = input(f'How much do you want to check in {country}? (Decimal form, e.g., 2.52)\n')
        try:
            amount = float(amount) #tries to change it to a float
        except ValueError: #if it can't convert it to a float
            print("Please enter only numbers.")
            continue
        if amount <= 0: #if it's 0 or less
            print("Please enter a positive number.")
            continue
        else: #if it's good
            return amount

#calculates the minimum number of coins/bills
def calculate(coins, country):
    amount = get_amount(country)
    amount = round(amount, 2)  #round to nearest 2 decimal places
    amount = int(amount * 100)  #convert to cents (integer)

    #start coin count at 0
    coin_counts = {coin[0]: 0 for coin in coins}

    #sort coins and bills by value, descending order
    coins = sorted(coins, key=lambda x: x[1], reverse=True)

    #calculate the minimum number of coins/bills
    for coin in coins:
        coin_name, coin_value = coin
        coin_value_in_cents = int(coin_value * 100)  #convert coin/bill value to cents
        while amount >= coin_value_in_cents:
            amount -= coin_value_in_cents
            coin_counts[coin_name] += 1

    #if there's any amount left that couldn't be matched, print an error
    if amount > 0:
        print(f"Couldn't make up the exact amount ({amount / 100:.2f}) with available coins/bills.")
    else:
        print(f"\nMinimum number of coins and bills for {country}:")
        for coin_name, count in coin_counts.items():
            if count > 0:
                print(f"{coin_name}: {count}")

#main function
def main():
    while True:
        #load coins data from CSV file
        coins_by_country = load_coins('Coin_Change_Problem/coins.csv')

        #user selects country
        country = input("Enter the country (e.g., 'United States Dollar', 'Euro', 'Japanese Yen', 'British Pound'): ")

        #make sure that country is in the available list
        if country in coins_by_country:
            #call the calculate function with the selected country's coins
            calculate(coins_by_country[country], country)
        else:
            print("Country not found. Please check your input.")

#call the main function
main()