# Day 5 Exercises — Lists and Tuples
# Run: python exercises.py

print("=" * 40)
print("DAY 5 EXERCISES")
print("=" * 40)

# ── EXERCISE 1 ──────────────────────────────
# Create a list of 5 of your favorite foods.
# Print the first, last, and middle item.
# Then print the whole list reversed.

print("\n--- Exercise 1: Indexing and Slicing ---")
# TODO


# ── EXERCISE 2 ──────────────────────────────
# Start with this list: scores = [88, 72, 95, 61, 83, 79, 91]
# 1. Add a score of 100 to the end.
# 2. Remove the score of 61.
# 3. Change the first score to 90.
# 4. Print the final list, sorted from highest to lowest.

print("\n--- Exercise 2: Modifying Lists ---")
scores = [88, 72, 95, 61, 83, 79, 91]
# TODO


# ── EXERCISE 3 ──────────────────────────────
# Write a function `list_stats(numbers)` that prints:
#   Count: X
#   Sum: X
#   Min: X
#   Max: X
#   Average: X.XX
# Test with [10, 24, 3, 57, 18, 42]

print("\n--- Exercise 3: List Stats ---")
# TODO


# ── EXERCISE 4 ──────────────────────────────
# Use a for loop to build a new list containing only the even numbers
# from this list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# (Don't use list comprehensions yet — just a loop and append.)

print("\n--- Exercise 4: Filter Evens ---")
# TODO


# ── EXERCISE 5 ──────────────────────────────
# Tuples and unpacking.
# Create a tuple with (first_name, last_name, age).
# Unpack it into three separate variables.
# Print: "Full name: {first} {last}, Age: {age}"

print("\n--- Exercise 5: Tuple Unpacking ---")
# TODO


# ── EXERCISE 6 ──────────────────────────────
# Write a function `find_duplicates(items)` that returns a list
# of items that appear more than once.
# Test with: [1, 2, 3, 2, 4, 1, 5]
# Expected: [1, 2] (order may vary)
# Hint: use .count() inside a loop.

print("\n--- Exercise 6: Find Duplicates ---")
# TODO


# ── EXERCISE 7 — CHALLENGE ──────────────────
# Shopping cart simulation.
# Start with an empty cart = []
# Build a menu loop:
#   "add <item>" — adds item to cart
#   "remove <item>" — removes item (print error if not in cart)
#   "view" — prints all items in cart
#   "quit" — exits
# Example input: "add apple", "add bread", "view", "remove apple", "quit"

print("\n--- Exercise 7: Shopping Cart ---")
cart = []
# TODO


print("\n" + "=" * 40)
print("Done! Update PROGRESS.md, then commit.")
print("=" * 40)
