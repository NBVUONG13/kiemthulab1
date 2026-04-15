def kiem_tra_so_chan_le(danh_sach_so):
    """
    Phương thức phân loại số chẵn và số lẻ từ một danh sách.
    """
    print(f"Danh sách cần kiểm tra: {danh_sach_so}\n")
    
    # 1. VÒNG LẶP: Duyệt qua từng con số trong danh sách
    for so in danh_sach_so:
        
        # 2. LỆNH RẼ NHÁNH: Kiểm tra điều kiện chia hết cho 2
        if so % 2 == 0:
            print(f"Số {so} là: Số Chẵn")
        else:
            print(f"Số {so} là: Số Lẻ")

# --- Phần thân chương trình chính ---
# Khởi tạo một danh sách các số ngẫu nhiên
cac_con_so = [12, 7, 3, 24, 19, 10]

# Gọi phương thức để thực thi
kiem_tra_so_chan_le(cac_con_so)