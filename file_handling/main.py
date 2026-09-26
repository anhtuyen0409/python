# read file
# file_obj = open("my_file.txt")
# content = file_obj.read()
# print(content)
# file_obj.close()

# sử dụng context manager đọc file
with open("my_file.txt") as file_obj:
    content = file_obj.read()
    print(content)

# write file - tạo file mới là new_file.txt
# with open("new_file.txt", "w") as f:
#     f.write("I am a software engineer")

# ghi tiếp nội dung vào file new_file.txt - append "a"
with open("new_file.txt", "a") as f:
    f.write("\nI love my job")

# x
with open("file.txt", "x") as f:
    pass