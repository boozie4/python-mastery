# Day 1 Exercises — Variables, Data Types, and Basic I/O
# Run this file: python exercises.py
# Fill in each TODO. Don't skip — every exercise builds a mental model.

print("=" * 40)
print("DAY 1 EXERCISES")
print("=" * 40)

# ── EXERCISE 1 ──────────────────────────────
# Create variables for your name, age, and city.
# Print them using an f-string in one sentence.
# Example output: "My name is Erik, I'm 32, and I live in Lake Geneva."

print("\n--- Exercise 1: Variables and f-strings ---")
# TODO: create name, age, city variables

name = "Erik"
age = 32
city = "Burlington"

# TODO: print them with an f-string

print(f"My name is {name}, I'm {age}, and I live in {city}.")

# ── EXERCISE 2 ──────────────────────────────
# Python math. Fill in each blank with the correct operator.
# Don't just type the answer — write the actual math expression.

print("\n--- Exercise 2: Math Operators ---")
a = 17
b = 5

# TODO: print a plus b
print(a + b)
# TODO: print a minus b
print(a - b)
# TODO: print a times b
print(a * b)
# TODO: print a divided by b (regular division)
print(a / b)
# TODO: print a floor-divided by b (no remainder)
print(a // b)
# TODO: print the remainder of a divided by b
print(a % b)
# TODO: print a to the power of b
print(a ** b)


# ── EXERCISE 3 ──────────────────────────────
# Type inspection. Use type() to check what type each value is.
# Print the result for each.

print("\n--- Exercise 3: Type Checking ---")
val1 = "thirty"
val2 = 30
val3 = 30.0
val4 = True
val5 = None

# TODO: print the type of each variable above (5 lines)

print(type(val1))
print(type(val2))
print(type(val3))
print(type(val4))
print(type(val5))



# ── EXERCISE 4 ──────────────────────────────
# Type conversion. Convert between types as instructed.

print("\n--- Exercise 4: Type Conversion ---")
price_str = "19.99"
count_str = "7"
score_int = 85

# TODO: Convert price_str to a float, store it as price_float, print it
price_float = float(price_str)
print(price_float)

# TODO: Convert count_str to an int, store it as count_int, print it
count_int = int(count_str)
print(count_int)

# TODO: Multiply price_float * count_int and print the total
total = price_float * count_int
print(total)

# TODO: Convert score_int to a string, store it as score_str
score_str = str(score_int)

# TODO: Print: "Your score: " + score_str  (use concatenation, not f-string)
print("Your score: " + score_str)


# ── EXERCISE 5 ──────────────────────────────
# User input. Ask the user for two numbers, add them, print the result.
# Remember: input() returns a string — you must convert!

print("\n--- Exercise 5: User Input ---")
# TODO: Ask for first number using input(), convert to int
num1 = int(input("Enter the first number: "))

# TODO: Ask for second number using input(), convert to int
num2 = int(input("Enter the second number: "))

# TODO: Add them and print: "X + Y = Z"
print(f"{num1} + {num2} = {num1 + num2}")



# ── EXERCISE 6 — CHALLENGE ──────────────────
# Build a simple "age calculator".
# Ask the user for their birth year.
# Calculate how old they are (current year is 2026).
# Print: "You are X years old." or "You will turn X this year."

print("\n--- Exercise 6: Age Calculator ---")
# TODO: implement the age calculator
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
if age > 0:
    print(f"You are {age} years old.")
else:
    print(f"You will turn {abs(age)} this year.")



print("\n" + "=" * 40)
print("Done! Update PROGRESS.md, then commit.")
print("=" * 40)
