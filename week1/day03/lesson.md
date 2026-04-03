# Day 3 — Loops: for, while, break, continue

## Why Loops?

Loops let you repeat actions without rewriting the same code. Python has two kinds.

## The `for` Loop

Use when you know **what you're iterating over**.

```python
# Loop over a range of numbers
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
# Output: 1 3 5 7 9

# Loop over a string
for letter in "Python":
    print(letter)
# Output: P y t h o n
```

`range(5)` produces: 0, 1, 2, 3, 4 — it stops **before** the end number.

## The `while` Loop

Use when you loop until a **condition becomes False**.

```python
count = 0
while count < 5:
    print(count)
    count += 1   # count = count + 1
# Output: 0 1 2 3 4
```

**Danger:** If the condition never becomes False, you get an infinite loop. Always make sure something changes in the loop body.

## `break` — Exit the Loop Early

```python
for i in range(10):
    if i == 5:
        break       # stop the loop entirely
    print(i)
# Output: 0 1 2 3 4
```

## `continue` — Skip to the Next Iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)
# Output: 1 3 5 7 9
```

## Accumulator Pattern

A very common pattern — build up a result across iterations:

```python
total = 0
for i in range(1, 6):
    total += i      # total = total + i
print(total)        # 15  (1+2+3+4+5)
```

## Nested Loops

A loop inside a loop:

```python
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()     # newline after each row
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
```

## `while True` with `break`

A common pattern for "keep asking until valid input":

```python
while True:
    answer = input("Type 'quit' to exit: ")
    if answer == "quit":
        break
    print(f"You said: {answer}")
```

## `enumerate` — Loop with Index

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

---

**Next:** Open `exercises.py` and work through each problem.
