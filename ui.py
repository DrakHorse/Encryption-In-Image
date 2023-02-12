"""
Encryption In Image 文本加密
交互界面

本文件完全开源，使用GPL3.0 开源许可证
未经允许，请勿用于商业用途
"""
import time

from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy, QPushButton, QGridLayout, QTextEdit, QLabel, \
    QComboBox, QCheckBox, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt, QPropertyAnimation, QPoint


class QWidgetRoom:
    pass


class SideBarButton(QPushButton):
    """内置侧边栏按钮类"""

    def __init__(self, parent, text, select=False):
        super().__init__(parent=parent, text=text)

        self.setStyleSheet(
            'background: #b8b8b8;'
            'border: 0'
        )

        self.select = select
        self.btn_event = lambda: 0

    def sel(self):
        self.select = True
        if self.select:
            self.setStyleSheet(
                'background: #939393;'
                'border: 0'
            )
        else:
            self.setStyleSheet(
                'background: #b8b8b8;'
                'border: 0'
            )

    def de_sel(self):
        self.select = False
        if self.select:
            self.setStyleSheet(
                'background: #939393;'
                'border: 0'
            )
        else:
            self.setStyleSheet(
                'background: #b8b8b8;'
                'border: 0'
            )

    def enterEvent(self, a0) -> None:
        if self.select:
            def dis():
                self.setStyleSheet(
                    f'background: #{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]};'
                    f'border: 0'
                )
                self.i -= 1
                if self.i <= 160 - 36:
                    self.tmr.stop()

            self.i = 184 - 36
            self.tmr = QTimer()
            self.tmr.setInterval(4)
            self.tmr.timeout.connect(dis)  # noqa
            self.tmr.start()
        else:
            def dis():
                self.setStyleSheet(
                    f'background: #{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]};'
                    f'border: 0'
                )
                self.i -= 1
                if self.i <= 160:
                    self.tmr.stop()

            self.i = 184
            self.tmr = QTimer()
            self.tmr.setInterval(4)
            self.tmr.timeout.connect(dis)  # noqa
            self.tmr.start()

    def leaveEvent(self, a0):
        if self.select:
            def dis():
                self.setStyleSheet(
                    f'background: #{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]};'
                    f'border: 0'
                )
                self.i += 1
                if self.i >= 184 - 36:
                    self.tmr.stop()

            self.i = 160 - 36
            self.tmr = QTimer()
            self.tmr.setInterval(4)
            self.tmr.timeout.connect(dis)  # noqa
            self.tmr.start()
        else:
            def dis():
                self.setStyleSheet(
                    f'background: #{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]};'
                    f'border: 0'
                )
                self.i += 1
                if self.i >= 184:
                    self.tmr.stop()

            self.i = 160
            self.tmr = QTimer()
            self.tmr.setInterval(4)
            self.tmr.timeout.connect(dis)  # noqa
            self.tmr.start()

    def mousePressEvent(self, e):
        if self.select:
            def dis():
                self.setStyleSheet(
                    f'background: #{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]};'
                    f'border: 0'
                )
                self.i -= 1
                if self.i <= 130 - 36:
                    self.tmr.stop()

            self.i = 160 - 36
            self.tmr = QTimer()
            self.tmr.setInterval(2)
            self.tmr.timeout.connect(dis)  # noqa
            self.tmr.start()
        else:
            def dis():
                self.setStyleSheet(
                    f'background: #{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]};'
                    f'border: 0'
                )
                self.i -= 1
                if self.i <= 130:
                    self.tmr.stop()

            self.i = 160
            self.tmr = QTimer()
            self.tmr.setInterval(2)
            self.tmr.timeout.connect(dis)  # noqa
            self.tmr.start()

    def mouseReleaseEvent(self, a0):
        if self.select:
            self.setStyleSheet(
                f'background: #7c7c7c;'
                f'border: 0'
            )
        else:
            def dis():
                self.setStyleSheet(
                    f'background: #{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]};'
                    f'border: 0'
                )
                self.i += 1
                if self.i >= 160:
                    self.tmr.stop()

            self.i = 130
            self.tmr = QTimer()
            self.tmr.setInterval(5)
            self.tmr.timeout.connect(dis)  # noqa
            self.tmr.start()

        self.btn_event()


