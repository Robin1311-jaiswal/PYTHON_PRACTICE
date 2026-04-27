a= int(input("enter your age:"))


if (a%2==0):
    print("a is even")
# if else elif ladder

if (a>18):
    print("you are above the age of the consent")
    print("Good for you")


elif(a<0):
    print("You are entering an ivalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else :
    print("You are below the age of consent")

print("End of program")