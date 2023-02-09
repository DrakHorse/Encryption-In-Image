"""
Encryption In Image 文本加密
交互界面

本文件完全开源，使用GPL3.0 开源许可证
未经允许，请勿用于商业用途
"""
from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer


class SideBarButton(QPushButton):
    """内置侧边栏按钮类"""

    def __init__(self, parent, text, select=False):
        super().__init__(parent=parent, text=text)

        self.setStyleSheet(
            'background: #b8b8b8;'
            'border: 0'
        )

        self.select = select

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
                'background: #939393;'
                'border: 0'
            )
        else:
            self.setStyleSheet(
                'background: #b8b8b8;'
                'border: 0'
            )


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

        self.bar_side_btn_home = SideBarButton(self.bar_side, text='文本加密')
        self.bar_side_btn_home.setGeometry(0, 40, 300, 40)

        self.bar_side_btn_home = SideBarButton(self.bar_side, text='文本解密')
        self.bar_side_btn_home.setGeometry(0, 80, 300, 40)

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

        self.pge_home_main_layout.addWidget(self.pge_home_main_label)

    def resizeEvent(self, a0) -> None:
        self.pge_home.setGeometry(300, 0, self.width() - 300, self.height())


def main():
    app = QApplication([])
    egw = EIIGUIWindow()
    egw.show()
    app.exec_()
