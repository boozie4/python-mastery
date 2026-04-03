# Day 2 Solutions

print("=" * 40)
print("DAY 2 SOLUTIONS")
print("=" * 40)

# ── EXERCISE 1 ──────────────────────────────
print("\n--- Exercise 1 ---")
number = int(input("Enter a number: "))
if number > 100:
    print("Big number!")
else:
    print("Small number.")


# ── EXERCISE 2 ──────────────────────────────
print("\n--- Exercise 2 ---")
score = int(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# ── EXERCISE 3 ──────────────────────────────
print("\n--- Exercise 3 ---")
age = int(input("Enter your age: "))
ticket = input("Do you have a ticket? (yes/no): ")
if age >= 18 and ticket == "yes":
    print("Welcome!")
else:
    print("Sorry, you cannot enter.")


# ── EXERCISE 4 ──────────────────────────────
print("\n--- Exercise 4 ---")
username = ""
if username:
    print(f"Hello, {username}!")
else:
    print("Please enter a username.")


# ── EXERCISE 5 ──────────────────────────────
print("\n--- Exercise 5 ---")
n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)


# ── EXERCISE 6 ──────────────────────────────
print("\n--- Exercise 6 ---")
correct_password = "python30"
correct_username = "admin"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("Access granted. Welcome!")
else:
    print("Wrong credentials. Access denied.")
