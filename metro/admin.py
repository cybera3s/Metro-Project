import sys
from models import Admin
from utils import *
from exceptions import RegisterError


def create_super_user():
    """register a new admin"""
    if sys.argv[1] == "createsuperuser":
        print("__________________ CREATE ADMIN USER__________________\n")

        fullname = input("enter your fullname: ")
        password = input("enter your password: ")

        try:

            admin = Admin(fullname, password)
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
