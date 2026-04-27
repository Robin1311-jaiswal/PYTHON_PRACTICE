marks={
    "Robin": 100,
    "ranjan":200,
    "sunul":300
}
# print(marks)
# print(marks["Robin"])
# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Robin": 120, "Rahul":300})
print(marks)

print(marks.get("Robinn"))  # print none if key is not present 
print(marks["Robinn"]) # returns error if value is not present