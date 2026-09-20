# có 1 string "hello"
# đầu ra: có 1 dictionary {"h": 1, "e": 1, "l": 2, "o": 1} - không tính khoảng trắng

#my_string = "welcome to my first program"
my_string = input("Nhập đầu vào: ")
my_dict = dict() # tạo 1 dictionary rỗng

# dùng vòng lặp for để duyệt qua các kí tự trong chuôi
for c in my_string:
    if c == " ":
        continue 
    else:
        # nếu c chưa phải là key trong dictionary thì ta phải khởi tạo trước -> tránh bị lỗi
        if c not in my_dict.keys():
            my_dict[c] = 1
        else:
            my_dict[c] += 1 # nếu c đã có trong dictionary thì tăng value lên 1

print("Số lần xuất hiện của các kí tự: ", my_dict)