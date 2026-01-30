class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def info(self):
        print(f"Dog Name: {self.name}")
        print(f"Age: {self.age} Years Old\n")

def main():
    my_dog = Dog("Buddy", 3)
    my_dog.info()

    Your_dog = Dog("Pailie", 2)
    Your_dog.info()

if __name__ == "__main__":
    main()
