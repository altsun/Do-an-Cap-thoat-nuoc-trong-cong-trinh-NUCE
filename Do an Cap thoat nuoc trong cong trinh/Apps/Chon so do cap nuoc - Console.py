# Functions
def khoi_tao_thiet_bi(ma_so):
    '''
    Các thông số của các thiết bị vệ sinh

    ma_so: int

    return: dict
    '''
    cac_thiet_bi = [
        # 1. Sen
        {
            'ten': 'Sen',
            'z': 1.0,
            'h_td': 3.0,
        },

        # 2. Rửa
        {
            'ten': 'Rửa',
            'z': 0.5,
            'h_td': 2.0,
        },

        # 3. Xí
        {
            'ten': 'Xí',
            'z': 0.2,
            'h_td': 1.0,
        },
    ]

    thiet_bi = cac_thiet_bi[ma_so-1]

    return thiet_bi

def nhap_so_lieu():
    '''
    Nhập các số liệu đầu vào

    return: tuple
    '''
    print('Nhập các số liệu')
    so_tang = int(input('Nhập số tầng của công trình: '))
    h_tang = float(input('Nhập chiều cao mỗi tầng (m): '))
    h_dd = float(input('Nhập tổn thất dọc đường (m): '))
    h_cb = float(input('Tổn thất cục bộ bằng bao nhiêu % của tổn thất dọc đường (20 - 30%): ')) / 100 * h_dd
    h_dong_ho = float(input('Nhập tổn thất qua đồng hồ (m): '))
    h_chon_ong = float(input('Nhập độ sâu chôn ống (m): '))
    z_san_nha = float(input('Nhập cao độ sân nhà (m): '))
    z_nen_tang_1 = float(input('Nhập cao độ nền tầng 1 (m): '))
    h_ngoai_max = float(input('Nhập áp lực bên ngoài max (m): '))
    h_ngoai_min = float(input('Nhập áp lực bên ngoài min (m): '))
    ma_so = int(input('Thiết bị bất lợi nhất là (1. Sen, 2. Rửa, 3. Xí): '))
    thiet_bi_bat_loi_nhat = khoi_tao_thiet_bi(ma_so)

    return so_tang, h_tang, h_dd, h_cb, h_dong_ho, h_chon_ong, z_san_nha, z_nen_tang_1, h_ngoai_max, h_ngoai_min, thiet_bi_bat_loi_nhat

def in_so_lieu(so_lieu):
    '''
    In ra các số liệu đã nhập với mục đích kiểm tra

    so_lieu: tuple, <- nhap_so_lieu()

    return: None
    '''
    so_tang, h_tang, h_dd, h_cb, h_dong_ho, h_chon_ong, z_san_nha, z_nen_tang_1, h_ngoai_max, h_ngoai_min, thiet_bi_bat_loi_nhat = so_lieu
    print('Các số liệu đã nhập')
    print('Số tầng: {} tầng'.format(so_tang))
    print('Chiều cao mỗi tầng: {} m'.format(h_tang))
    print('Tổn thất dọc đường: {} m'.format(h_dd))
    print('Tổn thất cục bộ: {} m'.format(format(h_cb, '.1f')))
    print('Tổn thất qua đồng hồ: {} m'.format(h_dong_ho))
    print('Độ sâu chôn ống: {} m'.format(h_chon_ong))
    print('Cao độ sân nhà: {} m'.format(z_san_nha))
    print('Cao độ nền tầng 1: {} m'.format(z_nen_tang_1))
    print('Áp lực bên ngoài max: {} m'.format(h_ngoai_max))
    print('Áp lực bên ngoài min: {} m'.format(h_ngoai_min))
    print('Thiết bị bất lợi nhất: ' + thiet_bi_bat_loi_nhat['ten'])

    return None

def tinh_ap_luc_can_thiet(so_lieu):
    '''
    Tính áp lực cần thiết của công trình
    
    so_lieu: tuple <- nhap_so_lieu()

    return: float
    '''
    so_tang, h_tang, h_dd, h_cb, h_dong_ho, h_chon_ong, z_san_nha, z_nen_tang_1, h_ngoai_max, h_ngoai_min, thiet_bi_bat_loi_nhat = so_lieu
    z = thiet_bi_bat_loi_nhat['z']
    h_td = thiet_bi_bat_loi_nhat['h_td']
    h_ct = (h_chon_ong + z_nen_tang_1 - z_san_nha + (so_tang-1) * h_tang + z) + h_dong_ho + h_dd + h_cb + h_td

    return h_ct

