from models.person import Person
from models.staff import Staff
from models.student import Student

obj_person = Person("Person", 00, "1110987654321")
student = Student("Mark", 18, "1234567891011", "68114541234")
staff = Staff("Mon", 26, "12345678910121", "758466587")
print(f"Person Name: {obj_person.name}\nage: {obj_person.age}")
print(f"\nStudent Name: {student.name}\nage: {student.age}")
print(f"\nStaff Name: {staff.name}\nage: {staff.age}")

def get_person_info(person):
    print(isinstance(person, Person))

get_person_info(Student)
get_person_info(Staff)