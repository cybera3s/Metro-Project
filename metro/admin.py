import sys
from models import Admin
from utils import *
from exceptions import RegisterError


def create_super_user():
    """register a new admin"""

    if sys.argv[1] == "createsuperuser":
        clear_screen()
        print("__________________ CREATE ADMIN USER__________________\n")

        fullname = input("enter your fullname: ")
        phone_number = input("enter your phone: ")
        password = input("enter your password: ")

        try:

            admin = Admin(fullname, phone_number, password)
            clear_screen()
            print(admin.register())

            print("\nsuccessfully registered !")
            enter_key()

        except RegisterError as e:

            clear_screen()
            print(e)
            enter_key()

    else:

        clear_screen()
        print("wrong PARAMETER !")


create_super_user()
