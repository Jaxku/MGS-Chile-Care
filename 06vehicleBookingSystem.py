vehicles = [
    {'number': 1, 'type': 'Suzuki Van', 'seats': 2, 'booked_by': None},
    {'number': 2, 'type': 'Toyota Corolla', 'seats': 4, 'booked_by': None},
    {'number': 3, 'type': 'Honda CRV', 'seats': 4, 'booked_by': None},
    {'number': 4, 'type': 'Suzuki Swift', 'seats': 4, 'booked_by': None},
    {'number': 5, 'type': 'Mitsibishi Airtrek', 'seats': 4, 'booked_by': None},
    {'number': 6, 'type': 'Nissan DC Ute', 'seats': 4, 'booked_by': None},
    {'number': 7, 'type': 'Toyota Previa', 'seats': 7, 'booked_by': None},
    {'number': 8, 'type': 'Toyota Hi Ace', 'seats': 12, 'booked_by': None},
    {'number': 9, 'type': 'Toyota Hi Ace', 'seats': 12, 'booked_by': None},
]

print("Welcome to the University's Vehicle Booking System!")
print("Please enter the number of seats you need (or -1 to exit):")
num_seats_needed = int(input())

while num_seats_needed != -1:
    available_vehicles = [vehicle for vehicle in vehicles if vehicle['booked_by'] is None and vehicle['seats'] >= num_seats_needed]
    if len(available_vehicles) == 0:
        print("Sorry, there are no available vehicles for that number of seats.")
    else:
        print("Available vehicles:")
        for vehicle in available_vehicles:
            if vehicle['seats'] >= num_seats_needed:
                print(f"{vehicle['number']}: {vehicle['type']} ({vehicle['seats']} seats)")
            else:
                print(f"{vehicle['number']}: {vehicle['type']} ({vehicle['seats']} seats) - Not enough seats")
        print("Please enter the number of the vehicle you want to book:")
        vehicle_num = int(input())
        vehicle = next((v for v in available_vehicles if v['number'] == vehicle_num), None)
        if vehicle is not None:
            print("Please enter your name:")
            name = input()
            vehicle['booked_by'] = name
            print(f"{vehicle['type']} (vehicle number {vehicle['number']}) has been booked by {name}.")
        else:
            print("Sorry, that vehicle is not available.")

    print("\nPlease enter the number of seats you need (or -1 to exit):")
    num_seats_needed = int(input())

print("\nEnd of day report:")
for vehicle in vehicles:
    if vehicle['booked_by'] is not None:
        print(f"Vehicle number {vehicle['number']}: {vehicle['type']}, booked by {vehicle['booked_by']}.")
