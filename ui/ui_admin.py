# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminOmKEcy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(1200, 800)
        AdminWindow.setMinimumSize(QSize(600, 400))
        self.gridLayout_2 = QGridLayout(AdminWindow)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(AdminWindow)
        self.MainFrame.setObjectName(u"MainFrame")
        self.gridLayout = QGridLayout(self.MainFrame)
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

        self.StackPages = QStackedWidget(self.MainFrame)
        self.StackPages.setObjectName(u"StackPages")
        self.RulePage = QWidget()
        self.RulePage.setObjectName(u"RulePage")
        self.RuleFrame = QFrame(self.RulePage)
        self.RuleFrame.setObjectName(u"RuleFrame")
        self.RuleFrame.setGeometry(QRect(10, 10, 1023, 782))
        self.RuleFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	border-radius: 15px\n"
"}\n"
"")
        self.RuleFrame.setFrameShape(QFrame.StyledPanel)
        self.RuleFrame.setFrameShadow(QFrame.Raised)
        self.RuleAdd = QPushButton(self.RuleFrame)
        self.RuleAdd.setObjectName(u"RuleAdd")
        self.RuleAdd.setGeometry(QRect(230, 140, 171, 51))
        self.RuleAdd.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.RuleAdd.setFont(font1)
        self.RuleAdd.setAutoFillBackground(False)
        self.RuleAdd.setStyleSheet(u"QPushButton {\n"
"background-color: #ffaa00;\n"
"color: #f9ffff;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(234, 156, 0);\n"
"}")
        self.RuleIcon = QLabel(self.RuleFrame)
        self.RuleIcon.setObjectName(u"RuleIcon")
        self.RuleIcon.setGeometry(QRect(110, 300, 54, 12))
        self.RuleIcon.setStyleSheet(u"background-color: transparent;")
        self.RuleIcon.setAlignment(Qt.AlignCenter)
        self.RuleBase = QLineEdit(self.RuleFrame)
        self.RuleBase.setObjectName(u"RuleBase")
        self.RuleBase.setGeometry(QRect(110, 70, 121, 50))
        self.RuleBase.setMinimumSize(QSize(0, 50))
        self.RuleBase.setFont(font)
        self.RuleBase.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 25px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.RuleBonus = QLineEdit(self.RuleFrame)
        self.RuleBonus.setObjectName(u"RuleBonus")
        self.RuleBonus.setGeometry(QRect(260, 70, 121, 50))
        self.RuleBonus.setMinimumSize(QSize(0, 50))
        self.RuleBonus.setFont(font)
        self.RuleBonus.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 25px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.RuleDel = QPushButton(self.RuleFrame)
        self.RuleDel.setObjectName(u"RuleDel")
        self.RuleDel.setGeometry(QRect(240, 290, 171, 51))
        self.RuleDel.setMinimumSize(QSize(0, 50))
        self.RuleDel.setFont(font1)
        self.RuleDel.setAutoFillBackground(False)
        self.RuleDel.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 68, 55);\n"
"color: #f9ffff;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(225, 15, 0);\n"
"}")
        self.RuleList = QListWidget(self.RuleFrame)
        self.RuleList.setObjectName(u"RuleList")
        self.RuleList.setGeometry(QRect(60, 410, 256, 192))
        self.RuleList.setFont(font)
        self.RuleList.setStyleSheet(u"        QListView {\n"
"            border: none;\n"
"            background-color: #edeef3;\n"
"        }\n"
"        \n"
"        QListView::item {\n"
"            height: 40px;\n"
"            margin: 5px 5px 5px 5px;\n"
"            background-color: white;\n"
"            border-radius: 6px;\n"
"        }\n"
"        \n"
"        QListView::item:hover{\n"
"            background-color: whitesmoke;\n"
"			border-radius: 15px;\n"
"        }\n"
"        \n"
"        QListView::item:selected{\n"
"            color: black;\n"
"            border: 1px solid lightgray;\n"
"        }\n"
"")
        self.RuleList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.RuleList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.RuleList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.RuleList.setSortingEnabled(False)
        self.RuleDelInfo = QLineEdit(self.RuleFrame)
        self.RuleDelInfo.setObjectName(u"RuleDelInfo")
        self.RuleDelInfo.setGeometry(QRect(110, 180, 121, 50))
        self.RuleDelInfo.setMinimumSize(QSize(0, 50))
        self.RuleDelInfo.setFont(font)
        self.RuleDelInfo.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 25px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.RuleDelInfo.setReadOnly(True)
        self.StackPages.addWidget(self.RulePage)
        self.MemberPage = QWidget()
        self.MemberPage.setObjectName(u"MemberPage")
        self.MemberFrame = QFrame(self.MemberPage)
        self.MemberFrame.setObjectName(u"MemberFrame")
        self.MemberFrame.setGeometry(QRect(20, 20, 1023, 782))
        self.MemberFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	border-radius: 15px\n"
