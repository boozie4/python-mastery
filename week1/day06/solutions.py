# Day 6 Solutions

print("=" * 40)
print("DAY 6 SOLUTIONS")
print("=" * 40)

print("\n--- Exercise 1 ---")
product = {
    "name": "Wireless Keyboard",
    "price": 79.99,
    "quantity": 50,
    "in_stock": True
}
for key, value in product.items():
    print(f"{key}: {value}")

print("\n--- Exercise 2 ---")
sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
for word, count in freq.items():
    print(f"{word}: {count}")

print("\n--- Exercise 3 ---")
config = {"debug": True, "max_retries": 3, "timeout": 30}
print(config["debug"])
print(config["max_retries"])
print(config.get("host", "localhost"))
print(config.get("port", 8080))
print(config.get("timeout", 60))

print("\n--- Exercise 4 ---")
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012",
    "Diana": "555-3456"
}
name = input("Look up contact: ")
print(phonebook.get(name, "Contact not found."))

print("\n--- Exercise 5 ---")
class_a = {"Alice", "Bob", "Charlie", "Diana", "Erik"}
class_b = {"Charlie", "Diana", "Frank", "Grace", "Erik"}
print("In both:", class_a & class_b)
print("Only in class A:", class_a - class_b)
print("All students:", class_a | class_b)

print("\n--- Exercise 6 ---")
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
seen = set()
result = []
for item in items:
    if item not in seen:
        result.append(item)
        seen.add(item)
print(result)  # [3, 1, 4, 5, 9, 2, 6]

print("\n--- Exercise 7 ---")
gradebook = {
    "Alice": {"math": 92, "english": 88, "science": 95},
    "Bob": {"math": 75, "english": 82, "science": 79},
    "Charlie": {"math": 98, "english": 91, "science": 87},
}
for student, grades in gradebook.items():
    avg = sum(grades.values()) / len(grades)
    print(f"{student}: {avg:.1f}")
