from models.person import Person

class Staff(Person):
    def __init__(self, name, age, pid, staff_id):
        super().__init__(name, age, pid)
        self.staff_id = staff_id

    def __str__(self):
        return f"Staff: {self.staff_id} Name: {self.name} age: {self.age}"