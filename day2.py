vowels = ["a", "e", "i", "o", "u"]
count = 0

name = input("Write your name: ").lower()

for letter in name:
    if letter in vowels:
        count += 1

print(count)
