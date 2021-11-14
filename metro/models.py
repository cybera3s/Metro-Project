import os
import pickle
import re

from metro.exceptions import RegisterError, LoginError, BankAccountError


class MetroCard:
    """base metro card class"""

    # todo: init >> balance >> expire >> price >> owner
    # todo: method >> save to cards.pk
    def __init__(self, price: int, owner, balance: int = 5000):
        self.balance = balance
        self.price = price
        self.owner = owner


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
        # todo : empty list of metro cards
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
    def login(cls, unique_id: int):
        with open("users/users.pk", "rb") as f:
            cls.users = pickle.load(f)

        users_id = list(map(lambda p: p.__unique_id, cls.users))
        if unique_id not in users_id:
            raise LoginError('Passenger', "Passenger Doesn't exist")

        index = users_id.index(unique_id)    # index of items will not change after applying map function to the list
        return cls.users[index]

    def __str__(self):
        msg = f"""
        unique_id:{self.__unique_id}
        fullname:{self.fullname}
        phone:{self.phone}
        email:{self.email}
        Bank Account: {self.bank_account}
        """
        return msg


class BankAccount:
    """Bank Account for every Passenger"""

    def __init__(self, owner: Passenger, initial_balance: int = 0) -> None:
        self.__owner = owner
        self.__balance = initial_balance

    def withdraw(self, amount):
        """Subtracts the amount from the account balance
         if balance minus the amount is not less than zero
         otherwise raises Error"""
        if (self.__balance - amount) <= 0:
            raise BankAccountError("withdraw", "NOT Enough balance to withdraw!")

        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        msg = f"""owner:{self.__owner.fullname}, balance:{self.__balance}"""
        return msg
