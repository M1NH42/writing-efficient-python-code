# hands on some of the important and most frequently used built-in functions
# 1 range(lower_limit, upper_limit)
# 2 range(start, stop, step)

# we can use range in number of different ways

print(list(range(0, 20, 2)))

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(nums_list2)
