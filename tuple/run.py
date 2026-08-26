# tuple trong python
# 1. tao tuple
tuple_1 = (3, "a")
print(tuple_1)
print(type(tuple_1))

tuple_2 = ("a")
print(type(tuple_2)) # string
# de khoi tao tuple 1 phan tu, ta can them dau ,
tuple_3 = ("a",)
print(type(tuple_3)) # tuple

# 2. duyet cac phan tu trong tuple
tuple_4 = (2, "a", 3, "b")
print(f"chieu dai cua tuple: {len(tuple_4)}")

for item in tuple_4:
    print(item)

# 3. cong cac tuple
tuple_5 = (3, "a", 4, "b")
tuple_6 = (5, "c", 6, "d")
new_tuple = tuple_5 + tuple_6
print(f"new tuple: {new_tuple}")

# 4. them, xoa phan tu
# tuple khong ho tro viec them xoa phan tu, tai vi tuple khong thay doi (khac voi list)
# vi vay, de them hoac xoa phan tu, minh se convert tuple sang list. Sau khi them, xoa phan tu xong thi se convert sang tuple nhu ban dau
tuple_7 = (1, "a", 2, "b")
list_7 = list(tuple_7)
list_7.append("hello")
list_7.remove(2)
new_tuple = tuple(list_7)
print(f"new tuple: {new_tuple}")

# 5. dem so lan xuat hien cua phan tu trong tuple
tuple_8 = (1, "a", 2, "b", "a")
print(f"so lan xuat hien cua 'a': {tuple_8.count("a")}")
# lay index
print(tuple_8.index("a")) # 1

# vi du
tuple_9 = ([1, 2, 3], 5, 6, "a", "b")
# tuple_9[0] = [0, 2, 3] # loi -> vi tuple khong the sua phan tu
tuple_9[0][0] = 0
print(tuple_9)
print(type(tuple_9[0])) # list
print(type(tuple_9[1])) # int