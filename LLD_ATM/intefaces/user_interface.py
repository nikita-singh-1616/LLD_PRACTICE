from abc import ABC


class User(ABC):
    def __init__(self):
        self.name = None
        self.aadhar = None
        self.phone = None
        self.email = None
        self.password = None

    def validate_login(self):
        pass

    def create_user(self):
        pass
        
    def get_user_specific_details(self):
        pass