from models import Passenger, SingleTrip, CreditCard, TimeCredit, Trip
from metro.exceptions import RegisterError, BankAccountError, AuthenticationError, TripError, MetroCardError
from metro.utils import clear_screen, main_menu_options, any_key, manage_bank_account_menu_options, \
    trip_management_menu_options, buy_cards_menu_options


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

            try:

                trip_management_menu(passenger)

            except BankAccountError as e:

                print(e)

            except Exception as e:

                print("\n", e)

        # admin panel
        elif option == "4":

            # todo: admin panel section
            pass

        # exit
        elif option == "5":

            clear_screen()
            print("Good Bye!")
            exit()

        else:
            clear_screen()
            print("wrong option, try again\n")
            input("Press any key to continue...")


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
        any_key()

    except RegisterError as e:
        clear_screen()
        print(e)
        any_key()


def authenticate():
    """authenticate a passenger by unique_id"""
    try:

        unique_id = int(input("enter your unique id: "))
        passenger = Passenger.authenticate(int(unique_id))
        return passenger

    except AuthenticationError as e:

        clear_screen()
        print(e)
        any_key()
        main_menu()

    except ValueError:

        clear_screen()
        print("All unique id characters must be integers !")
        any_key()
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
                any_key()
            except BankAccountError as e:

                clear_screen()
                print(e)
                any_key()

        elif option == "2":

            clear_screen()
            amount = input("enter your amount to withdraw: ")
            try:

                passenger.bank_account.withdraw(amount)
                print("withdraw was successful !")
                any_key()

            except BankAccountError as e:

                clear_screen()
                print(e)
                any_key()

        elif option == "3":

            clear_screen()
            print(passenger.bank_account.get_balance())
            any_key()

        elif option == "4":

            main_menu()

        else:

            print("wrong option, try again")


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
            register_trip(passenger)

        # buy new card
        elif option == "2":

            clear_screen()

            try:

                buy_cards_menu(passenger)

            except BankAccountError as e:

                clear_screen()
                print(e)
                any_key()

        # back to main menu
        elif option == "3":

            main_menu()

        else:

            clear_screen()
            print("wrong option, try again")
            any_key()


def register_trip(passenger):
    """register trip section"""

    # if passenger has no cards
    if not passenger.list_cards():

        print("There is no card to show, Buy first")
        any_key()
    else:

        my_cards = passenger.list_cards()

        print("Cards List")
        for i, c in enumerate(my_cards, 1):
            print(f"{i}: {c}")

        try:

            card = int(input("select your desired card: "))

            if card <= 0 or my_cards[card - 1] not in my_cards:
                raise IndexError()

            selected_card = my_cards[int(card) - 1]
            print(selected_card, "selected")

            if isinstance(selected_card, SingleTrip):

                selected_card.use_card()

            else:

                selected_card.use_card(Trip.PRICE)

        except (IndexError, TypeError):

            print("invalid option, try again")
            trip_management_menu(passenger)

        except MetroCardError as e:
            print(e)
            trip_management_menu(passenger)

        print(Trip.get_stations())

        origin = input("enter origin station: ")
        destination = input("enter destination station: ")

        try:

            trip = Trip(origin, destination)
            print(trip)
            trip.progress()

        except TripError as e:
            print(e)


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
            print("single trip metro card successfully purchased")
            any_key()

        # buy credit metro card for 5000
        elif option == "2":

            card = CreditCard(passenger)
            passenger.bank_account.withdraw(str(card.price))
            card.save_card()

            clear_screen()
            print("credit metro card successfully purchased")
            any_key()

        # buy time-credit metro card 6000
        elif option == "3":

            card = TimeCredit(passenger)
            passenger.bank_account.withdraw(str(card.price))
            card.save_card()

            clear_screen()
            print("time-credit metro card successfully purchased")
            any_key()

        # back to cards menu
        elif option == "4":

            trip_management_menu(passenger)

        else:

            clear_screen()
            print("wrong option, try again")
            any_key()