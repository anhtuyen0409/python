import random

so_dung = random.randint(1, 50) # ngẫu nhiên từ 1 đến 50
so_ban_doan = None
so_lan_doan = 5 # người dùng được phép đoán tối đa 5 lần

print("----------------GAME ĐOÁN SỐ-----------------")
print("Chương trình đưa ra số ngẫu nhiên từ 1 đến 50")
print("Bạn chỉ có ", so_lan_doan, " lần dự đoán")
print("Chúc may mắn nhé!!!")
print("---------------------------------------------")

while so_ban_doan != so_dung and so_lan_doan > 0:
    so_ban_doan = int(input("Nhập số bạn đoán: "))
    so_lan_doan -= 1

    if so_lan_doan >= 0:
        if so_ban_doan < so_dung:
            print("Số bạn đoán nhỏ hơn")
        elif so_ban_doan > so_dung:
            print("Số bạn đoán lớn hơn")
        else:
            print("Bạn đã đoán chính xác ^_^")
            print("Số của chương trình là: ", so_dung)
            break

        if so_lan_doan > 0:
            print("Bạn còn ", so_lan_doan, " lần dự đoán")
        else:
            print("Bạn đã hết lượt dự đoán :(( ")
            print("Số của chương trình là: ", so_dung)
    