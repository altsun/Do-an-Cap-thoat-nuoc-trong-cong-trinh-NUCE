# Import
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Classes
class ChonSoDoCapNuoc(QDialog):
    def __init__(self):
        # Initialize QDialog
        QDialog.__init__(self)

        # Create layout
        layout = QGridLayout()

        # Create elements
        self.nhan_so_lieu = QLabel('NHẬP SỐ LIỆU')
        self.nhan_so_tang = QLabel('Số tầng')
        self.nhap_so_tang = QLineEdit()
        self.nhan_h_tang = QLabel('Chiều cao mỗi tầng (m)')
        self.nhap_h_tang = QLineEdit()
        self.nhan_h_dd = QLabel('Tổn thất dọc đường (m)')
        self.nhap_h_dd = QLineEdit()
        self.nhan_h_cb = QLabel('Tổn thất cục bộ (% tổn thất dọc đường)')
        self.nhap_h_cb = QLineEdit()
        self.nhan_h_dong_ho = QLabel('Tổn thất qua đồng hồ (m)')
        self.nhap_h_dong_ho = QLineEdit()
        self.nhan_h_chon_ong = QLabel('Độ sâu chôn ống (m)')
        self.nhap_h_chon_ong = QLineEdit()
        self.nhan_z_san_nha = QLabel('Cao độ sân nhà (m)')
        self.nhap_z_san_nha = QLineEdit()
        self.nhan_z_nen_tang_1 = QLabel('Cao độ nền tầng 1 (m)')
        self.nhap_z_nen_tang_1 = QLineEdit()
        self.nhan_h_ngoai_max = QLabel('Áp lực bên ngoài max (m)')
        self.nhap_h_ngoai_max = QLineEdit()
        self.nhan_h_ngoai_min = QLabel('Áp lực bên ngoài min (m)')
        self.nhap_h_ngoai_min = QLineEdit()
        self.nhan_ma_so = QLabel('Thiết bị vệ sinh bất lợi nhất (m)')
        self.nhap_ma_so = QButtonGroup()
        self.nhan_sen = QLabel('Sen')
        self.sen = QRadioButton()
        self.nhan_rua = QLabel('Rửa')
        self.rua = QRadioButton()
        self.nhan_xi = QLabel('Xí')
        self.xi = QRadioButton()
        self.tinh = QPushButton('Tính')
        self.ket_qua = QTextEdit()

        # Prepare elements
            # Add radio buttons to group
        self.nhap_ma_so.addButton(self.sen, 0)
        self.nhap_ma_so.addButton(self.rua, 1)
        self.nhap_ma_so.addButton(self.xi, 2)
            # Set alignment for labels
        self.nhan_so_lieu.setAlignment(Qt.AlignHCenter)
        self.nhan_sen.setAlignment(Qt.AlignRight)
        self.nhan_rua.setAlignment(Qt.AlignRight)
        self.nhan_xi.setAlignment(Qt.AlignRight)
            # Set button sen checked
        self.sen.setChecked(True)
            # Set ket_qua to read-only
        self.ket_qua.setReadOnly(True)

        # Add elements to layout
        layout.addWidget(self.nhan_so_lieu, 0, 0)
        layout.addWidget(self.nhan_so_tang, 1, 0)
        layout.addWidget(self.nhap_so_tang, 1, 1)
        layout.addWidget(self.nhan_h_tang, 2, 0)
        layout.addWidget(self.nhap_h_tang, 2, 1)
        layout.addWidget(self.nhan_h_dd, 3, 0)
        layout.addWidget(self.nhap_h_dd, 3, 1)
        layout.addWidget(self.nhan_h_cb, 4, 0)
        layout.addWidget(self.nhap_h_cb, 4, 1)
        layout.addWidget(self.nhan_h_dong_ho, 5, 0)
        layout.addWidget(self.nhap_h_dong_ho, 5, 1)
        layout.addWidget(self.nhan_h_chon_ong, 6, 0)
        layout.addWidget(self.nhap_h_chon_ong, 6, 1)
        layout.addWidget(self.nhan_z_san_nha, 7, 0)
        layout.addWidget(self.nhap_z_san_nha, 7, 1)
        layout.addWidget(self.nhan_z_nen_tang_1, 8, 0)
        layout.addWidget(self.nhap_z_nen_tang_1, 8, 1)
        layout.addWidget(self.nhan_h_ngoai_max, 9, 0)
        layout.addWidget(self.nhap_h_ngoai_max, 9, 1)
        layout.addWidget(self.nhan_h_ngoai_min, 10, 0)
        layout.addWidget(self.nhap_h_ngoai_min, 10, 1)
        layout.addWidget(self.nhan_ma_so, 11, 0)
        layout.addWidget(self.nhan_sen, 12, 0)
        layout.addWidget(self.sen, 12, 1)
        layout.addWidget(self.nhan_rua, 13, 0)
        layout.addWidget(self.rua, 13, 1)
        layout.addWidget(self.nhan_xi, 14, 0)
        layout.addWidget(self.xi, 14, 1)
        layout.addWidget(self.tinh, 15, 0, 1, -1)   # span horizontal
        layout.addWidget(self.ket_qua, 16, 0, 1, -1)    # span horizontal

        # Set layout
        self.setLayout(layout)

        # Initialize UI
        self.init_ui()

        # Handle events
        self.tinh.clicked.connect(self.xuat_ket_qua)

    # Front-end functions
    def init_ui(self):
        # Set window title
        self.setWindowTitle('Chọn sơ đồ cấp nước')

        # Set window size
        self.setGeometry(50, 50, 400, 500)

        # Set window at center
        self.center()

        # Remove default focus
        self.setFocus()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    # Back-end functions
    def khoi_tao_thiet_bi(self, ma_so):
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
    # khoi_tao_thiet_bi

    def tra_so_lieu(self):
        '''
        Trả về số liệu đã nhập vào form

        return: tuple or None
        '''
        try:
            so_tang = int(self.nhap_so_tang.text())
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại số tầng')
            return None  # -> người dùng phải nhập lại

        try:
            h_tang = float(self.nhap_h_tang.text())
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại chiều cao mỗi tầng')
            return None  # -> người dùng phải nhập lại

        try:
            h_dd = float(self.nhap_h_dd.text())
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại tổn thất dọc đường')
            return None  # -> người dùng phải nhập lại
        
        try:
            h_cb = float(self.nhap_h_cb.text()) / 100 * h_dd
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại tổn thất cục bộ')
            return None  # -> người dùng phải nhập lại

        try:
            h_dong_ho = float(self.nhap_h_dong_ho.text())
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại tổn thất qua đồng hồ')
            return None  # -> người dùng phải nhập lại
        
        try:
            h_chon_ong = float(self.nhap_h_chon_ong.text())
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại độ sâu chôn ống')
            return None # -> người dùng phải nhập lại
        
        try:
            z_san_nha = float(self.nhap_z_san_nha.text())
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại cao độ sân nhà')
            return None # -> người dùng phải nhập lại

        try:
            z_nen_tang_1 = float(self.nhap_z_nen_tang_1.text())
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại cao độ nền tầng 1')
            return None # -> người dùng phải nhập lại
        
        try:
            h_ngoai_max = float(self.nhap_h_ngoai_max.text())
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại áp lực bên ngoài max')
            return None # -> người dùng phải nhập lại
        
        try:
            h_ngoai_min = float(self.nhap_h_ngoai_min.text())
        except:
            canh_bao = QMessageBox.warning(self, 'Số liệu không hợp lệ', 'Vui lòng nhập lại áp lực bên ngoài min')
            return None # -> người dùng phải nhập lại
        
        if self.sen.isChecked():
            ma_so = 1
        elif self.rua.isChecked():
            ma_so = 2
        elif self.xi.isChecked():
            ma_so = 3
        thiet_bi_bat_loi_nhat = self.khoi_tao_thiet_bi(ma_so)

        so_lieu = (so_tang, h_tang, h_dd, h_cb, h_dong_ho, h_chon_ong, z_san_nha, z_nen_tang_1, h_ngoai_max, h_ngoai_min, thiet_bi_bat_loi_nhat)

        return so_lieu
    # tra_so_lieu

    def tinh_ap_luc_can_thiet(self, so_lieu):
        '''
        Tính áp lực cần thiết của công trình
        
        so_lieu: tuple <- nhap_so_lieu()
        return: float or None
        '''
        if so_lieu == None:
            return None
        
        so_tang, h_tang, h_dd, h_cb, h_dong_ho, h_chon_ong, z_san_nha, z_nen_tang_1, h_ngoai_max, h_ngoai_min, thiet_bi_bat_loi_nhat = so_lieu
        z = thiet_bi_bat_loi_nhat['z']
        h_td = thiet_bi_bat_loi_nhat['h_td']
        h_ct = (h_chon_ong + z_nen_tang_1 - z_san_nha + (so_tang-1) * h_tang + z) + h_dong_ho + h_dd + h_cb + h_td
        return h_ct
    # tinh_ap_luc_can_thiet

    def chon_so_do(self, so_lieu):
        '''
        Chọn sơ đồ cấp nước
        so_lieu: tuple <- tra_so_lieu()
        return: dict or None
        '''
        if so_lieu == None:
            return None
        
        so_tang, h_tang, h_dd, h_cb, h_dong_ho, h_chon_ong, z_san_nha, z_nen_tang_1, h_ngoai_max, h_ngoai_min, thiet_bi_bat_loi_nhat = so_lieu
        h_ct = self.tinh_ap_luc_can_thiet(so_lieu)
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
    # chon_so_do

    def xuat_ket_qua(self, so_do):
        '''
        Xuất kết quả ra màn hình

        return: None
        '''
        du_lieu = ''

        so_lieu = self.tra_so_lieu()

        if so_lieu == None:
            return None

        h_ct = self.tinh_ap_luc_can_thiet(so_lieu)

        du_lieu += 'Áp lực cần thiết của công trình: {} m\n'.format(format(h_ct, '.1f'))

        so_do = self.chon_so_do(so_lieu)
        du_lieu += 'Chọn sơ đồ cấp nước {sd}\n'.format(sd=so_do['ten'])
        # Nếu có cách chia vùng thì in ra
        cach_chia = so_do['cach chia']
        if cach_chia != {}:
            for k, v in cach_chia.items():
                du_lieu += '\tVùng {a} ({n} tầng): sơ đồ {s}\n'.format(a=k, n=v['so tang'], s=v['so do'])

        self.ket_qua.setText(du_lieu)

        return None
    # xuat_ket_qua

# Main
app = QApplication(sys.argv)
chon_so_do_cap_nuoc = ChonSoDoCapNuoc()
chon_so_do_cap_nuoc.show()
app.exec_()