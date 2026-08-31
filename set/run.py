# tao set
# my_set = {"a", "b"}
# print(my_set, type(my_set))

# tao set rong
# my_set = set()

# khong cho phep cac phan tu lap lai
# my_set = {'a', 'b', 'a', 'b'}
# print(my_set) # {'a', 'b'}

# check set là unorder (mỗi lần chạy lại thứ tự các phần tử sẽ khác nhau)
# my_set = {'a', 'b', 'c', 'd'}
# print(my_set)

# update set
my_set = {'a', 'b', 'c', 'd'}
my_set.add('e') # thêm phần tử
print(my_set)
my_set.discard('a') # xoá phần tử
print(my_set)

# thao tác với nhiều set
my_set_1 = {'a', 'b', 'c', 'd'}
my_set_2 = {'c', 'd', 'e', 'f'}
# lấy phần giao của 2 set
new_set_1 = my_set_1.intersection(my_set_2)
print(f"Giao của 2 set: {new_set_1}") # {'c', 'd'}
# hợp của 2 set
new_set_2 = my_set_1.union(my_set_2)
print(f"Hợp của 2 set: {new_set_2}") # {'a', 'b', 'c', 'd', 'e', 'f'}
# các phần tử chỉ 2 set mới có
new_set_3 = my_set_1.symmetric_difference(my_set_2)
print(new_set_3) # {'a', 'b', 'e', 'f'}