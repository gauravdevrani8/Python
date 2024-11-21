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

