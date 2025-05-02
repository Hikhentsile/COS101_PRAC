# Initialize variables
ages = []
count = 0

# Ask 10 people for their ages
while count < 10:
    age = int(input(f"Enter age of person {count + 1}: "))
    ages.append(age)
    count += 1

# Calculate youngest, oldest, average, and count above 25
youngest = min(ages)
oldest = max(ages)
average_age = sum(ages) / len(ages)

# Count how many people are above 25
above_25 = 0
index = 0
while index < len(ages):
    if ages[index] > 25:
        above_25 += 1
    index += 1

print()
# Display results
print("-------------------------------------------")
print(f"Youngest age: {youngest}")
print(f"Oldest age: {oldest}")
print(f"Average age: {average_age:.2f}")
print(f"Number of people older than 25: {above_25}")
print("-------------------------------------------")
