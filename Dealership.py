
class Dealership:

    def __init__(self):
        self.staff = []
        self.inventory = []
        self.revenue = 0
        self.car_models = [ "1", "2", "3", "4"]

    def get_revenue(self):
        return self.revenue
    
    def sell_car(self, model_name, used, employee_who_sold):

        self.staff.remove(model_name)
        for staff in self.staff:
            if employee_who_sold == staff:
                employee_who_sold += 1

    def add_car(self, model_name, used):
        if model_name in self.car_models:
            self.inventory.append(model_name)
    
    def get_cars(self):
        return self.inventory
    
    def add_employee(self, name, position):
        new_employee = Employee(name,position)
        self.staff.append(new_employee)

    def fire(self, name):
        self.staff.remove(name)