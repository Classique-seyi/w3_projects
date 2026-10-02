# Read total seconds
total = int(input())

# Calculate hours, minutes, seconds
hours = total // 3600
minutes = (total - (hours*3600)) // 60
seconds = total - (hours*3600) - (minutes*60)
# Print the result
print(f"{hours}h {minutes}m {seconds}s")