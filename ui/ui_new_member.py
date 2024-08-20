from PyQt5.QtWidgets import QHBoxLayout, QRadioButton, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QRegExpValidator, QFont, QIntValidator
from PyQt5.QtCore import QRegExp
from datetime import datetime

class Ui_NewMember(object):
    def setupUi(self):
        self.setWindowTitle('会员注册')
        font = QFont('黑体', 12)
        layout = QVBoxLayout()

        # 标签和输入框的名称及默认值
        fields = [
            ('name', '姓名:', ''),
            ('phone', '电话:', ''),
            ('register_date', '注册日期:', datetime.now().strftime('%Y-%m-%d')),
            ('last_date', '最后更新日期:', datetime.now().strftime('%Y-%m-%d')),
            ('eye_left', '左眼视力:', ''),
            ('eye_right', '右眼视力:', ''), 
            ('pupil', '瞳距（mm）:', ''),
            ('balance', '余额:', '')
        ]

        # 创建标签和输入框
        self.inputs = {}
        for field, label_text, default_value in fields:
            label = QLabel(label_text)
            label.setFont(font)
            input_field = QLineEdit()
            input_field.setFont(font)
            input_field.setText(default_value)
            layout.addWidget(label)
            layout.addWidget(input_field)
            self.inputs[field] = input_field

        # 单选框组
        self.radio_layout = QHBoxLayout()
        self.Radio1 = QRadioButton("修改余额")
        self.Radio1.setFont(font)
        self.Radio2 = QRadioButton("添加余额")
        self.Radio2.setFont(font)
        self.Radio2.setChecked(True)
        self.radio_layout.addWidget(self.Radio1)
        self.radio_layout.addWidget(self.Radio2)
        layout.addLayout(self.radio_layout)

        # 保存按钮
        self.save_button = QPushButton('保存')
        self.save_button.setFont(font)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        # 输入验证
        self.inputs['phone'].setValidator(QRegExpValidator(QRegExp('^1[3-9][0-9]{9}$')))
        self.inputs['balance'].setValidator(QIntValidator())
        self.inputs['register_date'].setValidator(QRegExpValidator(QRegExp('[0-9]{4}-[0-9]{2}-[0-9]{2}')))
        self.inputs['last_date'].setValidator(QRegExpValidator(QRegExp('[0-9]{4}-[0-9]{2}-[0-9]{2}')))