# Day 1 — Variables, Data Types, and Basic I/O

## What is a Variable?

A variable is a named container for storing a value. In Python, you don't declare types — Python figures it out.

```python
name = "Erik"       # str (string)
age = 32            # int (integer)
height = 6.1        # float (decimal number)
is_founder = True   # bool (True or False)
nothing = None      # NoneType (absence of value)
```

## The 5 Core Data Types

| Type | Example | Use |
|------|---------|-----|
| `str` | `"hello"` | Text |
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `bool` | `True` / `False` | Yes/No logic |
| `None` | `None` | No value / empty |

## Checking the Type

```python
x = 42
print(type(x))   # <class 'int'>
```

## Basic Math Operators

```python
10 + 3   # 13  — addition
10 - 3   # 7   — subtraction
10 * 3   # 30  — multiplication
10 / 3   # 3.333... — division (always float)
10 // 3  # 3   — floor division (drops remainder)
10 % 3   # 1   — modulo (remainder only)
10 ** 3  # 1000 — exponentiation (power)
```

## String Basics

```python
greeting = "Hello"
name = "Erik"

# Concatenation (joining)
message = greeting + ", " + name + "!"
print(message)   # Hello, Erik!

# f-strings (the modern, preferred way)
message = f"Hello, {name}! You are {age} years old."
print(message)
```

## Getting Input from the User

```python
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
```

`input()` always returns a **string**. To use it as a number, convert it:

```python
age = int(input("How old are you? "))
years_left = 45 - age
print(f"You have {years_left} years until 45.")
```

## Type Conversion

```python
int("42")       # "42" → 42
float("3.14")   # "3.14" → 3.14
str(100)        # 100 → "100"
bool(0)         # 0 → False (0 is falsy)
bool(1)         # 1 → True (anything non-zero is truthy)
```

---

## Key Rules to Remember

1. Variable names are **case-sensitive**: `age` and `Age` are different.
2. Variable names can't start with a number: `2things` is invalid.
3. Use **snake_case** for variable names: `first_name`, not `firstName`.
4. Use `print()` to see output. Use `type()` to inspect what something is.

---

**Next:** Open `exercises.py` and work through each problem. Run with `python exercises.py`.
