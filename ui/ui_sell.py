# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sellgAabFc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_SellWindow(object):
    def setupUi(self, SellWindow):
        if not SellWindow.objectName():
            SellWindow.setObjectName(u"SellWindow")
        SellWindow.resize(1200, 800)
        SellWindow.setMinimumSize(QSize(600, 400))
        self.gridLayout_2 = QGridLayout(SellWindow)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(SellWindow)
        self.MainFrame.setObjectName(u"MainFrame")
        self.gridLayout = QGridLayout(self.MainFrame)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.MenuFrame = QFrame(self.MainFrame)
        self.MenuFrame.setObjectName(u"MenuFrame")
        self.MenuFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.3);\n"
"border-radius: 15px")
        self.MenuFrame.setFrameShape(QFrame.StyledPanel)
        self.MenuFrame.setFrameShadow(QFrame.Raised)
        self.ret_btn = QPushButton(self.MenuFrame)
        self.ret_btn.setObjectName(u"ret_btn")
        self.ret_btn.setGeometry(QRect(10, 10, 121, 31))
        self.ret_btn.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(12)
        self.ret_btn.setFont(font)
        self.ret_btn.setStyleSheet(u"background-color:grey;\n"
"color: white;\n"
"border-radius: 10px;")
        self.label = QLabel(self.MenuFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 70, 61, 41))
        self.label.setFont(font)
        self.label.setStyleSheet(u"border-radius:15px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.MenuFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 120, 120, 631))
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"border: 1px solid;\n"
"border-color:rgba(0, 170, 255, 0.5);\n"
"background-color:rgba(0, 170, 255, 0.5);\n"
"}\n"
"QScrollBar::handle:vertical {/*\u8bbe\u7f6e\u6ed1\u52a8\u6761*/\n"
"	border: none;\n"
"    border-radius:15px; \n"
"	background-color: rgb(55, 156, 212);\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 118, 629))
        self.sell_btn = QPushButton(self.scrollAreaWidgetContents)
        self.sell_btn.setObjectName(u"sell_btn")
        self.sell_btn.setGeometry(QRect(10, 60, 90, 90))
        self.sell_btn.setMinimumSize(QSize(90, 90))
        self.sell_btn.setMaximumSize(QSize(90, 90))
        self.sell_btn.setFont(font)
        self.sell_btn.setAutoFillBackground(False)
        self.sell_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	border:1px solid rgb(100, 100,189)\n"
"\n"
"}")
        self.rule_btn = QPushButton(self.scrollAreaWidgetContents)
        self.rule_btn.setObjectName(u"rule_btn")
        self.rule_btn.setGeometry(QRect(10, 180, 90, 90))
        self.rule_btn.setMinimumSize(QSize(90, 90))
        self.rule_btn.setMaximumSize(QSize(90, 90))
        self.rule_btn.setFont(font)
        self.rule_btn.setAutoFillBackground(False)
        self.rule_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	border:1px solid rgb(100, 100,189)\n"
"\n"
"}")
        self.mem_btn = QPushButton(self.scrollAreaWidgetContents)
        self.mem_btn.setObjectName(u"mem_btn")
        self.mem_btn.setGeometry(QRect(20, 300, 90, 90))
        self.mem_btn.setMinimumSize(QSize(90, 90))
        self.mem_btn.setMaximumSize(QSize(90, 90))
        self.mem_btn.setFont(font)
        self.mem_btn.setAutoFillBackground(False)
        self.mem_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	border:1px solid rgb(100, 100,189)\n"
"\n"
"}")
        self.tip_btn = QPushButton(self.scrollAreaWidgetContents)
        self.tip_btn.setObjectName(u"tip_btn")
        self.tip_btn.setGeometry(QRect(20, 430, 90, 90))
        self.tip_btn.setMinimumSize(QSize(90, 90))
        self.tip_btn.setMaximumSize(QSize(90, 90))
        self.tip_btn.setFont(font)
        self.tip_btn.setAutoFillBackground(False)
        self.tip_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	border:1px solid rgb(100, 100,189)\n"
"\n"
"}")
        self.sns_btn = QPushButton(self.scrollAreaWidgetContents)
        self.sns_btn.setObjectName(u"sns_btn")
        self.sns_btn.setGeometry(QRect(20, 540, 90, 90))
        self.sns_btn.setMinimumSize(QSize(90, 90))
        self.sns_btn.setMaximumSize(QSize(90, 90))
        self.sns_btn.setFont(font)
        self.sns_btn.setAutoFillBackground(False)
        self.sns_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color:rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	border:1px solid rgb(100, 100,189)\n"
