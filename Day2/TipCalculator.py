print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
num_of_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

print("Each person should pay: $" + str(round((total_bill + total_bill*tip_percentage/100)/num_of_people, 2)))
