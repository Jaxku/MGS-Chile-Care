""""Program to run silent auction
"""


def check_input(question):
    error = "That was not a valid number"
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


def welcome(text, symbol):
    print(symbol * len(text))
    print(text)
    print(symbol * len(text))
    print()


# Main routine
bid = 0.0
highest = 0.0
welcome("Mr Utting fantastic Auctions", "*")
item = input("What is the auction for? ")
reserve = check_input("What is the reserve price? $")
print()
print("The auction for the ", item, "has started!")

while bid != -1:
    print(f"\nThe highest bid so far is ${highest:.2f}")
    bid = check_input("What is your bid? (-1 to quit) $")
    if bid > highest:
        highest = bid
    elif bid == -1:
        break
    else:
        print("\nSorry, that id was not high enough")


if highest >= reserve:
    print()
    print("=================================")
    print(f"The {item} sold at auction for ${highest:.2f}")
else:
    print(f"The {item} was not sold because the\n"
          f"reserve of ${reserve:.2f} was not met\n"
          f"The highest bid was only ${highest:.2f}")
