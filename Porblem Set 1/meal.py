

def main():
    meal_time = input("What time is it? (in HH:MM format) ")
    converted_time = convert(meal_time)
    if 7.0 <= converted_time <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= converted_time <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= converted_time <= 19.0:
         print("It's dinner time!")

def convert(time):
    hours, minutes = map(int, time.split(":"))  # Convert hours and minutes to integers
    return hours + minutes / 60  # Convert time to decimal format (e.g., 7:30 becomes 7.5 hours)


main()