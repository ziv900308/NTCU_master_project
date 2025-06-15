# Parent class
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def speak(self):
        print("This is speak from Animal...")
        pass  # Placeholder method to be overridden by child classes

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print("This is speak from Dog...")
        return f"{self.name} barks!"  # Override the speak method

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())