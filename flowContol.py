print("True and True equals to: " +str(True and True))
print("True and False equals to: " +str(True and False))
print("False and True equals to: " +str(False and True))
print("False and False equals to: " +str(False and False))
print()
print("True or True equals to: " +str(True or True))
print("True or False equals to: " +str(True or False))
print("False or True equals to: " +str(False or True))
print("False or False equals to: " +str(False or False))
print()

name="Carol"
print("Name :" +name)
age=3000
print("Age :" + str(age))
print(age)
if name == "Alice":
    print("Hello Alice.")
elif age < 12:
    print("You're not Alice Kiddo.")
elif age >2000:
    print("Unlike you, Allice in not undead, immortal vampire.")
elif age >100:
    print("You're not Allice, grannie.")

print()

name="Carol"
print("Name :" +name)
age=3000
print("Age :" + str(age))
print(age)
if name == "Alice":
    print("Hello Alice.")
elif age < 12:
    print("You're not Alice Kiddo.")
elif age >100: # wrong checking condition (start with greater value and go to lower)
    print("You're not Allice, grannie.")
elif age >2000:
    print("Unlike you, Allice in not undead, immortal vampire.")