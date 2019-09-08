import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建窗体
    app = QApplication(sys.argv)
    # 创建窗口
    w = QWidget()
    # 设置大小
    w.resize(500, 300)
    # 可以移动
    w.move(300, 300)
    # 设置标题
    w.setWindowTitle('我的第一个PyQt5')
    # 显示窗体
    w.show()
    # 默认关闭
    sys.exit(app.exec_())
