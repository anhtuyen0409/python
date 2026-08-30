# khoi tao dictionary
name_age = {"Nam": 1, "Bac": 2, "Tay": 3}
# tao dictionary rong
# name_age = dict()
# name_age = {}

# truy cap
print(name_age["Bac"]) # 2

# update phan tu
name_age["Nam"] = 4
print(name_age)

# them phan tu
name_age["Dong"] = 5
print(name_age)

# duyet cac phan tu
# duyet theo keys
# cach 1
for k in name_age:
    print(k)
# cach 2
for k in name_age.keys():
    print(k)

# duyet theo values
for v in name_age.values():
    print(v)

# duyet theo key, value
for k, v in name_age.items():
    print(k, v)