def chon_so_do(so_lieu):
    '''
    Chọn sơ đồ cấp nước

    so_lieu: tuple <- nhap_so_lieu()

    return: dict
    '''
    so_tang, h_tang, h_dd, h_cb, h_dong_ho, h_chon_ong, z_san_nha, z_nen_tang_1, h_ngoai_max, h_ngoai_min, thiet_bi_bat_loi_nhat = so_lieu
    h_ct = tinh_ap_luc_can_thiet(so_lieu)
    # Xem nhà có phải là cao tầng hay không
    if so_tang >= 8:
        nha_cao_tang = True
    else:
        nha_cao_tang = False
    
    # Trường hợp nhà thấp tầng
    if not nha_cao_tang:
        ten_so_do = 'Trạm bơm - Két nước - Bể chứa'
        vung = {} # Cách chia vùng, rỗng (vì không cần chia), tuy nhiên vẫn phải trả về
    # Trường hợp nhà cao tầng
    else:
        ten_so_do = 'Phân vùng'
        # Chia vùng
        # Tính xem vùng 1 có dùng sơ đồ đơn giản hay không
        if h_ngoai_min < 8:
            co_don_gian = False
        else:
            co_don_gian = True # Có sơ đồ đơn giản (vùng 1)
        
        if co_don_gian:
            vung = {}
            # Tính số tầng vùng 1
            vung[1] = {}
            vung[1]['so do'] = 'Đơn giản'
            vung[1]['so tang'] = int(1 + (h_ngoai_min - 8) // 4)
            # Số tầng còn lại cần chia
            so_tang_con_lai = so_tang - vung[1]['so tang']
            # Giả sử mỗi vùng có 4 tầng
            so_tang_du = so_tang_con_lai % 4 # số tầng dư
            n = so_tang_con_lai // 4
            so_vung = n + 1
            # Chia cho mỗi vùng 4 tầng
            for i in range(2, so_vung+1):
                vung[i] = {}
                vung[i]['so do'] = 'Trạm bơm - Két nước - Bể chứa'
                vung[i]['so tang'] = 4
            if so_tang_du != 0: # nếu số tầng dư khác 0
                for i in range(2, so_vung+1):
                    if so_tang_du <= 0:
                        break
                    else:
                        vung[i]['so tang'] += 1
                        so_tang_du -= 1
        else:
            vung = {}
            # Số tầng còn lại cần chia
            so_tang_con_lai = so_tang
            # Giả sử mỗi vùng có 4 tầng
            so_tang_du = so_tang_con_lai % 4 # số tầng dư
            n = so_tang_con_lai // 4
            so_vung = n
            # Chia cho mỗi vùng 4 tầng
            for i in range(1, so_vung+1):
                vung[i] = {}
                vung[i]['so do'] = 'Trạm bơm - Két nước - Bể chứa'
                vung[i]['so tang'] = 4
            if so_tang_du != 0: # nếu số tầng dư khác 0
                for i in range(1, so_vung+1):
                    if so_tang_du <= 0:
                        break
                    else:
                        vung[i]['so tang'] += 1
                        so_tang_du -= 1
    
    # Chuẩn bị trả về
    so_do = {'ten': ten_so_do, 'cach chia': vung}

    # Trả về
    return so_do


# Main
so_lieu = nhap_so_lieu()

print()

in_so_lieu(so_lieu)

print()

h_ct = tinh_ap_luc_can_thiet(so_lieu)
print('Áp lực cần thiết của công trình: {} m'.format(format(h_ct, '.1f')))

so_do = chon_so_do(so_lieu)
print('Chọn sơ đồ cấp nước', so_do['ten'])
# Nếu có cách chia vùng thì in ra
cach_chia = so_do['cach chia']
if cach_chia != {}:
    for k, v in cach_chia.items():
        print('\tVùng {a} ({n} tầng): sơ đồ {s}'.format(a=k, n=v['so tang'], s=v['so do']))