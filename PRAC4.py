# Given list
list = [1, 1, 3, 2, 4, 6, 5, 7, 5, 0, 0]

# a. Print the list without repeating items
single_items = []
for item in list:
    if item not in single_items:
        single_items.append(item)
print("items: Single display:", single_items)

 # b. Print the repeated items
repeated_items = []
for item in list:
    if list.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)
print("items: repeated items:", repeated_items)

# c. Calculate and print the Average for each list
avg_single = sum(single_items) / len(single_items)
avg_repeated = sum(repeated_items) / len(repeated_items)
print("Average of single items list:", avg_single)
print("Average of repeated items list:", avg_repeated)

# d. Print the maximum number in the original list using a loop
max_num = list[0]
for num in list:
    if num > max_num:
        max_num = num
print("Maximum number in the original list:", max_num)