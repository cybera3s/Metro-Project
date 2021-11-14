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

    def __init__(self, id, fullname: str, phone: str, password: str, email: str = None):
        """get user info"""
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.password = password
        self.email = email
