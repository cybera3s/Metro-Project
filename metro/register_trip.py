from utils import enter_key, clear_screen
from models import *
from metro.menus import trip_management_menu
from metro.exceptions import TripError


def register_trip(passenger):
    """register trip section"""

    # list cards section

    # if passenger has no cards
    if not passenger.list_cards():

        print("There is no card to show, Buy first")
        enter_key()

    else:

        my_cards = passenger.list_cards()

        print("__________________ CARDS LIST __________________\n")
        for i, c in enumerate(my_cards, 1):
            print(f"\t{i}: {c}")

        try:

            card = int(input("\nselect your desired card: "))

            if card <= 0 or my_cards[card - 1] not in my_cards:
                raise IndexError()

            selected_card = my_cards[card - 1]
            clear_screen()
            print(selected_card, "selected")
            clear_screen(1)
            # use different cards
            if isinstance(selected_card, SingleTrip):
                selected_card.use_card()  # just delete it from card list

            else:
                selected_card.use_card(Trip.PRICE)
                print(selected_card)

            print("Pay successfully...")
            clear_screen(1.5)

        except (IndexError, ValueError):

            clear_screen()
            print("invalid option, try again")
            enter_key()
            trip_management_menu(passenger)

        except MetroCardError as e:

            clear_screen()
            print(e)
            enter_key()
            trip_management_menu(passenger)

        while True:

            clear_screen()
            print("Available stations: ", Trip.get_stations())

            origin = input("\torigin station: ")
            destination = input("\tdestination station: ")

            try:

                clear_screen()
                trip = Trip(origin.upper(), destination.upper(), passenger)
                trip.progress()
                clear_screen()
                print("trip successfully done !!!")
                trip.save()
                print("__________________ TRIP INFO __________________", trip, sep="\n")
                enter_key()
                trip_management_menu(passenger)

            except TripError as e:

                clear_screen()
                print(e)
                enter_key()
