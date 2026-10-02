n = int(input("Enter your number: "))

# Check if n is a palindrome using arithmetic (no string conversion)
ispalindrome = "Yes"
left = n
right = 0
while n > 0:
  digit = n % 10
  right = right * 10 + digit
  n = n // 10
  
if left == right:
  print(ispalindrome)
else:
  print("No")