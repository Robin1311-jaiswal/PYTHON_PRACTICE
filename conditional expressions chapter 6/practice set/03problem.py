# A spam comment is defined as a text containing following keywords:
#  "Make a lot of money", "Buy now", "subscribe this" , "Click this". 
#  write a prgram to detect these spams.

p1 =  "Make a lot of money"
p2= "Buy Now"
p3= "Subscribe this"
p4= "click this"

message= input("Enter your comment:")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")