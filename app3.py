from models.student import Student
from models.classroom import ClassRoom

oop = ClassRoom("OOP")
oop.add_student(Student(1, "Alice", 20, "S001"))
oop.add_student(Student(2, "Bob", 22, "S002"))
print(f"{oop.name} registerd {len(oop)} Students")

oop.add_student(Student(3, "Charlie", 21, "S003"))
print(len(oop))

print("Students in the class:")
for i in range(len(oop)):
    print(oop[i])