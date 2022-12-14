from hash_module import check_hash, hash_password
from user import User
from user_storage import UserStorage


def some_function():
    print("Some function")

def register(username: str, password: str, user_storage: UserStorage):
    hashed_password = hash_password(password)

    new_user = User(username, password=hashed_password)
    user_storage.add_to_registered(new_user)

def login(username: str, password: str, user_storage: UserStorage):
    if user_storage.is_registered(username):
        pass


def logout(username: str, user_storage: UserStorage):
    if user_storage.is_logged_in(username):
        user_storage.remove_from_logged_in(username)
