# List Methods

# Example 1: Using `pop()` to remove the last element or a specific index
numbers = [10, 20, 30, 40]
last_value = numbers.pop()  # Removes the last element from the list
print("After pop:", numbers)  # Output: [10, 20, 30]
print("Popped value:", last_value)  # Output: 40

# Example 2: Using `.remove()` to remove the first occurrence of a value
numbers = [10, 20, 30, 10]
numbers.remove(10)  # Removes the first occurrence of 10
print("After remove:", numbers)  # Output: [20, 30, 10]

# Example 3: Using `insert()` to add a value at a specific index
names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")  # Inserts "David" at index 1
print("After insert:", names)  # Output: ['Alice', 'David', 'Bob', 'Charlie']

# Example 4: Using `.copy()` to create a shallow copy of a list
original_list = [1, 2, 3]
copied_list = original_list.copy()  # Creates a shallow copy of the original list
copied_list.append(4)  # Modifying the copied list does not affect the original
print("Original list:", original_list)  # Output: [1, 2, 3]
print("Copied list:", copied_list)  # Output: [1, 2, 3, 4]

# Example 5: Generating a list using list comprehensions
squares = [x**2 for x in range(10)]  # Generates squares of numbers from 0 to 9
print("Squares:", squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 6: Replacing an element in a list by index
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"  # Replace the element at index 1 (banana)
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# Example 7: Replacing multiple elements in a list using slicing
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [10, 20, 30]  # Replace elements from index 1 to 3
print(numbers)  # Output: [1, 10, 20, 30, 5]

# Example 8: Deleting an element by index
fruits = ["apple", "banana", "cherry"]
del fruits[1]  # Deletes the element at index 1 (banana)
print(fruits)  # Output: ['apple', 'cherry']

# Example 9: Clearing all elements from a list
numbers = [1, 2, 3, 4, 5]
numbers.clear()  # Removes all elements from the list
print(numbers)  # Output: []

# Example 10: Using `pop()` to remove and return an element by index
fruits = ["apple", "banana", "cherry"]
removed_element = fruits.pop(1)  # Removes and returns the element at index 1 (banana)
print(fruits)  # Output: ['apple', 'cherry']
print("Removed element:", removed_element)  # Output: 'banana'

# Additional List Methods

# Example 11: Using `sort()` to sort a list in ascending order
numbers = [5, 3, 8, 6, 7, 2]
numbers.sort()  # Sorts the list in-place in ascending order
print("Sorted numbers:", numbers)  # Output: [2, 3, 5, 6, 7, 8]

# Example 12: Using `reverse()` to reverse the order of the list
numbers = [5, 3, 8, 6, 7, 2]
numbers.reverse()  # Reverses the list in-place
print("Reversed numbers:", numbers)  # Output: [2, 7, 6, 8, 3, 5]

# Example 13: Using `index()` to find the index of the first occurrence of a value
fruits = ["apple", "banana", "cherry"]
index_of_banana = fruits.index("banana")  # Finds the index of "banana"
print("Index of banana:", index_of_banana)  # Output: 1

# Example 14: Using `count()` to count the occurrences of a value in the list
fruits = ["apple", "banana", "cherry", "banana"]
banana_count = fruits.count("banana")  # Counts how many times "banana" appears
print("Count of 'banana':", banana_count)  # Output: 2

# Example 15: Using `extend()` to add elements from another iterable to a list
fruits = ["apple", "banana"]
extra_fruits = ["cherry", "date"]
fruits.extend(extra_fruits)  # Adds elements from extra_fruits to fruits
print("Extended fruits:", fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Example 16: Using `all()` to check if all elements in the list are true
bool_list = [True, True, False]
all_true = all(bool_list)  # Returns True if all elements are True
print("All elements are true:", all_true)  # Output: False

# Example 17: Using `any()` to check if any element in the list is true
any_true = any(bool_list)  # Returns True if any element is True
print("Any element is true:", any_true)  # Output: True

# Example 18: Using `min()` to get the smallest element in the list
numbers = [10, 20, 30, 40]
min_value = min(numbers)  # Finds the smallest value in the list
print("Minimum value:", min_value)  # Output: 10

# Example 19: Using `max()` to get the largest element in the list
max_value = max(numbers)  # Finds the largest value in the list
print("Maximum value:", max_value)  # Output: 40

# Example 20: Using `sum()` to calculate the sum of all elements in the list
total_sum = sum(numbers)  # Sums up all the elements in the list
print("Total sum:", total_sum)  # Output: 100

# Example 21: Using `zip()` to combine two lists into pairs
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
combined = list(zip(names, scores))  # Combines the two lists into pairs
print("Zipped result:", combined)  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 95)]
