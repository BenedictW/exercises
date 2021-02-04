# This program says hello and ask for my name
"""
print("Hello world!")
print("What is Your name?")
my_name=input() #input function
print("It's good to meet you "+my_name)
print("The length of your name is:")
print(len(my_name))
print("What is your age?") #ask about age
my_age=input() 
print("You will be "+str(int(my_age)+1)+ " in a year.")
"""
print("I'm "+"29"+" old")
print("I've "+ str(41)+ " years old.")

print("wpisz liczbę:")
spam = input()

print("zmienna jest typu: "+ str(type(spam)))
spam1 = int(spam)
print("po użyciu funkcji int(zmienna) zmienna jest typu: "+ 
str(type(spam1)))
print(spam1)
spam2 = float(spam)
print("po użyciu funkcji float(zmienna) zmienna jest typu: "+
str(type(spam2)))
print(spam2)