"\n"
"}")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.MenuFrame, 0, 0, 1, 1)

        self.MarketFrame = QFrame(self.MainFrame)
        self.MarketFrame.setObjectName(u"MarketFrame")
        self.MarketFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.3);\n"
"border-radius: 15px")
        self.MarketFrame.setFrameShape(QFrame.StyledPanel)
        self.MarketFrame.setFrameShadow(QFrame.Raised)
        self.Logined = QLabel(self.MarketFrame)
        self.Logined.setObjectName(u"Logined")
        self.Logined.setGeometry(QRect(30, 10, 121, 41))
        self.Logined.setMinimumSize(QSize(0, 30))
        self.Logined.setFont(font)
        self.Logined.setStyleSheet(u"border-radius:15px;\n"
"border:1px solid rgb(100, 100,189)")
        self.Logined.setAlignment(Qt.AlignCenter)
        self.Logined.setWordWrap(True)
        self.MemberRegist = QPushButton(self.MarketFrame)
        self.MemberRegist.setObjectName(u"MemberRegist")
        self.MemberRegist.setGeometry(QRect(0, 60, 101, 41))
        self.MemberRegist.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.MemberRegist.setFont(font1)
        self.MemberRegist.setAutoFillBackground(False)
        self.MemberRegist.setStyleSheet(u"QPushButton {\n"
"background-color: #57bd6a;\n"
"color: #f9ffff;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #4eaa5f;\n"
"}")
        self.MemberLogin = QPushButton(self.MarketFrame)
        self.MemberLogin.setObjectName(u"MemberLogin")
        self.MemberLogin.setGeometry(QRect(100, 60, 101, 41))
        self.MemberLogin.setMinimumSize(QSize(0, 30))
        self.MemberLogin.setFont(font1)
        self.MemberLogin.setAutoFillBackground(False)
        self.MemberLogin.setStyleSheet(u"QPushButton {\n"
"background-color: #57bd6a;\n"
"color: #f9ffff;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #4eaa5f;\n"
"}")
        self.FinalPrice = QLabel(self.MarketFrame)
        self.FinalPrice.setObjectName(u"FinalPrice")
        self.FinalPrice.setGeometry(QRect(40, 620, 111, 41))
        self.FinalPrice.setMinimumSize(QSize(0, 30))
        self.FinalPrice.setFont(font)
        self.FinalPrice.setStyleSheet(u"border-radius:15px;\n"
"border:1px solid rgb(100, 100,189)")
        self.FinalPrice.setAlignment(Qt.AlignCenter)
        self.GachaButton = QPushButton(self.MarketFrame)
        self.GachaButton.setObjectName(u"GachaButton")
        self.GachaButton.setGeometry(QRect(20, 710, 101, 41))
        self.GachaButton.setMinimumSize(QSize(0, 30))
        self.GachaButton.setFont(font1)
        self.GachaButton.setAutoFillBackground(False)
        self.GachaButton.setStyleSheet(u"QPushButton {\n"
"background-color: #ffaa00;\n"
"color: #f9ffff;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(234, 156, 0);\n"
"}")
        self.MarketList = QFrame(self.MarketFrame)
        self.MarketList.setObjectName(u"MarketList")
        self.MarketList.setGeometry(QRect(30, 160, 120, 80))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MarketList.sizePolicy().hasHeightForWidth())
        self.MarketList.setSizePolicy(sizePolicy)
        self.MarketList.setFont(font)
        self.MarketList.setStyleSheet(u"QFrame{\n"
"border-radius: 15px;\n"
"background-color:transparent;\n"
"}")
        self.MarketList.setFrameShape(QFrame.StyledPanel)
        self.MarketList.setFrameShadow(QFrame.Raised)
        self.ClearButton = QPushButton(self.MarketFrame)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setGeometry(QRect(120, 710, 101, 41))
        self.ClearButton.setMinimumSize(QSize(0, 30))
        self.ClearButton.setFont(font1)
        self.ClearButton.setAutoFillBackground(False)
        self.ClearButton.setStyleSheet(u"QPushButton {\n"
"background-color: #ffaa00;\n"
"color: #f9ffff;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(234, 156, 0);\n"
"}")

        self.gridLayout.addWidget(self.MarketFrame, 0, 1, 1, 1)

        self.ProductFrame = QFrame(self.MainFrame)
        self.ProductFrame.setObjectName(u"ProductFrame")
        self.ProductFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	border-radius: 15px\n"
"}")
        self.ProductFrame.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame.setFrameShadow(QFrame.Raised)
        self.MySlider = QSlider(self.ProductFrame)
        self.MySlider.setObjectName(u"MySlider")
        self.MySlider.setGeometry(QRect(170, 210, 160, 30))
        self.MySlider.setMinimumSize(QSize(0, 30))
        self.MySlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"            border: none;\n"
