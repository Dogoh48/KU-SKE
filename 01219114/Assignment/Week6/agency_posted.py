CITY_AIRPORT_CODES = {'Don Mueang': 'DMK', 'Chiang Mai': 'CNX',
                      'Chiang Rai': 'CEI', 'Phitsanulok': 'PHS',
                      'Khon Kaen': 'KKC', 'Udon Thani': 'UTH',
                      'Ubon Ratchathani': 'UBP', 'Phuket': 'HKT',
                      'Hat Yai': 'HDY', 'Surat Thani': 'URT', 'Krabi': 'KBV'
                      }

AIRPORT_CODES = ['DMK', 'CNX', 'CEI', 'PHS', 'KKC', 'UTH', 'UBP', 'HKT',
                 'HDY', 'URT', 'KBV'
                 ]

TICKET_PRICES = {'DMK': {'CNX': 1630, 'CEI': 1230, 'PHS': 1040, 'KKC': 1080,
                         'UTH': 1260, 'UBP': 1130, 'HKT': 1650, 'HDY': 1520,
                         'URT': 1150, 'KBV': 990
                         },
                 'CNX': {'DMK': 1630, 'KKC': 1250, 'HKT': 2180, 'HDY': 1870,
                         'URT': 1620, 'KBV': 1860},
                 'CEI': {'DMK': 1230},
                 'PHS': {'DMK': 1040},
                 'KKC': {'DMK': 1080, 'CNX': 1250, 'HKT': 1600},
                 'UTH': {'DMK': 1260, 'HKT': 2620},
                 'UBP': {'DMK': 1130},
                 'HKT': {'DMK': 1650, 'CNX': 2180, 'KKC': 1600, 'UTH': 2620,
                         'HDY': 2090},
                 'HDY': {'DMK': 1520, 'CNX': 1870, 'HKT': 2090},
                 'URT': {'DMK': 1150, 'CNX': 1620},
                 'KBV': {'DMK': 990, 'CNX': 1860}
                 }


def find_airport_code():
    """ Read city name from user input.
        If user enters invalid city name, keep asking user to input
        another city name.
        If city name is valid, display the airport code.
    """
    while True:
        choice = input('Enter city or Done: ')
        if choice == 'Done':
            break
        else:
            try:
                airport_code = CITY_AIRPORT_CODES[choice]
                print(f'Airport code of {choice} is {airport_code}')
            except KeyError:
                print(f'Airport code of {choice} is not available')
                print('Available airports:')
                print('Don Mueang / Chiang Mai / Chiang Rai / Phitsanulok /')
                print('Khon Kaen / Udon Thani / Ubon Ratchathani /')
                print('Phuket / Hat Yai/ Surat Thani / Krabi')



def read_airport_code(msg):
    """ Receive msg string as function parameter. This string msg to show
        user what to input.
        If user enters invalid airport code, keep asking user to input another
        airport code.
        If airport code is valid, return such airport code.
    """
    while True:
        airport_code = input(msg)
        if airport_code in AIRPORT_CODES:
            return airport_code


def get_flight_info_str(direct, origin, destination, price):
    """ From the information of flight (direct or not, origin and destination
        airport codes, and flight price),
        Return the string contain flight information

        :param direct: boolean
        :param origin:  string
        :param destination: string
        :param price:  int
        :return: total payment based on the customer's choices
        where each room fee costs 2500 Baht per day.
        >>> get_flight_info_str(True, 'DMK', 'HKT', 1650)
        'DMK-HKT: 1650.00 Baht'
        >>> get_flight_info_str(True, 'HKT', 'KKC', 1600)
        'HKT-KKC: 1600.00 Baht'
        >>> get_flight_info_str(False, 'CEI', 'HKT', 2880)
        'CEI-DMK-HKT: 2880.00 Baht'
        >>> get_flight_info_str(False, 'PHS', 'UBP', 2170)
        'PHS-DMK-UBP: 2170.00 Baht'
    """
    if direct == True:
        return f'{origin}-{destination}: {price:.2f} Baht'
    else:
        return f'{origin}-DMK-{destination}: {price:.2f} Baht'


def find_direct_flights_under_budget():
    """ Read budget value and origin from user inputs.
        Report direct flights with price below the budget, starting from origin.
        If there is no direct flight, report None.
    """
    count = 0
    budget = int(input('Enter your budget: '))
    origin = read_airport_code('Enter origin airport code: ')
    print(f'Available direct flights from {origin}:')
    if origin in TICKET_PRICES:
        for destination, price in TICKET_PRICES[origin].items():
            if price < budget:
                count = count + 1
                print(f'{origin}-{destination}: {price:.2f} Baht')
    if count == 0:
        print('None')


