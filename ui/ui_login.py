from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QSizePolicy, QFrame, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QSpacerItem

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):

        # 获取屏幕大小
        screen_rect = QApplication.desktop().screenGeometry()
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()
        LoginWindow.resize(screen_width, screen_height)
        print(f'{screen_width=}, {screen_height=}')

        self.verticalLayout = QVBoxLayout(LoginWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.bottomSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # central frame
        self.frame = QFrame(LoginWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet("border: none; background-color: rgba(255, 255, 255, 0.5); border-radius: 15px;")
        self.frame.setFixedSize(400, 300)  # 固定大小
        # 弹簧1-frame-弹簧2
        self.verticalLayout.addItem(self.topSpacer)
        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignCenter)
        self.verticalLayout.addItem(self.bottomSpacer)

        # 设置框架内部的布局
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.label_system_name = QLabel(self.frame)
        self.label_system_name.setObjectName(u"label_system_name")
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")  # 黑体
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_system_name.setFont(font)
        self.label_system_name.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_system_name, 0, 0, 1, 3)

        self.label_user_name = QLabel(self.frame)
        self.label_user_name.setObjectName(u"label_user_name")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_user_name.setFont(font)
        self.gridLayout.addWidget(self.label_user_name, 1, 1, 1, 1)

        self.user_name = QLineEdit(self.frame)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setFont(font)
        self.user_name.setAutoFillBackground(False)
        self.gridLayout.addWidget(self.user_name, 1, 2, 1, 1)

        self.label_password = QLabel(self.frame)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font)
        self.gridLayout.addWidget(self.label_password, 2, 1, 1, 1)

        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setFont(font)
        self.password.setEchoMode(QLineEdit.Password)
        self.gridLayout.addWidget(self.password, 2, 2, 1, 1)

        self.login_btn = QPushButton(self.frame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setFont(font)
        self.gridLayout.addWidget(self.login_btn, 3, 1, 1, 2)

        self.retranslateUi(LoginWindow)
        QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow",u"\u773c\u955c\u5e97\u4f1a\u5458\u4e0e\u9500\u552e\u7cfb\u7edf-\u767b\u5f55", None))
        self.label_system_name.setText(QCoreApplication.translate("LoginWindow", u"\u773c\u955c\u5e97\u4f1a\u5458\u4e0e\u9500\u552e\u7cfb\u7edf", None))
        self.label_user_name.setText(QCoreApplication.translate("LoginWindow", u"\u7528\u6237\u540d\uff1a", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u8bf7\u8f93\u5165", None))
        self.user_name.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u8bf7\u8f93\u5165", None))
        self.login_btn.setText(QCoreApplication.translate("LoginWindow", u"\u767b\u5f55", None))
        self.label_password.setText(QCoreApplication.translate("LoginWindow", u"\u5bc6\u7801\uff1a", None))