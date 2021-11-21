import os
import pickle
import re
from abc import ABC, abstractmethod
from metro.exceptions import RegisterError, AuthenticationError, BankAccountError, TripError, MetroCardError
from datetime import datetime, timedelta
import time


class Passenger:
    """Passenger class"""
    users = None

    def __init__(self, fullname: str, phone: str, email: str = None):
        """get user info and check them finally add them end of users list"""
        self.__check_user_data(fullname, phone, email)
        self.bank_account = BankAccount(self)
        self.__unique_id = int(str(id(self))[4:])  # Use obj id number from index four to last -> int
        self.fullname = fullname
        self.phone = phone
        self.email = email

    def _get_unique_id(self):
        return self.__unique_id

    @classmethod
    def _check_create_user_db(cls):
        """checks if users.pk file exists then assign it to users list
         otherwise users list is a empty list
         return users"""
        if os.path.exists('users/users.pk'):

            cls.users = cls.load_data()
        else:
            cls.users = []

        return cls.users

    @staticmethod
    def __check_user_data(fullname: str, phone: str, email: str):
        """checks user data and raise registerError"""
        fullname_regex = r"^([a-zA-Z]+)\s{1}([a-zA-Z]+)$"
        if not re.match(fullname_regex, fullname):
            msg = "fullname must contain only letters and one space between first name and last name e.g:Sajad Safa"
            raise RegisterError(msg, "fullname", fullname)

        if not phone.startswith('09') or not len(phone) == 11:
            raise RegisterError("must start with 09...", "phone", phone)

        if email:

            email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            if not re.match(email_regex, email):
                raise RegisterError("Invalid email format", "email", email)

    def register(self):
        """checks passenger data then returns corresponding user"""
        Passenger.users = self._check_create_user_db()
        Passenger.users.append(self)
        self.save_data()
        return self

    @classmethod
    def load_data(cls):
        """load users data of file"""
        with open("users/users.pk", "rb") as f:
            return pickle.load(f)

    @classmethod
    def save_data(cls):
        """save Passenger users list to file"""
        with open("users/users.pk", 'wb') as f:
            pickle.dump(cls.users, f)

    @classmethod
    def authenticate(cls, unique_id: int):
        """authenticates a Passenger by unique_id"""
        if not cls._check_create_user_db():
            raise AuthenticationError('No file', "Passenger Doesn't exist")

        cls.users = cls.load_data()
        users_id = list(map(lambda p: p.__unique_id, cls.users))

        if unique_id not in users_id:
            raise AuthenticationError('authentication', "wrong unique id, Passenger Doesn't exist")

        index = users_id.index(unique_id)  # index of items will not change after applying map function to the list
        return cls.users[index]

    def list_cards(self):
        if os.path.exists('cards/cards.pk'):
            with open("cards/cards.pk", 'rb') as f:
                cards = pickle.load(f)
                my_cards = list(filter(lambda c: c.owner.__unique_id == self.__unique_id, cards))

                if my_cards:
                    return my_cards
                else:
                    return False
        else:
            return False

    def __str__(self):
        msg = f"""
    unique_id: {self.__unique_id}
    fullname: {self.fullname}
    phone: {self.phone}
    email: {self.email}
    Bank Account: \n{self.bank_account}"""

        return msg


class Admin(Passenger):
    """represent admin user"""

    is_admin = True

    def __init__(self, fullname, password):
        super().__init__(fullname, "09123456789")
        self.fullname = fullname
        self.__password = password

    def _get_password(self):
        """return user password"""
        return self.__password

    @classmethod
    def login(cls, unique_id, password):
        """login admin with password and unique id and returns that user"""
        user = cls.authenticate(unique_id)
        if not user:
            raise AuthenticationError("authentication", "this admin user doesn't exists")
        if user.__password != password:
            raise AuthenticationError("password", "password is incorrect !")

        return user

    def __str__(self):
        return f"\n\tadmin: {self.is_admin}" + super().__str__()


class MetroCard(ABC):
    """base metro card class"""
    cards = None

    def __init__(self, price: int, owner: Passenger):
        self.price = price
        self.owner = owner
        self.serial_number = int(str(id(self))[4:])

    @staticmethod
    def load_cards():
        """load list cards"""
        if os.path.exists('cards/cards.pk'):
            with open("cards/cards.pk", "rb") as f:
                cards = pickle.load(f)
        else:
            cards = []

        return cards

    def save_card(self):
        """save cards list to file"""
        MetroCard.cards = self.load_cards()
        cards_serial_number = list(map(lambda c: c.serial_number, MetroCard.cards))

        if self.serial_number in cards_serial_number:  # checks if card is already exists then changes it

            index = cards_serial_number.index(self.serial_number)

            if isinstance(self, SingleTrip):
                MetroCard.cards.pop(index)
            else:
                MetroCard.cards[index] = self

        else:

            MetroCard.cards.append(self)

        with open("cards/cards.pk", "wb") as f:
            pickle.dump(MetroCard.cards, f)

    @abstractmethod
    def __str__(self):
        pass


