import os
import time


def clear_screen(delay=None):
    """clear the screen in gnu/linux and Microsoft wimdows"""
    if delay:
        time.sleep(delay)

    if os.name == "posix":
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")


def main_menu_options():
    """prints main menu options"""
    print("_____________________ MAIN MENU _____________________\n")
    print("\t1. register new Passenger")
    print("\t2. manage bank account")
    print("\t3. trip management")
    print("\t4. admin panel")
    print("\t5. exit")


def manage_bank_account_menu_options():
    """prints bank account menu optioans"""
    print("_____________________ BANK ACCOUNT MANAGEMENT _____________________\n")
    print("\t1. deposit")
    print("\t2. withdraw")
    print("\t3. show account balance")
    print("\t4. Back to main menu")


def trip_management_menu_options():
    print("_____________________ TRIP MANAGEMENT MENU _____________________\n")
    print("\t1. register new trip")
    print("\t2. buy new card")
    print("\t3. back to main menu")


def any_key():
    key = input("\npress any key to continue...")
