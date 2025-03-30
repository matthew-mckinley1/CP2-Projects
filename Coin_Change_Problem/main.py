import csv

# Loads coins from the CSV file and returns them as a dictionary for each country
def load_coins(csv_file):
    coins_by_country = {}

    # Open the CSV file to read
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)

        # Go through each row (each country and its coins)
        for row in csv_reader:
            country_name = row[0]
            country_coins = []

            # Add each coin and its value for this country
            for i in range(1, len(row), 2):
                coin_name = row[i]
                coin_value = row[i + 1]
                try:
                    coin_value = float(coin_value)  # Convert value to float
                except ValueError:
                    print(f"Error converting coin value '{coin_value}' to float. Skipping.")
                    continue
                country_coins.append((coin_name, coin_value))

            coins_by_country[country_name] = country_coins

    return coins_by_country

# Obtains an amount of money from the user
def get_amount(country):
    while True:
        amount = input(f'How much do you have in {country}? (Decimal form, e.g., 2.52)\n')
        try:
            amount = float(amount)
        except ValueError:
            print("Please enter only numbers.")
            continue
        if amount <= 0:
            print("Please enter a positive number.")
            continue
        else:
            return amount

# Calculates the minimum number of coins/bills
def calculate(coins, country):
    amount = get_amount(country)
    amount = round(amount, 2)  # Round to nearest 2 decimal places
    amount = int(amount * 100)  # Convert to cents (integer)

    # Initialize coin counts to 0
    coin_counts = {coin[0]: 0 for coin in coins}

    # Sort coins and bills by value, descending order
    coins = sorted(coins, key=lambda x: x[1], reverse=True)

    # Calculate the minimum number of coins/bills
    for coin in coins:
        coin_name, coin_value = coin
        coin_value_in_cents = int(coin_value * 100)  # Convert coin/bill value to cents
        while amount >= coin_value_in_cents:
            amount -= coin_value_in_cents
            coin_counts[coin_name] += 1

    # If there's any amount left that couldn't be matched, print an error
    if amount > 0:
        print(f"Warning: Couldn't make up the exact amount ({amount / 100:.2f}) with available coins/bills.")
    else:
        print(f"\nMinimum number of coins and bills for {country}:")
        for coin_name, count in coin_counts.items():
            if count > 0:
                print(f"{coin_name}: {count}")

# Main function
def main():
    while True:
        # Load coins data from CSV file
        coins_by_country = load_coins('Coin_Change_Problem/coins.csv')

        # User selects country
        country = input("Enter the country (e.g., 'United States Dollar', 'Euro', 'Japanese Yen', 'British Pound'): ")

        # Ensure country is in the available list
        if country in coins_by_country:
            # Call the calculate function with the selected country's coins
            calculate(coins_by_country[country], country)
        else:
            print("Country not found. Please check your input.")

# Call the main function
main()