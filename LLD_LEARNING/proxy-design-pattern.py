from abc import ABC, abstractmethod


class EmployeeInterface(ABC):
    @abstractmethod
    def create(self, emp):
        pass

    @abstractmethod
    def delete(self, emp):
        pass

    @abstractmethod
    def get(self, emp):
        pass


class EmployeeConcreteClass(EmployeeInterface):
    def __init__(self):
        self.employees = {}

    def create(self, emp_obj):
        self.employees[emp_obj['user_id']] = emp_obj

    def delete(self, emp_id):
        self.employees[emp_id].status = False

    def get(self, emp_id):
        if emp_id in self.employees:
            return self.employees[emp_id]
        else:
            return None


class EmployeeProxy(EmployeeInterface):
    def __init__(self):
        self.concrete_class = EmployeeConcreteClass()

    def create(self, emp):
        if emp['user_role'] == 'ADMIN':
            # can perform masking or marshalling
            emp_obj = {
                'user_id': emp['user_id'],
                'status': True,
                'username': emp['username']
            }
            self.concrete_class.create(emp_obj)
        else:
            print('Access Denied')

    def delete(self, emp):
        if emp['user_role'] == 'ADMIN':
            self.concrete_class.delete(emp['user_id'])
        else:
            print('Access Denied')

    def get(self, emp):
        if emp['user_role'] in ['USER', 'ADMIN']:
            return self.concrete_class.get(emp['user_id'])
        else:
            print('Access Denied')


class Main:
    def __init__(self):
        self.employee_manager = EmployeeProxy()
        self.user_role = 'ADMIN'
        print(f'Role:{self.user_role}')
        self.create_employee()
        self.change_role()
        print(f'Role:{self.user_role}')
        self.create_employee()
        self.get_user()

    def create_employee(self):
        emp_obj = {
            'user_role': self.user_role,
            'user_id': input('enter user id: '),
            'username': input('enter username: ')
        }
        self.employee_manager.create(emp_obj)

    def change_role(self):
        self.user_role = 'USER'

    def get_user(self):
        emp_obj = {
            'user_role': self.user_role,
            'user_id': input('enter userid to get: ')
        }
        emp = self.employee_manager.get(emp_obj)
        print(emp)


Main()
