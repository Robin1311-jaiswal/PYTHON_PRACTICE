# write a program to greet all the person names stored in a list 'l' and which starts with R.
l=["Robin", "Ranjan", "Sachin", "Rahul"]

for name in l:
    if (name.startswith("R")):
        print(f"Hello {name}")

