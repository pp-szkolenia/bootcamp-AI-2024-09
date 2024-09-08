class User:
    def __init__(self, user_id, username, email_address, password):
        self.user_id = user_id
        self.username = username
        self.email_address = email_address
        self.password = password

    def save_to_database(self):
        pass

    def change_my_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password


class Admin(User):
    def __init__(self, user_id, username, email_address, password, can_add_users):
        super().__init__(user_id, username, email_address, password)
        self.can_add_users = can_add_users

    def add_user(self, user_id, username, email_address, password):
        if self.can_add_users:
            new_user = User(user_id, username, email_address, password)
            return new_user

    def change_password_of_another_user(self, user, new_password):
        user.password = new_password
