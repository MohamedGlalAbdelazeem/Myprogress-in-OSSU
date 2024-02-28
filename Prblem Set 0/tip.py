def main():
    # take input form user about the price of the meal
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
      # Remove the leading $
    amount_str = d[1:]
    # Convert the string to a float
    amount_float = float(amount_str)
    return amount_float


def percent_to_float(p):
   # Remove the trailing %
    percentage_str = p[:-1]
    # Convert the string to a float and divide by 100 to get the decimal representation
    percentage_float = float(percentage_str) / 100
    return percentage_float

main()