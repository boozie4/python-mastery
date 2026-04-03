# Day 7 Exercises — Strings + Week 1 Mini Project
# Run: python exercises.py

print("=" * 40)
print("DAY 7 EXERCISES")
print("=" * 40)

# ── EXERCISE 1 ──────────────────────────────
# String methods practice.
# Given the string below, apply the listed transformations.

print("\n--- Exercise 1: String Methods ---")
raw = "  python programming is GREAT!  "

# TODO: Print it stripped (no whitespace on ends)
# TODO: Print it in all lowercase
# TODO: Print it in all uppercase
# TODO: Replace "GREAT" with "awesome" (do strip first)
# TODO: Split into a list of words and print the list
# TODO: Print the number of times the letter "i" appears (case-insensitive)


# ── EXERCISE 2 ──────────────────────────────
# Username validator.
# A valid username must:
#   - Be between 3 and 20 characters
#   - Contain only letters and numbers (no spaces, no special chars)
#   - Not start with a number
# Write a function `is_valid_username(username)` that returns True/False.
# Test with: "erik32", "a", "hello world", "2cool", "ValidUser123", "this_has_underscore"

print("\n--- Exercise 2: Username Validator ---")
# TODO


# ── EXERCISE 3 ──────────────────────────────
# Caesar cipher — a simple encryption technique.
# Each letter is shifted by a fixed number of positions in the alphabet.
# Write `encrypt(text, shift)` that shifts each letter.
# "hello" with shift=3 → "khoor"
# Keep non-letters unchanged. Wrap around: z+1 = a.
# Hint: use ord() and chr() to get/set ASCII codes.
#   ord('a') = 97, chr(97) = 'a'

print("\n--- Exercise 3: Caesar Cipher ---")
# TODO: define encrypt(text, shift)
# TODO: test with encrypt("hello", 3) → "khoor"
# TODO: test with encrypt("Hello, World!", 5)


# ── WEEK 1 MINI PROJECT ─────────────────────
# TEXT ANALYZER
# Build a program with the following features.
# Organize your code into functions — one function per feature.

print("\n" + "=" * 40)
print("WEEK 1 MINI PROJECT: Text Analyzer")
print("=" * 40)

sample_text = """
Python is a versatile programming language. Python is used for web development,
data science, automation, and artificial intelligence. Many developers love Python
because it is easy to read and write. The Python community is large and supportive.
Learning Python opens many career doors. Python powers companies like Google,
Instagram, and Dropbox.
"""

# FEATURE 1: Basic stats
# Write a function `basic_stats(text)` that prints:
#   - Total characters (including spaces)
#   - Total characters (excluding spaces)
#   - Total words
#   - Total sentences (count periods)
#   - Total lines

def basic_stats(text):
    # TODO
    pass


# FEATURE 2: Word frequency
# Write a function `word_frequency(text)` that:
#   - Converts to lowercase
#   - Strips punctuation from words
#   - Returns a dict of {word: count}
#   - Prints the top 5 most common words

def word_frequency(text):
    # TODO
    pass


# FEATURE 3: Search
# Write a function `search_text(text, keyword)` that:
#   - Prints how many times keyword appears (case-insensitive)
#   - Prints each sentence containing the keyword

def search_text(text, keyword):
    # TODO
    pass


# FEATURE 4: Summary
# Write a function `summarize(text)` that prints a one-line summary:
#   "X words, Y sentences, most common word: 'Z'"

def summarize(text):
    # TODO
    pass


# Run all features
basic_stats(sample_text)
print()
word_frequency(sample_text)
print()
search_text(sample_text, "Python")
print()
summarize(sample_text)

print("\n" + "=" * 40)
print("Week 1 Complete! Update PROGRESS.md, then commit.")
print("=" * 40)
