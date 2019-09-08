# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(140, 170, 93, 28))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "btn"))
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

