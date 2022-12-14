from user import User

class UserStorage:
    def __init__(self):
        self.registered: list[User] = list()
        self.logged_in: list[User] = list()

    def add_to_registered(self, user: User):
        if user not in self.registered:
            self.registered.append(user)
        else:
            print("Već je registrovan")

    def remove_from_registered(self, user:User):
        if user in self.registered:
            self.registered.remove(user)
        else:
            print("Već je neregistrovan")

    def log_in(self, user:User):
        if user not in self.logged_in:
            self.logged_in.append(user)
        else:
            print("Već je logiran")

    def is_logged_in(self, user:User):
        if user in self.logged_in:
            return True
        return False