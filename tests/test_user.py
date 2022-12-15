import logging
import unittest

from unittest.mock import MagicMock, patch

from user_manager import User
from hash_module import hash_password


class TestUser(unittest.TestCase):
    def test__constructor__when_parameters_are_ok__expect_user_instance(self):
        actual_value = User("name", hash_password("123456"))

        expected_type = User
        self.assertIsInstance(actual_value, expected_type)

    def test__constructor__when_password_is_not_valid__expect_exception(self):
        with self.assertRaises(Exception) as actual_exception:
            User("name", "invalid_pass")

        expected_error_message = "Password does not match criteria."
        self.assertEqual(expected_error_message, str(actual_exception.exception))

    @patch("user_manager.scripts.user.logging.log")
    def test__properties(self, mock_log: MagicMock):
        username = "name"
        password = hash_password("123456")
        user_instance = User(username, password)

        self.assertEqual(username, user_instance.username)
        self.assertEqual(password, user_instance.password)

        new_username = "name2"
        new_password = hash_password("654321")
        user_instance.username = new_username
        user_instance.password = new_password

        self.assertEqual(new_username, user_instance.username)
        self.assertEqual(new_password, user_instance.password)

        contact = User("contact", hash_password("123"))
        user_instance.contacts = contact
        user_instance.contacts = contact

        self.assertEqual([contact], user_instance.contacts)
        mock_log.assert_called_once_with(
            logging.INFO, f"{contact} already exists in contacts."
        )

        del user_instance.contacts
        self.assertEqual([], user_instance.contacts)

    @patch("user_manager.scripts.user.logging.log")
    def test__delete_contact_by_user(self, mock_log: MagicMock):
        user_instance = User("name", hash_password("123"))
        contact = User("contact", hash_password("123"))

        user_instance.delete_contact_by_user(contact)
        mock_log.assert_called_once()

        user_instance.contacts = contact
        self.assertTrue(contact in user_instance.contacts)

        user_instance.delete_contact_by_user(contact)
        self.assertFalse(contact in user_instance.contacts)

    @patch("user_manager.scripts.user.logging.log")
    def test__delete_contact_by_index(self, mock_log: MagicMock):
        user_instance = User("name", hash_password("123"))
        contact = User("contact", hash_password("123"))

        user_instance.delete_contact_by_index(0)
        user_instance.delete_contact_by_index("invalid")
        mock_log.assert_called()

        user_instance.contacts = contact
        self.assertTrue(contact in user_instance.contacts)

        user_instance.delete_contact_by_index(0)
        self.assertFalse(contact in user_instance.contacts)

    def test__iterator(self):
        user_instance = User("name", hash_password("123"))
        contact = User("contact", hash_password("123"))
        user_instance.contacts = contact
        iterator = iter(user_instance)

        self.assertEqual(contact, next(user_instance))

        with self.assertRaises(StopIteration) as actual_exception:
            next(user_instance)

    def test__dunders(self):
        user_instance = User("name", hash_password("123"))

        string_representation = str(user_instance)
        self.assertEqual("Username: name", string_representation)
        self.assertEqual(len(user_instance), 0)

        another_user = User("jane_doe", hash_password("123"))
        self.assertFalse(user_instance == another_user)


if __name__ == "__main__":
    unittest.main()
