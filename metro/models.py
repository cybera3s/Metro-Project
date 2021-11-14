import pickle


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

    def __init__(self, id, fullname: str, phone: str, password: str, email: str = None):
        """get user info"""
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.password = password
        self.email = email

    @classmethod
    def __check_create_user_db(cls):

        if os.path.exists('users/users.pk'):

            with open('users/users.pk', 'rb') as f:
                cls.users = pickle.load(f)
        else:
            cls.users = {}

        return cls.users

    def register(self):
        """save Passenger obj to users file"""

        with open("users/users.pk", "wb") as f:
            pickle.dump(self, f)
        return self

    @classmethod
    def login(cls, username: str, password: str):
        if os.path.exists('users/users.db'):
            with open('users/users.db', 'rb') as f:
                data = pickle.load(f)
        else:
            raise LoginError('Username', "Username Doesn't exist")

        if username not in data:
            raise LoginError('Username', "Username Doesn't exist")

        if data[username]['password'] != password:
            raise LoginError("Password", "Entered password doesn't match")

        return data[username]['obj']

    def __str__(self):
        msg = f"id:{self.id}\nfullname:{self.fullname}\nphone:{self.phone}\nemail:{self.email}"
        return msg
