# Day 3 Solutions

print("=" * 40)
print("DAY 3 SOLUTIONS")
print("=" * 40)

print("\n--- Exercise 1 ---")
for i in range(1, 21):
    print(i)

print("\n--- Exercise 2 ---")
total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050

print("\n--- Exercise 3 ---")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

print("\n--- Exercise 4 ---")
count = 10
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

print("\n--- Exercise 5 ---")
for i in range(1, 31):
    if i % 2 != 0:
        continue
    print(i)

print("\n--- Exercise 6 ---")
secret_number = 42
guesses = 0
while True:
    guess = int(input("Guess the number (1-100): "))
    guesses += 1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You got it in {guesses} guesses.")
        break

print("\n--- Exercise 7 ---")
height = int(input("Triangle height: "))
for i in range(1, height + 1):
    print("*" * i)
