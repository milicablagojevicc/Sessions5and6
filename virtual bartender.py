#virtual bartender
drinks = ("vodka", "whiskey", "gin", "tequila", "run", "rakia", "sake")
print("Welcome to the virtual pub")
name = input("I am the virtual bartender, how do I call you?")
try:
    age = input(f"How old are you, {name}?")
    age = int(age) #try to convert to a number
    country = input(f"Where are you from, {name}? ")
    if age >= 21:
        legal = True
   elif age < 16:
legal = False
else:
age >= 16 and country == "Luxembourg":
        legal = True
        if legal == True:
            print("you are allowed to drink")
        else:
            print("you are NOT allowed to drink")
except ValueError:
    print("Please give a valid age")
