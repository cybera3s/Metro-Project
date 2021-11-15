from models import Passenger
from exceptions import RegisterError, AuthenticationError


def main_menu():
    """main menu function"""
    while True:
        print("1. register new Passenger")
        print("2. manage bank account")
        print("3. register new trip")
        print("4. admin panel")
        print("5. exit")

        option = input(">>> ")

        if option == "1":

            register_menu()

        elif option == "2":

            unique_id = int(input("enter your unique id: "))
            manage_bank_account_menu(authenticate(unique_id))

        elif option == "3":

            # todo: new trip
            pass

        elif option == "4":

            # todo: admin panel section
            pass

        elif option == "5":

            # todo: exit
            exit()

        else:
            print("wrong option, try again")


def register_menu():
    """register new Passenger"""
    fullname = input("enter your fullname : ")
    phone_number = input("enter your phone number : ")
    email = input("enter your email(optional): ")

    try:
        passenger = Passenger(fullname, phone_number, email)
        print(passenger.register())
    except RegisterError as e:
        print(e)


def authenticate(unique_id):
    """authenticate a passenger by unique_id"""

    try:
        return Passenger.authenticate(unique_id)

    except AuthenticationError as e:
        print(e)


def manage_bank_account_menu(passenger):
    """management panel for bank account"""
    while True:
        print("1. deposit")
        print("2. withdraw")
        print("3. show account balance")
        print("4. Back to main menu")

        option = input("enter your option: ")

        if option == "1":

            amount = int(input("enter your amount to deposit: "))
            passenger.bank_account.deposit(amount)

        elif option == "2":

            amount = input("enter your amount to deposit: ")
            passenger.bank_account.withdraw(int(amount))

        elif option == "3":

            print(passenger.bank_account.get_balance())

        elif option == "4":

            main_menu()

        else:

            print("wrong option, try again")
