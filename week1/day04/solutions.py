# Day 4 Solutions

print("=" * 40)
print("DAY 4 SOLUTIONS")
print("=" * 40)

print("\n--- Exercise 1 ---")
def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

greet("Erik")
greet("Alice")
greet("Bob")

print("\n--- Exercise 2 ---")
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(f"3 + 5 = {add(3, 5)}")
print(f"3 * 5 = {multiply(3, 5)}")

print("\n--- Exercise 3 ---")
def is_even(n):
    return n % 2 == 0

for i in range(1, 11):
    print(f"{i}: {is_even(i)}")

print("\n--- Exercise 4 ---")
def temperature_convert(value, unit):
    """Convert between Celsius and Fahrenheit."""
    if unit == "C":
        return round((value * 9/5) + 32, 1)
    elif unit == "F":
        return round((value - 32) * 5/9, 1)

print(temperature_convert(100, "C"))  # 212.0
print(temperature_convert(32, "F"))   # 0.0

print("\n--- Exercise 5 ---")
def make_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(make_greeting("Erik"))
print(make_greeting("Erik", "Hey"))

print("\n--- Exercise 6 ---")
def summarize(numbers):
    """Return (min, max, average) of a list."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

nums = [4, 7, 2, 9, 1, 5]
low, high, avg = summarize(nums)
print(f"Min: {low}, Max: {high}, Avg: {avg:.2f}")

print("\n--- Exercise 7 ---")
def is_palindrome(word):
    """Return True if word is the same forwards and backwards."""
    return word == word[::-1]

for w in ["racecar", "hello", "level", "python"]:
    print(f"{w}: {is_palindrome(w)}")
