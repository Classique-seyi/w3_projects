text = input().strip().lower()

# Count vowels and print
vowels = ["a", "e", "i", "o", "u"]
count = 0
for letter in text:
  if letter in vowels:
    count += 1
print(f"Vowels: {count}")