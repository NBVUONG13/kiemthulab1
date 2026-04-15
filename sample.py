# Nhập một số nguyên từ bàn phím
n = int(input("Nhập một số nguyên: "))

# Vòng lặp từ 1 đến n
for i in range(1, n + 1):
    # Lệnh rẽ nhánh kiểm tra số chẵn/lẻ
    if i % 2 == 0:
        print(i, "là số chẵn")
    else:
        print(i, "là số lẻ")