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