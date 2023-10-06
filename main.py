# Class Definition
class Animal:
    # Class Variable
    num_of_animals = 0

    # Constructor (Initializer) Method
    def __init__(self, name, age):
        # Instance Variables
        self.name = name
        self.age = age
        Animal.num_of_animals += 1

    # Instance Method
    def speak(self):
        pass

    # Class Method
    @classmethod
    def get_num_of_animals(cls):
        return cls.num_of_animals

# Inheritance
class Dog(Animal):
    # Constructor Override
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    # Method Override
    def speak(self):
        return "Woof!"

# Encapsulation
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"

# Abstraction
class Shape:
    def area(self):
        pass

# Polymorphism
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Composition
class Person:
    def __init__(self, name):
        self.name = name
        self.pet = None

# Aggregation
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

# Instantiating Objects
dog = Dog("Fido", 5, "Labrador")
cat = Cat("Whiskers", 3)
account = BankAccount()
circle = Shape()

# Using Objects
dog_speech = dog.speak()
cat_speech = cat.speak()

account.deposit(1000)
withdrawal_result = account.withdraw(500)

# Print Results
print(f"{dog.name} says: {dog_speech}")
print(f"{cat.name} says: {cat_speech}")
print(f"Balance after withdrawal: {withdrawal_result}")

# Demonstrating Inheritance
print(f"Number of animals: {Animal.get_num_of_animals()}")

# Demonstrating Composition
person = Person("John")
person.pet = cat
print(f"{person.name}'s pet says: {person.pet.speak()}")

# Demonstrating Aggregation
department = Department("Engineering")
employee1 = Person("Alice")
employee2 = Person("Bob")
department.add_employee(employee1)
department.add_employee(employee2)

print(f"Employees in {department.name} department:")
for employee in department.employees:
    print(employee.name)
