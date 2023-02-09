"""
Encryption In Image 文本加密
交互界面

本文件完全开源，使用GPL3.0 开源许可证
未经允许，请勿用于商业用途
"""
from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy, QPushButton, QGridLayout, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt


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
            def dis():
                self.setStyleSheet(
                    f'background: #{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]}'
                    f'{hex(self.i)[2:]};'
                    f'border: 0'
                )
                self.i += 1
                if self.i >= 160 - 36:
                    self.tmr.stop()

            self.i = 130 - 36
            self.tmr = QTimer()
            self.tmr.setInterval(5)
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
                if self.i >= 160:
                    self.tmr.stop()

            self.i = 130
            self.tmr = QTimer()
            self.tmr.setInterval(7)
            self.tmr.timeout.connect(dis)  # noqa
            self.tmr.start()


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

        self.pge_home_main_label = QTextEdit()
        self.pge_home_main_label.setHtml(f"""
<h1>Encryption In Image 文本加密</h1>
Version 0.6.0

<h2>0. 简介</h2>
<h3>0.1 什么是 Encryption In Image</h3>
Encryption In Image(简称EII)是一种文本加密技术，其加密方法是将文本隐藏于图片的颜色中，对图片颜色做出细微更改以无损保存文本内容

<h3>0.2 性能</h3>
EII 多次对算法做出优化，经多次测试，一张4K图片储存20000个字符，加密需0.3秒，解密需0.2秒(其中包含打开与保存图片的时间)

<h3>0.3 储存率</h3>
EII的储存原理是将字符的Unicode编码储存与颜色的RGB数组当中

一张图片最多可储存 2097152(128^3)个字符，因此，若想要储存极限个字符，仅需一张最少(1920x1093)的图片即可

根据使用像素颜色储存字符的算法，EII算法本没有字符数限制，但因算法第2像素储存文本长度信息，但每个像素仅能储存0-2097152(128^3)，因此，有字符数限制，
这可以通过改进算法解决，但目前无需储存过多的字符，因此没有突破限制的必要

<h3>0.4 版权声明</h3>
该项目完全开源免费，因此，任何付费使用均为盗版

该项目开源协议为 GNU GPL 3.0

团队: DarkHorse  https://github.com/DarkHorse/ <br>
联系：leafjuly@outlook.com

<h2>1. 使用</h2>
<h3>1.1 交互界面使用</h3>
打开目录下的 encryption_in_image_ui.exe(linux为encryption_in_image_ui) 以运行<br>
左侧导航栏中点击加密/解密以使用

或者，运行src目录中的 main.py

<h3>1.2 接口使用</h3>
EII接口完全开源，文件位于src目录下的eii.py""")
        self.pge_home_main_label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pge_home_main_label.setReadOnly(True)

        self.pge_home_main_layout.addWidget(self.pge_home_main_label, 0, 0)

    def resizeEvent(self, a0) -> None:
        self.pge_home.setGeometry(300, 0, self.width() - 300, self.height())


def main():
    app = QApplication([])
    egw = EIIGUIWindow()
    egw.show()
    app.exec_()
