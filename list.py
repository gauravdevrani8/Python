
# Example 1: Using `pop()` to remove the last element or a specific index
numbers = [10, 20, 30, 40]
last_value = numbers.pop()  # Removes the last element from the list

# Example 2: Using `.remove()` to remove the first occurrence of a value
numbers = [10, 20, 30, 10]
numbers.remove(10)  # Removes the first occurrence of 10

# Example 3: Using `insert()` to add a value at a specific index
names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")  # Inserts "David" at index 1

# Example 4: Using `.copy()` to create a shallow copy of a list
original_list = [1, 2, 3]
copied_list = original_list.copy()  # Creates a shallow copy of the original list
copied_list.append(4)  # Modifying the copied list does not affect the original

# Example 5: Generating a list using list comprehensions
squares = [x**2 for x in range(10)]  # Generates squares of numbers from 0 to 9

# Example 6: Replacing an element in a list by index
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"  # Replace the element at index 1 (banana)

# Example 7: Replacing multiple elements in a list using slicing
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [10, 20, 30]  # Replace elements from index 1 to 3

# Example 8: Deleting an element by index
fruits = ["apple", "banana", "cherry"]
del fruits[1]  # Deletes the element at index 1 (banana)

# Example 9: Clearing all elements from a list
numbers = [1, 2, 3, 4, 5]
numbers.clear()  # Removes all elements from the list

# Example 10: Using `pop()` to remove and return an element by index
fruits = ["apple", "banana", "cherry"]
removed_element = fruits.pop(1)  # Removes and returns the element at index 1 (banana)

# Additional List Methods

# Example 11: Using `sort()` to sort a list in ascending order
numbers = [5, 3, 8, 6, 7, 2]
numbers.sort()  # Sorts the list in-place in ascending order

# Example 12: Using `reverse()` to reverse the order of the list
numbers = [5, 3, 8, 6, 7, 2]
numbers.reverse()  # Reverses the list in-place

# Example 13: Using `index()` to find the index of the first occurrence of a value
fruits = ["apple", "banana", "cherry"]
index_of_banana = fruits.index("banana")  # Finds the index of "banana"

# Example 14: Using `count()` to count the occurrences of a value in the list
fruits = ["apple", "banana", "cherry", "banana"]
banana_count = fruits.count("banana")  # Counts how many times "banana" appears

# Example 15: Using `extend()` to add elements from another iterable to a list
fruits = ["apple", "banana"]
extra_fruits = ["cherry", "date"]
fruits.extend(extra_fruits)  # Adds elements from extra_fruits to fruits

# Example 16: Using `all()` to check if all elements in the list are true
bool_list = [True, True, False]
all_true = all(bool_list)  # Returns True if all elements are True

# Example 17: Using `any()` to check if any element in the list is true
any_true = any(bool_list)  # Returns True if any element is True

# Example 18: Using `min()` to get the smallest element in the list
numbers = [10, 20, 30, 40]
min_value = min(numbers)  # Finds the smallest value in the list

# Example 19: Using `max()` to get the largest element in the list
max_value = max(numbers)  # Finds the largest value in the list

# Example 20: Using `sum()` to calculate the sum of all elements in the list
total_sum = sum(numbers)  # Sums up all the elements in the list

# Example 21: Using `zip()` to combine two lists into pairs
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
combined = list(zip(names, scores))  # Combines the two lists into pairs
