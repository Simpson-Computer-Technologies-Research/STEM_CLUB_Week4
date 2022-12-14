
# /////////////////
# //   Classes   //
# /////////////////

# // Note:
# // You do not need to have an __init__(self) function.
class MyClass:
    name = "Tristan"

    # // Whenever the Class is initalized
    def __init__(self):
        # // Set the name to something different
        self.name = "Dave"

        # // Print an initialization message
        print("MyClass Initialized")


    # // A function accessable through the class
    def print_person(self, age):
        print(f"{self.name}: {age}")


# // Initalize the class. The content inside
# // __init__(self) will be called
my_class = MyClass()

# // Run the function inside the class
my_class.print_person(age = 16)
