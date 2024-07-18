print('hi')

class Dealership:

    def __init__(self):
        self.staff = []
        self.inventory = []
        self.revenue = 0

    def get_revenue(self):
        return self.revenue
    
    def sell_car(self, model_name, used, employee_who_sold):

        self.staff.remove(model_name)
        for staff in self.staff:
            if employee_who_sold == staff:
                employee_who_sold += 1
