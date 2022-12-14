import unittest

from unittest.mock import MagicMock, patch

from user_manager import User, UserStorage, print_contacts


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.logged_user = User("Valentino", "123")
        self.other_user = User("Budlak", "123")
        self.logged_user.contacts = self.other_user
        self.user_storage = UserStorage()
        self.user_storage.log_in(self.logged_user)

    @patch("user_manager.scripts.functions.print")
    @patch("user_manager.scripts.functions.logging.error")
    def test__print_contacts(self, mock_logerror: MagicMock, mock_print: MagicMock):
        print_contacts(self.logged_user, self.user_storage)
        mock_print.assert_called_once_with("Username: Budlak")

        print_contacts(self.other_user, self.user_storage)
        mock_logerror.assert_called_once_with("Budlak is not logged in.")
