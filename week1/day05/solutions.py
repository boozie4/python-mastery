# Day 5 Solutions

print("=" * 40)
print("DAY 5 SOLUTIONS")
print("=" * 40)

print("\n--- Exercise 1 ---")
foods = ["pizza", "tacos", "sushi", "burgers", "pasta"]
print(foods[0])           # first
print(foods[-1])          # last
print(foods[len(foods)//2])  # middle
print(foods[::-1])        # reversed

print("\n--- Exercise 2 ---")
scores = [88, 72, 95, 61, 83, 79, 91]
scores.append(100)
scores.remove(61)
scores[0] = 90
scores.sort(reverse=True)
print(scores)

print("\n--- Exercise 3 ---")
def list_stats(numbers):
    print(f"Count: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Average: {sum(numbers)/len(numbers):.2f}")

list_stats([10, 24, 3, 57, 18, 42])

print("\n--- Exercise 4 ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)

print("\n--- Exercise 5 ---")
person = ("Erik", "Boozell", 32)
first_name, last_name, age = person
print(f"Full name: {first_name} {last_name}, Age: {age}")

print("\n--- Exercise 6 ---")
def find_duplicates(items):
    seen = []
    duplicates = []
    for item in items:
        if items.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))  # [1, 2]

print("\n--- Exercise 7 ---")
cart = []
while True:
    command = input("Enter command (add/remove/view/quit): ").strip()
    if command.startswith("add "):
        item = command[4:]
        cart.append(item)
        print(f"Added '{item}' to cart.")
    elif command.startswith("remove "):
        item = command[7:]
        if item in cart:
            cart.remove(item)
            print(f"Removed '{item}'.")
        else:
            print(f"'{item}' not in cart.")
    elif command == "view":
        print("Cart:", cart if cart else "(empty)")
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("Unknown command.")
