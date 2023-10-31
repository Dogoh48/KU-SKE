def get_travel_info(): # Function to get travel information from the user destination(country), month, duration(days)
    destination = input('What is your destination?: ')
    month = input('Departing Month?: ')
    if month in high_season:
        print('During the peak travel season, ticket prices will increase by 20%.')
    duration = int(input('How many days?: '))
    return destination, month, duration


def get_passenger_info(): # Function to get passenger information from the user
    passenger_amount = int(input('How many passenger?: '))
    for i in range(1, passenger_amount + 1):
        print(f'Please enter passenger#{i} info')
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        passenger_class = input('Class: ')
        print('********')
        passenger = [first_name, last_name, passenger_class]
        passenger_info.append(passenger)
    return passenger_info


def check_high_season(month): # Function to check if the given month is in the high season
    if month in high_season:
        return 1
    else:
        return 0


def get_travel_fee(country): # Function to calculate travel fee based on the country and will return travel_fee and region of destination country
    if country in europe:
        index = europe.index(country)
        travel_fee = europe_distance[index] * 10
        region = 'Europe'
    else:
        index = asia.index(country)
        travel_fee = asia_distance[index] * 10
        region = 'Asia'
    travel_info = [travel_fee, region]
    return travel_info


def get_hotel_fee(number_person, number_night): # Function to calculate hotel fee based on the number of people and nights
    hotel_fee = (number_person*3000) * number_night
    return hotel_fee


europe = ["England", "Germany", "Italy", "France", "Belgium"]
europe_distance = [9435, 8672, 8705, 9390, 9097]
asia = ["China", "Japan", "Indonesia", "India", "Singapore"]
asia_distance = [3442, 4312, 2333, 4213, 2108]
high_season = ['November', 'December', 'January']
passenger_info = []
total_price = 0

# Main part
# Fill in code for main part below

# This section Gather travel information from the user, including destination, departure month, and duration 
# and retrieve passenger information while calculating the high season status and hotel fee.
destination, month, duration = get_travel_info()
passenger_info = get_passenger_info()
high_season = check_high_season(month)
passenger_amount = len(passenger_info)
hotel_fee = get_hotel_fee(passenger_amount, duration)

total_price = total_price + hotel_fee # Add travel fee to the total price

for i in range(passenger_amount): # Display passenger information and travel fee
    travel_info = get_travel_fee(destination)
    travel_fee = travel_info[0]
    if high_season == 1:
        travel_fee = travel_fee + (travel_fee*0.20) # Apply a 20% increase in travel fee during high season
    if passenger_info[i][2] == 'Business':
        travel_fee = travel_fee + (travel_fee*0.50) # Apply a 50% discount for Business class passengers
    print(f'Passenger Name: {passenger_info[i][0]} {passenger_info[i][1]}')
    print(f'From Bangkok to {destination} ({travel_info[1]})')
    print(f'Traveling fee: {travel_fee:.2f} Baht ({passenger_info[i][2]})')
    print('********')
    total_price = total_price + travel_fee

# Display the hotel fee and total cost
print(f'Hotel fee for {passenger_amount} rooms x {duration} nights is {hotel_fee:.2f} Baht')
print(f'The total cost is {total_price:.2f} Baht')
print(f'Enjoy your trip :)')





