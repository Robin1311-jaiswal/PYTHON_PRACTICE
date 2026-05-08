# f = open("file.txt", "r")
# data = f.read()
# print(data)
# f.close()

#The same can be written using with statement like this :

with open("file.txt") as f :
    print(f.read())


#we dont have to explicitly  close the file