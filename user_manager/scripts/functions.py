import logging
from time import sleep

from hash_module import check_hash, hash_password
from multiprocessing import Process
from .user import User
from .user_storage import UserStorage


__all__ = ["add_contact", "login", "logout", "login_process", "print_contacts", "register", "remove_contact"]

NOT_LOGGED_IN_ERROR = "{} not logged in"


def login_process(username):
    sleep(1)
    print(f"User {username} is logged in")


def print_contacts(user: User, user_storage: UserStorage):
    if user_storage.is_logged_in(user.username):
        contacts_iterator = iter(user)
        while True:
            try:
                print(next(contacts_iterator))
            except StopIteration:
                logging.info("Reached the end of the contacts list")
                break
    else:
        logging.error(NOT_LOGGED_IN_ERROR.format(user.username))


def register(username: str, password: str, user_storage: UserStorage):
    hashed_password = hash_password(password)

    new_user = User(username, password=hashed_password)
    user_storage.add_to_registered(new_user)


def login(username: str, password: str, user_storage: UserStorage):
    if user_storage.is_registered(username):
        user = user_storage.get_user(username)
        if check_hash(user.password, password):
            process = Process(target=login_process, args=(username,))
            process.start()
            process.join()
            user_storage.log_in(user)
        else:
            logging.error("Wrong password")
    else:
        logging.error("Not registered")


def logout(username: str, user_storage: UserStorage):
    if user_storage.is_logged_in(username):
        user_storage.remove_from_logged_in(username)
        logging.info(f"{username} logged out.")
    else:
        logging.info(f"{username} is not logged in.")


def add_contact(username: str, contact: User, user_storage: UserStorage):
    if user_storage.is_logged_in(username):
        user = user_storage.get_user(username)
        user.contacts = contact
    else:
        logging.error(NOT_LOGGED_IN_ERROR.format(username))


def remove_contact(username: str, user_storage: UserStorage):
    if user_storage.is_logged_in(username):
        user = user_storage.get_user(username)
        del user.contacts
    else:
        logging.error(NOT_LOGGED_IN_ERROR.format(username))
