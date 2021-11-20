import os


def clear_screen():
    """clear the screen in gnu/linux and Microsoft wimdows"""
    if os.name == "posix":
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")