from random import randint

num1 = randint(1, 10) 
num2 = randint(1, 10)
question = f"What is {num1} * {num2}? " # the f string is for formatting
answer = int(input(question))

if answer == num1 * num2:
    print("Correct!")
else:
    print("That was not correct")

print(f"The answer should have been {num1 * num2}.")

print(f"The answer should have been {num1 * num2}.")

