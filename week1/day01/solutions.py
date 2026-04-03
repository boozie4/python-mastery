# Day 1 Solutions — only look after attempting exercises yourself!

print("=" * 40)
print("DAY 1 SOLUTIONS")
print("=" * 40)

# ── EXERCISE 1 ──────────────────────────────
print("\n--- Exercise 1: Variables and f-strings ---")
name = "Erik"
age = 32
city = "Lake Geneva"
print(f"My name is {name}, I'm {age}, and I live in {city}.")


# ── EXERCISE 2 ──────────────────────────────
print("\n--- Exercise 2: Math Operators ---")
a = 17
b = 5
print(a + b)    # 22
print(a - b)    # 12
print(a * b)    # 85
print(a / b)    # 3.4
print(a // b)   # 3
print(a % b)    # 2
print(a ** b)   # 1419857


# ── EXERCISE 3 ──────────────────────────────
print("\n--- Exercise 3: Type Checking ---")
val1 = "thirty"
val2 = 30
val3 = 30.0
val4 = True
val5 = None
print(type(val1))  # <class 'str'>
print(type(val2))  # <class 'int'>
print(type(val3))  # <class 'float'>
print(type(val4))  # <class 'bool'>
print(type(val5))  # <class 'NoneType'>


# ── EXERCISE 4 ──────────────────────────────
print("\n--- Exercise 4: Type Conversion ---")
price_str = "19.99"
count_str = "7"
score_int = 85

price_float = float(price_str)
print(price_float)          # 19.99

count_int = int(count_str)
print(count_int)            # 7

total = price_float * count_int
print(total)                # 139.93

score_str = str(score_int)
print("Your score: " + score_str)  # Your score: 85


# ── EXERCISE 5 ──────────────────────────────
print("\n--- Exercise 5: User Input ---")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
result = first + second
print(f"{first} + {second} = {result}")


# ── EXERCISE 6 — CHALLENGE ──────────────────
print("\n--- Exercise 6: Age Calculator ---")
birth_year = int(input("What year were you born? "))
current_year = 2026
age = current_year - birth_year
print(f"You are {age} years old.")
