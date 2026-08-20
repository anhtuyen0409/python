# methods of list
# 1. add list element (1 element): append()
my_lst = [1, 3, 6, 8, -10]
my_lst.append(12)
print(my_lst)

# 2. add elements: extend()
lst_1 = [1, 3, 5, 7, 9]
lst_2 = ["hello", "hi"]
lst_1.extend(lst_2)
print(lst_1)

# 3. sort list: sort() or sorted()
# cach 1
lst_3 = [5, 3, 7, -5, 10]
lst_3.sort() # tang dan
print(lst_3)
lst_3.sort(reverse=True) # giam dan
print(lst_3)

# cach 2: sorted
lst_4 = [6, 8, 2, -5, 12]
new_lst = sorted(lst_4) # tao ra 1 list moi la new_lst, lst_4 khong thay doi
print(lst_4)
print(new_lst)

# 4. reverse list
# cach 1
lst_5 = [3, 5, -10, 4, 8]
lst_5.reverse()
print(lst_5) # [8, 4, -10, 5, 3]

#cach 2
lst_6 = [2, 4, 5, 7, 9]
lst_7 = lst_6[::-1]
print(lst_7) # [9, 7, 5, 4, 2]
# 5. insert element: insert(index, value)
lst_8 = [1, 2, 3, 4, 5]
lst_8.insert(1, 6)
print(lst_8) # [1, 6, 2, 3, 4, 5]

# 6. delete element: del list_name[index] or remove(ele)
lst_9 = [3, 5, 7, 9, 12]
del lst_9[0]
print(lst_9) # [5, 7, 9, 12]

lst_10 = [1, 2, 3, 4, 5]
del lst_10[:2]
print(lst_10) # [3, 4, 5]

# 7. tra ve index dau tien cua element duoc khop: index() (ko co error)
lst_11 = [3, 5, 10, 34, 22]
ind = lst_11.index(10)
print(ind) # 2
# 8. pop(index) ko truyen xoa ele cuoi
lst_12 = [2, 4, 6, 8, 10]
ele = lst_12.pop(3)
print(ele) # 8
print(lst_12) # [2, 4, 6, 10]