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
        self.__check_user_data(fullname, username, password, phone, email)

        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.password = password
        self.email = email

        Passenger.users = User.__check_create_user_db()
        Passenger.users[self.id] = {"fullname": self.fullname, "email": self.email, "password": self.password,
                                    "obj": self}

    @classmethod
    def __check_create_user_db(cls):

        if os.path.exists('users/users.pk'):

            with open('users/users.pk', 'rb') as f:
                cls.users = pickle.load(f)
        else:
            cls.users = {}

        return cls.users

    @staticmethod
    def __check_user_data(fullname: str, username: str, password: str, phone: str, email: str):

        if not fullname.isalpha():
            raise RegisterError("invalid name", "fullname", fullname)

        if not username.lower() and not username.isalnum():
            msg = "Invalid username: username must be in lower case and contain only numbers and letters"
            raise RegisterError(msg, "username", username)

        if len(password) < 8:
            raise RegisterError("Invalid Password: must be more than 8 characters", "password", password)

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
