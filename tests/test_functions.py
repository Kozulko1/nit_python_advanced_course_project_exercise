import unittest

from unittest.mock import MagicMock, patch

from user_manager import User, UserStorage, print_contacts


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.logged_user = User("Valentino", "123")
        self.other_user = User("Budlak", "123")
        self.user_storage = UserStorage()
        self.user_storage.log_in(self.logged_user)
