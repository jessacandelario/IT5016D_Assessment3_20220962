
class Username:

    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.status = "Open"

    def user_info(self):
        return self.user_id, self.username, self.email


