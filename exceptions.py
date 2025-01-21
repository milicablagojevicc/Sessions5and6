name = input("what is your name")
print("hello", name)
age = input("how old are you?")
try:
    print(f"{name}, you were born in {2024-int(age)}.")
except:
    print("age must be a valid number")
    print(f" the value that you typed was {age}.")
print("thanks for playing")