# Day 5 — Lists and Tuples

## Lists

A list is an **ordered, mutable** collection of items. Items can be any type.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [3, 1, 4, 1, 5, 9]
mixed = ["Erik", 32, True, None]
empty = []
```

## Indexing and Slicing

```python
fruits = ["apple", "banana", "cherry", "date"]

fruits[0]     # "apple"   — first item
fruits[-1]    # "date"    — last item
fruits[1:3]   # ["banana", "cherry"]  — index 1 up to (not including) 3
fruits[:2]    # ["apple", "banana"]   — from start to index 2
fruits[2:]    # ["cherry", "date"]    — from index 2 to end
fruits[::-1]  # ["date", "cherry", "banana", "apple"]  — reversed
```

## Modifying Lists

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("date")        # add to end
fruits.insert(1, "avocado")  # insert at index 1
fruits.remove("banana")      # remove first occurrence
fruits.pop()                 # remove and return last item
fruits.pop(0)                # remove and return item at index 0

fruits[0] = "mango"          # change an item
```

## Useful List Methods and Functions

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

len(numbers)         # 8  — length
sum(numbers)         # 31 — sum
min(numbers)         # 1  — minimum
max(numbers)         # 9  — maximum
numbers.sort()       # sort in place: [1, 1, 2, 3, 4, 5, 6, 9]
sorted(numbers)      # returns new sorted list, original unchanged
numbers.reverse()    # reverse in place
numbers.count(1)     # 2  — how many times 1 appears
numbers.index(4)     # position of first 4
```

## Checking Membership

```python
fruits = ["apple", "banana", "cherry"]
"banana" in fruits   # True
"mango" in fruits    # False
```

## Looping Over Lists

```python
for fruit in fruits:
    print(fruit)

# With index:
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

## Tuples

A tuple is like a list, but **immutable** — you can't change it after creation. Use parentheses (or just commas):

```python
point = (3, 7)
rgb = (255, 128, 0)
single = (42,)     # trailing comma needed for single-item tuple

point[0]    # 3
point[1]    # 7
```

Tuples are faster than lists and signal "this data shouldn't change" — e.g., coordinates, RGB colors, database rows.

## Unpacking

```python
point = (3, 7)
x, y = point
print(x, y)   # 3 7

first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

---

**When to use which:**
- **List** → ordered collection that will change (shopping cart, scores)
- **Tuple** → fixed collection that won't change (coordinates, config values)

**Next:** Open `exercises.py`.
