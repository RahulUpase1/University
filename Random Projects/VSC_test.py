print("Hello World")
name = input("your name? ")
print("Hello {0}".format(name))
info = [name]
age = int(input("How old are you? "))
if age <= 20:
    print("Wow {0} is quite young".format(age))
elif 20 < age < 50:
    print("Wow you should be doing well in your career at {0} years old".format(age))
else:
    print("Old is Gold")
info.append(age)
location = input("Where do you live? ")
info.append(location)
print(info)