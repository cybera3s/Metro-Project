import register_trip
from metro.exceptions import *
from metro.utils import *
from models import Passenger, SingleTrip, CreditCard, TimeCredit, Admin, Trip
from logger import Logger

Logger.set_logger(__name__)
logger = Logger.logger


def main_menu():
    """main menu function"""
    while True:
        clear_screen()
        main_menu_options()

        option = input("\nyour option >>> ")
        logger.debug(f"{option} entered, main_menu")

        # register new Passenger
        if option == "1":

            clear_screen()
            register_menu()

        # manage bank account
        elif option == "2":

            clear_screen()
            passenger = authenticate()
            logger.info(f"{passenger.fullname} authenticated")
            manage_bank_account_menu(passenger)

        # trip management
        elif option == "3":

            clear_screen()
            passenger = authenticate()
            logger.info(f"{passenger.fullname} authenticated")
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
    logger.debug(f"fullname : {fullname}, phone_number : {phone_number}, email: {email}")

    try:

        passenger = Passenger(fullname, phone_number, email)
        clear_screen()
        print(passenger.register())

        logger.debug(f"{fullname} successfully registered")
        print("\nsuccessfully registered !")
        enter_key()

    except RegisterError as e:

        clear_screen()
        print(e)
        logger.error(f"failed to register , {e.msg} , {e.data} entered")
        enter_key()


def authenticate():
    """authenticate a passenger by unique_id"""
    try:

        unique_id = int(input("enter your unique id: "))
        logger.debug(f"{unique_id} entered for unique_id field")

        passenger = Passenger.authenticate(unique_id)
        return passenger

    except AuthenticationError as e:

        clear_screen()
        print(e)
        logger.error(f"{e.msg}, {e.reason}")
        enter_key()
        main_menu()

    except ValueError:

        clear_screen()
        print("All unique id characters must be integers !")
        logger.error(f"{e.msg}, {e.reason}")
        enter_key()
        main_menu()


def manage_bank_account_menu(passenger: Passenger):
    """management panel for bank account"""
    while True:

        clear_screen()
        manage_bank_account_menu_options()

        owner = passenger.bank_account.owner.fullname
        option = input(f"\n({owner}\'s account) >>> ")
        logger.debug(f"{passenger.fullname} entered {option}, manage_bank_account_menu")

        # deposit
        if option == "1":

            clear_screen()
            amount = input("enter your amount to deposit: ")
            logger.debug(f"{passenger.fullname} entered {amount}$ for deposit")

            try:

                passenger.bank_account.deposit(amount)
                logger.info(f"{passenger.fullname} deposit {amount}$ to his bank account successfully")
                print("deposit was successful !")
                enter_key()

            except BankAccountError as e:

                clear_screen()
                print(e)
                logger.error(f"{passenger.fullname} deposit failed due to {e.msg}")
                enter_key()

        # withdraw
        elif option == "2":

            clear_screen()
            amount = input("enter your amount to withdraw: ")
            logger.debug(f"{passenger.fullname} entered {amount}$ for withdraw")

            try:

                passenger.bank_account.withdraw(amount)
                logger.info(f"{passenger.fullname} withdraw {amount}$ of his bank account successfully")
                print("withdraw was successful !")
                enter_key()

            except BankAccountError as e:

                clear_screen()
                print(e)
                logger.error(f"{passenger.fullname} withdraw failed due to {e.msg}")
                enter_key()

        # get balance
        elif option == "3":

            clear_screen()
            print(passenger.bank_account.get_balance())
            logger.info(f"{passenger.fullname} get his bank account balance")
            enter_key()

        # Back to main menu
        elif option == "4":

            main_menu()

        else:

            wrong_option()
            logger.info(f"{passenger.fullname} enter wrong option, manage_bank_account_menu")


def trip_management_menu(passenger: Passenger):
    """trip management menu """
    while True:

        clear_screen()
        trip_management_menu_options()

        user = passenger.fullname
        option = input(f"\n(user: {user}) >>> ")
        logger.debug(f"{user} entered {option}, trip_management_menu")

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
                logger.error(f"{passenger.fullname} , {e} , for buy cards")
                enter_key()

        # back to main menu
        elif option == "3":

            main_menu()

        else:

            wrong_option()
            logger.error(f"{passenger.fullname} , entered wrong option , trip_management_menu")


