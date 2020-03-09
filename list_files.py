import os

print("The files and folder in {} are: ".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)
