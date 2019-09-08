from PyQt5.Qt import *
import sys

# 创建应用对象
# sys.argv 根据传递的参数 执行不同的逻辑
app = QApplication(sys.argv)

# region 控件操作
window = QWidget()
window.setWindowTitle('第一个PyQtDemo')
window.resize(500, 500)
window.move(400, 200)
label = QLabel(window)
label.setText('hello World')
label.move(200, 200)
window.show()
# endregion
# 执行应用程序 进入循环 系统退出码 0 正常退出
# app.exec_()用户退出的状态
sys.exit(app.exec_())
