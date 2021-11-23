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