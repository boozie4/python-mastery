# Day 2 — Control Flow: if / elif / else

## Making Decisions in Code

Programs need to make choices. Control flow lets your code take different paths based on conditions.

## The if Statement

```python
temperature = 75

if temperature > 80:
    print("It's hot outside.")
```

- The condition (`temperature > 80`) evaluates to `True` or `False`.
- The **indented block** only runs if the condition is `True`.
- Python uses **4 spaces** of indentation (not tabs).

## if / else

```python
temperature = 75

if temperature > 80:
    print("It's hot.")
else:
    print("It's comfortable.")
```

## if / elif / else

```python
temperature = 75

if temperature > 90:
    print("Very hot!")
elif temperature > 70:
    print("Comfortable.")
elif temperature > 50:
    print("A bit cool.")
else:
    print("Cold!")
```

Only **one** branch runs — Python checks top to bottom and stops at the first `True`.

## Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | equal to | `age == 30` |
| `!=` | not equal to | `name != "Bob"` |
| `>` | greater than | `score > 90` |
| `<` | less than | `score < 60` |
| `>=` | greater than or equal | `age >= 18` |
| `<=` | less than or equal | `age <= 65` |

**Important:** `=` assigns a value. `==` compares two values.

## Logical Operators

Combine multiple conditions:

```python
age = 25
has_license = True

if age >= 16 and has_license:
    print("You can drive.")

if age < 18 or age > 65:
    print("Special rate applies.")

if not has_license:
    print("You need a license.")
```

| Operator | True when... |
|----------|-------------|
| `and` | **both** conditions are True |
| `or` | **at least one** condition is True |
| `not` | the condition is **False** |

## Truthy and Falsy

In Python, conditions don't have to be `True`/`False` explicitly:

```python
name = ""
if name:          # Empty string is falsy
    print("Hello, " + name)
else:
    print("No name given.")

count = 0
if count:         # 0 is falsy
    print("Has items")
else:
    print("Empty")
```

**Falsy values:** `False`, `0`, `0.0`, `""`, `None`, `[]`, `{}`
**Everything else is truthy.**

## Nested if

```python
score = 85
passed = True

if passed:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    else:
        print("C")
else:
    print("Failed")
```

Keep nesting shallow — deeply nested code is hard to read.

---

**Next:** Open `exercises.py` and work through each problem.
