# create and empty disctionary. allow 4 friends to enter their favuorite language as value and use key as their names,
# assume that the names unique
d= {}

name = input("Eter friends name:")
lang = input("enter language name")

d.update({name:lang})
name = input("Eter friends name:")
lang = input("enter language name")

d.update({name:lang})
name = input("Eter friends name:")
lang = input("enter language name:")

d.update({name:lang})
name = input("Eter friends name:")
lang = input("enter language namw:")

d.update({name:lang})
print(d)