"            height: 2px;\n"
"            background-color: lightgray;\n"
"        }\n"
"\n"
"        QSlider::handle:horizontal {\n"
"            background-color: #f1964c;\n"
"            width: 16px;\n"
"            margin: -8px 0px -8px 0px;\n"
"            border-radius: 8px;\n"
"        }\n"
"\n"
"        QSlider::sub-page:horizontal {\n"
"            background-color: #f1964c;\n"
"        }")
        self.MySlider.setMinimum(1)
        self.MySlider.setMaximum(10)
        self.MySlider.setOrientation(Qt.Horizontal)
        self.ProductsList = QFrame(self.ProductFrame)
        self.ProductsList.setObjectName(u"ProductsList")
        self.ProductsList.setGeometry(QRect(140, 280, 120, 80))
        self.ProductsList.setFont(font)
        self.ProductsList.setStyleSheet(u"QFrame\n"
"{\n"
"	border-radius: 15px;\n"
"	background-color:transparent;\n"
"}")
        self.ProductsList.setFrameShape(QFrame.StyledPanel)
        self.ProductsList.setFrameShadow(QFrame.Raised)
        self.MySearch = QLineEdit(self.ProductFrame)
        self.MySearch.setObjectName(u"MySearch")
        self.MySearch.setGeometry(QRect(240, 110, 113, 40))
        self.MySearch.setMinimumSize(QSize(0, 40))
        self.MySearch.setFont(font)
        self.MySearch.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 15px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.Radio1 = QRadioButton(self.ProductFrame)
        self.Radio1.setObjectName(u"Radio1")
        self.Radio1.setGeometry(QRect(90, 90, 86, 16))
        self.Radio2 = QRadioButton(self.ProductFrame)
        self.Radio2.setObjectName(u"Radio2")
        self.Radio2.setGeometry(QRect(90, 130, 86, 16))
        self.widget = QWidget(self.ProductFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(410, 270, 120, 80))

        self.gridLayout.addWidget(self.ProductFrame, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 17)

        self.gridLayout_2.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(SellWindow)

        QMetaObject.connectSlotsByName(SellWindow)
    # setupUi

    def retranslateUi(self, SellWindow):
        SellWindow.setWindowTitle(QCoreApplication.translate("SellWindow", u"\u9500\u552e\u4e2d", None))
        self.ret_btn.setText(QCoreApplication.translate("SellWindow", u"\u8fd4\u56de\u767b\u5f55\u754c\u9762", None))
        self.label.setText(QCoreApplication.translate("SellWindow", u"\u6536\u94f6\u53f0\n"
"\u60a8\u597d\uff0c\u9500\u552e\u5458", None))
        self.sell_btn.setText(QCoreApplication.translate("SellWindow", u"\u6536\u94f6\u4e3b\u9875", None))
        self.rule_btn.setText(QCoreApplication.translate("SellWindow", u"\u5145\u503c\u89c4\u5219", None))
        self.mem_btn.setText(QCoreApplication.translate("SellWindow", u"\u4f1a\u5458\u4fe1\u606f", None))
        self.tip_btn.setText(QCoreApplication.translate("SellWindow", u"\u8ba2\u5355\u4fe1\u606f", None))
        self.sns_btn.setText(QCoreApplication.translate("SellWindow", u"\u53d1\u9001\u77ed\u4fe1", None))
        self.Logined.setText(QCoreApplication.translate("SellWindow", u"\u5f53\u524d\u4f1a\u5458\uff1a\u672a\u9009", None))
        self.MemberRegist.setText(QCoreApplication.translate("SellWindow", u"\u4f1a\u5458\u6ce8\u518c", None))
        self.MemberLogin.setText(QCoreApplication.translate("SellWindow", u"\u9009\u62e9\u4f1a\u5458", None))
        self.FinalPrice.setText(QCoreApplication.translate("SellWindow", u"\u603b\u91d1\u989d\uff1a0\u5143", None))
        self.GachaButton.setText(QCoreApplication.translate("SellWindow", u"\u7ed3\u7b97", None))
        self.ClearButton.setText(QCoreApplication.translate("SellWindow", u"\u6e05\u7a7a", None))
        self.MySearch.setPlaceholderText(QCoreApplication.translate("SellWindow", u"\u952e\u5165\u4fe1\u606f\u4ee5\u7b5b\u9009\u5546\u54c1...", None))
        self.Radio1.setText(QCoreApplication.translate("SellWindow", u"\u6309\u540d\u79f0", None))
        self.Radio2.setText(QCoreApplication.translate("SellWindow", u"\u6309\u4ef7\u683c", None))
    # retranslateUi

