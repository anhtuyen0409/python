# ví dụ 1
num = int(input("Nhập vào 1 số nguyên: "))
if num % 2 == 0:
    print(f"{num} là số chẵn")
else:
    print(f"{num} là số lẻ")

# ví dụ 2
score = float(input("Nhập vào điểm trung bình học kỳ của bạn: "))
if score >= 8.:
    print("Bạn đạt loại giỏi")
elif score >= 6.5:
    print("Bạn đạt loại khá")
elif score >= 5.:
    print("Bạn đạt loại trung bình")
else:
    print("Cần cố gắng hơn nhé")