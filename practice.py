# find the largest number in list 

li = [1, 2, 3, 4, 5]
largest_no = [0]
for i in li:
    if i > largest_no[0]:
        largest_no[0] = i
print(largest_no)