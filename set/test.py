# thao tác với nhiều set bằng cách | & - ^
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# union
new_set = A | B # tạo ra set mới và 2 set ban đầu giữ nguyên (nếu sử dụng cách A.union(B) thì nó sẽ update trực tiếp set A)
print(f"Hợp của A và B: {new_set}")

# intersection
new_set_inter = A & B
print(f"Giao của A và B: {new_set_inter}")

# symetric difference
new_set_sym_dif = A ^ B # tập hợp các phần tử chỉ mỗi set mới có
print(new_set_sym_dif) # {1, 2, 5, 6}

# difference
new_set_dif_A = A - B # các phần tử trong set A chỉ set A mới có mà set B không có
print(new_set_dif_A) # {1, 2}

new_set_dif_B = B - A # các phần tử trong set B chỉ set B mới có mà set A không có
print(new_set_dif_B) # {5, 6}