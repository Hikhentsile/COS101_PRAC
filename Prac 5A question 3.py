### Q3:
def count_odd_numbers(*numbers):

    odd_count = 0
    for num in numbers:
        # A number is odd if dividing by 2 leaves remainder 1
        if num % 2 != 0:
            odd_count = odd_count + 1
    return odd_count


sequence = (1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9)
result = count_odd_numbers(1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9)
print("Total number of odd numbers in the sequence:", result)