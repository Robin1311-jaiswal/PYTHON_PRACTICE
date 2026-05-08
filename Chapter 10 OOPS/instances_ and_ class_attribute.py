class Employee:
    language = "Python"  # this is a class attribute
    salary = 120000

robin = Employee()
robin.language= "javaScript"  # This is an instances attribute
print(robin.language, robin.salary)