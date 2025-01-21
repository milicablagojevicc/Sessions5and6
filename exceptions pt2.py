name = input("what is your name")
print("hello", name)
age = input("how old are you?")

try:
    print(f"{name}, you were born in {2024 - int(age)}.")
    division = int(age) / 0
except ValueError:
    print("age must be a valid number")
    print(f"the value that you typed was {age}")
except ZeroDivisionError:
    print("you can't divide by zero")
except Exception as e:
    print(f"no idea what can go wrong: {e}")
else:
    print("thanks for being a good sport and not crashing")
finally:
    print("thanks for playing")