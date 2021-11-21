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
    """prints trip management menu options optioans"""
    print("_____________________ TRIP MANAGEMENT MENU _____________________\n")
    print("\t1. register new trip")
    print("\t2. buy new card")
    print("\t3. back to main menu")


def buy_cards_menu_options():
    """prints buy cards menu options optioans"""

    print("_____________________ BUY CARDS MENU _____________________\n")
    print("\t1. Single Trip card - price: 1000$")
    print("\t2. credit card - price: 5000$, initial credit: 3000$")
    print("\t3. time-credit card - price: 6000$,  initial credit: 6000$, duration: 5 days")
    print("\t4. back to cards menu")


def any_key():
    key = input("\npress any key to continue...")


def wrong_option():
    """wrong option for menus"""
    clear_screen()
    print("wrong option, try again")
    any_key()
