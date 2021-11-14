from models import Passenger
from exceptions import RegisterError, LoginError


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
            pass
        elif option == "2":
            login_menu()
        elif option == "3":
            # todo: new trip
            pass
        elif option == "4":
            # todo: admin panel section
            pass
        elif option == "5":
            # todo: exit
            break
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


def login_menu():
    """login menu passenger"""
    unique_id = int(input("enter your unique id: "))
    try:
        Passenger.login(unique_id)
    except LoginError as e:
        print(e)


def manage_bank_account_menu():
    """management panel for bank account"""
    while True:
        print("1. deposit")
        print("2. withdraw")
        print("3. show account balance")
        print("4. Back to main menu")

        option = input("enter your option: ")

        if option == "1":
            pass
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            main_menu()
        else:
            print("wrong option, try again")
            break
