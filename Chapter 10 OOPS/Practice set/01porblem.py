# Create a class "Programmer" for storing information of few programmers working ar mcirosoft

class Programmer:
    Company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name= name
        self.salary = salary
        self.pin =pin
p = Programmer("Robin", 120000, 302017)
print(p.name, p.salary, p.pin, p.Company)