"}\n"
"")
        self.MemberFrame.setFrameShape(QFrame.StyledPanel)
        self.MemberFrame.setFrameShadow(QFrame.Raised)
        self.MemInput1 = QLineEdit(self.MemberFrame)
        self.MemInput1.setObjectName(u"MemInput1")
        self.MemInput1.setGeometry(QRect(90, 80, 121, 30))
        self.MemInput1.setMinimumSize(QSize(0, 30))
        self.MemInput1.setFont(font)
        self.MemInput1.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 15px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.MemInput2 = QLineEdit(self.MemberFrame)
        self.MemInput2.setObjectName(u"MemInput2")
        self.MemInput2.setGeometry(QRect(90, 130, 121, 30))
        self.MemInput2.setMinimumSize(QSize(0, 30))
        self.MemInput2.setFont(font)
        self.MemInput2.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 15px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.MemInput4 = QLineEdit(self.MemberFrame)
        self.MemInput4.setObjectName(u"MemInput4")
        self.MemInput4.setGeometry(QRect(270, 130, 121, 30))
        self.MemInput4.setMinimumSize(QSize(0, 30))
        self.MemInput4.setFont(font)
        self.MemInput4.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 15px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.MemLabel1 = QLabel(self.MemberFrame)
        self.MemLabel1.setObjectName(u"MemLabel1")
        self.MemLabel1.setGeometry(QRect(10, 70, 131, 41))
        self.MemLabel1.setFont(font)
        self.MemLabel1.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.MemLabel1.setAlignment(Qt.AlignCenter)
        self.MemLabel2 = QLabel(self.MemberFrame)
        self.MemLabel2.setObjectName(u"MemLabel2")
        self.MemLabel2.setGeometry(QRect(10, 120, 131, 41))
        self.MemLabel2.setFont(font)
        self.MemLabel2.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.MemLabel2.setAlignment(Qt.AlignCenter)
        self.MemLabel3 = QLabel(self.MemberFrame)
        self.MemLabel3.setObjectName(u"MemLabel3")
        self.MemLabel3.setGeometry(QRect(200, 70, 131, 41))
        self.MemLabel3.setFont(font)
        self.MemLabel3.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.MemLabel3.setAlignment(Qt.AlignCenter)
        self.MemLabel4 = QLabel(self.MemberFrame)
        self.MemLabel4.setObjectName(u"MemLabel4")
        self.MemLabel4.setGeometry(QRect(170, 120, 131, 41))
        self.MemLabel4.setFont(font)
        self.MemLabel4.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.MemLabel4.setAlignment(Qt.AlignCenter)
        self.MemFilter = QPushButton(self.MemberFrame)
        self.MemFilter.setObjectName(u"MemFilter")
        self.MemFilter.setGeometry(QRect(150, 230, 101, 41))
        self.MemFilter.setMinimumSize(QSize(0, 30))
        self.MemFilter.setFont(font1)
        self.MemFilter.setAutoFillBackground(False)
        self.MemFilter.setStyleSheet(u"QPushButton {\n"
"background-color: #00aaff;\n"
"color: #f9ffff;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #0096e0;\n"
"}")
        self.MemReFilter = QPushButton(self.MemberFrame)
        self.MemReFilter.setObjectName(u"MemReFilter")
        self.MemReFilter.setGeometry(QRect(270, 230, 101, 41))
        self.MemReFilter.setMinimumSize(QSize(0, 30))
        self.MemReFilter.setFont(font1)
        self.MemReFilter.setAutoFillBackground(False)
        self.MemReFilter.setStyleSheet(u"QPushButton {\n"
"background-color: #00aaff;\n"
"color: #f9ffff;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #0096e0;\n"
"}")
        self.MemAdd = QPushButton(self.MemberFrame)
        self.MemAdd.setObjectName(u"MemAdd")
        self.MemAdd.setGeometry(QRect(210, 290, 101, 41))
        self.MemAdd.setMinimumSize(QSize(0, 30))
        self.MemAdd.setFont(font1)
        self.MemAdd.setAutoFillBackground(False)
        self.MemAdd.setStyleSheet(u"QPushButton {\n"
"background-color: #57bd6a;\n"
"color: #f9ffff;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #4eaa5f;\n"
"}")
        self.MemTable = QTableWidget(self.MemberFrame)
        self.MemTable.setObjectName(u"MemTable")
        self.MemTable.setGeometry(QRect(100, 450, 256, 192))
        self.MemTable.setFont(font)
        self.MemTable.setStyleSheet(u"		QHeaderView::section\n"
"		{\n"
"   			font-size:14px;\n"
"    		font-family:\"Microsoft YaHei\";\n"
"   			color:#000000;\n"
"		}\n"
"        \n"
"        QHeaderView::section:hover\n"
"        {   \n"
"            border: none;\n"
"            background-color: #a2c7ae;\n"
"        }\n"
"        \n"
"        QHeaderView::section::horizontal:checked\n"
"        {   \n"
"            border: none;\n"
"            border-bottom: 1px solid #3a714a;\n"
"            background-color: #c0daca;\n"
"            color: #2f5b53;\n"
"        }\n"
"        \n"
"        QHeaderView::section::vertical:checked\n"
"        {   \n"
"            border: none;\n"
"            border-right: 1px solid #3a714a;\n"
"            background-color: #c0daca;\n"
"            color: #2f5b53;\n"
"        }\n"
"        \n"
"        QTableView {\n"
"            selection-background-color: transparent;\n"
"            selection-color: black;\n"
"			background-color: transparent;\n"
"			border-radius: 15px;\n"
"        }\n"
"        \n"
"   "
                        "     QTableView::item:selected {\n"
"            border: 1px solid #3a714a;\n"
"}")
        self.MemTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.MemTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.MemTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.MemInput3 = QLineEdit(self.MemberFrame)
        self.MemInput3.setObjectName(u"MemInput3")
        self.MemInput3.setGeometry(QRect(310, 80, 121, 30))
        self.MemInput3.setMinimumSize(QSize(0, 30))
        self.MemInput3.setFont(font)
        self.MemInput3.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 15px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.StackPages.addWidget(self.MemberPage)
        self.TipPage = QWidget()
        self.TipPage.setObjectName(u"TipPage")
        self.TipFrame = QFrame(self.TipPage)
        self.TipFrame.setObjectName(u"TipFrame")
        self.TipFrame.setGeometry(QRect(10, 20, 1023, 782))
        self.TipFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	border-radius: 15px\n"
