# write a program to fill in a letter templete given below with name and date 
letter = '''Dear <|name|>,
you are selected!
<|Date|>'''

print (letter.replace("<|name|>", "Robin Jaiswal").replace("<|Date|>", "13 Nov"))