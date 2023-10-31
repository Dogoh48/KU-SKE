def read_customer_info():
    print('Welcome to SKE diner')
    name = input('Please enter your name: >? ')
    age = int(input('Please enter your age: >? '))
    gender = input('Please enter your gender (F/M): >? ')
    member_status = input('Are you diner member (Yes/No): >? ')
    return name, age, gender, member_status


def get_suggested_menu(_age, _gender):
    if _age <= 25:
        _suggested_app = 'fries'
        if _gender == 'F':
            _suggested_entree1 = 'fish and chips'
            _suggested_entree2 = 'sandwich'
        else:
            _suggested_entree1 = 'fried chicken'
            _suggested_entree2 = 'hamburger'
    elif _age <= 50:
        _suggested_app = 'shrimp cocktail'
        if _gender == 'F':
            _suggested_entree1 = 'beef burrito'
            _suggested_entree2 = 'fish steak'
        else:
            _suggested_entree1 = 'BBQ ribs'
            _suggested_entree2 = 'steak'
    else:
        _suggested_app = 'gratin'
        if _gender == 'F':
            _suggested_entree1 = 'broiled fish'
            _suggested_entree2 = 'baked chicken'
        else:
            _suggested_entree1 = 'meatloaf'
            _suggested_entree2 = 'stew'
    return _suggested_app, _suggested_entree1, _suggested_entree2


def take_app_order(suggested_app):
    print(f'Appetizer menu: soup, salad, {suggested_app}, or none')
    appitizer = input('Select appetizer choice: ')
    return appitizer


def take_entree_order(suggested_entree1, suggested_entree2):
    print(f'Entree menu: pasta, pizza, {suggested_entree1}, {suggested_entree2}, or none')
    entree = input('Select entree choice: ')
    return entree


def take_dessert_order():
    print('Dessert menu: apple pie, cheesecake, or none')
    dessert = input('Select dessert choice: >? ')
    return dessert


def take_drink_order():
    print('Drink menu: water, soda, juice, tea, coffee, or none')
    drink = input('Select drink choice: >? ')
    return drink


def take_order(suggested_app, suggested_entree1, suggested_entree2):
    app_choice = take_app_order(suggested_app)
    entree_choice = take_entree_order(suggested_entree1 , suggested_entree2)
    dessert_choice = take_dessert_order()
    drink_choice = take_drink_order()
    return app_choice, entree_choice, dessert_choice, drink_choice


def get_prices(app_choice, entree_choice, dessert_choice, drink_choice):
    app_prices = {'salad': 50, 'soup': 79, 'fries': 55, 'shrimp cocktail': 150,
                  'gratin': 80, 'none': 0}
    entree_prices = {'pizza': 170, 'pasta': 250,
                     'fish and chips': 235, 'fried chicken': 225,
                     'sandwich': 209, 'hamburger': 299,
                     'fish steak': 220, 'steak': 390,
                     'beef burrito': 340, 'BBQ ribs': 430,
                     'baked chicken': 320, 'meatloaf': 280,
                     'broiled fish': 349, 'stew': 399, 'none': 0}
    dessert_prices = {'apple pie': 170, 'cheesecake': 155, 'none': 0}
    drink_prices = {'water': 15, 'soda': 30, 'juice': 65, 'tea': 70,
                    'coffee': 80, 'none': 0}
    if app_prices.get(app_choice) is None:
        app_choice = 'none'
    if entree_prices.get(entree_choice) is None:
        entree_choice = 'none'
    if dessert_prices.get(dessert_choice) is None:
        dessert_choice = 'none'
    if drink_prices.get(drink_choice) is None:
        drink_choice = 'none'
    return app_prices[app_choice], entree_prices[entree_choice], \
        dessert_prices[dessert_choice], drink_prices[drink_choice]


def calculate_payment(app_choice, entree_choice, dessert_choice, drink_choice):
    """ From the customer's choices of appetizer, entree, dessert and drink,
        Return the total payment based on the customer's choices.

        :param app_choice: string
        :param entree_choice:  string
        :param dessert_choice:  string
        :param drink_choice:  string
        :return: total payment based on the customer's choices
        where each room fee costs 2500 Baht per day.
        >>> calculate_payment('salad', 'pizza', 'apple pie', 'water')
        405
        >>> calculate_payment('soup', 'pasta', 'cheesecake', 'coffee')
        564
        >>> calculate_payment('shrimp cocktail', 'BBQ ribs', 'none', 'juice')
        645
    """
    app_prices, entree_prices, dessert_prices, drink_prices = get_prices(app_choice, entree_choice, 
                                                                        dessert_choice, drink_choice)
    total_payments = app_prices + entree_prices + dessert_prices + drink_prices
    return total_payments 

def apply_discount(_total_payment, _member='No'):
    _discount = 0.0
    if _member == 'Yes':
        _discount = 0.1 * _total_payment
    return _discount


def summarize_order(name, app, entree, dessert, drink):
    r""" From the customer's name and choices of appetizer, entree, dessert
    and  drink,
        Return a string containing information about the order.

        :param _name: string
        :param _app: string
        :param _entree: string
        :param _dessert: string
        :param _drink: string
        :return: String containing information about the order
        >>> _order = summarize_order('Ann', 'x', 'y' ,'z', 'w')
        >>> print(_order)
        Thank you, Ann, for visiting the diner.
        Today, you've ordered:
        x for appetizer,
        y for entree,
        z for dessert,
        and w for drink.
    """
    order_summary = (
        f"Thank you, {name}, for visiting the diner.\n"
        "Today, you've ordered:\n"
        f"{app} for appetizer,\n"
        f"{entree} for entree,\n"
        f"{dessert} for dessert,\n"
        f"and {drink} for drink."
    )
    return order_summary


def summarize_receipt(total_payment, discount):
    r""" From total_payment and discount
        Return a string containing information about payment.

        Note that the final payment is total payment deducted with discount.

        :param _total_payment: float
        :param _discount: float
        :return: String containing information about payment
        >>> _receipt = summarize_receipt(1000.256, 100.025)
        >>> print(_receipt)
        Your total payment is 1000.26 Baht.
        You receive 100.03 Baht for discount.
        Your final payment is 900.23 Baht.
    """
    final_payment = total_payment - discount
    receipt_info = (
        f"Your total payment is {total_payment:.2f} Baht.\n"
        f"You receive {discount:.2f} Baht for discount.\n"
        f"Your final payment is {final_payment:.2f} Baht."
    )
    return receipt_info



# main part
# Fill in code for main part below
name, age, gender, member_status = read_customer_info()
suggested_app, suggested_entree1, suggested_entree2 = get_suggested_menu(age, gender)
app_choice, entree_choice, dessert_choice, drink_choice = take_order(suggested_app, suggested_entree1, suggested_entree2)
print("")
total_payments = calculate_payment(app_choice, entree_choice, dessert_choice, drink_choice)
discount = apply_discount(total_payments, member_status)
order_summary = summarize_order(name, app_choice, entree_choice, dessert_choice, drink_choice)
receipt_info = summarize_receipt(total_payments, discount)
print(order_summary)
print(receipt_info)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest

    doctest.testmod()
