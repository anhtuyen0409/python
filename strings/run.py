my_string = "Hello world"
print(my_string)
print(type(my_string))

# chieu dai str len()
print(len(my_string))

# truy cap den ki tu -> index
# index duong: 0 -> len(str) - 1
print(my_string[0]) # H
# index am: -len(str) -> -1
print(my_string[-1]) # d

# slicing for string
print(my_string[1:4]) # indices: 1, 2, 3 -> kq: 'ell'
print(my_string[1:]) # indices: 1, 2, 3,... -> kq: 'ello world'
print(my_string[:-1]) # kq: 'Hello worl'

# noi chuoi
str_1 = "Hello"
str_2 = " everyone"
str_concat = str_1 + str_2
print(str_concat)

# duyet qua cac ki tu trong chuoi
my_str = "Hello"
for str in my_str:
    print(str)

# kiem tra chuoi con co trong chuoi khong?
str_3 = "Hello anh em"
if "anh" in str_3:
    print("OK")
else:
    print("No")