# find the largest number in list 

li = [1, 2, 3, 4, 5]
largest_no = [0]
for i in li:
    if i > largest_no[0]:
        largest_no[0] = i
print(largest_no)

# find even numbers in list and store it in new list 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
list2 = []
for i in list1:
    if i % 2 == 0:
        list2.append(i)
print(list2)

# print star pattern 

# method 1 
n = 5
for i in range(1, n + 1):
    print('*' * i)
# or 
print("--------------------------------------------------------------------------------------")

for i in range(1,6):
    print('*' * i)
# method 2

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()  # Move to the next line

# method 3
n = 5
for i in range(1, n + 1):
    print(''.join(['*' for _ in range(i)]))

# method 4 
def print_pattern(n, i=1):
    if i > n:
        return
    print('*' * i)
    print_pattern(n, i + 1)

n = 5
print_pattern(n)

# method 5
n = 5
i = 1
while i <= n:
    print('*' * i)
    i += 1


# upside down start pattern 
for i in range(6,0,-1):
    print('*' * i)
# print
# 55555
# 4444
# 333
# 22
# 1

for i in range(5, 0,-1):  
    print(str(i) * i)      

# method 2 

for i in range(5, 0, -1):  # Outer loop for numbers from 5 to 1
    for j in range(i):     # Inner loop to repeat the number 'i' times
        print(i, end='')   # Print 'i' without moving to a new line
    print()                # Move to the next line after inner loop
