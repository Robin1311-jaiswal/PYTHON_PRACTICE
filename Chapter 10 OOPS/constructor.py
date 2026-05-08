class Employee:
    language = "Python" 
    salary= 120000

    def __init__(self, name ,salary, language): # dunder method which is automatically called
        self.name = name
        self.salary=salary
        self.language=language

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

robin = Employee("Robin", 12000, "JavaScript")
#robin.name = "Robin"
print(robin.name, robin.salary, robin.language)

# ranjan = Employee()