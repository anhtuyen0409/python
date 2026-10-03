# cách tạo list thông thường
# lst = [1, 2, 3, 4, 5]
# new_lst = []
# for x in lst:
#     new_lst.append(x ** 2)
# print(new_lst)

# list comprehension
# lst = [1, 2, 3, 4, 5]
# new_lst = [x ** 2 for x in lst]
# print(new_lst)

# filter element
# [expression for item in iterable if condition == true]
# lst = [1, 2, 3, 4, 5]
# new_lst = [x for x in lst if x % 2 == 1]
# print(new_lst)

# apply function to each element
# [expression_1 if condition == true else expression_2 for item in iterable]
# lst = [1, 2, 3, 4, 5]
# new_lst = [x if x % 2 == 0 else x + 2 for x in lst] # nếu x chẵn thì giữ nguyên, x lẻ thì + thêm 2
# print(new_lst) # [3, 2, 5, 4, 7]

# dictionary comprehension
# [k: v for item in iterable]
# lst = [1, 2, 3, 4, 5]
# new_dict = {k: k**2 for k in lst}
# print(new_dict)

# # set comprehension
# # {item for item in iterable}
# my_string = "minmin"
# new_set = {letter for letter in my_string}
# print(new_set)

# Multiple loops
# nested_lst = [[i for i in range(5)] for _ in range(5)] # for lồng nhau
# print(nested_lst)

arr_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# flatten_lst = [num for row in arr_2d for num in row]
# print(flatten_lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_lst = []
for row in arr_2d:
    for num in row:
        new_lst.append(num)
print(new_lst)