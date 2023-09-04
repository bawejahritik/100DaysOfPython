import os
user_choice = "yes"
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program.")

bidders = {}

while user_choice=="yes":
    name = input("What is your name?: ")
    bid = int(input("What's yoru bid?: $"))
    user_choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bidders[name] = bid
    if user_choice=="yes":
        os.system('cls')
    else:
        highest_bid = max(bidders, key= lambda k:bidders[k])
        print(f"The winner is {highest_bid} with a bid of ${bidders[highest_bid]}")