# Day 6 Exercises — Dictionaries and Sets
# Run: python exercises.py

print("=" * 40)
print("DAY 6 EXERCISES")
print("=" * 40)

# ── EXERCISE 1 ──────────────────────────────
# Create a dictionary for a product with keys:
#   name, price, quantity, in_stock (bool)
# Print each key-value pair using .items().

print("\n--- Exercise 1: Product Dict ---")
# TODO


# ── EXERCISE 2 ──────────────────────────────
# Word frequency counter.
# Count how many times each word appears in this sentence.
# Use a dict where keys are words and values are counts.

print("\n--- Exercise 2: Word Frequency ---")
sentence = "the quick brown fox jumps over the lazy dog the fox"
# TODO: split the sentence into words with .split()
# TODO: build a frequency dict
# TODO: print each word and its count


# ── EXERCISE 3 ──────────────────────────────
# Safe access with .get()
# Given this config dict, print each setting.
# For missing keys, print a default value.

print("\n--- Exercise 3: Safe Access ---")
config = {
    "debug": True,
    "max_retries": 3,
    "timeout": 30
}
# TODO: print config["debug"]
# TODO: print config["max_retries"]
# TODO: print config.get("host", "localhost")   — missing, use default
# TODO: print config.get("port", 8080)          — missing, use default
# TODO: print config.get("timeout", 60)         — exists, ignore default


# ── EXERCISE 4 ──────────────────────────────
# Phonebook. Build a dict of name → phone number.
# Add at least 4 contacts.
# Ask the user for a name.
# Print the phone number, or "Contact not found." if not in phonebook.

print("\n--- Exercise 4: Phonebook ---")
phonebook = {}
# TODO: add contacts
# TODO: ask for name, look up and print


# ── EXERCISE 5 ──────────────────────────────
# Set operations.
# You have two lists of students.
# Find: students in both classes, students in only class_a, all unique students.

print("\n--- Exercise 5: Set Operations ---")
class_a = ["Alice", "Bob", "Charlie", "Diana", "Erik"]
class_b = ["Charlie", "Diana", "Frank", "Grace", "Erik"]

# TODO: Convert to sets
# TODO: Print students in BOTH classes (intersection)
# TODO: Print students ONLY in class_a (difference)
# TODO: Print ALL unique students (union)


# ── EXERCISE 6 ──────────────────────────────
# Remove duplicates from a list while preserving order.
# (A set removes duplicates but loses order — do it another way.)
# Input: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Expected output: [3, 1, 4, 5, 9, 2, 6]
# Hint: use a set to track what you've seen.

print("\n--- Exercise 6: Remove Duplicates (Ordered) ---")
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# TODO


# ── EXERCISE 7 — CHALLENGE ──────────────────
# Grade book using nested dicts.
# Structure: {"student_name": {"math": score, "english": score, "science": score}}
# Add at least 3 students with 3 subject scores each.
# Print each student's name and their average score.

print("\n--- Exercise 7: Grade Book ---")
gradebook = {}
# TODO: populate gradebook
# TODO: print name and average for each student


print("\n" + "=" * 40)
print("Done! Update PROGRESS.md, then commit.")
print("=" * 40)
