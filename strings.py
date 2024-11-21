# strings methods
# 
# Question 1: Concatenate "Hello" and "World!" with a space in between
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # Concatenates with a space in between
print(result)

# Question 2: Extract "Programming" from the string "PythonProgramming" using slicing
s = "PythonProgramming"
substring = s[6:]  # Extracts characters from index 6 to the end
print(substring)

# Some basics of strings

# Initialize the list of tea varieties
tea_varities = ['Black', 'green', 'Masala', 'White']

# Slicing at index 1 to 1 results in an empty list
print(tea_varities[1:1])

# Insert two elements at index 1 using slicing
tea_varities[1:1] = ["test", "test"]
print(tea_varities)

# Slice from index 1 to 2
print(tea_varities[1:2])

# Slice from index 1 to 3
print(tea_varities[1:3])

# Remove the elements in the slice from index 1 to 3
tea_varities[1:3] = []
print(tea_varities)

# String Operations

# Example 1: String concatenation using the `+` operator
original_string = "Hello"
new_data = " World"
result = original_string + new_data  # Concatenates two strings
print("Concatenated string:", result)

# Example 2: Using f-strings for string formatting
original_string = "Hello"
new_data = "World"
result = f"{original_string} {new_data}"  # Embeds variables directly into the string
print("Formatted string:", result)

# Example 3: Inserting a substring using slicing
original_string = "HelloWorld"
position = 5
substring = " "
new_string = original_string[:position] + substring + original_string[position:]
print("String after insertion:", new_string)

# Example 4: Repeating strings using multiplication
repeated_string = "Ha" * 3  # Repeats "Ha" 3 times
print("Repeated string:", repeated_string)

# Replacing a substring in a string
original_string = "I like apples"
updated_string = original_string.replace("apples", "bananas")
print(updated_string)

# Modifying a string by replacing a character
original_string = "Hello"
updated_string = original_string[:3] + "y" + original_string[4:]
print(updated_string)

# Removing part of a string using slicing
original_string = "Hello World"
updated_string = original_string[:5]  # Removes " World"
print(updated_string)

# Removing characters from a string by converting it to a list and deleting elements
original_list = list("Hello World")
del original_list[5:]  # Removes the space and "World"
updated_string = ''.join(original_list)
print(updated_string)

# Additional String Methods

# 1. String Length
text = "Hello"
length = len(text)
print("Length of text:", length)

# 2. Converting to Uppercase and Lowercase
text = "hello"
upper_text = text.upper()  # Converts to uppercase
lower_text = text.lower()  # Converts to lowercase
print("Uppercase:", upper_text)
print("Lowercase:", lower_text)

# 3. Checking if a String Starts or Ends with a Substring
text = "Hello World"
print(text.startswith("Hello"))
print(text.endswith("World"))

# 4. Stripping Whitespace
text = "  Hello World  "
clean_text = text.strip()  # Removes whitespace from both sides
print("Stripped text:", clean_text)

# 5. Splitting a String
text = "Hello World Python"
words = text.split()  # Splits by default whitespace
print("Splitted text:", words)

# 6. Joining List Elements into a String
words = ['Hello', 'World', 'Python']
sentence = ' '.join(words)  # Joins with a space
print("Joined sentence:", sentence)

# 7. Finding a Substring
text = "Hello World"
index = text.find("World")
print("Index of 'World':", index)

# 8. Counting Substring Occurrences
text = "Hello Hello World"
count = text.count("Hello")
print("Count of 'Hello':", count)

# 9. Replacing Substring
text = "I like apples"
updated_text = text.replace("apples", "bananas")
print("Updated text:", updated_text)

# 10. String Formatting with format()
name = "Alice"
age = 25
sentence = "My name is {} and I am {} years old.".format(name, age)
print("Formatted sentence:", sentence)

# 11. String Reversal
text = "Hello"
reversed_text = text[::-1]
print("Reversed text:", reversed_text)

# 12. Checking for Digits
text = "12345"
print("Is digit:", text.isdigit())

# 13. Checking for Alphabetic Characters
text = "Hello"
print("Is alphabetic:", text.isalpha())

# 14. String Padding
text = "42"
padded_text = text.zfill(5)  # Pads with zeros to make length 5
print("Padded text:", padded_text)



