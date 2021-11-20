from utils import any_key, clear_screen
from models import *
from menus import trip_management_menu


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

            clear_screen()
            print(selected_card, "selected")

            if isinstance(selected_card, SingleTrip):

                selected_card.use_card()

            else:

                selected_card.use_card(Trip.PRICE)

            print("Pay successfully")

        except (IndexError, TypeError):

            print("invalid option, try again")
            trip_management_menu(passenger)

        except MetroCardError as e:
            print(e)
            trip_management_menu(passenger)

        clear_screen()
        print("Available stations")
        print(Trip.get_stations())

        origin = input("enter origin station: ")
        destination = input("enter destination station: ")

        try:

            trip = Trip(origin, destination)
            print(trip)
            trip.progress()
            print("trip successfully done")

        except TripError as e:
            print(e)
