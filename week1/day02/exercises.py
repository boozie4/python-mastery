# Day 2 Exercises — Control Flow
# Run: python exercises.py

print("=" * 40)
print("DAY 2 EXERCISES")
print("=" * 40)

# ── EXERCISE 1 ──────────────────────────────
# Basic if/else
# Ask the user for a number. If it's greater than 100, print "Big number!"
# Otherwise print "Small number."

print("\n--- Exercise 1: Basic if/else ---")
# TODO


# ── EXERCISE 2 ──────────────────────────────
# Grade classifier
# Ask for a test score (0-100).
# Print the letter grade:
#   90-100 → "A"
#   80-89  → "B"
#   70-79  → "C"
#   60-69  → "D"
#   below 60 → "F"

print("\n--- Exercise 2: Grade Classifier ---")
# TODO


# ── EXERCISE 3 ──────────────────────────────
# Logical operators
# Ask for the user's age and whether they have a ticket ("yes"/"no").
# They can enter a show if: age >= 18 AND they have a ticket.
# Print "Welcome!" or "Sorry, you cannot enter."

print("\n--- Exercise 3: Logical Operators ---")
# TODO


# ── EXERCISE 4 ──────────────────────────────
# Truthy/Falsy
# The variable `username` might be empty.
# If it has a value, print "Hello, {username}!"
# If it's empty, print "Please enter a username."
# Try changing username to test both paths.

print("\n--- Exercise 4: Truthy/Falsy ---")
username = ""  # Try changing to "Erik" and back to ""
# TODO


# ── EXERCISE 5 ──────────────────────────────
# FizzBuzz — a classic interview problem.
# Ask for a number. Apply these rules:
#   Divisible by both 3 and 5 → print "FizzBuzz"
#   Divisible by 3 only        → print "Fizz"
#   Divisible by 5 only        → print "Buzz"
#   Otherwise                  → print the number
# Hint: use the % (modulo) operator to check divisibility.
# Hint: check the combined case (3 AND 5) FIRST.

print("\n--- Exercise 5: FizzBuzz ---")
# TODO


# ── EXERCISE 6 — CHALLENGE ──────────────────
# Build a simple login system.
# Set a correct_password = "python30" at the top.
# Ask the user to enter a password.
# If correct: print "Access granted. Welcome!"
# If wrong: print "Wrong password. Access denied."
# BONUS: Also check that the username is "admin".
#        Only grant access if BOTH are correct.

print("\n--- Exercise 6: Login System ---")
correct_password = "python30"
correct_username = "admin"
# TODO


print("\n" + "=" * 40)
print("Done! Update PROGRESS.md, then commit.")
print("=" * 40)
