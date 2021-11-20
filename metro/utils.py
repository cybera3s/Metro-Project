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
