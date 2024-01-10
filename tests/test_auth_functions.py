# test authorization
import unittest
from helpers import validate_user_login, user_authentication


config = configparser.ConfigParser()
config.read("config.ini")

# Configure JWT settings
SECRET_KEY = config["misc-keys"]["secret-jwt"]
ALGORITHM = config["misc-keys"]["algorithm"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(config["misc-keys"]["access-token-expiration"])


class UserAuthenticationTest(unittest.TestCase):
    def testValidateUserLogin(self):
        result = validate_user_login("admin", "admin")
        result2 = user_authentication(result.access_token)
        self.assertEqual(result2.username, "admin")


