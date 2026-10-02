n = int(input())
arr = list(map(int, input().split()))
print(arr)

# Compute and print the alternating sum

result = 0
for i in range(len(arr)):
  if i % 2 != 0:
    result -= arr[i]
    #num += 2
  else:
    result += arr[i]
print(result)