"}\n"
"")
        self.TipFrame.setFrameShape(QFrame.StyledPanel)
        self.TipFrame.setFrameShadow(QFrame.Raised)
        self.TipInput3 = QLineEdit(self.TipFrame)
        self.TipInput3.setObjectName(u"TipInput3")
        self.TipInput3.setGeometry(QRect(560, 90, 121, 30))
        self.TipInput3.setMinimumSize(QSize(0, 30))
        self.TipInput3.setFont(font)
        self.TipInput3.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 15px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.TipLabel5 = QLabel(self.TipFrame)
        self.TipLabel5.setObjectName(u"TipLabel5")
        self.TipLabel5.setGeometry(QRect(450, 80, 131, 41))
        self.TipLabel5.setFont(font)
        self.TipLabel5.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.TipLabel5.setAlignment(Qt.AlignCenter)
        self.TipLabel6 = QLabel(self.TipFrame)
        self.TipLabel6.setObjectName(u"TipLabel6")
        self.TipLabel6.setGeometry(QRect(420, 130, 131, 41))
        self.TipLabel6.setFont(font)
        self.TipLabel6.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.TipLabel6.setAlignment(Qt.AlignCenter)
        self.TipLabel3 = QLabel(self.TipFrame)
        self.TipLabel3.setObjectName(u"TipLabel3")
        self.TipLabel3.setGeometry(QRect(20, 130, 131, 41))
        self.TipLabel3.setFont(font)
        self.TipLabel3.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.TipLabel3.setAlignment(Qt.AlignCenter)
        self.TipFilter = QPushButton(self.TipFrame)
        self.TipFilter.setObjectName(u"TipFilter")
        self.TipFilter.setGeometry(QRect(170, 200, 101, 41))
        self.TipFilter.setMinimumSize(QSize(0, 30))
        self.TipFilter.setFont(font1)
        self.TipFilter.setAutoFillBackground(False)
        self.TipFilter.setStyleSheet(u"QPushButton {\n"
"background-color: #00aaff;\n"
"color: #f9ffff;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #0096e0;\n"
"}")
        self.TipReFilter = QPushButton(self.TipFrame)
        self.TipReFilter.setObjectName(u"TipReFilter")
        self.TipReFilter.setGeometry(QRect(290, 200, 101, 41))
        self.TipReFilter.setMinimumSize(QSize(0, 30))
        self.TipReFilter.setFont(font1)
        self.TipReFilter.setAutoFillBackground(False)
        self.TipReFilter.setStyleSheet(u"QPushButton {\n"
"background-color: #00aaff;\n"
"color: #f9ffff;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #0096e0;\n"
"}")
        self.TipTable = QTableWidget(self.TipFrame)
        self.TipTable.setObjectName(u"TipTable")
        self.TipTable.setGeometry(QRect(120, 420, 256, 192))
        self.TipTable.setFont(font)
        self.TipTable.setStyleSheet(u"		QHeaderView::section\n"
"		{\n"
"   			font-size:14px;\n"
"    		font-family:\"Microsoft YaHei\";\n"
"   			color:#000000;\n"
"		}\n"
"        \n"
"        QHeaderView::section:hover\n"
"        {   \n"
"            border: none;\n"
"            background-color: #a2c7ae;\n"
"        }\n"
"        \n"
"        QHeaderView::section::horizontal:checked\n"
"        {   \n"
"            border: none;\n"
"            border-bottom: 1px solid #3a714a;\n"
"            background-color: #c0daca;\n"
"            color: #2f5b53;\n"
"        }\n"
"        \n"
"        QHeaderView::section::vertical:checked\n"
"        {   \n"
"            border: none;\n"
"            border-right: 1px solid #3a714a;\n"
"            background-color: #c0daca;\n"
"            color: #2f5b53;\n"
"        }\n"
"        \n"
"        QTableView {\n"
"            selection-background-color: transparent;\n"
"            selection-color: black;\n"
"			background-color: transparent;\n"
"			border-radius: 15px;\n"
"        }\n"
"        \n"
"   "
                        "     QTableView::item:selected {\n"
"            border: 1px solid #3a714a;\n"
"}")
        self.TipTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TipTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.TipTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.TipInput1 = QLineEdit(self.TipFrame)
        self.TipInput1.setObjectName(u"TipInput1")
        self.TipInput1.setGeometry(QRect(100, 140, 121, 30))
        self.TipInput1.setMinimumSize(QSize(0, 30))
        self.TipInput1.setFont(font)
        self.TipInput1.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 15px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.TipInput4 = QLineEdit(self.TipFrame)
        self.TipInput4.setObjectName(u"TipInput4")
        self.TipInput4.setGeometry(QRect(520, 140, 121, 30))
        self.TipInput4.setMinimumSize(QSize(0, 30))
        self.TipInput4.setFont(font)
        self.TipInput4.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 15px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.TipInput2 = QLineEdit(self.TipFrame)
        self.TipInput2.setObjectName(u"TipInput2")
        self.TipInput2.setGeometry(QRect(320, 140, 121, 30))
        self.TipInput2.setMinimumSize(QSize(0, 30))
        self.TipInput2.setFont(font)
        self.TipInput2.setStyleSheet(u"QLineEdit {\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 15px;\n"
"            padding-left: 5px;\n"
"            padding-right: 60px;\n"
"            background-color: rgba(255, 255, 255, 0.8);\n"
"        }")
        self.TipLabel4 = QLabel(self.TipFrame)
        self.TipLabel4.setObjectName(u"TipLabel4")
        self.TipLabel4.setGeometry(QRect(220, 130, 131, 41))
        self.TipLabel4.setFont(font)
        self.TipLabel4.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.TipLabel4.setAlignment(Qt.AlignCenter)
        self.TipLabel1 = QLabel(self.TipFrame)
        self.TipLabel1.setObjectName(u"TipLabel1")
        self.TipLabel1.setGeometry(QRect(20, 60, 131, 41))
        self.TipLabel1.setFont(font)
        self.TipLabel1.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.TipLabel1.setAlignment(Qt.AlignCenter)
        self.TipLabel2 = QLabel(self.TipFrame)
        self.TipLabel2.setObjectName(u"TipLabel2")
        self.TipLabel2.setGeometry(QRect(220, 80, 131, 41))
        self.TipLabel2.setFont(font)
        self.TipLabel2.setStyleSheet(u"border-radius:15px;\n"
"background-color:transparent;")
        self.TipLabel2.setAlignment(Qt.AlignCenter)
        self.TipStart = QDateEdit(self.TipFrame)
        self.TipStart.setObjectName(u"TipStart")
        self.TipStart.setGeometry(QRect(130, 80, 110, 30))
        self.TipStart.setMinimumSize(QSize(0, 30))
        self.TipStart.setStyleSheet(u"            QDateEdit {\n"
"                border: 1px solid lightgray;\n"
"                border-radius: 25px;\n"
"                padding-left: 5px;\n"
"                padding-right: 60px;\n"
"                background-color: rgba(255, 255, 255, 0.8);\n"
"            }\n"
"            QCalendarWidget {\n"
"                background-color: white;\n"
"            }\n"
"            QCalendarWidget QWidget {\n"
"                color: black;\n"
"            }\n"
"            QCalendarWidget QAbstractItemView:enabled {\n"
"                color: white;  /* \u5de5\u4f5c\u65e5\u65e5\u671f\u6570\u5b57\u4e3a\u767d\u8272 */\n"
"            }\n"
"")
        self.TipEnd = QDateEdit(self.TipFrame)
        self.TipEnd.setObjectName(u"TipEnd")
        self.TipEnd.setGeometry(QRect(340, 90, 110, 30))
        self.TipEnd.setMinimumSize(QSize(0, 30))
        self.TipEnd.setStyleSheet(u"            QDateEdit {\n"
"                border: 1px solid lightgray;\n"
"                border-radius: 25px;\n"
"                padding-left: 5px;\n"
"                padding-right: 60px;\n"
"                background-color: rgba(255, 255, 255, 0.8);\n"
"            }\n"
"            QCalendarWidget {\n"
"                background-color: white;\n"
"            }\n"
"            QCalendarWidget QWidget {\n"
"                color: black;\n"
"            }\n"
"            QCalendarWidget QAbstractItemView:enabled {\n"
"                color: white;  /* \u5de5\u4f5c\u65e5\u65e5\u671f\u6570\u5b57\u4e3a\u767d\u8272 */\n"
"            }\n"
"")
        self.StackPages.addWidget(self.TipPage)

        self.gridLayout.addWidget(self.StackPages, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 20)

        self.gridLayout_2.addWidget(self.MainFrame, 0, 0, 1, 1)


        self.retranslateUi(AdminWindow)

        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"\u7ba1\u7406\u754c\u9762", None))
        self.ret_btn.setText(QCoreApplication.translate("AdminWindow", u"\u8fd4\u56de\u767b\u5f55\u754c\u9762", None))
        self.label.setText(QCoreApplication.translate("AdminWindow", u"\u6536\u94f6\u53f0\n"
"\u60a8\u597d\uff0c\u7ba1\u7406\u5458", None))
        self.sell_btn.setText(QCoreApplication.translate("AdminWindow", u"\u6536\u94f6\u4e3b\u9875", None))
        self.rule_btn.setText(QCoreApplication.translate("AdminWindow", u"\u5145\u503c\u89c4\u5219", None))
        self.mem_btn.setText(QCoreApplication.translate("AdminWindow", u"\u4f1a\u5458\u4fe1\u606f", None))
        self.tip_btn.setText(QCoreApplication.translate("AdminWindow", u"\u8ba2\u5355\u4fe1\u606f", None))
        self.sns_btn.setText(QCoreApplication.translate("AdminWindow", u"\u53d1\u9001\u77ed\u4fe1", None))
        self.RuleAdd.setText(QCoreApplication.translate("AdminWindow", u"\u6dfb\u52a0\u89c4\u5219", None))
        self.RuleIcon.setText(QCoreApplication.translate("AdminWindow", u"TextLabel", None))
        self.RuleBase.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"\u8bf7\u8f93\u5165\u5145\u503c\u91d1\u989d...", None))
        self.RuleBonus.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"\u8bf7\u8f93\u5165\u83b7\u8d60\u91d1\u989d...", None))
        self.RuleDel.setText(QCoreApplication.translate("AdminWindow", u"\u5220\u9664\u89c4\u5219", None))
        self.RuleDelInfo.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"\u8bf7\u4efb\u610f\u9009\u62e9\u4e0a\u65b9\u7684\u884c\u6765\u5220\u9664", None))
        self.MemInput1.setPlaceholderText("")
        self.MemInput2.setPlaceholderText("")
        self.MemInput4.setPlaceholderText("")
        self.MemLabel1.setText(QCoreApplication.translate("AdminWindow", u"\u6700\u5c0f\u4f59\u989d\uff1a", None))
        self.MemLabel2.setText(QCoreApplication.translate("AdminWindow", u"\u6700\u5927\u4f59\u989d\uff1a", None))
        self.MemLabel3.setText(QCoreApplication.translate("AdminWindow", u"\u4f1a\u5458\u540d\uff1a", None))
        self.MemLabel4.setText(QCoreApplication.translate("AdminWindow", u"\u624b\u673a\u53f7\uff1a", None))
        self.MemFilter.setText(QCoreApplication.translate("AdminWindow", u"\u67e5\u8be2", None))
        self.MemReFilter.setText(QCoreApplication.translate("AdminWindow", u"\u91cd\u7f6e", None))
        self.MemAdd.setText(QCoreApplication.translate("AdminWindow", u"\u6dfb\u52a0\u4f1a\u5458", None))
        self.MemInput3.setPlaceholderText("")
        self.TipInput3.setPlaceholderText("")
        self.TipLabel5.setText(QCoreApplication.translate("AdminWindow", u"\u4f1a\u5458\u540d\uff1a", None))
        self.TipLabel6.setText(QCoreApplication.translate("AdminWindow", u"\u624b\u673a\u53f7\uff1a", None))
        self.TipLabel3.setText(QCoreApplication.translate("AdminWindow", u"\u4ef7\u683c\u8d77\u59cb\uff1a", None))
        self.TipFilter.setText(QCoreApplication.translate("AdminWindow", u"\u67e5\u8be2", None))
        self.TipReFilter.setText(QCoreApplication.translate("AdminWindow", u"\u91cd\u7f6e", None))
        self.TipInput1.setPlaceholderText("")
        self.TipInput4.setPlaceholderText("")
        self.TipInput2.setPlaceholderText("")
        self.TipLabel4.setText(QCoreApplication.translate("AdminWindow", u"\u4ef7\u683c\u7ec8\u6b62\uff1a", None))
        self.TipLabel1.setText(QCoreApplication.translate("AdminWindow", u"\u5f00\u59cb\u65e5\u671f\uff1a", None))
        self.TipLabel2.setText(QCoreApplication.translate("AdminWindow", u"\u7ed3\u675f\u65e5\u671f\uff1a", None))
    # retranslateUi

