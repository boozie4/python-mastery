# Day 4 Exercises — Functions
# Run: python exercises.py

print("=" * 40)
print("DAY 4 EXERCISES")
print("=" * 40)

# ── EXERCISE 1 ──────────────────────────────
# Write a function called `greet` that takes a name
# and prints "Hello, {name}! Welcome to Python."
# Call it 3 times with different names.

print("\n--- Exercise 1: greet() ---")
# TODO: define greet()

# TODO: call it 3 times


# ── EXERCISE 2 ──────────────────────────────
# Write a function `add(a, b)` that returns the sum.
# Write a function `multiply(a, b)` that returns the product.
# Print: "3 + 5 = 8" and "3 * 5 = 15"

print("\n--- Exercise 2: add() and multiply() ---")
# TODO


# ── EXERCISE 3 ──────────────────────────────
# Write a function `is_even(n)` that returns True if n is even, False if odd.
# Test it with numbers 1-10 and print each result.

print("\n--- Exercise 3: is_even() ---")
# TODO


# ── EXERCISE 4 ──────────────────────────────
# Write a function `temperature_convert(value, unit)` where:
#   unit = "C" → convert Celsius to Fahrenheit: (value * 9/5) + 32
#   unit = "F" → convert Fahrenheit to Celsius: (value - 32) * 5/9
# Return the converted value (rounded to 1 decimal).
# Test: 100C = 212.0F, 32F = 0.0C

print("\n--- Exercise 4: temperature_convert() ---")
# TODO


# ── EXERCISE 5 ──────────────────────────────
# Write a function `make_greeting(name, greeting="Hello")` with a default param.
# Calling make_greeting("Erik") should return "Hello, Erik!"
# Calling make_greeting("Erik", "Hey") should return "Hey, Erik!"
# Print both.

print("\n--- Exercise 5: Default Parameters ---")
# TODO


# ── EXERCISE 6 ──────────────────────────────
# Write a function `summarize(numbers)` that takes a list of numbers and returns:
# (minimum, maximum, average) as three separate values.
# Test with [4, 7, 2, 9, 1, 5].
# Hint: use min(), max(), sum(), len() built-ins.

print("\n--- Exercise 6: summarize() ---")
# TODO


# ── EXERCISE 7 — CHALLENGE ──────────────────
# Write a function `is_palindrome(word)` that returns True if the word reads
# the same forwards and backwards (e.g., "racecar", "level", "noon").
# Test with: "racecar", "hello", "level", "python"
# Hint: word == word[::-1] reverses a string.

print("\n--- Exercise 7: is_palindrome() ---")
# TODO


print("\n" + "=" * 40)
print("Done! Update PROGRESS.md, then commit.")
print("=" * 40)
