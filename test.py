

def menu():
        choice = ""
        while choice != "5":
            print("___________________________________________")
            print("Welcome to MGS Childcare")
            print("What would you like do today here at MGS Childcare")
            print("___________________________________________")
            print()
            print("1. Drop off a child")
            print("2. Pick up a child")
            print("3 Calculate cost")
            print("4. Print roll")
            print("5. Exit")
            print()


        choice = int(input("Enter your choice (number between 1 and 5): "))
        if choice==1:
                dropOff()

        elif choice==2:
                pickUp()

        elif choice==3:
                calcCost()

        elif choice==4:
                printRoll()

        elif choice==5:
             print("Goodbye")


        else:
                print("Invaild Response, Please try again")

menu()




