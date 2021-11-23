from utils import enter_key, clear_screen
from models import *
import menus
from exceptions import TripError
from logger import Logger

Logger.set_logger(__name__)
logger = Logger.logger


def register_trip(passenger: Passenger):
    """register trip section"""

    # if passenger has no cards
    if not passenger.list_cards():

        print("There is no card to show, Buy first")
        logger.info(f"{passenger.fullname} has no card")
        enter_key()

    else:

        my_cards = passenger.list_cards()
        logger.debug(f"{passenger.fullname} has {len(my_cards)} cards")

        print("__________________ CARDS LIST __________________\n")
        for i, c in enumerate(my_cards, 1):
            print(f"\t{i}: {c}")

        try:

            card = int(input("\nselect your desired card: "))
            logger.debug(f"{passenger.fullname} entered {card} to select card")

            if card <= 0 or my_cards[card - 1] not in my_cards:
                raise IndexError()

            selected_card = my_cards[card - 1]
            clear_screen()
            print(selected_card, "selected")
            logger.info(f"{passenger.fullname} select {selected_card}")
            clear_screen(1)

            # use different cards
            if isinstance(selected_card, SingleTrip):

                selected_card.use_card()  # just delete it from card list
                logger.info(f"{passenger.fullname} used {selected_card}, has been deleted from list")

            else:

                selected_card.use_card(Trip.PRICE)
                print(selected_card)
                logger.info(f"{passenger.fullname} used {selected_card},Travel price were deducted of {selected_card}")

            print("Paid successfully...")
            logger.info(f"{passenger.fullname} paid successfully")
            clear_screen(1.5)

        except (IndexError, ValueError) as e:

            clear_screen()
            print("invalid option, try again")
            logger.error(f"{passenger.fullname} entered wrong option , {e}")
            enter_key()
            menus.trip_management_menu(passenger)

        except MetroCardError as e:

            clear_screen()
            print(e)
            logger.error(f"{passenger.fullname} , {e.reason} ,{e.msg}")
            enter_key()
            menus.trip_management_menu(passenger)

        while True:

            clear_screen()
            print("Available stations: ", Trip.get_stations())

            origin = input("\torigin station: ")
            destination = input("\tdestination station: ")
            logger.debug(f"{passenger.fullname} entered origin:{origin}, destination: {destination}")

            try:

                clear_screen()
                trip = Trip(origin.upper(), destination.upper(), passenger)
                trip.progress()
                clear_screen()
                print("trip successfully done !!!")
                logger.debug(f"{passenger.fullname} trip successfully done , {repr(trip)}")

                trip.save()
                logger.debug(f"{repr(trip)} was saved")
                print("__________________ TRIP INFO __________________", trip, sep="\n")
                enter_key()
                menus.trip_management_menu(passenger)

            except TripError as e:

                clear_screen()
                print(e)
                logger.error(f"{passenger.fullname} , {e}")
                enter_key()
