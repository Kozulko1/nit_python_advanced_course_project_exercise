import unittest

from unittest.mock import MagicMock, patch

from user_manager import (
    User,
    UserStorage,
    print_contacts,
    register,
    add_contact,
    remove_contact,
    login_process,
    login,
    logout,
)
from hash_module import hash_password


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.logged_user = User("Valentino", hash_password("123"))
        self.other_user = User("Budlak", hash_password("123"))
        self.logged_user.contacts = self.other_user
        self.user_storage = UserStorage()
        self.user_storage.add_to_registered(self.logged_user)
        self.user_storage.add_to_registered(self.other_user)
        self.user_storage.log_in(self.logged_user)

    @patch("user_manager.scripts.functions.logging.error")
    def test__register__when_user_not_registered__expect_no_logging(
        self, mock_logging_error: MagicMock
    ):
        register("USERNAME", "12345678", self.user_storage)
        mock_logging_error.assert_not_called()

    @patch("user_manager.scripts.functions.logging.error")
    def test__register__when_user_registered__expect_logging_error(
        self, mock_logging_error: MagicMock
    ):
        register(self.logged_user.username, "12345678", self.user_storage)
        mock_logging_error.assert_called_once_with("Already registered")

    @patch("user_manager.scripts.functions.logging.error")
    @patch("user_manager.scripts.functions.Process")
    def test__login__when_registered_and_password_matches__expect_no_logging_error(
        self, mock_process: MagicMock, mock_logging_error: MagicMock
    ):
        login(
            self.other_user.username,
            hash_password(self.other_user.password),
            self.user_storage,
        )
        mock_logging_error.assert_not_called()
        mock_process.assert_called_once()

    @patch("user_manager.scripts.functions.logging.error")
    @patch("user_manager.scripts.functions.Process")
    def test__login__when_not_registered__expect_logging_error(
        self, mock_process: MagicMock, mock_logging_error: MagicMock
    ):
        login("unregistered_username", "some_password", self.user_storage)
        mock_logging_error.assert_called_once_with("Not registered")
        mock_process.assert_not_called()

    @patch("user_manager.scripts.functions.logging.error")
    @patch("user_manager.scripts.functions.Process")
    def test__login__when_wrong_password__expect_logging_error(
        self, mock_process: MagicMock, mock_logging_error: MagicMock
    ):
        login(self.other_user.username, "WRONG", self.user_storage)
        mock_logging_error.assert_called_once_with("Wrong password")
        mock_process.assert_not_called()

    @patch("user_manager.scripts.functions.UserStorage.remove_from_logged_in")
    def test__logout__when_user_logged_in__expect_remove_called_once(
        self, mock_remove: MagicMock
    ):
        logout(self.logged_user.username, self.user_storage)
        mock_remove.assert_called_once_with(self.logged_user.username)

    @patch("user_manager.scripts.functions.UserStorage.remove_from_logged_in")
    def test__logout__when_user_not_logged_in__expect_remove_not_called(
        self, mock_remove: MagicMock
    ):
        logout(self.other_user.username, self.user_storage)
        mock_remove.assert_not_called()

    @patch("user_manager.scripts.functions.sleep")
    @patch("user_manager.scripts.functions.print")
    def test__login_process__always__expect_print_and_sleep_called(
        self, mock_print: MagicMock, mock_sleep: MagicMock
    ):
        login_process(self.logged_user.username)
        mock_print.assert_called_once_with(
            f"User {self.logged_user.username} is logged in"
        )
        mock_sleep.assert_called_once_with(1)

    @patch("user_manager.scripts.functions.print")
    @patch("user_manager.scripts.functions.logging.error")
    @patch("user_manager.scripts.functions.logging.info")
    def test__print_contacts(
        self,
        mock_logging_info: MagicMock,
        mock_logerror: MagicMock,
        mock_print: MagicMock,
    ):
        print_contacts(self.logged_user, self.user_storage)
        mock_print.assert_called_once_with(self.other_user)
        mock_logging_info.assert_called_once_with(
            "Reached the end of the contacts list"
        )

        print_contacts(self.other_user, self.user_storage)
        mock_logerror.assert_called_once_with(
            f"{self.other_user.username} not logged in"
        )

    @patch("user_manager.scripts.functions.logging.error")
    def test__add_contact__when_user_logged_in__expect_no_logging_error(
        self, mock_logging_error: MagicMock
    ):
        add_contact(self.logged_user.username, self.other_user, self.user_storage)
        mock_logging_error.assert_not_called()

    @patch("user_manager.scripts.functions.logging.error")
    def test__add_contact__when_user_not_logged_in__expect_logging_error(
        self, mock_logging_error: MagicMock
    ):
        add_contact(self.other_user.username, self.other_user, self.user_storage)
        mock_logging_error.assert_called_once_with(
            f"{self.other_user.username} not logged in"
        )

    @patch("user_manager.scripts.functions.logging.error")
    def test__remove_contact__when_user_logged_in__expect__no_logging_error(
        self, mock_logging_error: MagicMock
    ):
        remove_contact(self.logged_user.username, self.user_storage)
        mock_logging_error.assert_not_called()

    @patch("user_manager.scripts.functions.logging.error")
    def test__remove_contact__when_user_not_logged_in__expect_logging_error(
        self, mock_logging_error: MagicMock
    ):
        remove_contact(self.other_user.username, self.user_storage)
        mock_logging_error.assert_called_once_with(
            f"{self.other_user.username} not logged in"
        )


if __name__ == "__main__":
    unittest.main()
