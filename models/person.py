class Person:
    def __init__(self, name, age, pid):
        self.name = name
        self.age = age
        self.pid = pid
    
    def __str__(self):
        return f"Name: {self.name} age: {self.age} pid: {self.pid}"

