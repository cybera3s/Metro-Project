from models import Passenger
from exceptions import RegisterError


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
            # todo: manage bank account
            pass
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


main_menu()