def find_direct_flight_price(origin, destination):
    """ From the given origin and dst, return the price of direct flight
        from source to dst. If there is no direct flight available, return zero.

        :param origin: string
        :param destination: string
        :return: price if direct flight between origin and dst exists.
        Otherwise, return zero.
        >>> find_direct_flight_price('DMK', 'HKT')
        1650
        >>> find_direct_flight_price('CNX', 'KBV')
        1860
        >>> find_direct_flight_price('CEI', 'KKC')
        0
        >>> find_direct_flight_price('HDY', 'URT')
        0
    """
    if origin in TICKET_PRICES and destination in TICKET_PRICES[origin]:
        return TICKET_PRICES[origin][destination]
    else:
        return 0


def find_connecting_flight_price(origin, destination):
    """ Given origin and dst, find price of connecting flight from origin to
        DMK and from DMK to destination.

        In addition, let the connecting point be DMK only.  This airline only
        operates connecting flights that stop at DMK.

        If either origin or destination is DMK, it will return price of
        direct flight.

        If both origin and destination are the same, return zero.

        :param origin: string
        :param destination: string
        :return: price of connecting flight between origin and destination,
        where (1) the first direct flight in this connecting flight is from
        origin to DMK, and
              (2) the second direct flight is from DMK to destination.
        >>> find_connecting_flight_price('CEI', 'HKT')
        2880
        >>> find_connecting_flight_price('PHS', 'UBP')
        2170
        >>> find_connecting_flight_price('UTH', 'URT')
        2410
        >>> find_connecting_flight_price('KBV', 'CEI')
        2220
        >>> find_connecting_flight_price('CNX', 'CNX')
        0
        >>> find_connecting_flight_price('DMK', 'CEI')
        1230
        >>> find_connecting_flight_price('KBV', 'DMK')
        990
    """
    if origin == 'DMK' or destination == 'DMK':
        if origin in TICKET_PRICES:
            if destination in TICKET_PRICES[origin]:
                return TICKET_PRICES[origin][destination]
        else:
            return 0
    if origin == destination:
        return 0
    else:
        price_to_dmk = 0
        price_from_dmk = 0
        if origin in TICKET_PRICES and 'DMK' in TICKET_PRICES[origin]:
            price_to_dmk = TICKET_PRICES[origin]['DMK']

        if 'DMK' in TICKET_PRICES and destination in TICKET_PRICES['DMK']:
            price_from_dmk = TICKET_PRICES['DMK'][destination]

        return price_to_dmk + price_from_dmk


def find_flight_price():
    """ Read origin and destination from user inputs.
        If direct flight exists, report price of direct flight.
        Otherwise, find and report price of connecting flight.
    """
    origin = read_airport_code('Enter the origin: ')
    destination = read_airport_code('Enter destination: ')
    if origin == destination:
        print('Origin and destination cannot be the same.')
        return

    direct_flight_price = find_direct_flight_price(origin, destination)
    if direct_flight_price > 0:
        print(f"Direct flight: {origin}-{destination}: {direct_flight_price:.2f} Baht")
    else:
        connecting_flight_price = find_connecting_flight_price(origin, destination)
        if connecting_flight_price > 0:
            print(f"Connecting flight: {origin}-DMK-{destination}: {connecting_flight_price:.2f} Baht")


def find_all_flights_from_origin():
    """ Read origin from user input.
        First, report information of direct flights, starting from origin.
        Then, report information of connecting flights, starting from origin.
    """
    origin = read_airport_code('Enter origin: ')
    print(f"Direct flights:")
    for destination, price in TICKET_PRICES[origin].items():
        print(get_flight_info_str(True, origin, destination, price))

    print(f"Connecting flights:")
    for via_airport in AIRPORT_CODES:
        if via_airport != origin:
            to_via_price = find_direct_flight_price(origin, via_airport)
            if to_via_price > 0:
                for destination, price in TICKET_PRICES[via_airport].items():
                    if destination != origin:
                        total_price = to_via_price + price
                        print(f"{origin}-{via_airport}-{destination}: {total_price:.2f} Baht")


