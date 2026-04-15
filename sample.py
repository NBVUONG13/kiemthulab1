def kiem_tra_so_chan(danh_sach):
    count = 0
    for so in danh_sach:
        if so % 2 == 0:
            count += 1
    return count