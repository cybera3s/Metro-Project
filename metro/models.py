import os
import pickle
import random
import re

from metro.exceptions import RegisterError, LoginError


class MetroCard:
    """base metro card class"""
    pass


class SingleTrip(MetroCard):
    """Metro Single Trip card class"""
    pass


class CreditCard(MetroCard):
    """Metro Credit Card class"""
    pass


class TimeCredit(MetroCard):
    """Metro time credit card class"""
    pass


class Trip:
    """Trip class"""
    pass


class BankAccount:
    """Bank Account for every Passenger"""
    pass


class Passenger:
    """Passenger class"""
    users = None

    def __init__(self, fullname: str, phone: str, email: str = None):
        """get user info"""
        self.__check_user_data(fullname, phone, email)

        self.__unique_id = self.__generate_unique_id()
        self.fullname = fullname
        self.phone = phone
        self.email = email

        Passenger.users = Passenger.__check_create_user_db()
        Passenger.users[self.__unique_id] = {"fullname": self.fullname, "phone": self.phone, "email": self.email,
                                             "obj": self}

    @staticmethod
    def __generate_unique_id(self) -> int:
        """generate a random number more than 6 digits"""
        unique_id = random.randrange(100000, 10 ** 10)
        return unique_id

    @classmethod
    def __check_create_user_db(cls):

        if os.path.exists('users/users.pk'):

            with open('users/users.pk', 'rb') as f:
                cls.users = pickle.load(f)
        else:
            cls.users = {}

        return cls.users

    @staticmethod
    def __check_user_data(fullname: str, password: str, phone: str, email: str):

        if not fullname.isalpha():
            raise RegisterError("invalid name", "fullname", fullname)

        if len(password) < 4:
            raise RegisterError("Invalid Password: must be more than 4 characters", "password", password)

        if not phone.startswith('09'):
            raise RegisterError("must start with 09...", "phone", phone)

        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        if not re.match(email_regex, email):
            raise RegisterError("Invalid email format", "email", email)

    def register(self):
        """save Passenger obj to users file"""

        with open("users/users.pk", "wb") as f:
            pickle.dump(self, f)
        return self

    @classmethod
    def login(cls, unique_id):

        pass

    def __str__(self):
        msg = f"unique_id:{self.__unique_id}\nfullname:{self.fullname}\nphone:{self.phone}\nemail:{self.email}"
        return msg
