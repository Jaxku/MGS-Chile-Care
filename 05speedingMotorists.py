# Constants
FINE_SCALE = {
    0: 30,
    10: 80,
    15: 120,
    20: 170,
    25: 230,
    30: 300,
    35: 400,
    40: 510
}
ARRESTED_PERSONS = ['James Wilson', 'Helga Norman', 'Zachary Conroy']

# Variables
speeders = []
total_fines = 0

# Functions
def calculate_fine(amount_over_speed_limit):
    """
    Given the amount over the speed limit, calculates the fine using the FINE_SCALE.
    """
    for limit, fine in sorted(FINE_SCALE.items(), reverse=True):
        if amount_over_speed_limit >= limit:
            return fine + 100 * (amount_over_speed_limit - limit)
    return 630

def display_summary():
    """
    Displays the summary of the day's activities.
    """
    print("Total fines:", len(speeders))
    for i, (name, amount_over_speed_limit) in enumerate(speeders):
        print(f"{i+1}) Name: {name} Amount Over Limit: {amount_over_speed_limit}")

# Input mode
while True:
    name = input("Enter name of speeder: ")
    if name == "$":
        break
    amount_over_speed_limit = int(input("Enter the amount over speed limit: "))
    fine = calculate_fine(amount_over_speed_limit)
    print(f"{name} to be fined ${fine}")
    if name in ARRESTED_PERSONS:
        print(f"{name.upper()} - WARRANT TO ARREST")
    speeders.append((name, amount_over_speed_limit))
    total_fines += fine

# Summary mode
display_summary()
