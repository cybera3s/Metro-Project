from utils import any_key, clear_screen
from models import *
from metro.menus import trip_management_menu
from metro.exceptions import TripError


def register_trip(passenger):
    """register trip section"""

    # if passenger has no cards
    if not passenger.list_cards():

        print("There is no card to show, Buy first")
        any_key()
    else:

        my_cards = passenger.list_cards()

        print("Cards List")
        for i, c in enumerate(my_cards, 1):
            print(f"{i}: {c}")

        try:

            card = int(input("\nselect your desired card: "))

            if card <= 0 or my_cards[card - 1] not in my_cards:
                raise IndexError()

            selected_card = my_cards[int(card) - 1]

            print(selected_card, "selected")
            clear_screen(1.5)

            if isinstance(selected_card, SingleTrip):

                selected_card.use_card()

            else:

                selected_card.use_card(Trip.PRICE)

            print("Pay successfully")

        except (IndexError, TypeError):

            clear_screen()
            print("invalid option, try again")
            any_key()
            trip_management_menu(passenger)

        except MetroCardError as e:

            clear_screen()
            print(e)
            any_key()
            trip_management_menu(passenger)

        clear_screen(1.5)
        print("Available stations")
        print(Trip.get_stations())

        while True:
            origin = input("origin station: ")
            destination = input("destination station: ")

            try:

                trip = Trip(origin, destination)
                print(trip)
                trip.progress()
                print("trip successfully done")

            except TripError as e:

                clear_screen()
                print(e)
                any_key()
