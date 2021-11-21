import register_trip
from metro.exceptions import *
from metro.utils import *
from models import Passenger, SingleTrip, CreditCard, TimeCredit, Admin


def main_menu():
    """main menu function"""
    while True:
        clear_screen()
        main_menu_options()

        option = input("\nyour option >>> ")

        # register new Passenger
        if option == "1":

            clear_screen()
            register_menu()

        # manage bank account
        elif option == "2":

            clear_screen()
            passenger = authenticate()
            manage_bank_account_menu(passenger)

        # trip management
        elif option == "3":

            clear_screen()
            passenger = authenticate()
            trip_management_menu(passenger)

        # admin panel
        elif option == "4":

            clear_screen()
            admin = login()
            control_menu(admin)

        # exit
        elif option == "5":

            clear_screen()
            print("Good Bye!")
            exit()

        else:

            wrong_option()


def register_menu():
    """register new Passenger"""
    print("_____________________REGISTER MENU_____________________\n")

    fullname = input("enter your fullname (e.g : Harry Potter) : ")
    phone_number = input("enter your phone number : ")
    email = input("enter your email (optional): ")

    try:

        passenger = Passenger(fullname, phone_number, email)
        clear_screen()
        print(passenger.register())

        print("\nsuccessfully registered !")
        enter_key()

    except RegisterError as e:
        clear_screen()
        print(e)
        enter_key()


def authenticate():
    """authenticate a passenger by unique_id"""
    try:

        unique_id = int(input("enter your unique id: "))
        passenger = Passenger.authenticate(unique_id)
        return passenger

    except AuthenticationError as e:

        clear_screen()
        print(e)
        enter_key()
        main_menu()

    except ValueError:

        clear_screen()
        print("All unique id characters must be integers !")
        enter_key()
        main_menu()


def manage_bank_account_menu(passenger):
    """management panel for bank account"""
    while True:

        clear_screen()
        manage_bank_account_menu_options()

        owner = passenger.bank_account.owner.fullname
        option = input(f"\n({owner}\'s account) >>> ")

        if option == "1":

            clear_screen()
            amount = input("enter your amount to deposit: ")

            try:

                passenger.bank_account.deposit(amount)
                print("deposit was successful !")
                enter_key()
            except BankAccountError as e:

                clear_screen()
                print(e)
                enter_key()

        elif option == "2":

            clear_screen()
            amount = input("enter your amount to withdraw: ")
            try:

                passenger.bank_account.withdraw(amount)
                print("withdraw was successful !")
                enter_key()

            except BankAccountError as e:

                clear_screen()
                print(e)
                enter_key()

        elif option == "3":

            clear_screen()
            print(passenger.bank_account.get_balance())
            enter_key()

        elif option == "4":

            main_menu()

        else:

            wrong_option()


def trip_management_menu(passenger):
    """trip management menu """
    while True:

        clear_screen()
        trip_management_menu_options()
        user = passenger.fullname
        option = input(f"\n(user: {user}) >>> ")

        # register new trip
        if option == "1":

            clear_screen()
            register_trip.register_trip(passenger)

        # buy new card
        elif option == "2":

            clear_screen()

            try:

                buy_cards_menu(passenger)

            except BankAccountError as e:

                clear_screen()
                print(e)
                enter_key()

        # back to main menu
        elif option == "3":

            main_menu()

        else:

            wrong_option()


def buy_cards_menu(passenger):
    """buy cards menu"""
    while True:

        clear_screen()
        buy_cards_menu_options()
        option = input(">>> ")

        # buy Single Trip metro card for 1000
        if option == "1":

            card = SingleTrip(passenger)
            passenger.bank_account.withdraw(str(card.price))
            card.save_card()

            clear_screen()
            print("single trip card successfully purchased")
            enter_key()

        # buy credit metro card for 5000
        elif option == "2":

            card = CreditCard(passenger)
            passenger.bank_account.withdraw(str(card.price))
            card.save_card()

            clear_screen()
            print("credit card successfully purchased")
            enter_key()

        # buy time-credit metro card 6000
        elif option == "3":

            card = TimeCredit(passenger)
            passenger.bank_account.withdraw(str(card.price))
            card.save_card()

            clear_screen()
            print("time-credit card successfully purchased")
            enter_key()

        # back to cards menu
        elif option == "4":

            trip_management_menu(passenger)

        else:

            wrong_option()


def control_menu(admin):
    """admin control menu"""
    admin = admin
    while True:
        clear_screen()
        control_menu_options()

        option = input(f"\n(ADMIN: {admin.fullname}) >>> ")

        # register trip
        if option == "1":

            clear_screen()
            admin_register_trip(admin)
            enter_key()

        # manage users
        elif option == "2":

            clear_screen()
            admin_manage_users(admin)
            enter_key()

        # manage trips
        elif option == "3":

            clear_screen()

        elif option == "4":

            clear_screen()
            main_menu()

        else:

            wrong_option()


def login():
    """admin login section"""
    try:

        unique_id = int(input("enter your unique id: "))
        password = input("enter your password: ")
        admin = Admin.login(unique_id, password)
        return admin

    except AuthenticationError as e:

        clear_screen()
        print(e)
        enter_key()
        main_menu()

    except ValueError:

        clear_screen()
        print("All unique id characters must be integers !")
        enter_key()
        main_menu()
    except Exception as e:
        print(e)
        enter_key()
        main_menu()


def admin_register_trip(admin):
    """register trip and save it"""
    trips = admin.load_trips()
    if trips:
        for i, trip in enumerate(trips, 1):
            print(f" {i} : " + 60 * "_" + f"{trip}")
    else:
        print("theres is no trips yet to show !!!")


def admin_manage_users(admin):
    """manage users section"""
    users = admin.load_users()
    if users:
        for i, user in enumerate(users, 1):
            print(f" {i} : " + 60 * "_" + f"{user}")

    else:
        print("theres is no user to show !!!")
