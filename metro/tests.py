from models import *
from exceptions import *
import unittest


class TestPassenger(unittest.TestCase):
    """test class for Passenger model"""

    def setUp(self) -> None:
        self.p1 = Passenger("sajad safa", "09224023292", "cybera.3s@gmail.com")

    def test1_fullname_fail(self):
        self.assertRaises(RegisterError, Passenger, "sajadsafa", "09224023292", "cybera.3s@gmail.com")

    def test2_phoneNumber_fail(self):
        self.assertRaises(RegisterError, Passenger, "sajad safa", "0922402", "cybera.3s@gmail.com")

    def test3_email_fail(self):
        self.assertRaises(RegisterError, Passenger, "sajad safa", "09224023292", "cybera.3sgmail.com")

    def test4_obj_success(self):
        self.assertTrue(self.p1)

    def test_authenticate_fail(self):
        self.assertRaises(AuthenticationError, Passenger.authenticate, 123456789)


class TestAdmin(unittest.TestCase):
    """test class for Admin model"""

    def setUp(self) -> None:
        self.admin = Admin("sajad safa", "09224023292", "123456789")

    def test_passwords_fail(self):
        self.assertRaises(RegisterError, Admin, "sajad safa", "09224023292", "1")
        self.assertRaises(RegisterError, Admin, "sajad safa", "09224023292", "as")
        self.assertRaises(RegisterError, Admin, "sajad safa", "09224023292", "")

    def test_obj_success(self):
        self.assertTrue(self.admin)

    def test1_login_fail(self):
        self.assertRaises(AuthenticationError, Admin.login, 123, "321645")

    def test2_login_fail(self):
        self.assertRaises(AuthenticationError, Admin.login, 123, "")


class TestMetroCard(unittest.TestCase):
    """test class for MetroCard"""

    def test_load_cards(self):
        self.assertIsInstance(MetroCard.load_cards(), list)


class TestCreditCard(unittest.TestCase):
    """test CreditCard class"""

    def setUp(self):
        p = Passenger("sajad safa", "09123456789")
        card = CreditCard(p, )
