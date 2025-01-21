drinks = ("vodka", "whiskey", "gin", "tequila", "rum", "rakia", "sake")
print("Welcome to the virtual pub")
name = input("I am the virtual bartender, how do I call you? ")

try:
    age = input(f"How old are you, {name}? ")
    age = int(age)  # Try to convert age to an integer
    legal = False

    # Check if age is between 16 and 21 before asking for the country
    if age < 16:
        legal = False
    elif age >= 18:
        legal = True  # Default rule for most countries
    elif 16 <= age < 21:
        country = input(f"Where are you from, {name}? ")
        if country.lower() == "usa" and age < 21:
            legal = False
        elif country.lower() == "luxembourg" and age >= 16:
            legal = True
        else:
            legal = False

    # Check drinking eligibility
    if legal:
        print("You are allowed to drink. What would you like? Here's the menu:")
        print(", ".join(drinks))
    else:
        print("You are NOT allowed to drink.")
except ValueError:
    print("Please provide a valid age.")