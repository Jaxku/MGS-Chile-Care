name = input("What is the driver's name: ")

tripCount = 0
totalTime = 0.0  # Setting these up to take floats
totalIncome = 0.0
baseCost = 6.30  # Using constants rather than literals for
minuteCost = 0.60
startNewTrip = "yes"  # Set the loop to true

while startNewTrip == "yes":
    # Float allows for half minutes
    tripTime = float(input("How many minutes did the trip take? "))
    tripCount += 1
    totalTime += tripTime
    tripCost = (tripTime * minuteCost) + baseCost
    totalIncome += tripCost
    print(f"This trip cost ${tripCost:.2f}")
    print()
    startNewTrip = input("Do you want to enter aa new trip? Yes or No: ").lower()
    # No will break the leep

print("______________________________________________________________________")
print(f"Driber {name} had {tripCount} trips totalling {round(totalTime)} "
      f"minutes\n"
      f"The average time of al the trips was {round(totalTime / tripCount)}"
      f"minutes\n"
      f"The total income for the day was ${totalIncome:.2f}\n"
      f"The average cost of all trips was ${totalIncome / tripCount:.2f}")

