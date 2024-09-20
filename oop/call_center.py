class Employee:
    def __init__(self, name, is_occupied):
        self.name = name
        self.access_level = 0
        self.is_occupied = is_occupied

    def toggle_occupied(self):
        self.is_occupied = not self.is_occupied

class Director(employee):
    def __init__(self, name):
        self.access_level = 3

class Manager(employee):
    def __init__(self, name):
        self.access_level = 2

class Respondent(employee):
    def __init__(self, name):
        self.access_level = 1

class Call:
    def __init__(self, caller_id, prio):
        self.caller_id = caller_id
        self.priority = prio


class Call_Center:
    def __init__(self, comp_name):
        self.company_name = comp_name

        self.director_list = []
        self.manager_list = []
        self.respondent_list = []

    def dispatch_call(self, call):
        is_call_dispatched = False

        if call.priority is 1:
            employee_list = respondent_list
        elif call.priority is 2:
            employee_list = manager_list
        else:
            employee_list = director_list
        
        for employee in employee_list:
            if not employee.is_occupied:
                employee.toggle_occupied()
                is_call_dispatched = True
                break

        if not is_call_dispatched:
            return "Apologies, no agents are currently available, please try again later."
        else:
            return 1 #indicating successful call dispatch