word = input().strip().lower()

# Check if palindrome and print
ispalindrome = "Yes"
reversed_word = word[::-1]

if word == reversed_word:
  print(ispalindrome)
else:
  print("No")