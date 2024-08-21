class Greeting:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
    
    def print_message(self):
        print(f"{self.greeting}, {self.name}!!!!!!!")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python greet.py [name] [greeting]")
        sys.exit(1)
    name = sys.argv[1]
    greeting = sys.argv[2]
    greeting_instance = Greeting(name, greeting)
    greeting_instance.print_message()
    