def buy_cards_menu(passenger: Passenger):
    """buy cards menu"""
    while True:

        clear_screen()
        buy_cards_menu_options()
        option = input(">>> ")
        logger.debug(f"{passenger.fullname} entered {option} , buy_cards_menu")

        # buy Single Trip metro card for 1000
        if option == "1":

            card = SingleTrip(passenger)
            passenger.bank_account.withdraw(str(card.price))
            logger.debug(f"{passenger.fullname} withdraw {card.price}$ of his bank account")
            card.save_card()

            clear_screen()
            print("single trip card successfully purchased")
            logger.debug(f"{passenger.fullname} buy {card} successfully ")
            enter_key()

        # buy credit metro card for 5000
        elif option == "2":

            card = CreditCard(passenger)
            passenger.bank_account.withdraw(str(card.price))
            logger.debug(f"{passenger.fullname} withdraw {card.price}$ of his bank account")
            card.save_card()

            clear_screen()
            print("credit card successfully purchased")
            logger.debug(f"{passenger.fullname} buy {card} successfully ")
            enter_key()

        # buy time-credit metro card 6000
        elif option == "3":

            card = TimeCredit(passenger)
            passenger.bank_account.withdraw(str(card.price))
            logger.debug(f"{passenger.fullname} withdraw {card.price}$ of his bank account")
            card.save_card()

            clear_screen()
            print("time-credit card successfully purchased")
            logger.debug(f"{passenger.fullname} buy {card} successfully ")
            enter_key()

        # back to cards menu
        elif option == "4":

            trip_management_menu(passenger)

        else:

            wrong_option()
            logger.debug(f"{passenger.fullname} entered wrong option, buy_cards_menu")


def control_menu(admin: Admin):
    """admin control menu"""
    admin = admin

    while True:

        clear_screen()
        control_menu_options()

        option = input(f"\n(ADMIN: {admin.fullname}) >>> ")
        logger.debug(f"{admin.fullname} entered {option} , control_menu")

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
            admin_manage_trips(admin)

        # manage cards
        elif option == "4":

            clear_screen()
            admin_manage_cards(admin)
            enter_key()

        elif option == "5":

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
        logger.debug(f"{admin.fullname} logged in successfully")
        return admin

    except AuthenticationError as e:

        clear_screen()
        print(e)
        logger.debug(f"user failed to login due to {e}")
        enter_key()
        main_menu()

    except ValueError:

        clear_screen()
        print("All unique id characters must be integers !")
        logger.debug(f"user failed to login due to {e}")
        enter_key()
        main_menu()

    except Exception as e:

        print(e)
        logger.debug(f"user failed to login due to {e}")
        enter_key()
        main_menu()


def admin_register_trip(admin: Admin):
    """register trip and save it"""
    if not admin.load_users():

        print("there is no users yet to pass as traveler !")
        logger.info(f"{admin.fullname} get empty users list, admin_register_trip")
        enter_key()
        control_menu(admin)

    else:

        users = admin.load_users()
        logger.info(f"{admin.fullname} get {len(users)} users , admin_register_trip")

        print("__________________ REGISTER NEW TRIP __________________\n")

        users_name = list(map(lambda u: u.fullname, users))

        print("NOTE: ")
        print("\tSTATIONS : ", Trip.get_stations())
        print("\tUSERS : ", end=" ")

        for i, traveler in enumerate(users_name, 1):
            print(f"{i}. {traveler}", end=" ")

        print("\n", "_" * 80)

        try:

            origin = input("\norigin >>> ")
            destination = input("destination >>> ")
            traveler_num = int(input("traveler >>> "))
            logger.debug(f"{admin.fullname} entered:origin:{origin},destination:{destination},traveler:{traveler_num}")
            chosen = users[traveler_num - 1]

            new_trip = Trip(origin.upper(), destination.upper(), chosen)
            new_trip.save()
            print(f"trip registered successfully")
            logger.debug(f"{admin.fullname} registered a trip successfully, {trip}")

        except (ValueError, IndexError) as e:

            clear_screen()
            print("invalid option for traveler ! try again")
            logger.error(f"{admin.fullname} get error due to {e}")
            enter_key()
            admin_register_trip(admin)

        except Exception as e:  # TripError

            clear_screen()
            print(e)
            logger.error(f"{admin.fullname} get error due to {e}")
            enter_key()
            control_menu(admin)