def find_available_flight_info(origin, destination):
    """ Given origin and dst, find price of available flight from origin to
        destination.
        If direct flight is available, return the price of such direct flight.
        Otherwise, use connecting flight.
        Return 2 values that are (1) corresponding flight string (from
        function get_flight_str) and (2) price of the flight

        :param origin: string
        :param destination: string
        :return: flight string and price of the flight from origin to
        destination.

        >>> find_available_flight_info('CEI', 'HKT')
        ('CEI-DMK-HKT: 2880.00 Baht', 2880)
        >>> find_available_flight_info('PHS', 'UBP')
        ('PHS-DMK-UBP: 2170.00 Baht', 2170)
        >>> find_available_flight_info('UTH', 'DMK')
        ('UTH-DMK: 1260.00 Baht', 1260)
        >>> find_available_flight_info('KBV', 'CEI')
        ('KBV-DMK-CEI: 2220.00 Baht', 2220)
    """
    if origin == destination:
        return f"", 0

    direct_price = find_direct_flight_price(origin, destination)

    if direct_price > 0:
        direct_flight_str = get_flight_info_str(True, origin, destination, direct_price)
        return direct_flight_str, direct_price
    else:
        to_dmk_price = find_direct_flight_price(origin, 'DMK')
        from_dmk_price = find_direct_flight_price('DMK', destination)

        if to_dmk_price > 0 and from_dmk_price > 0:
            total_price = to_dmk_price + from_dmk_price
            connecting_flight_str = f'{origin}-DMK-{destination}: {total_price:.2f} Baht'
            return connecting_flight_str, total_price


def reserve_ticket(_booking_list):
    """ Receive _booking list as function parameter.
        Note that _booking_list is a list of booking dictionaries.
        Each dictionary has 7 keys: first name, last name, origin, destination,
        flight info (which is flight string), price, and status.
        The status for ticket reservation is always 'Waiting'

        Read origin, destination, first name, last name from user inputs.
        Find available flight price from origin to destination.
        Add dictionary of booking items into a _booking list.
    """
    origin = read_airport_code('Enter origin: ')
    destination = read_airport_code('Enter destination: ')
    if origin == destination:
        print('Origin and destination cannot be the same. Try again.')
        return
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    flight_info, price = find_available_flight_info(origin, destination)
    booking = {
        "first_name": first_name,
        "last_name": last_name,
        "origin": origin,
        "destination": destination,
        "flight_info": flight_info,
        "price": price,
        "status": "Waiting"
    }
    _booking_list.append(booking)
    print(f'{first_name} {last_name}: {flight_info}, Status: Waiting')

def display_booking_list(_booking_list):
    """ Display information of _booking_list
    """
    for booking in _booking_list:
        first_name = booking['first_name']
        last_name = booking['last_name']
        flight_info = booking['flight_info']
        status = booking['status']
        print(f"{first_name} {last_name}: {flight_info}, Status: {status}")


def change_booking_status(_booking_list):
    """ Receive _booking list as function parameter.
        Read first name and last name from user inputs.
        In addition, ask user for new status to update: Confirmed (or CF) or
        Canceled (CC)
        If ticket under the given first name and last name is found in the
        _booking_list, change status of that ticket.
        If ticket under the given first name and last name is not found in the
        _booking_list, notify user.
    """
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    while True:
        new_status = input("Do you want to confirm or cancel booking (CF/CC)? ")

        if new_status in ('CF', 'CC'):
            break
        else:
            pass
    booking_found = False
    count = 0
    for booking in _booking_list:
        if booking['first_name'] == first_name and booking['last_name'] == last_name:
            if new_status == 'CF':
                booking['status'] = 'Confirmed'

            else:
                booking['status'] = 'Canceled'
            booking_found = True
            print(f"{first_name} {last_name}: {booking['flight_info']}, Status: {booking['status']}")
            count = count + 1
            break
    if count == 0:
        print('Invalid first name or last name. Please try again.')



def run_choice(_choice, _booking_list):
    """ Receive menu choice (_choice) and booking_list as function parameters.
        Call function corresponding to each choice.
    """
    if _choice == 1:
        find_airport_code()
    elif _choice == 2:
        find_direct_flights_under_budget()
    elif _choice == 3:
        find_flight_price()
    elif _choice == 4:
        find_all_flights_from_origin()
    elif _choice == 5:
        reserve_ticket(_booking_list)
    elif _choice == 6:
        display_booking_list(_booking_list)
    elif _choice == 7:
        change_booking_status(_booking_list)


def read_choice():
    """ Reade menu choice (_choice) as user input.
        If user enters invalid menu choice, keep asking user to enter
        another menu choice.
        Once the menu choice is valid, return such menu choice.
    """

    ### The following partial code is given.
    ### Feel free to use it to show the choice menu.
    print('\nChoices')
    print('1. Find airport code')
    print('2. Find direct flights under budget')
    print('3. Find price')
    print('4. Find all flights from origin')
    print('5. Reserve ticket')
    print('6. Display booking list')
    print('7. Change booking status')
    print('0. Exit')



# Main
booking_list = []
# Fill the remaining main part
while True:
    read_choice()
    choice = int(input('Enter your choice: '))
    if choice == 0:
        break
    elif choice > 7 or choice < 0:
        print('Your choice is invalid. Choose again.')
    else:
        run_choice(choice, booking_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest

    doctest.testmod()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/