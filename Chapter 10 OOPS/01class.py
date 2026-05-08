class Employee:
    
    language= "PY"  #this is a class attribute
    salary = 1200000

robin = Employee()
robin.name = "Robin"   # this is an object   instances attribute
print( robin.name ,robin.language, robin.salary)

ranjan = Employee()
ranjan.name = "Ranjan"
print(ranjan.name, ranjan.salary, ranjan.language)


# here name is object attrubute and salary and language are class attributes as they directly belong to the class 
