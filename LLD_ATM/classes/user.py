from intefaces.user_interface import User


class BankUser(User):
    def __init__(self) -> None:
        super().__init__()
        self.name = None
        self.aadhar = None
        self.phone = None
        self.email = None
        self.password = None
        self.date_of_birth = None

    def validate_login(self,email,password):
        if email == self.email and password == self.password:
            return True
        return False

    def create_user(self):
        self.name = input('enter your name ')
        self.aadhar = input('enter your aadhar ')
        self.phone = input('enter your phone number ')
        self.email = input('enter your email ')
        self.password = input('enter your password ')
        self.date_of_birth = input('enter your date of birth ')
        
    def get_user_specific_details(self,param):
        output_based_on_param = {
            'name':self.name,
            'aadhar':self.aadhar,
            'phone':self.phone,
            'email':self.email,
            'password':self.password,
            'date_of_birth':self.date_of_birth
        }
        if param not in output_based_on_param:
            return False
        return output_based_on_param[param]