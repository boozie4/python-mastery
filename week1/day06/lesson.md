# Day 6 — Dictionaries and Sets

## Dictionaries

A dictionary stores **key-value pairs**. Keys must be unique. Think of it like a real dictionary: look up a word (key) to get a definition (value).

```python
person = {
    "name": "Erik",
    "age": 32,
    "city": "Lake Geneva"
}
```

## Accessing Values

```python
person["name"]          # "Erik"
person.get("age")       # 32
person.get("email")     # None — safe, no error if key missing
person.get("email", "N/A")  # "N/A" — default if missing
```

Using `dict["key"]` raises a `KeyError` if missing. `dict.get("key")` returns `None` instead.

## Adding and Updating

```python
person["email"] = "erik@example.com"   # add new key
person["age"] = 33                      # update existing key
```

## Removing

```python
del person["city"]          # delete key
person.pop("email")         # delete and return the value
person.pop("phone", None)   # safe — no error if missing
```

## Checking for Keys

```python
"name" in person    # True
"phone" in person   # False
```

## Looping Over Dictionaries

```python
# Keys only
for key in person:
    print(key)

# Values only
for value in person.values():
    print(value)

# Both
for key, value in person.items():
    print(f"{key}: {value}")
```

## Nested Dictionaries

```python
users = {
    "erik": {"age": 32, "city": "Lake Geneva"},
    "alice": {"age": 28, "city": "Chicago"},
}
print(users["erik"]["city"])   # Lake Geneva
```

## Sets

A set is an **unordered collection of unique values**. No duplicates allowed.

```python
colors = {"red", "blue", "green", "red"}  # "red" stored only once
print(colors)   # {'red', 'blue', 'green'} — order not guaranteed

empty_set = set()    # NOT {} — that creates an empty dict
```

## Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # union: {1, 2, 3, 4, 5, 6}
a & b    # intersection: {3, 4}
a - b    # difference: {1, 2}  — in a but not b
a ^ b    # symmetric difference: {1, 2, 5, 6}  — in one but not both
```

## Common Set Uses

```python
# Remove duplicates from a list
items = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(items))   # [1, 2, 3, 4]

# Fast membership testing
valid_colors = {"red", "green", "blue"}
if "red" in valid_colors:   # O(1) — much faster than a list
    print("Valid!")
```

---

**When to use which:**
- **Dict** → you need to look things up by name/key
- **Set** → you need unique values or fast membership checks

**Next:** Open `exercises.py`.
