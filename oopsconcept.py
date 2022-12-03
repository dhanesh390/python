import myconstants


class Employee:
    """ This class represents the employee class object"""
    company_name = 'Ideas2it'

    # Parametrized constructor for the employee instance object
    def __init__(self, first_name, last_name, employee_id, role, date_of_birth, date_of_joining):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.role = role
        self.date_of_birth = date_of_birth
        self.date_of_joining = date_of_joining

    def __repr__(self):
        return f'Welcome {self.first_name} {self.last_name} to {self.company_name}'

    def __del__(self):
        """ Destructor method which will delete the reference object once the reference counter hits Zero"""
        return f'employee object has been deleted'


list_of_employees = {}

_id = 1


def add():
    # new_employee = Employee()
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    global _id
    employee_id = myconstants.COMPANY_ID + str(_id + 1)
    role = input('Enter your role:  ')
    date_of_birth = input('Enter your date of birth: ')
    date_of_joining = input('Enter your date of joining: ')
    new_employee = Employee(first_name, last_name, employee_id, role, date_of_birth, date_of_joining)
    print(new_employee)
    return new_employee


def _init():
    is_continue = True
    while is_continue:
        print('Enter 1 to add\nEnter 2 to view')
        user_input = input('Enter your choice: ')
        match user_input:
            case 1:
                print(add())


if __name__ == '__main__':
    _init()
