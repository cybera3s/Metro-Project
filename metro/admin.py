import sys
from models import Admin
from utils import *
from exceptions import RegisterError
from logger import Logger

Logger.set_logger(__name__)
logger = Logger.logger


def create_super_user():
    """register a new admin"""

    if sys.argv[1] == "createsuperuser":
        clear_screen()
        print("__________________ CREATE ADMIN USER__________________\n")

        fullname = input("enter your fullname: ")
        phone_number = input("enter your phone: ")
        password = input("enter your password: ")
        logger.info(f"fullname: {fullname},phone_number:{phone_number},passenger:{password} entered at createsuperuser")

        try:

            admin = Admin(fullname, phone_number, password)
            clear_screen()
            print(admin.register())
            logger.info(f"{fullname} admin successfully registered")
            print("\nsuccessfully registered !")
            enter_key()

        except RegisterError as e:

            clear_screen()
            print(e)
            logger.error(f"admin failed to register : {e}")
            enter_key()

    else:

        clear_screen()
        print("wrong PARAMETER !")


create_super_user()
