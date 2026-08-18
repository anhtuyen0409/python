# Tao list
my_lst = [3, 5.5, "hello", [7, 8]]
print(my_lst)
print(type(my_lst))

# do dai list
print(len(my_lst))

# index duong (0 -> len()-1)
print(my_lst[1]) # 5.5

# index am (-len() -> -1)
print(my_lst[-1]) # [7, 8]

print(my_lst[1:]) # [5.5, "hello", [7, 8]]
print(my_lst[:-1]) # [3, 5.5, "hello"]

# duyet cac phan tu trong list
for x in my_lst:
    print(x)

# noi list
lst_1 = [1, 2.5, 3]
lst_2 = ["hello", "hi"]
concat_lst = lst_1 + lst_2
print(concat_lst)

# list is mutable
# sau khi dinh nghia 1 list, co the thay doi gia tri cac phan tu trong list
lst_3 = [1, 2, 3]
lst_3[1] = "hello"
print(lst_3) # [1, "hello", 3]