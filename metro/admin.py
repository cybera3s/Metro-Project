import sys
from models import *
from utils import *


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