def admin_manage_users(admin: Admin):
    """manage users section"""

    if not admin.load_users():

        print("there is no users yet")
        logger.info(f"{admin.fullname} get empty users list , admin_manage_users")
        enter_key()
        control_menu(admin)

    else:

        users = admin.load_users()
        logger.info(f"{admin.fullname} get {len(users)} users list , admin_manage_users")

        print("___________________________ USERS LIST ___________________________\n")

        for i, user in enumerate(users, 1):
            print(f" {i} : " + 60 * "_" + f"{user}")


def admin_manage_trips(admin: Admin):
    """manage trips"""

    if not admin.load_trips():

        clear_screen()
        print("there is no trips yet")
        enter_key()
        control_menu(admin)

    else:
        trips = admin.load_trips()
        clear_screen()
        print("__________________ MANAGE TRIPS __________________\n")

        print("Operations : ", "\t1. DELETE", "\t2. RE-VALUE", "\t3. BACK", sep="\n")
        opt = input("\nselect operations : ")

        # delete section
        if opt == "1":

            clear_screen()
            # trips list
            for i, trip in enumerate(trips, 1):
                print(f" {i}- {repr(trip)}")

            try:

                selected_trip = int(input("\nenter trip number to delete : "))
                if selected_trip <= 0:
                    raise IndexError("negative index")

                trips.pop(selected_trip - 1)
                Trip.trips = trips
                Trip.save()
                print("the trip removed !")
                enter_key()

            except (IndexError, ValueError):

                clear_screen()
                print("Invalid options !")
                enter_key()
                admin_manage_trips(admin)

        # re-value section
        elif opt == "2":

            clear_screen()
            # trips list
            for i, trip in enumerate(trips, 1):
                print(f" {i}- {repr(trip)}")

            users = admin.load_users()
            if not users:

                print("there is no user yet to pass as traveler !")
                enter_key()
                control_menu(admin)

            else:

                travelers_name = list(map(lambda u: u.fullname, users))

                print("\nNOTE: ")
                print("\tUSERS : ", end=" ")
                for i, traveler in enumerate(travelers_name, 1):
                    print(f"{i}.{traveler}", end="  ")

                print("\n\tSTATIONS: ", Trip.get_stations())

                try:

                    selected_trip = int(input("\nenter trip number to re-value : "))

                    if selected_trip <= 0:
                        raise IndexError("negative index")

                    origin = input("\tnew origin : ")
                    destination = input("\tnew destination : ")
                    chosen_traveler = int(input("\tnew traveler : "))

                    if chosen_traveler <= 0:
                        raise IndexError("negative index")

                    trips[selected_trip - 1] = Trip(origin.upper(), destination.upper(), users[chosen_traveler - 1])
                    Trip.trips = trips
                    Trip.save()

                    print("the trip revalued !")
                    enter_key()

                except (IndexError, ValueError):

                    clear_screen()
                    print("Invalid options !")
                    enter_key()
                    admin_manage_trips(admin)

                except Exception as e:  # TripError

                    clear_screen()
                    print(e)
                    enter_key()
                    admin_manage_trips(admin)

        elif opt == "3":

            control_menu(admin)

        else:

            clear_screen()
            print("wrong option!")
            enter_key()
            control_menu(admin)


def admin_manage_cards(admin: Admin):
    """load cards section"""
    if not admin.load_cards():

        print("There is no cards yet !!!")
        enter_key()
        control_menu(admin)

    else:

        cards = admin.load_cards()
        print("___________________________ CARDS LIST ___________________________\n")

        for i, card in enumerate(cards, 1):
            print(f" {i}. {repr(card)}")
