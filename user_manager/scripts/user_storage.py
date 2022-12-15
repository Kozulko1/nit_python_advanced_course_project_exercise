import logging
from .user import User


class UserStorage:
    def __init__(self):
        self.registered: list[User] = list()
        self.logged_in: list[User] = list()

    def add_to_registered(self, user: User):
        if user not in self.registered:
            self.registered.append(user)
        else:
            logging.error("Already registered")

    def get_user(self, username: str):
        for user in self.registered:
            if user.username == username:
                return user

    def is_registered(self, username: str):
        for user in self.registered:
            if user.username == username:
                return True
        return False

    def remove_from_logged_in(self, username: str):
        for user in self.logged_in:
            if user.username == username:
                self.logged_in.remove(user)
                break
        else:
            logging.error("Not logged in")

    def log_in(self, user: User):
        if user not in self.logged_in:
            self.logged_in.append(user)
        else:
            logging.error("Already logged in")

    def is_logged_in(self, username: str):
        for user in self.logged_in:
            if user.username == username:
                return True
        return False
