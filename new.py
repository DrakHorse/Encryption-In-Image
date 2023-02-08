import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QTimer
from PyQt5.QtGui import QPalette,QColor


class QmyWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel(self)
        self.label.setText('控件淡入')
        self.label.setAutoFillBackground(True)
        # 设置标签背景色
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(141, 91, 153))
        self.label.setPalette(palette)
        # 设置透明度
        self.opacity = QGraphicsOpacityEffect()  # 透明度对象
        self.opacity.setOpacity(0)  # 初始化设置透明度为0，即完全透明
        self.label.setGraphicsEffect(self.opacity)  # 把标签的透明度设置为为self.opacity

        self.draw()  # 淡入效果开始

    def draw(self):
        self.opacity.i = 1  # 用于记录透明度变化与循环次数

        def timeout():  # 超时函数：改变透明度
            self.opacity.setOpacity(self.opacity.i / 100)
            self.label.setGraphicsEffect(self.opacity)  # 改变标签透明度
            self.opacity.i += 1
            if self.opacity.i >= 100:  # 此时透明度为1，即不透明，控件已经完全显示出来了
                self.timer.stop()  # 计时器停止
                self.timer.deleteLater()

        self.timer = QTimer()  # 计时器
        self.timer.setInterval(10)  # 设置间隔时间，毫秒为单位
        self.timer.timeout.connect(timeout)  # 超时槽函数，每到达间隔时间，调用该函数
        self.timer.start()  # 计时器开始


if __name__ == '__main__':  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyWindow()  # 创建窗体
    form.show()  # 显示窗体
    sys.exit(app.exec_())
