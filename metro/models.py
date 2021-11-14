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
        """get user info and check them finally add them end of users list"""
        self.__check_user_data(fullname, phone, email)

        self.__unique_id = int(str(id(self))[4:])  # Use obj id number from index four to last -> int
        self.fullname = fullname
        self.phone = phone
        self.email = email

        Passenger.users = Passenger.__check_create_user_db()
        Passenger.users.append(self)

    @classmethod
    def __check_create_user_db(cls):
        """checks if users.pk file exists then assign it to users list
         otherwise users list is a empty list
         return users"""
        if os.path.exists('users/users.pk'):

            with open('users/users.pk', 'rb') as f:
                cls.users = pickle.load(f)
        else:
            cls.users = []

        return cls.users

    @staticmethod
    def __check_user_data(fullname: str, phone: str, email: str):
        """checks user data and raise registerError"""
        if not fullname.isalpha():
            raise RegisterError("invalid name", "fullname", fullname)

        if not phone.startswith('09'):
            raise RegisterError("must start with 09...", "phone", phone)

        if email:

            email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            if not re.match(email_regex, email):
                raise RegisterError("Invalid email format", "email", email)

    def register(self):
        """save Passenger obj to users.pk file"""

        with open("users/users.pk", "wb") as f:
            pickle.dump(Passenger.users, f)
        return self

    @classmethod
    def login(cls, unique_id):

        pass

    def __str__(self):
        msg = f"unique_id:{self.__unique_id}\nfullname:{self.fullname}\nphone:{self.phone}\nemail:{self.email}"
        return msg
