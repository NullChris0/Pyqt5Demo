from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QListWidgetItem
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QDate
import qtawesome
from typing import List
import ui.back  # 导入资源文件
from ui.ui_custom import *
from ui.ui_admin import Ui_AdminWindow

class AdminUI(QWidget, Ui_AdminWindow):
    back_to_login = pyqtSignal()

    def __init__(self, db):
        super().__init__()
        self.setWindowIcon(QIcon(':back/icon.png'))
        self.setupUi(self)
        self.rules = None
        self.member_infos = None
        self.sms_list = []
        self.db = db

        self.setupWidgets()
        self.setupLayouts()

        self.mode_change(mode='RULE')

    def setupLayouts(self):
        # 设置 MenuFrame 的布局
        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.ret_btn)
        menu_layout.addWidget(self.label)
        menu_layout.addWidget(self.scrollArea)
        self.MenuFrame.setLayout(menu_layout)

        # 设置滚动区域的内容布局
        scroll_layout = QGridLayout(self.scrollAreaWidgetContents)
        scroll_layout.addWidget(self.sell_btn)
        scroll_layout.addWidget(self.rule_btn)
        scroll_layout.addWidget(self.mem_btn)
        scroll_layout.addWidget(self.tip_btn)
        scroll_layout.addWidget(self.sns_btn)
        self.scrollAreaWidgetContents.setLayout(scroll_layout)

        # 设置规则区域的布局
        rule_layout = QVBoxLayout()
        rule_layout.setContentsMargins(0, 0, 0, 0)
        rule_layout.addWidget(self.RuleFrame)
        self.RulePage.setLayout(rule_layout)
        internal_rule_layout = QHBoxLayout()
        internal_rule_layout_right = QVBoxLayout()
        rule_input_layout = QHBoxLayout()
        rule_del_layout = QHBoxLayout()
        rule_input_layout.addWidget(self.RuleBase)
        rule_input_layout.addWidget(self.RuleBonus)
        rule_del_layout.addWidget(self.RuleDelInfo)
        rule_del_layout.addWidget(self.RuleDel)
        rule_del_layout.setStretch(0, 1)
        rule_del_layout.setStretch(1, 1)
        # 将各个组件添加到右侧布局
        internal_rule_layout_right.addLayout(rule_input_layout)
        internal_rule_layout_right.addWidget(self.RuleAdd)
        internal_rule_layout_right.addWidget(self.RuleList)
        internal_rule_layout_right.addLayout(rule_del_layout)
        # 将左侧图标和右侧布局添加到整体布局
        internal_rule_layout.addWidget(self.RuleIcon)
        internal_rule_layout.addLayout(internal_rule_layout_right)
        internal_rule_layout.setStretch(0, 1)
        internal_rule_layout.setStretch(1, 2)
        self.RuleFrame.setLayout(internal_rule_layout)

        # 设置会员区域的布局
        member_layout = QVBoxLayout()
        member_layout.setContentsMargins(0, 0, 0, 0)
        member_layout.addWidget(self.MemberFrame)
        self.MemberPage.setLayout(member_layout)
        internal_mem_layout = QGridLayout()
        internal_mem_layout.addWidget(self.MemLabel1, 0, 0, 1, 1)
        internal_mem_layout.addWidget(self.MemInput1, 0, 1, 1, 1)
        internal_mem_layout.addWidget(self.MemLabel3, 0, 2, 1, 1)
        internal_mem_layout.addWidget(self.MemInput3, 0, 3, 1, 1)
        internal_mem_layout.addWidget(self.MemFilter, 0, 4, 1, 1)
        internal_mem_layout.addWidget(self.MemReFilter, 0, 5, 1, 1)
        internal_mem_layout.addWidget(self.MemLabel2, 1, 0, 1, 1)
        internal_mem_layout.addWidget(self.MemInput2, 1, 1, 1, 1)
        internal_mem_layout.addWidget(self.MemLabel4, 1, 2, 1, 1)
        internal_mem_layout.addWidget(self.MemInput4, 1, 3, 1, 1)
        internal_mem_layout.addWidget(self.MemAdd, 1, 4, 1, 2)
        internal_mem_layout.addWidget(self.MemTable, 2, 0, 1, 6)
        internal_mem_layout.setColumnStretch(0, 1)
        internal_mem_layout.setColumnStretch(1, 4)
        internal_mem_layout.setColumnStretch(2, 1)
        internal_mem_layout.setColumnStretch(3, 4)
        internal_mem_layout.setColumnStretch(4, 2)
        internal_mem_layout.setColumnStretch(5, 2)
        internal_mem_layout.setRowStretch(0, 2)
        internal_mem_layout.setRowStretch(1, 2)
        internal_mem_layout.setRowStretch(2, 10)
        self.MemberFrame.setLayout(internal_mem_layout)
        # 列宽自动，行高依据内容（为了撑满按钮组件）
        self.MemTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.MemTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # 设置订单区域的布局
        tip_layout = QVBoxLayout()
        tip_layout.setContentsMargins(0, 0, 0, 0)
        tip_layout.addWidget(self.TipFrame)
        self.TipPage.setLayout(tip_layout)
        internal_tip_layout = QGridLayout()
        internal_tip_layout.addWidget(self.TipLabel1, 0, 0, 1, 1)
        internal_tip_layout.addWidget(self.TipStart, 0, 1, 1, 1)
        internal_tip_layout.addWidget(self.TipLabel2, 0, 2, 1, 1)
        internal_tip_layout.addWidget(self.TipEnd, 0, 3, 1, 1)
        internal_tip_layout.addWidget(self.TipLabel5, 0, 4, 1, 1)
        internal_tip_layout.addWidget(self.TipInput3, 0, 5, 1, 1)
        internal_tip_layout.addWidget(self.TipFilter, 0, 6, 1, 1)
        internal_tip_layout.addWidget(self.TipLabel3, 1, 0, 1, 1)
        internal_tip_layout.addWidget(self.TipInput1, 1, 1, 1, 1)
        internal_tip_layout.addWidget(self.TipLabel4, 1, 2, 1, 1)
        internal_tip_layout.addWidget(self.TipInput2, 1, 3, 1, 1)
        internal_tip_layout.addWidget(self.TipLabel6, 1, 4, 1, 1)
        internal_tip_layout.addWidget(self.TipInput4, 1, 5, 1, 1)
        internal_tip_layout.addWidget(self.TipReFilter, 1, 6, 1, 1)
        internal_tip_layout.addWidget(self.TipTable, 2, 0, 1, 7)
        internal_tip_layout.setColumnStretch(0, 1)
        internal_tip_layout.setColumnStretch(1, 3)
        internal_tip_layout.setColumnStretch(2, 1)
        internal_tip_layout.setColumnStretch(3, 3)
        internal_tip_layout.setColumnStretch(4, 1)
        internal_tip_layout.setColumnStretch(5, 3)
        internal_tip_layout.setColumnStretch(6, 2)
        internal_tip_layout.setRowStretch(0, 2)
        internal_tip_layout.setRowStretch(1, 2)
        internal_tip_layout.setRowStretch(2, 10)
        self.TipFrame.setLayout(internal_tip_layout)
        # 列宽自动，行高依据内容（为了撑满按钮组件）
        self.TipTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.TipTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.TipStart.setDate(QDate.currentDate())
        self.TipEnd.setDate(QDate.currentDate())
        self.TipStart.setDisplayFormat('yyyy-MM-dd')
        self.TipEnd.setDisplayFormat('yyyy-MM-dd')
        self.TipStart.setCalendarPopup(True)
        self.TipEnd.setCalendarPopup(True)

    def setupWidgets(self):
        self.sell_btn.setEnabled(False); self.sns_btn.setEnabled(False)
        self.ret_btn.clicked.connect(self.logout)  # 登出按钮
        self.rule_btn.clicked.connect(lambda: self.mode_change(mode='RULE'))  # 规则管理按钮
        self.mem_btn.clicked.connect(lambda: self.mode_change(mode='MEMBER'))  # 会员管理按钮
        self.tip_btn.clicked.connect(lambda: self.mode_change(mode='TIP'))  # 订单管理按钮
        # Rule 部分
        self.RuleList.currentItemChanged.connect(self.on_RuleList_rowSelect)  # 监听选择的行内容
        self.RuleIcon.setPixmap(qtawesome.icon('fa5s.money-bill-alt', color='green').pixmap(256, 256))
        self.RuleBase.setValidator(QIntValidator())  # 筛选框限定
        self.RuleBonus.setValidator(QIntValidator())  # 筛选框限定
        # Member 部分
        self.MemInput1.setValidator(QIntValidator())  # 筛选框限定
        self.MemInput2.setValidator(QIntValidator())  # 筛选框限定
        self.MemInput4.setValidator(QIntValidator())  # 筛选框限定
        # Tip 部分
        self.TipInput1.setValidator(QIntValidator())  # 筛选框限定
        self.TipInput2.setValidator(QIntValidator())  # 筛选框限定
        self.TipInput4.setValidator(QIntValidator())  # 筛选框限定
    
    def mode_change(self, mode: str):
        if mode == 'RULE':
            self.StackPages.setCurrentIndex(0)
            query = 'SELECT * FROM RechargeRules'
            # 按照充值基数从大到小排序
            self.rules = self.db.get_rules()
            self.RuleList.clear()
            for index, rule in enumerate(self.rules, start=1):
                item = QListWidgetItem()
                item.setText(f"{index}. 充值{rule[1]}元，送{rule[2]}元")
                self.RuleList.addItem(item)

        elif mode == 'MEMBER':
            self.StackPages.setCurrentIndex(1)
            query = "SELECT * FROM Member"
            member_data = self.db.fetch_dicts(query)
            self.table_init(table=self.MemTable, data=member_data, create_function=self.create_MemberBtnGroup,
                            title=['会员名','手机号', '余额', '注册日期', '活跃日期', '左眼视力', '右眼视力', '瞳距', '操作'])

        elif mode == 'TIP':
            self.StackPages.setCurrentIndex(2)
            query = """
                SELECT Orders.id, Member.name, Member.phone, Orders.total_price, Orders.create_date
                FROM Orders
                JOIN Member ON Orders.member_id = Member.id
            """
            tip_data = self.db.fetch_dicts(query)
            self.table_init(table=self.TipTable, data=tip_data, create_function=self.create_TipBtnGroup,
                            title=['会员名', '手机号', '总金额', '创建日期', '操作'])
    
    @pyqtSlot()
    def on_RuleAdd_clicked(self):
        amount = self.RuleBase.text(); bonus = self.RuleBonus.text()
        if amount and bonus:
            query = "INSERT OR IGNORE INTO RechargeRules (amount, bonus) VALUES (?, ?)"
            self.db.execute_query(query, (amount, bonus))
            self.RuleBase.clear(); self.RuleBonus.clear()
            self.mode_change(mode='RULE')
        else:
            QMessageBox.warning(self, '警告', '请输入充值金额和赠送金额')

    @pyqtSlot()
    def on_RuleDel_clicked(self):
        if not self.RuleDelInfo.text():
            QMessageBox.warning(self, '警告', '尚未选择')
            return
        # 从self.rules中找出正确的数据库索引（并非列表索引）
        index = self.rules[int(self.RuleDelInfo.text()[0]) - 1][0]
        query = "DELETE FROM RechargeRules WHERE id = ?"
        self.db.execute_query(query, (index,))
        self.RuleDelInfo.clear()
        self.mode_change('RULE')

    def on_RuleList_rowSelect(self, current_item, _):
        '''选择某一行规则时，在下方显示详细信息'''
        if current_item:
            self.RuleDelInfo.setText(current_item.text())

    @pyqtSlot()
    def on_MemAdd_clicked(self):
        dialog = NewMemberDialog(self.db)
        if dialog.exec_() == QDialog.Accepted:
            QMessageBox.information(self, "会员添加", "会员添加成功")
            self.mode_change('MEMBER')

    @pyqtSlot()
    def on_MemFilter_clicked(self):
        name = self.MemInput3.text()
        phone = self.MemInput4.text()
        balance1 = self.MemInput1.text()
        balance2 = self.MemInput2.text()

        query = "SELECT * FROM Member WHERE 1=1"
        params = []
        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        if phone:
            query += " AND phone LIKE ?"
            params.append(f"%{phone}%")
        if balance1:
            query += " AND balance >= ?"
            params.append(balance1)
        if balance2:
            query += " AND balance <= ?"
            params.append(balance2)
        results = self.db.fetch_dicts(query, params)
        self.table_init(table=self.MemTable, data=results, create_function=self.create_MemberBtnGroup, title=['会员名','手机号', '余额', '注册日期', '活跃日期', '左眼视力', '右眼视力', '瞳距', '操作'])

    @pyqtSlot()
    def on_MemReFilter_clicked(self):
        self.MemInput3.clear()
        self.MemInput4.clear()
        self.MemInput1.clear()
        self.MemInput2.clear()
        self.mode_change('MEMBER')

    @pyqtSlot()
    def on_TipFilter_clicked(self):
        total1 = self.TipInput1.text()
        total2 = self.TipInput2.text()
        n = self.TipInput3.text()
        p = self.TipInput4.text()
        st = self.TipStart.date().toString('yyyy-MM-dd')
        ed = self.TipEnd.date().toString('yyyy-MM-dd')

        query = """SELECT Orders.id, Member.name, Member.phone, Orders.total_price, Orders.create_date
                FROM Orders
                JOIN Member ON Orders.member_id = Member.id
                WHERE 1=1"""
        params = []
        query += " AND Orders.create_date BETWEEN ? AND ?"
        params.append(f"{st}"); params.append(f"{ed}")
        if total1:
            query += " AND total_price >= ?"
            params.append(total1)
        if total2:
            query += " AND total_price <= ?"
            params.append(total2)
        if n:
            query += " AND Member.name LIKE ?"
            params.append(f"%{n}%")
        if p:
            query += " AND Member.phone = ?"
            params.append(str(p))
        results = self.db.fetch_dicts(query, params)
        self.table_init(table=self.TipTable, data=results, create_function=self.create_TipBtnGroup, title=['会员名', '手机号', '总金额', '创建日期', '操作'])

    @pyqtSlot()
    def on_TipReFilter_clicked(self):
        self.TipInput1.clear()
        self.TipInput2.clear()
        self.TipInput3.clear()
        self.TipInput4.clear()
        self.mode_change('TIP')

    def create_MemberBtnGroup(self, member):
        '''实际创建表格功能组件对象的创建方法，需要传递AdminUI的引用，来使用table_init方法
        \n参数：self@AdminUI，表格行数据'''
        group = MemberBtnGroup(member, self.db, self.sms_list)
        group.setParentUI(self)
        return group    
    
    def create_TipBtnGroup(self, member):
        group = TipBtnGroup(member, self.db)
        group.setParentUI(self)
        return group

    def table_init(self, table: QTableWidget,title:list, data: List[dict], create_function):
        if not data:
            table.clear()
            QMessageBox.warning(self, '警告', '没有数据')
            return
        # 首先设置表格格数
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))  # id 不展示
        table.setHorizontalHeaderLabels(title)
        # 为功能按钮列调整列宽
        table.horizontalHeader().setSectionResizeMode(len(data[0])-1, QHeaderView.ResizeToContents)
        for row, row_data in enumerate(data):
            for col, (key, value) in enumerate({k: v for k, v in row_data.items() if k != 'id'}.items()):
                table.setItem(row, col, QTableWidgetItem(str(value)))
            # 创建自定义 QWidget 并添加到表格中
            table.setCellWidget(row, len(row_data) - 1, create_function(row_data))
    
    def logout(self):
        self.back_to_login.emit()
        self.close()

    def paintEvent(self, event):
        '''重写paintEvent方法，自适应绘制背景图'''
        background_image = QPixmap(':/back/0.png')
        painter = QPainter(self)
        # 获取窗口大小
        window_width = self.width()
        window_height = self.height()
        # 将背景图片缩放到窗口大小
        scaled_pixmap = background_image.scaled(window_width, window_height)
        # 计算图片绘制的起始点，使其居中
        x = (window_width - scaled_pixmap.width()) // 2
        y = (window_height - scaled_pixmap.height()) // 2
        # 绘制背景图片
        painter.drawPixmap(x, y, scaled_pixmap)
        super().paintEvent(event)