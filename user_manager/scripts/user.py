from __future__ import annotations

import logging


__all__ = ["User"]


class User:
    def __init__(self, username: str, password: str) -> None:
        self.__check_password_validity(password)
        self.__username: str = username
        self.__password: str = password
        self.__contacts: list[User] = []

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, new_username: str) -> None:
        self.__username = new_username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password) -> None:
        self.__check_password_validity(new_password)
        self.__password = new_password

    @property
    def contacts(self) -> list[User]:
        return self.__contacts

    @contacts.setter
    def contacts(self, new_user: User) -> None:
        if new_user not in self.__contacts:
            self.__contacts.append(new_user)
        else:
            logging.log(logging.INFO, f"{new_user} already exists in contacts.")

    def delete_contact_by_user(self, user: User) -> None:
        try:
            del self.__contacts[self.__contacts.index(user)]
        except ValueError as exc:
            logging.log(logging.INFO, f"Tried to delete a nonexisting contact. Received {exc}")

    def delete_contact_by_index(self, index: int) -> None:
        try:
            del self.__contacts[index]
        except IndexError as exc:
            logging.log(logging.INFO, f"Tried to delete a nonexisting contact. Received {exc}")
        except TypeError as exc:
            logging.log(logging.INFO, f"Function parameter must be an integer. Received {exc}")

    def __iter__(self) -> None:
        self.__element_pointer = 0
        return self

    def __next__(self) -> User:
        if self.__element_pointer < len(self.__contacts):
            self.__element_pointer += 1
            return self.__contacts[self.__element_pointer - 1]
        raise StopIteration

    def __len__(self) -> int:
        return len(self.__contacts)

    def __eq__(self, rhs: User) -> bool:
        return self.__username == rhs.__username

    def __str__(self):
        output = f"Username: {self.__username}"
        if self.__contacts:
            output += "\nContacts:"
            for contact in self.__contacts:
                output += f"\n\t{contact.username}"
        return output

    def __check_password_validity(self, password: str):
        if not password.isnumeric() or len(password) not in range(1, 12):
            raise Exception("Password does not match criteria.")
