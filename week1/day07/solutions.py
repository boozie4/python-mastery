# Day 7 Solutions

import string

print("=" * 40)
print("DAY 7 SOLUTIONS")
print("=" * 40)

print("\n--- Exercise 1 ---")
raw = "  python programming is GREAT!  "
stripped = raw.strip()
print(stripped)
print(stripped.lower())
print(stripped.upper())
print(stripped.replace("GREAT", "awesome"))
print(stripped.lower().split())
print(stripped.lower().count("i"))

print("\n--- Exercise 2 ---")
def is_valid_username(username):
    if not (3 <= len(username) <= 20):
        return False
    if not username.isalnum():
        return False
    if username[0].isdigit():
        return False
    return True

tests = ["erik32", "a", "hello world", "2cool", "ValidUser123", "this_has_underscore"]
for t in tests:
    print(f"{t!r}: {is_valid_username(t)}")

print("\n--- Exercise 3 ---")
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print(encrypt("hello", 3))          # khoor
print(encrypt("Hello, World!", 5))  # Mjqqt, Btwqi!

print("\n" + "=" * 40)
print("WEEK 1 MINI PROJECT SOLUTIONS")
print("=" * 40)

sample_text = """
Python is a versatile programming language. Python is used for web development,
data science, automation, and artificial intelligence. Many developers love Python
because it is easy to read and write. The Python community is large and supportive.
Learning Python opens many career doors. Python powers companies like Google,
Instagram, and Dropbox.
"""

def basic_stats(text):
    print("--- Basic Stats ---")
    print(f"Characters (with spaces): {len(text)}")
    print(f"Characters (no spaces): {len(text.replace(' ', ''))}")
    words = text.split()
    print(f"Words: {len(words)}")
    print(f"Sentences: {text.count('.')}")
    print(f"Lines: {len(text.strip().splitlines())}")

def word_frequency(text):
    print("--- Word Frequency (Top 5) ---")
    words = text.lower().split()
    cleaned = [w.strip(string.punctuation) for w in words if w.strip(string.punctuation)]
    freq = {}
    for word in cleaned:
        freq[word] = freq.get(word, 0) + 1
    top5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
    for word, count in top5:
        print(f"  {word}: {count}")
    return freq

def search_text(text, keyword):
    print(f"--- Search: '{keyword}' ---")
    lower_text = text.lower()
    count = lower_text.count(keyword.lower())
    print(f"Appears {count} times.")
    sentences = text.replace("\n", " ").split(".")
    for s in sentences:
        if keyword.lower() in s.lower():
            print(f"  ...{s.strip()}...")

def summarize(text):
    words = text.split()
    sentences = text.count(".")
    freq = {}
    for w in text.lower().split():
        w = w.strip(string.punctuation)
        if w:
            freq[w] = freq.get(w, 0) + 1
    most_common = max(freq, key=freq.get)
    print(f"Summary: {len(words)} words, {sentences} sentences, most common word: '{most_common}'")

basic_stats(sample_text)
print()
word_frequency(sample_text)
print()
search_text(sample_text, "Python")
print()
summarize(sample_text)
