# create a class with a class attribute a; create an object from it and set 'a'
# directly using object.a = 0. does this change the class attribute?

class Demo:
    a =4

o = Demo()
print(o.a)  # prints the class attributes because instance attribute is not present

o.a = 0 #Instance attributes is set

print(o.a) #Prints the instances attributes because instance attribute is present
print(Demo.a )  # print the class attribute