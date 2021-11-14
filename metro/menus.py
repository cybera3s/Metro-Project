def main_menu():
    """main menu function"""
    while True:
        print("1. register new user")
        print("2. manage bank account")
        print("3. register new trip")
        print("4. admin panel")
        print("5. exit")

        option = input(">>> ")

        if option == "1":
            # todo: user register
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
