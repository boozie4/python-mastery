# Day 7 — String Methods + Week 1 Mini Project

## String Methods

Strings have powerful built-in methods. Remember: strings are **immutable** — methods return new strings, they don't change the original.

```python
s = "  Hello, World!  "

s.upper()           # "  HELLO, WORLD!  "
s.lower()           # "  hello, world!  "
s.strip()           # "Hello, World!"    — removes leading/trailing whitespace
s.lstrip()          # "Hello, World!  "  — left only
s.rstrip()          # "  Hello, World!"  — right only
s.replace("World", "Python")  # "  Hello, Python!  "
s.split(", ")       # ["  Hello", "World!  "]
s.split()           # ["Hello,", "World!"]  — split on any whitespace
```

## Checking String Content

```python
"hello".startswith("he")   # True
"hello".endswith("lo")     # True
"hello".find("ll")         # 2  — index of first match, -1 if not found
"hello".count("l")         # 2
"  ".isspace()             # True
"hello".isalpha()          # True — all letters
"123".isdigit()            # True — all digits
"hello123".isalnum()       # True — all letters or digits
```

## Joining

```python
words = ["Python", "is", "awesome"]
" ".join(words)    # "Python is awesome"
"-".join(words)    # "Python-is-awesome"
", ".join(words)   # "Python, is, awesome"
```

## f-strings — Advanced Usage

```python
name = "Erik"
score = 95.678
price = 19.99

f"{name.upper()}"         # "ERIK"
f"{score:.2f}"            # "95.68"  — 2 decimal places
f"{price:>10.2f}"         # "     19.99"  — right-align in 10 chars
f"{42:05d}"               # "00042"  — pad with zeros
f"{1000000:,}"            # "1,000,000"  — thousands separator
```

## String Formatting Recap

```python
# Three ways — prefer f-strings (modern)
f"Hello, {name}!"                    # f-string (best)
"Hello, {}!".format(name)            # .format()
"Hello, %s!" % name                  # % formatting (old, avoid)
```

---

## Week 1 Mini Project: Text Analyzer

Build a program that analyzes a block of text. This brings together everything from Week 1:
- Variables and types (Day 1)
- Control flow (Day 2)
- Loops (Day 3)
- Functions (Day 4)
- Lists (Day 5)
- Dictionaries (Day 6)
- Strings (Day 7)

See `exercises.py` for the full specification.

---

**Quick String Reference:**

| Method | What it does |
|--------|-------------|
| `.upper()` / `.lower()` | Change case |
| `.strip()` | Remove whitespace from ends |
| `.split(sep)` | Split into list |
| `sep.join(list)` | Join list into string |
| `.replace(old, new)` | Replace substring |
| `.find(sub)` | Find index of substring |
| `.startswith(s)` / `.endswith(s)` | Check start/end |
| `.count(sub)` | Count occurrences |
