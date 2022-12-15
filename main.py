import sys
import logging

from user_manager import (
    add_contact,
    login,
    logout,
    print_contacts,
    register,
    remove_contact,
    User,
    UserStorage,
)


def main():
    user_storage = UserStorage()
    while True:
        print(
            (
                "1 - Register user\n"
                "2 - Login\n"
                "3 - Add a new contact\n"
                "4 - Remove contact from a user\n"
                "5 - Print contacts from a user\n"
                "6 - Logout\n"
                "7 - Exit app"
            )
        )
        selection = int(input("Select option 1-7 -> "))
        if selection not in range(1, 8):
            continue
        manage_input(selection, user_storage)


def manage_input(selection: int, storage: UserStorage):
    if selection == 1:
        try:
            register(input("Username: "), input("Password: "), storage)
        except Exception as exc:
            logging.error(exc)
    elif selection == 2:
        login(input("Username: "), input("Password: "), storage)
    elif selection == 3:
        user = input("Username: ")
        contact = storage.get_user(input("Contact: "))
        if isinstance(contact, User):
            add_contact(user, contact, storage)
    elif selection == 4:
        user = input("Username: ")
        remove_contact(user, storage)
    elif selection == 5:
        user = storage.get_user(input("Username: "))
        if isinstance(user, User):
            print_contacts(user, storage)
        else:
            logging.error("That user does not exist.")
    elif selection == 6:
        logout(input("Username: "), storage)
    elif selection == 7:
        sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(
        level=getattr(logging, "INFO", None),
        format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    main()
