class Greeting:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
    
    def print_message(self):
        print(f"{self.greeting}, {self.name}!")
