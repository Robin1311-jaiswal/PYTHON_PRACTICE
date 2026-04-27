# write a program to find out whether a given post is talking about "Robin" or not

post = input("Enter the post:")

if ("robin" in post.lower()):
    print("This post is talking about robin")

else: 
    print("this post is not talking about robin")