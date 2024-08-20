from PyQt5.QtCore import Qt, pyqtSignal, QSize
from PyQt5.QtGui import QFont, QPixmap, QCursor, QPainter, QPen, QBrush, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QLabel, QMenu, QVBoxLayout, QGridLayout, QHBoxLayout, QDesktopWidget, QCheckBox, QDialog, QFormLayout, QLineEdit, QPushButton, QFileDialog, QMessageBox, QAction
import os, shutil
from ui.ui_new_member import Ui_NewMember
import app_path
APP = app_path.get_app_path()

class NewProductDialog(QDialog):
    def __init__(self, db, product=None):
        super().__init__()
        self.db = db
        self.product = product
        self.path = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('添加/修改商品')
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(12)
        self.setFont(font)
        layout = QFormLayout()
        self.setLayout(layout)

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.price_input.setValidator(QDoubleValidator())

        layout.addRow('名字:', self.name_input)
        layout.addRow('价格:', self.price_input)

        self.submit_button = QPushButton('保存')
        self.submit_button.clicked.connect(self.save_product)
        self.select_button = QPushButton('选择图片')
        self.select_button.clicked.connect(self.select_image)
        self.image_label = QLabel('无图片')
        layout.addRow(self.select_button)
        layout.addRow(self.image_label)
        layout.addRow(self.submit_button)

        if self.product:  # 如果product不为空，表示修改商品
            self.name_input.setText(self.product[1])
            self.price_input.setText(str(self.product[2]))
            if len(self.product) == 4:  # 如果product包含图片路径
                self.path = self.product[3]
                self.image_label.setPixmap(QPixmap(self.path).scaled(200, 200, Qt.KeepAspectRatio))

    def select_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择图片', directory='C:/Users', filter='Image files (*.jpg *.png)')
        if filename:
            self.path = filename
            pixmap = QPixmap(filename)
            self.image_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))

    def save_product(self):
        name = self.name_input.text()
        price = self.price_input.text()

        if self.path:
            # 复制图片到项目文件夹
            new_path = APP + '/resources/' + self.product[1]
            print(self.path, new_path)
            try:
                shutil.copyfile(self.path, new_path)
            except shutil.SameFileError as e:
                print(e)

        if not (name and price):
            QMessageBox.warning(self, '警告', '所有字段均为必填项')
            return

        if self.product:
            query = '''UPDATE Product SET name=?, price=? WHERE id=?'''
            params = (name, price, self.product[0])
        else:
            query = '''INSERT INTO Product (name, price) VALUES (?, ?)'''
            params = (name, price, )

        self.db.execute_query(query, params)
        self.accept()


class ClickedeQlabel(QLabel):
    clicked = pyqtSignal(tuple)  # 左击信号

    def __init__(self, db, signal):
        super().__init__()
        self.reloads = signal  # 刷新商品的信号
        self.db = db
        self.this_product = None  # 保存商品信息，元组
        self.is_actions = True  # 是否可以操作
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)

    def rightMenuShow(self, pos):   #  添加右键菜单，用作商品信息的增删改
            menu = QMenu(self)
            menu.addAction(QAction('增加商品', menu))
            menu.addAction(QAction('删除商品', menu))
            menu.addAction(QAction('修改商品', menu))
            menu.triggered.connect(self.menuSlot)

            for a in menu.actions():
                a.setEnabled(self.is_actions)
            menu.exec_(QCursor.pos())

    def menuSlot(self, act):
        # 注意
        # `QMessageBox.information()`方法产生的提示框Widget可以自定义
        # 如果写的是`self`，那么提示框也会是我们的图片组件，这不符合预期
        if act.text() == '增加商品':
            dialog = NewProductDialog(self.db)
            if dialog.exec_() == QDialog.Accepted:
                QMessageBox.information(QWidget(), "商品创建", "商品创建成功")
                self.reloads.emit()  # 重新加载商品信息

        elif act.text() == '删除商品':
            if self.this_product:
                product_id = self.this_product[0]
                query = "DELETE FROM Product WHERE id=?"
                self.db.execute_query(query, (product_id,))
                QMessageBox.information(QWidget(), "商品删除", "商品删除成功")
                self.reloads.emit()  # 重新加载商品信息

        elif act.text() == '修改商品':
            if self.this_product:
                dialog = NewProductDialog(self.db, self.this_product)
                if dialog.exec_() == QDialog.Accepted:
                    QMessageBox.information(QWidget(), "商品修改", "商品修改成功")
                    self.reloads.emit()  # 重新加载商品信息

    # 重写鼠标点击事件，用作选择商品
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.this_product:
            self.clicked.emit(self.this_product)
        else:
            super().mousePressEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.pixmap():
            painter.setBrush(QBrush(Qt.GlobalColor.white))
            painter.setPen(QPen(Qt.PenStyle.NoPen))
            painter.drawRoundedRect(self.rect(), 15, 15)
        else:
            painter.setBrush(QBrush(self.pixmap()))
            painter.setPen(QPen(Qt.PenStyle.NoPen))
            painter.drawRoundedRect(self.rect(), 15, 15)
        painter.end()


