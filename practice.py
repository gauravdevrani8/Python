# find the largest number in list 

# li = [1, 2, 3, 4, 5]
# largest_no = [0]
# for i in li:
#     if i > largest_no[0]:
#         largest_no[0] = i
# print(largest_no)

# # find even numbers in list and store it in new list 
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# list2 = []
# for i in list1:
#     if i % 2 == 0:
#         list2.append(i)
# print(list2)

# # print star pattern 

# # method 1 
# n = 5
# for i in range(1, n + 1):
#     print('*' * i)
# # or 
# print("--------------------------------------------------------------------------------------")

# for i in range(1,6):
#     print('*' * i)
# # method 2

# n = 5
# for i in range(1, n + 1):
#     for j in range(i):
#         print('*', end='')
#     print()  # Move to the next line

# # method 3
# n = 5
# for i in range(1, n + 1):
#     print(''.join(['*' for _ in range(i)]))

# # method 4 
# def print_pattern(n, i=1):
#     if i > n:
#         return
#     print('*' * i)
#     print_pattern(n, i + 1)

# n = 5
# print_pattern(n)

# # method 5
# n = 5
# i = 1
# while i <= n:
#     print('*' * i)
#     i += 1


# # upside down start pattern 
# for i in range(6,0,-1):
#     print('*' * i)
# # print
# # 55555
# # 4444
# # 333
# # 22
# # 1

# for i in range(5, 0,-1):  
#     print(str(i) * i)      

# # method 2 

# for i in range(5, 0, -1):  # Outer loop for numbers from 5 to 1
#     for j in range(i):     # Inner loop to repeat the number 'i' times
#         print(i, end='')   # Print 'i' without moving to a new line
#     print()                # Move to the next line after inner loop

# # print
# # 1  
# # 22  
# # 333  
# # 4444  
# # 55555

# for i in range(1,6):
#     print(str(i)*i)


# # method 2

# for i in range(1, 6):     # Outer loop: Numbers from 1 to 5
#     for j in range(i):    # Inner loop: Repeat the number `i` times
#         print(i, end='')  # Print the number without moving to a new line
#     print()               # Move to the next line after inner loop


# # print
# # 1
# #   2
# #     3
# #       4
# #         5


# for i in range(1, 6):  # Loop through numbers 1 to 5
#     print(' ' * (i - 1) + str(i))  # Add (i-1) spaces followed by the number i


# # print 
# #     *
# #    ***
# #   *****
# #  *******
# # *********


# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     print(' ' * (n-i) + '*' * (2*i - 1))

# # generate a tabel containing 500 entries of students data
# from random import randint, choice

# data = []
# for i in range(500):
#     name = 'Student ' + str(i + 1)
#     age = randint(18, 25)  # random age between 18 and 25
#     grade = choice(['A', 'B', 'C', 'D', 'F'])  # random grade
#     data.append([name, age, grade])

# print(data)

# # generate random valuable names for table data and age 
# from random import randint, choice
# names =[]
# for i in range(5):
#     name = ''.join(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
#     names.append(name)
# print(names)


print('------------------------------------------------------------------------------------------------------------------------------------')
# continue 
print('------------------------------------------------------------------------------------------------------------------------------------')
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
skip = int(input("Enter the number to skip: "))
for i in range ( start, end ):
    if i == skip:
        continue
    print(i)

#pass
print('------------------------------------------------------------------------------------------------------------------------------------')
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)

# break
print('------------------------------------------------------------------------------------------------------------------------------------')
for i in range(10):
    if i == 5:
        break
    print(i)

# password check 

password = input("Enter your password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long")
    exit()

if not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter")
    exit()

if not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter")
    exit()

if not any(char.isdigit() for char in password):
    print("Password must contain at least one digit")
    exit()

print("Password is valid")