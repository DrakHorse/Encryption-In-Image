"""
Encryption In Image 文本加密
交互界面

本文件完全开源，使用GPL3.0 开源许可证
未经允许，请勿用于商业用途
"""
from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer


class EIIGUIWindow(QWidget):
    """交互界面主窗口类"""

    def __init__(self):
        super().__init__()
        self.initUI()

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
        self.bar_side_btn_home = QPushButton(self.bar_side, text='Encryption In Image 主页')
        self.bar_side_btn_home.setStyleSheet(
            'background: #b8b8b8;'
            'border: 0'
        )
        self.bar_side_btn_home.enterEvent = self.bar_side_btn_home_event_enter
        self.bar_side_btn_home.leaveEvent = self.bar_side_btn_home_event_leave
        self.bar_side_btn_home.setGeometry(0, 0, 300, 40)

        self.bar_side_btn_enc = QPushButton(self.bar_side, text='文本加密')
        self.bar_side_btn_enc.setStyleSheet(
            'background: #b8b8b8;'
            'border: 0'
        )
        self.bar_side_btn_enc.setGeometry(0, 40, 300, 40)

        self.bar_side_btn_dec = QPushButton(self.bar_side, text='文本解密')
        self.bar_side_btn_dec.setStyleSheet(
            'background: #b8b8b8;'
            'border: 0'
        )
        self.bar_side_btn_dec.setGeometry(0, 80, 300, 40)

    def bar_side_btn_home_event_enter(self, event):
        def dis():
            self.bar_side_btn_home.setStyleSheet(
                f'background: #{hex(self.bar_side_btn_home.i)[2:]}'
                f'{hex(self.bar_side_btn_home.i)[2:]}'
                f'{hex(self.bar_side_btn_home.i)[2:]};'
                f'border: 0'
            )
            self.bar_side_btn_home.i -= 1
            if self.bar_side_btn_home.i <= 160:
                self.bar_side_btn_home_event_enter_tmr.stop()

        self.bar_side_btn_home.i = 184
        self.bar_side_btn_home_event_enter_tmr = QTimer()
        self.bar_side_btn_home_event_enter_tmr.setInterval(4)
        self.bar_side_btn_home_event_enter_tmr.timeout.connect(dis)  # noqa
        self.bar_side_btn_home_event_enter_tmr.start()

    def bar_side_btn_home_event_leave(self, event):
        def dis():
            self.bar_side_btn_home.setStyleSheet(
                f'background: #{hex(self.bar_side_btn_home.i)[2:]}'
                f'{hex(self.bar_side_btn_home.i)[2:]}'
                f'{hex(self.bar_side_btn_home.i)[2:]};'
                f'border: 0'
            )
            self.bar_side_btn_home.i += 1
            if self.bar_side_btn_home.i >= 184:
                self.bar_side_btn_home_event_enter_tmr.stop()

        self.bar_side_btn_home.i = 160
        self.bar_side_btn_home_event_enter_tmr = QTimer()
        self.bar_side_btn_home_event_enter_tmr.setInterval(4)
        self.bar_side_btn_home_event_enter_tmr.timeout.connect(dis)  # noqa
        self.bar_side_btn_home_event_enter_tmr.start()


def main():
    app = QApplication([])
    egw = EIIGUIWindow()
    egw.show()
    app.exec_()