# noinspection DuplicatedCode
class EIIGUIWindow(QWidget):
    """交互界面主窗口类"""

    def __init__(self):
        super().__init__()
        self.initUI()
        self.page = 'home'

    def initUI(self):
        """
        UI自初始化方法
        :return:
        """

        # 窗口初始化
        self.resize(900, 600)
        self.setWindowTitle("Encryption In Image 文本加密")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setStyleSheet(
            'background: #dedede;'
        )

        # 初始化侧边栏
        self.initSideBar()

        # 初始化各页面
        self.initPage()

    def initSideBar(self):
        """
        初始化侧边栏
        :return:
        """
        # 创建侧边栏
        self.bar_side = QWidget(self)
        self.bar_side.setGeometry(0, 0, 300, 114514)
        self.bar_side.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        self.bar_side.setStyleSheet(
            'background: #c9c9c9;'
        )

        # 侧边栏控件
        self.bar_side_btn_home = SideBarButton(self.bar_side, text='Encryption In Image 主页')
        self.bar_side_btn_home.sel()
        self.bar_side_btn_home.setGeometry(0, 0, 300, 40)
        self.bar_side_btn_home.btn_event = self.To_page_home

        self.bar_side_btn_enc = SideBarButton(self.bar_side, text='文本加密')
        self.bar_side_btn_enc.setGeometry(0, 40, 300, 40)
        self.bar_side_btn_enc.btn_event = self.To_page_enc

        self.bar_side_btn_dec = SideBarButton(self.bar_side, text='文本解密')
        self.bar_side_btn_dec.setGeometry(0, 80, 300, 40)
        self.bar_side_btn_dec.btn_event = self.To_page_dec

    def initPage(self):
        # 主页
        self.pge_home = QWidget(self)
        self.pge_home.setGeometry(300, 0, self.width() - 300, self.height())
        self.pge_home.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        self.pge_home.setStyleSheet(
            'background: #e6e6e6;'
        )

        self.pge_home_main_layout = QGridLayout()
        self.pge_home.setLayout(self.pge_home_main_layout)

        self.pge_home_main_label = QTextEdit()
        self.pge_home_main_label.setHtml(f"""This Only A Test""")
        self.pge_home_main_label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pge_home_main_label.setReadOnly(True)

        self.pge_home_main_layout.addWidget(self.pge_home_main_label, 0, 0)

        # 加密页面
        self.pge_enc = QWidget(self)
        self.pge_enc.setGeometry(300, 0, self.width() - 300, self.height())
        self.pge_enc.setStyleSheet(
            'background: #e6e6e6;'
        )
        self.pge_enc.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)

        self.pge_enc_main_layout = QGridLayout()

        self.pge_enc_room = QWidgetRoom()
        self.pge_enc_room.title = QLabel(self.pge_enc, text='<h1>Encryption In Image 加密</h1>')  # noqa
        self.pge_enc_room.btn_sel_image = QPushButton(self.pge_enc, text="选择图片")
        self.pge_enc_room.btn_sel_image.mouseReleaseEvent = self.C_enc_cel_image
        self.pge_enc_room.inp_sel_image = QLineEdit(self.pge_enc)
        self.pge_enc_room.inp_sel_image.setPlaceholderText("选择一原图或直接输入路径")
        self.pge_enc_room.inp_text = QTextEdit(self.pge_enc)
        self.pge_enc_room.btn_load_file = QPushButton(self.pge_enc, text='从文件中导入')
        self.pge_enc_room.btn_load_file.mouseReleaseEvent = self.C_enc_open_file
        self.pge_enc_room.cbb_file_encoding = QComboBox(self.pge_enc)
        self.pge_enc_room.cbb_file_encoding.addItems(['utf-8', 'utf-16', 'gbk', 'iso-8859-01', 'ascii'])
        self.pge_enc_room.inp_token = QLineEdit()
        self.pge_enc_room.inp_token.setPlaceholderText("留空则不使用密钥")
        self.pge_enc_room.lbl_token = QLabel(self.pge_enc, text='密钥:')  # noqa
        self.pge_enc_room.lbl_token.lower()
        self.pge_enc_room.cbb_des_image = QCheckBox(self.pge_enc, text="破坏原图")  # noqa
        self.pge_enc_room.btn_enc = QPushButton(self.pge_enc, text='加密')
        self.pge_enc_room.inp_log = QTextEdit(self.pge_enc)
        self.pge_enc_room.inp_log.setReadOnly(True)

        self.pge_enc_main_layout.addWidget(self.pge_enc_room.title, 1, 0, 1, 2)
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.btn_sel_image, 2, 0)
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.inp_sel_image, 2, 1)
        self.pge_enc_main_layout.addWidget(QLabel(self.pge_enc, text='文本:'), 3, 0)  # noqa
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.inp_text, 3, 1)
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.btn_load_file, 4, 0)
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.cbb_file_encoding, 4, 1)
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.lbl_token, 5, 0)  # noqa
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.inp_token, 5, 1)
        self.pge_enc_main_layout.addWidget(QLabel(self.pge_enc, text='更多选项:'), 6, 0)  # noqa
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.cbb_des_image, 6, 1)
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.btn_enc, 5, 0, 5, 2)
        self.pge_enc_main_layout.addWidget(QLabel(self.pge_enc, text='输出日志:'), 8, 0)  # noqa
        self.pge_enc_main_layout.addWidget(self.pge_enc_room.inp_log, 8, 1, 8, 2)

        self.pge_enc_main_layout.setColumnStretch(0, 1)
        self.pge_enc_main_layout.setColumnStretch(1, 4)
        self.pge_enc_main_layout.setRowStretch(1, 1)
        self.pge_enc_main_layout.setRowStretch(2, 1)
        self.pge_enc_main_layout.setRowStretch(3, 5)
        self.pge_enc_main_layout.setRowStretch(4, 1)
        self.pge_enc_main_layout.setRowStretch(5, 1)
        self.pge_enc_main_layout.setRowStretch(6, 1)
        self.pge_enc_main_layout.setRowStretch(7, 1)
        self.pge_enc_main_layout.setRowStretch(8, 1)

        self.pge_enc.setLayout(self.pge_enc_main_layout)
        self.pge_enc.move(114514, 1919810)

        # 解密页面
        self.pge_dec = QWidget(self)
        self.pge_dec.setGeometry(300, 0, self.width() - 300, self.height())
        self.pge_dec.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        self.pge_dec.setStyleSheet(
            'background: #e6e6e6;'
        )

        self.pge_dec_main_layout = QGridLayout()

        self.pge_dec_room = QWidgetRoom()
        self.pge_dec_room.title = QLabel(self.pge_dec, text='<h1>Encryption In Image 解密</h1>')  # noqa
        self.pge_dec_room.btn_sel_cimage = QPushButton(self.pge_dec, text="选择原图")
        self.pge_dec_room.inp_sel_cimage = QLineEdit(self.pge_dec)
        self.pge_dec_room.inp_sel_cimage.setPlaceholderText("选择一原图或直接输入路径")
        self.pge_dec_room.btn_sel_eimage = QPushButton(self.pge_dec, text="选择加密图")
        self.pge_dec_room.inp_sel_eimage = QLineEdit(self.pge_dec)
        self.pge_dec_room.inp_sel_eimage.setPlaceholderText("选择一加密图或直接输入路径")
        self.pge_dec_room.lbl_token = QLabel(self.pge_dec, text='密钥:')  # noqa
        self.pge_dec_room.lbl_token.lower()
        self.pge_dec_room.inp_log = QTextEdit(self.pge_dec)
        self.pge_dec_room.inp_log.setReadOnly(True)
        self.pge_dec_room.inp_text = QTextEdit(self.pge_dec)
        self.pge_dec_room.btn_save = QPushButton(self.pge_dec, text='保存文本')
        self.pge_dec_room.btn_dec = QPushButton(self.pge_dec, text='解密')
        self.pge_dec_room.cbb_file_encoding = QComboBox(self.pge_dec)
        self.pge_dec_room.cbb_file_encoding.addItems(['utf-8', 'utf-16', 'gbk', 'iso-8859-01', 'ascii'])

        self.pge_dec_room.inp_token = QLineEdit(self.pge_dec)

        self.widget = self.pge_dec_main_layout.addWidget(self.pge_dec_room.title, 1, 0, 1, 2)
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.btn_sel_cimage, 2, 0)
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.inp_sel_cimage, 2, 1)
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.btn_sel_eimage, 3, 0)
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.inp_sel_eimage, 3, 1)
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.lbl_token, 4, 0)
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.inp_token, 4, 1)
        self.pge_dec_main_layout.addWidget(QLabel(self.pge_dec, text="输出日志:"), 5, 0)  # noqa
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.inp_log, 5, 1)
        self.pge_dec_main_layout.addWidget(QLabel(self.pge_dec, text="解密文本:"), 6, 0)  # noqa
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.inp_text, 6, 1)
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.btn_dec, 7, 0, 7, 2)
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.btn_save, 8, 0)
        self.pge_dec_main_layout.addWidget(self.pge_dec_room.cbb_file_encoding, 8, 1)

        self.pge_dec_main_layout.setColumnStretch(0, 1)
        self.pge_dec_main_layout.setColumnStretch(1, 4)

        self.pge_dec_main_layout.setRowStretch(1, 2)
        self.pge_dec_main_layout.setRowStretch(2, 2)
        self.pge_dec_main_layout.setRowStretch(3, 2)
        self.pge_dec_main_layout.setRowStretch(4, 2)
        self.pge_dec_main_layout.setRowStretch(5, 5)
        self.pge_dec_main_layout.setRowStretch(6, 5)
        self.pge_dec_main_layout.setRowStretch(7, 2)
        self.pge_dec_main_layout.setRowStretch(8, 2)

        self.pge_dec.setLayout(self.pge_dec_main_layout)

        self.pge_dec.move(114514, 1919810)

    def resizeEvent(self, a0) -> None:
        self.pge_home.resize(self.width() - 300, self.height())
        self.pge_enc.resize(self.width() - 300, self.height())
        self.pge_dec.resize(self.width() - 300, self.height())

    def To_page_enc(self):
        """切换到加密界面"""
        self.bar_side_btn_home.de_sel()
        self.bar_side_btn_dec.de_sel()
        self.bar_side_btn_enc.sel()

        if self.page == 'home':
            self.page = 'enc'
            ani = QPropertyAnimation(self.pge_home, b'pos', self)
            ani.setKeyValueAt(0, QPoint(300, 0))
            ani.setKeyValueAt(0.2, QPoint(300 + self.pge_home.width() // 3, 0))
            ani.setKeyValueAt(0.5, QPoint(300 + self.pge_home.width() // 3 * 2, 0))
            ani.setKeyValueAt(0.99, QPoint(300 + self.pge_home.width(), 0))
            ani.setKeyValueAt(1, QPoint(114514, 1919810))
            ani.setDuration(100)

            self.pge_enc.lower()
            ani2 = QPropertyAnimation(self.pge_enc, b'pos', self)
            ani2.setKeyValueAt(0, QPoint(300 - self.pge_enc.width(), 0))
            ani2.setKeyValueAt(0.2, QPoint(300 - self.pge_enc.width() + self.pge_enc.width() // 3, 0))
            ani2.setKeyValueAt(0.5, QPoint(300 - self.pge_enc.width() + self.pge_enc.width() // 3 * 2, 0))
            ani2.setKeyValueAt(1, QPoint(300, 0))
            ani2.setDuration(160)

            ani.start()
            ani2.start()

        if self.page == 'dec':
            self.page = 'enc'
            ani = QPropertyAnimation(self.pge_dec, b'pos', self)
            ani.setKeyValueAt(0, QPoint(300, 0))
            ani.setKeyValueAt(0.2, QPoint(300 + self.pge_dec.width() // 3, 0))
            ani.setKeyValueAt(0.5, QPoint(300 + self.pge_dec.width() // 3 * 2, 0))
            ani.setKeyValueAt(0.99, QPoint(300 + self.pge_dec.width(), 0))
            ani.setKeyValueAt(1, QPoint(114514, 1919810))
            ani.setDuration(100)

            self.pge_enc.lower()
            ani2 = QPropertyAnimation(self.pge_enc, b'pos', self)
            ani2.setKeyValueAt(0, QPoint(300 - self.pge_enc.width(), 0))
            ani2.setKeyValueAt(0.2, QPoint(300 - self.pge_enc.width() + self.pge_enc.width() // 3, 0))
            ani2.setKeyValueAt(0.5, QPoint(300 - self.pge_enc.width() + self.pge_enc.width() // 3 * 2, 0))
            ani2.setKeyValueAt(1, QPoint(300, 0))
            ani2.setDuration(160)

            ani.start()
            ani2.start()

    def To_page_home(self):
        """切换到主界面"""
        self.bar_side_btn_home.sel()
        self.bar_side_btn_dec.de_sel()
        self.bar_side_btn_enc.de_sel()

        if self.page == 'enc':
            self.page = 'home'
            ani = QPropertyAnimation(self.pge_enc, b'pos', self)
            ani.setKeyValueAt(0, QPoint(300, 0))
            ani.setKeyValueAt(0.2, QPoint(300 + self.pge_enc.width() // 3, 0))
            ani.setKeyValueAt(0.5, QPoint(300 + self.pge_enc.width() // 3 * 2, 0))
            ani.setKeyValueAt(0.99, QPoint(300 + self.pge_enc.width(), 0))
            ani.setKeyValueAt(1, QPoint(114514, 1919810))
            ani.setDuration(100)

            self.pge_home.lower()
            ani2 = QPropertyAnimation(self.pge_home, b'pos', self)
            ani2.setKeyValueAt(0, QPoint(300 - self.pge_home.width(), 0))
            ani2.setKeyValueAt(0.2, QPoint(300 - self.pge_home.width() + self.pge_home.width() // 3, 0))
            ani2.setKeyValueAt(0.5, QPoint(300 - self.pge_home.width() + self.pge_home.width() // 3 * 2, 0))
            ani2.setKeyValueAt(1, QPoint(300, 0))
            ani2.setDuration(160)

            ani.start()
            ani2.start()

        if self.page == 'dec':
            self.page = 'home'
            ani = QPropertyAnimation(self.pge_dec, b'pos', self)
            ani.setKeyValueAt(0, QPoint(300, 0))
            ani.setKeyValueAt(0.2, QPoint(300 + self.pge_dec.width() // 3, 0))
            ani.setKeyValueAt(0.5, QPoint(300 + self.pge_dec.width() // 3 * 2, 0))
            ani.setKeyValueAt(0.99, QPoint(300 + self.pge_dec.width(), 0))
            ani.setKeyValueAt(1, QPoint(114514, 1919810))
            ani.setDuration(100)

            self.pge_home.lower()
            ani2 = QPropertyAnimation(self.pge_home, b'pos', self)
            ani2.setKeyValueAt(0, QPoint(300 - self.pge_home.width(), 0))
            ani2.setKeyValueAt(0.2, QPoint(300 - self.pge_home.width() + self.pge_home.width() // 3, 0))
            ani2.setKeyValueAt(0.5, QPoint(300 - self.pge_home.width() + self.pge_home.width() // 3 * 2, 0))
            ani2.setKeyValueAt(1, QPoint(300, 0))
            ani2.setDuration(160)

            ani.start()
            ani2.start()

    def To_page_dec(self):
        """切换到解密界面"""
        self.bar_side_btn_home.de_sel()
        self.bar_side_btn_dec.sel()
        self.bar_side_btn_enc.de_sel()

        if self.page == 'home':
            self.page = 'dec'
            ani = QPropertyAnimation(self.pge_home, b'pos', self)
            ani.setKeyValueAt(0, QPoint(300, 0))
            ani.setKeyValueAt(0.2, QPoint(300 + self.pge_home.width() // 3, 0))
            ani.setKeyValueAt(0.5, QPoint(300 + self.pge_home.width() // 3 * 2, 0))
            ani.setKeyValueAt(0.99, QPoint(300 + self.pge_home.width(), 0))
            ani.setKeyValueAt(1, QPoint(114514, 1919810))
            ani.setDuration(100)

            self.pge_dec.lower()
            ani2 = QPropertyAnimation(self.pge_dec, b'pos', self)
            ani2.setKeyValueAt(0, QPoint(300 - self.pge_dec.width(), 0))
            ani2.setKeyValueAt(0.2, QPoint(300 - self.pge_dec.width() + self.pge_dec.width() // 3, 0))
            ani2.setKeyValueAt(0.5, QPoint(300 - self.pge_dec.width() + self.pge_dec.width() // 3 * 2, 0))
            ani2.setKeyValueAt(1, QPoint(300, 0))
            ani2.setDuration(200)

            ani.start()
            ani2.start()

        if self.page == 'enc':
            self.page = 'dec'
            ani = QPropertyAnimation(self.pge_enc, b'pos', self)
            ani.setKeyValueAt(0, QPoint(300, 0))
            ani.setKeyValueAt(0.2, QPoint(300 + self.pge_enc.width() // 3, 0))
            ani.setKeyValueAt(0.5, QPoint(300 + self.pge_enc.width() // 3 * 2, 0))
            ani.setKeyValueAt(0.99, QPoint(300 + self.pge_enc.width(), 0))
            ani.setKeyValueAt(1, QPoint(114514, 1919810))
            ani.setDuration(100)

            self.pge_dec.lower()
            ani2 = QPropertyAnimation(self.pge_dec, b'pos', self)
            ani2.setKeyValueAt(0, QPoint(300 - self.pge_dec.width(), 0))
            ani2.setKeyValueAt(0.2, QPoint(300 - self.pge_dec.width() + self.pge_dec.width() // 3, 0))
            ani2.setKeyValueAt(0.5, QPoint(300 - self.pge_dec.width() + self.pge_dec.width() // 3 * 2, 0))
            ani2.setKeyValueAt(1, QPoint(300, 0))
            ani2.setDuration(200)

            ani.start()
            ani2.start()

    def C_enc_cel_image(self, a0):
        directory = QFileDialog.getOpenFileName(self, "选取原图", '',
                                                "PNG Files (*.png);;BMP Files (*.bmp);;All Files (*)")  # 起始路径
        self.pge_enc_room.inp_sel_image.setText(directory[0])
        self.Log_enc("已选择图片")

    def C_enc_open_file(self, a0):
        directory = QFileDialog.getOpenFileName(self, "选取文件", '',
                                                "All Files (*)")  # 起始路径
        try:
            file = open(directory[0], 'r', encoding=self.pge_enc_room.cbb_file_encoding.currentText()).read()
        except UnicodeDecodeError:
            self.Log_enc(f"读取文件失败，无法使用{self.pge_enc_room.cbb_file_encoding.currentText()}编码方式读取该文件")
            return
        self.pge_enc_room.inp_text.insertPlainText(file)
        self.Log_enc("已成功读取文件文本")

    def Log_enc(self, text):
        self.pge_enc_room.inp_log.insertPlainText(time.strftime("[%H:%M:%S] ") + text + '\n')


def main():
    app = QApplication([])
    egw = EIIGUIWindow()
    egw.show()
    app.exec_()
