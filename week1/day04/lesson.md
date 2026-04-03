# Day 4 — Functions

## What is a Function?

A function is a named, reusable block of code. You define it once, call it as many times as you need.

```python
def greet():
    print("Hello!")

greet()   # Hello!
greet()   # Hello!
```

## Parameters and Arguments

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Erik")   # Hello, Erik!
greet("Alice")  # Hello, Alice!
```

- **Parameter**: the variable in the function definition (`name`)
- **Argument**: the actual value passed in when calling (`"Erik"`)

## Multiple Parameters

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8
```

## `return`

`return` sends a value back to the caller. Without it, the function returns `None`.

```python
def square(n):
    return n * n

x = square(4)   # x = 16
print(x)
```

You can return early:

```python
def is_even(n):
    if n % 2 == 0:
        return True
    return False
```

## Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Erik")            # Hello, Erik!
greet("Erik", "Hey")     # Hey, Erik!
```

Default parameters must come **after** regular parameters.

## Keyword Arguments

```python
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe(age=32, city="Lake Geneva", name="Erik")  # order doesn't matter
```

## Scope — Local vs Global

Variables inside a function are **local** — they don't exist outside:

```python
def my_func():
    x = 10      # local to my_func
    print(x)

my_func()
print(x)   # NameError — x doesn't exist here
```

## Docstrings

Document your functions:

```python
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32
```

## Multiple Return Values

Python can return multiple values as a tuple:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)   # 1 9
```

---

**Key rules:**
1. `def` keyword starts a function definition.
2. Always indent the function body.
3. `return` sends a value back — without it you get `None`.
4. Functions should do **one thing** well.

**Next:** Open `exercises.py`.
