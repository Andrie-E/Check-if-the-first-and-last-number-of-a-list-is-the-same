# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Pseudocode

# Create the function
def is_first_and_last_same(numbers):
    return len(numbers) > 0 and numbers[0] == numbers[-1]
# Provide the list
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
# Test the function
result_x = is_first_and_last_same(numbers_x)
result_y = is_first_and_last_same(numbers_y)
# Print
print(f"given list: {numbers_x}")
print(f"result is: {result_x}")
print(f"numbers_y: {numbers_y}")
print(f"result is: {result_y}")