class SingleTrip(MetroCard):
    """Metro Single Trip card class"""

    def __init__(self, owner: Passenger, price: int = 1000):
        super().__init__(price, owner)

    def use_card(self):
        self.save_card()

    def __str__(self):
        return f"Single trip"


class CreditCard(MetroCard):
    """Metro Credit Card class"""

    def __init__(self, owner: Passenger, balance: int = 3000, price: int = 5000):
        super().__init__(price, owner)
        self.balance = balance

    def use_card(self, price):
        if (self.balance - price) < 0:
            raise MetroCardError("balance", "not enough balance!")
        self.balance -= price
        self.save_card()

    def __str__(self):
        return f"credit card (balance: {self.balance})"


class TimeCredit(MetroCard):
    """Metro time credit card class"""
    DURABILITY: int = 5

    def __init__(self, owner: Passenger, balance: int = 6000, price: int = 6000):
        super().__init__(price, owner)
        self.balance = balance
        self.manufacture_date = datetime.now()
        self.expire_date = datetime.now() + timedelta(days=TimeCredit.DURABILITY)
        self.remaining_time = self.expire_date - self.manufacture_date

    def use_card(self, price):
        if self.expire_date != datetime.now():
            if (self.balance - price) < 0:
                raise MetroCardError("balance", "not enough balance!")
            self.balance -= price
            self.save_card()
        else:
            raise MetroCardError("expire_date", "the card is expired!")

    def __str__(self):
        return f"time-credit (balance: {self.balance} ,{self.remaining_time.days}days to expire)"


class Trip:
    """Trip class"""
    PRICE: int = 1500
    STATIONS = ["A", "B", "C", "D", "E", "F"]

    def __init__(self, origin, destination):

        self.__check_data(origin, destination)
        self.origin = origin
        self.destination = destination

        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(seconds=self.duration())

    @staticmethod
    def __check_data(origin: str, destination: str):

        if origin not in Trip.STATIONS:
            raise TripError("origin", f"there is no '{origin}' station ")

        if destination not in Trip.STATIONS:
            raise TripError("destination", f"there is no '{destination}' station ")

    def duration(self):
        """get trip duration"""
        distance = abs(Trip.STATIONS.index(self.destination) - Trip.STATIONS.index(self.origin))
        return distance * 5  # The time to reach each station is 5 seconds

    @classmethod
    def get_stations(cls):
        """get stations"""
        return ", ".join(cls.STATIONS)

    def progress(self):
        origin = self.origin
        destination = self.destination

        print(f"{origin}:", end=" ")
        for s in range(self.duration()):
            print(">", end=" ")
            time.sleep(1)
        print(f": {destination}")

    def __str__(self):
        msg = f"""origin: {self.origin}
destination: {self.destination}
start time: {self.start_time}
end time: {self.end_time}
duration: {self.duration()} seconds"""
        return msg


class BankAccount:
    """Bank Account for every Passenger"""

    def __init__(self, owner: Passenger, initial_balance: int = 0) -> None:
        self.owner = owner
        self.__balance = initial_balance

    def withdraw(self, amount: str):
        """If the amount is valid and does not make the account balance less than zero,
         it will be deducted from the account balance, otherwise it will return an error."""

        if not amount.isdigit() or int(amount) <= 0:
            raise BankAccountError("withdraw", "withdraw amount must be a number and greater than zero!")

        if (self.__balance - int(amount)) <= 0:
            raise BankAccountError("withdraw", "NOT Enough balance to withdraw!")

        self.__balance -= int(amount)
        self.owner.save_data()

    def deposit(self, amount: str):
        """If the input amount is valid, adds
        it to the account balance then saves it
         , otherwise it returns an error."""

        if not amount.isdigit() or int(amount) <= 0:
            raise BankAccountError("deposit", "deposit amount must be a number and greater than zero!")

        self.__balance += int(amount)
        self.owner.save_data()

    def get_balance(self):
        return f"your balance : {self.__balance}"

    def __str__(self):
        msg = f"""\towner: {self.owner.fullname}\n\tbalance: {self.__balance}"""
        return msg