class ProductComponent(QWidget):
    def __init__(self, db, signal):
        super().__init__()
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(12)
        # 每个商品组件隐藏时保持原有的布局
        sn = self.sizePolicy()
        sn.setRetainSizeWhenHidden(True)
        self.setSizePolicy(sn)

        self.image = ClickedeQlabel(db, signal)
        self.name = QLabel()
        self.price = QLabel()
        self.name.setFont(font)
        self.price.setFont(font)
        layout = QVBoxLayout()
        layout.setSpacing(0)
        self.image.setStyleSheet("""QLabel{
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 0px;
            background-color: rgb(255, 255, 255);
            }
        """)
        self.name.setStyleSheet("""
            border-radius: 0px;
            background-color: rgb(255, 255, 255);
        """)
        self.price.setStyleSheet("""
            border-top-left-radius: 0px;
            border-top-right-radius: 0px;
            border-bottom-left-radius: 15px;
            border-bottom-right-radius: 15px;
            background-color: rgb(255, 255, 255);
        """)
        layout.addWidget(self.image)
        layout.addWidget(self.name)
        layout.addWidget(self.price)
        layout.setStretch(0, 3)
        layout.setStretch(1, 1)
        layout.setStretch(2, 1)
        layout.setContentsMargins(0, 0, 0, 0)  # 设置边距
        self.setLayout(layout)


class MarketComponent(QWidget):
    def __init__(self, signal):
        super().__init__()
        self.out_signal = signal  # 刷新Market的信号
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(12)

        # 每个购物栏组件隐藏时保持原有的布局
        sn = self.sizePolicy()
        sn.setRetainSizeWhenHidden(True)
        self.setSizePolicy(sn)

        self.i = QLabel()
        self.n = QLabel()
        self.p = QLabel()
        self.ap = QLabel()
        self.cnt = QLabel()
        self.plus = QPushButton('+')
        self.minus = QPushButton('-')
        self.i.setFont(font)
        self.n.setFont(font)
        self.p.setFont(font)
        self.ap.setFont(font)
        self.cnt.setFont(font)
        self.plus.setFont(font)
        self.minus.setFont(font)

        self.setStyleSheet("""
            border: 1px solid rgb(100, 100, 189);
        """)
        self.cnt.setStyleSheet('color: red;')
        self.ap.setStyleSheet('color: red;')
        
        layout = QGridLayout()
        # 添加部件到布局中
        layout.addWidget(self.i, 0, 0, 2, 1)  # 图片占据两行
        layout.addWidget(self.n, 0, 1, 1, 3)  # 名称占据第一行
        layout.addWidget(self.ap, 1, 1, 1, 3)  # 总价占据第二行
        layout.addWidget(self.p, 2, 0, 1, 1)  # 单价占据第三行的左边
        layout.addWidget(self.minus, 2, 1, 1, 1)  # 减少按钮占据第三行的中间
        layout.addWidget(self.cnt, 2, 2, 1, 1)  # 数量标签占据第三行的中间
        layout.addWidget(self.plus, 2, 3, 1, 1)  # 增加按钮占据第三行的右边
        
        # 设置布局的伸缩比例
        layout.setColumnStretch(0, 3)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        
        # 设置布局的边距和间距
        layout.setContentsMargins(0, 0, 0, 0)  # 设置边距
        layout.setSpacing(2)  # 设置控件之间的间距
        self.setLayout(layout)

        self.plus.clicked.connect(self.__plus)
        self.minus.clicked.connect(self.__minus)

    # 点击按钮时触发信号，发送商品名给外部的槽函数
    def __minus(self):
        self.out_signal.emit(('minus', self.n.text(),))
    def __plus(self):
        self.out_signal.emit(('plus', self.n.text(),))


class MemberDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("选择会员")

        self.name_label = QLabel("用户名或手机号:")
        self.name_input = QLineEdit()
        self.button = QPushButton("查找会员")
        # 点击按钮时关闭对话框，作为提示外部开始查询会员的信号
        self.button.clicked.connect(self.check_input)
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def check_input(self):
        member_name = self.name_input.text().strip()
        if not member_name:
            QMessageBox.warning(self, '警告', '请输入信息')
        else:
            self.accept()  # 输入框不为空时才关闭对话框并返回accept


class NewMemberDialog(QDialog, Ui_NewMember):
    def __init__(self, db, member=None):
        super().__init__()
        self.setupUi()
        self.db = db
        self.member = member
        self.rule = db.get_rules()
        self.save_button.clicked.connect(self.save_member)

        if self.member:  # 更新已有信息
            for key, value in self.member.items():
                if key in self.inputs:
                    self.inputs[key].setText(str(value))

    def save_member(self):
        name = self.inputs['name'].text()
        phone = self.inputs['phone'].text()
        balance = self.inputs['balance'].text()
        register_date = self.inputs['register_date'].text()
        last_date = self.inputs['last_date'].text()
        eye_left = self.inputs['eye_left'].text()
        eye_right = self.inputs['eye_right'].text()
        pupil = self.inputs['pupil'].text()
        
        if not (name and phone and balance and register_date and last_date and eye_left and eye_right and pupil):
            QMessageBox.warning(self, '警告', '所有字段均为必填项')
            return

        if self.Radio2.isChecked():
            balance = self.get_true_balance(float(balance))
        if self.member:
            the_id = self.member['id']
            query = '''UPDATE Member SET name=?, phone=?, balance=?, register_date=?, last_date=?, 
                       eye_left=?, eye_right=?, pupil=? WHERE id=?'''
            params = (name, phone, balance, register_date, last_date, eye_left, eye_right, pupil, the_id)
        else:
            query = '''INSERT INTO Member (name, phone, balance, register_date, last_date, eye_left, eye_right, pupil) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            params = (name, phone, balance, register_date, last_date, eye_left, eye_right, pupil)

        self.db.execute_query(query, params)
        self.accept()

    def get_true_balance(self, this_time):
        before = float(self.member['balance']) if self.member else 0
        for r in self.rule:
            if this_time >= r[1]:
                before += r[2] + this_time
                QMessageBox.information(self, '提示', f'实际充值金额为: {this_time + r[2]}')
                return before

        before += this_time
        return before
    

class MemberBtnGroup(QWidget):
    def __init__(self, member, db, sms):
        super().__init__()
        self.parent_ui = None
        self.member = member
        self.db = db
        self.sms_list = sms
        self.setupUi()
        self.CheckBox.stateChanged.connect(self.change_sms_list)
        self.DelBtn.clicked.connect(self.delete_member)
        self.EditBtn.clicked.connect(self.edit_member)

    def setupUi(self):
        # 编辑按钮
        self.EditBtn = QPushButton("修改", self)
        self.EditBtn.setObjectName("EditBtn")
        self.EditBtn.setMinimumSize(QSize(50, 20))
        font = QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.EditBtn.setFont(font)
        self.EditBtn.setAutoFillBackground(False)
        self.EditBtn.setStyleSheet("QPushButton {\n"
                                   "background-color: #00aaff;\n"
                                   "color: #f9ffff;\n"
                                   "border-radius: 10px;\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "background-color: #0096e0;\n"
                                   "}")

        # 删除按钮
        self.DelBtn = QPushButton("删除", self)
        self.DelBtn.setObjectName("DelBtn")
        self.DelBtn.setMinimumSize(QSize(50, 20))
        self.DelBtn.setFont(font)
        self.DelBtn.setAutoFillBackground(False)
        self.DelBtn.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(255, 68, 55);\n"
                                  "color: #f9ffff;\n"
                                  "border-radius: 10px;\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "background-color: rgb(225, 15, 0);\n"
                                  "}")

        # 短信候选复选框
        self.CheckBox = QCheckBox("短信候选", self)
        self.CheckBox.setObjectName("CheckBox")
        font1 = QFont()
        font1.setFamily("黑体")
        font1.setPointSize(12)
        self.CheckBox.setFont(font1)

        # 布局管理
        layout = QHBoxLayout()
        layout.addWidget(self.CheckBox)
        layout.addWidget(self.EditBtn)
        layout.addWidget(self.DelBtn)

        self.setLayout(layout)

    def setParentUI(self, parent_ui):  # 传递 AdminUI 实例
        self.parent_ui = parent_ui

    def edit_member(self):
        dialog = NewMemberDialog(self.db, member=self.member)
        if dialog.exec_() == QDialog.Accepted:
            QMessageBox.information(self, "会员修改", "会员修改成功")
        self.parent_ui.mode_change(mode='MEMBER')

    def delete_member(self):
        confirm_box = QMessageBox()
        confirm_box.setIcon(QMessageBox.Question)
        confirm_box.setWindowTitle("确认删除")
        confirm_box.setText("你确定要删除这条记录吗？")
        confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_box.setDefaultButton(QMessageBox.No)
        reply = confirm_box.exec()

        if reply == QMessageBox.Yes:
            query = "DELETE FROM Member WHERE id = ?"
            self.db.execute_query(query, (self.member['id'],))
            self.parent_ui.mode_change(mode='MEMBER')

    def change_sms_list(self, state):
        if state == Qt.Checked and self.member['id'] not in self.sms_list:
            self.sms_list.append(self.member['id'])
        elif state == Qt.Unchecked and self.member['id'] in self.sms_list:
            self.sms_list.remove(self.member['id'])

class TipBtnGroup(QWidget):
    def __init__(self, tip, db):
        super().__init__()
        self.parent_ui = None
        self.tip = tip
        self.db = db
        self.setupUi()
        self.DelBtn.clicked.connect(self.delete_tip)
        self.ViewBtn.clicked.connect(self.view_tip)

    def setupUi(self):
        # 编辑按钮
        self.ViewBtn = QPushButton("查看", self)
        self.ViewBtn.setObjectName("ViewBtn")
        self.ViewBtn.setMinimumSize(QSize(50, 20))
        font = QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ViewBtn.setFont(font)
        self.ViewBtn.setAutoFillBackground(False)
        self.ViewBtn.setStyleSheet("QPushButton {\n"
                                   "background-color: #00aaff;\n"
                                   "color: #f9ffff;\n"
                                   "border-radius: 10px;\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "background-color: #0096e0;\n"
                                   "}")

        # 删除按钮
        self.DelBtn = QPushButton("删除", self)
        self.DelBtn.setObjectName("DelBtn")
        self.DelBtn.setMinimumSize(QSize(50, 20))
        self.DelBtn.setFont(font)
        self.DelBtn.setAutoFillBackground(False)
        self.DelBtn.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(255, 68, 55);\n"
                                  "color: #f9ffff;\n"
                                  "border-radius: 10px;\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "background-color: rgb(225, 15, 0);\n"
                                  "}")
        # 布局管理
        layout = QHBoxLayout()
        layout.addWidget(self.ViewBtn)
        layout.addWidget(self.DelBtn)
        self.setLayout(layout)

    def setParentUI(self, parent_ui):  # 传递 AdminUI 实例
        self.parent_ui = parent_ui
    
    def delete_tip(self):
        reply = QMessageBox.question(self, '确认删除', f'确定要删除订单 {self.tip["id"]} 吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            query = "DELETE FROM Orders WHERE id = ?"
            self.db.execute_query(query, (self.tip['id'],))
            try:
                os.remove(f"{APP}/tips/order{self.tip['id']}.txt")
            except FileNotFoundError:
                QMessageBox.warning(self, '警告', f'订单文件 {self.tip["id"]} 不存在')
            self.parent_ui.mode_change(mode='TIP')

    def view_tip(self):
        try:
            order_file = f"{APP}/tips/order{self.tip['id']}.txt"
            if os.path.exists(order_file):
                with open(order_file, 'r', encoding='utf-8') as file:
                    content = file.read()
                display_widget = DisplayWidget(content)
                display_widget.show()
                display_widget.exec_()
            else:
                QMessageBox.warning(self, '警告', f'订单文件 {order_file} 不存在')
        except Exception as e:
            QMessageBox.critical(self, '错误', f'查看订单失败: {str(e)}')
        

class DisplayWidget(QDialog):
    def __init__(self, content):
        super().__init__()
        self.setWindowTitle('订单详情')
        self.content = content
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.content_label = QLabel(self.content)
        self.content_label.setWordWrap(True)
        layout.addWidget(self.content_label)
        self.setLayout(layout)
        font = QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)

        self.show_in_center()

    def show_in_center(self):  # 窗口移动至中央
        cp = QDesktopWidget().availableGeometry().center()
        # cp is tuple of (x, y, w, h)
        self.resize(cp.x(), cp.y())
        _, _, width, height = self.frameGeometry().getRect()
        self.move(cp.x() - width // 2, cp.y() - height // 2)