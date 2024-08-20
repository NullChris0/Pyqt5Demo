from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QThread, QTimer
import ui.back  # 导入资源文件
from datetime import datetime
from pathlib import Path
from typing import List
from ui.ui_custom import *
from ui.ui_sell import Ui_SellWindow
import app_path
APP = app_path.get_app_path()

class SellUI(QWidget, Ui_SellWindow):
    back_to_login = pyqtSignal()
    reload_signal = pyqtSignal()  # 刷新商品信号、总金额信号
    change_signal = pyqtSignal(tuple)  # 购物车变化信号，用于更新购物车
    require_member = pyqtSignal()  # 结算购物车时，若未登录，则发出此信号

    def __init__(self, db):
        super().__init__()
        self.setWindowIcon(QIcon(':back/icon.png'))
        self.setupUi(self)
        self.db = db
        self.current_page = 1  # 当前商品页

        self.setupLayouts()  # 自定义布局方法
        self.setupWidgets()

        # 初始化购物车
        self.my_market = Market(self.MyMarkets, self.db, self.require_member, self.Logined)
        self.GachaButton.clicked.connect(self.my_market.gacha)  # 结算
        self.change_signal.connect(self.my_market.changement)
        # 图片组件绑定单击事件（添加单个商品）
        for _, product in enumerate(self.MyProducts):
            product.image.clicked.connect(self.my_market.add_product)

        # 单独开启一个线程，用于刷新商品和总金额
        self.reload_thread = SellThread(self.reload_signal, self.my_market.market)
        self.reload_thread.start()
        self.reload_signal.connect(self.load_products)
        self.reload_signal.connect(self.setMenuEnable)
        self.reload_signal.connect(self.my_market.render)
        self.reload_signal.connect(lambda: self.FinalPrice.setText(f'总金额：{self.my_market.final_price}元'))

    def load_products(self):
        # 定义商品加载语句、筛选语句（两个字段分别精确查询）
        parms = '%{0}%'.format(self.MySearch.text().strip())
        offset = (self.current_page - 1) * 9
        if parms != '':
            query = "SELECT * FROM Product WHERE name LIKE ? LIMIT 9 OFFSET ?" if self.Radio1.isChecked() else "SELECT * FROM Product WHERE price LIKE ? LIMIT 9 OFFSET ?" 
            product = self.db.fetch_all(query, (parms, offset))
        else:
            query = "SELECT * FROM Product LIMIT 9 OFFSET ?"
            product = self.db.fetch_all(query, (offset, ))

        fp = Path(f"{APP}/resources/")
        for id, s in enumerate(product):
            widget = self.MyProducts[id]
            widget.setVisible(True)
            widget.name.setText(s[1])  # name字段
            widget.price.setText(f'{s[2]}元')  # price字段
            widget.image.this_product = s  # image对象存储信息
            t = list(fp.rglob(s[1] + '.png')) + list(fp.rglob(s[1] + '.jpg'))
            if len(t) != 0:
                tt = str(t[0]).replace('\\', '/')
                widget.image.setText('')
                widget.image.setPixmap(QPixmap(tt).scaled(widget.image.width(), 100))
                widget.image.this_product = s + (tt, )  # 元组合并
            else:
                widget.image.setPixmap(QPixmap(''))
        for i in range(len(product), 9):
            self.MyProducts[i].setVisible(False)

    def setMenuEnable(self):
        if self.my_market.market:
            for widget in self.MyProducts:
                widget.image.is_actions = False
        else:
            for widget in self.MyProducts:
                widget.image.is_actions = True

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

        # 设置MarketFrame的布局
        market_layout = QGridLayout()
        market_layout.addWidget(self.Logined, 0, 0, 1, 2)
        market_layout.addWidget(self.MemberRegist, 1, 0, 1, 1)
        market_layout.addWidget(self.MemberLogin, 1, 1, 1, 1)
        market_layout.addWidget(self.MarketList, 2, 0, 1, 2)
        market_layout.addWidget(self.FinalPrice, 3, 0, 1, 2)
        market_layout.addWidget(self.GachaButton, 4, 0, 1, 1)
        market_layout.addWidget(self.ClearButton, 4, 1, 1, 1)
        market_layout.setRowStretch(0, 1)
        market_layout.setRowStretch(1, 1)
        market_layout.setRowStretch(2, 16)
        market_layout.setRowStretch(3, 1)
        market_layout.setRowStretch(4, 1)
        self.MarketFrame.setLayout(market_layout)

        # 商品展示区域
        product_layout = QGridLayout()
        product_layout.addWidget(self.Radio1, 0, 0, 1, 1)
        product_layout.addWidget(self.Radio2, 1, 0, 1, 1)
        product_layout.addWidget(self.MySearch, 0, 1, 2, 1)
        product_layout.addWidget(self.MySlider, 2, 0, 1, 2)
        product_layout.addWidget(self.ProductsList, 3, 0, 1, 2)
        self.ProductFrame.setLayout(product_layout)

    def setupWidgets(self):
        # 创建9个商品展示块，6个购物车展示块
        self.MyProducts = [ProductComponent(self.db, self.reload_signal) for _ in range(9)]
        self.MyMarkets = [MarketComponent(self.change_signal) for _ in range(6)]
        products_grid = QGridLayout()
        market_vertical = QVBoxLayout()
        market_vertical.setContentsMargins(0, 0, 0, 0)
        products_grid.setSpacing(10)
        products_grid.setContentsMargins(0, 0, 0, 0)

        # 更新布局器
        for i, product in enumerate(self.MyProducts):
            products_grid.addWidget(product, i // 3, i % 3)
        self.ProductsList.setLayout(products_grid)
        for i, market in enumerate(self.MyMarkets):
            market_vertical.addWidget(market)
        self.MarketList.setLayout(market_vertical)

        self.sns_btn.setEnabled(False)
        self.tip_btn.setEnabled(False)
        self.mem_btn.setEnabled(False)
        self.rule_btn.setEnabled(False)
        self.ret_btn.clicked.connect(self.logout)  # 登出按钮
        self.ClearButton.clicked.connect(lambda: self.my_market.market.clear())  # 清空按钮
        self.require_member.connect(self.on_MemberLogin_clicked)  # 结算时跳转登录
        self.MySlider.valueChanged.connect(lambda x: setattr(self, "current_page", x))  # 更新页码
        self.Radio1.setChecked(True)

    @pyqtSlot()
    def on_MemberLogin_clicked(self):
        dialog = MemberDialog()
        if dialog.exec_() == QDialog.Accepted:
            member_name = dialog.name_input.text().strip()
            self.my_market.member = self.db.get_member(member_name)
            if self.my_market.member:
                # 需要开启QLabel的WordRrap属性
                self.Logined.setText("当前会员：" + self.my_market.member["name"] + "\n余额：" + str(self.my_market.member["balance"]))
            else:
                QMessageBox.warning(QWidget(), "查找失败", "未找到会员，请检查用户名或手机号。")
    @pyqtSlot()
    def on_MemberRegist_clicked(self):
        dialog = NewMemberDialog(self.db)
        if dialog.exec_() == QDialog.Accepted:
            self.my_market.member = self.db.get_member(dialog.inputs['name'].text().strip())
            self.Logined.setText("当前会员：" + self.my_market.member["name"] + "\n余额：" + str(self.my_market.member["balance"]))

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


class Market(object):
    def __init__(self, component:List[MarketComponent], db, signal, holder):
        self.db = db
        self.market = []  # 商品信息字典的列表
        self.component = component
        self.member = {}
        self.holder = holder
        self.require_signal = signal

    @property
    def final_price(self):
        return sum(item['total_price'] for item in self.market)

    def render(self):
        '''渲染购物车商品'''
        for i in range(len(self.market)):
            if i == 6:
                break  # TODO:目前只能渲染6个商品

            self.component[i].setVisible(True)
            product = self.market[i]
            
            self.component[i].n.setText(product['name'])  # 商品名称
            self.component[i].p.setText('单价:' + str(product['price']) + '元')  # 商品单价
            self.component[i].cnt.setText('数量:' + str(product['quantity']))  # 商品数量
            self.component[i].ap.setText('总计:' + str(product['total_price']) + '元')  # 商品总价
            if product['path']:
                self.component[i].i.setStyleSheet('''
                    QLabel{{border: 1px solid rgb(100, 100, 189); border-image: url({0})}}
                    '''.format(product['path']))
            else:
                self.component[i].i.setText('暂无图片')
                self.component[i].i.setStyleSheet('border: 1px solid rgb(100, 100, 189);')
        for i in range(len(self.market), 6):
            self.component[i].setVisible(False)

    def add_product(self, product):
        id, name, price = product[:3]
        img = product[3:]  # 剩下的元素作为 img 列表

        new_item = {
            'id': id,
            'name': name,
            'price': price,
            'quantity': 1,  # 数量
            'total_price': price,  # 初始总价为单价
            'path': None if len(img) == 0 else img[0]
        }
        # 购物车为空则直接添加新商品，否则需要遍历购物车并更新商品数量
        if not self.market:
            self.market.append(new_item)
        else:
            for item in self.market:
                if item['name'] == new_item['name']:
                    item['quantity'] += 1
                    item['total_price'] = item['quantity'] * item['price']
                    break
            else:
                self.market.append(new_item)

    def changement(self, info):
        op, name = info
        index, price = (None, None)
        # 遍历寻找商品名对应的索引
        for i, j in enumerate(self.market):
            if j['name'] == name:
                index = i; price = j['price']
                break
        if op == 'minus':
            if self.market[index]['quantity'] == 1:
                self.market.pop(index)
                return
            self.market[index]['quantity'] -= 1
            self.market[index]['total_price'] -= float(price)
        elif op == 'plus':
            self.market[index]['quantity'] += 1
            self.market[index]['total_price'] += float(price)

    def gacha(self):
        if self.member == {}:
            QMessageBox.warning(QWidget(), '警告', '请先登录')
            self.require_signal.emit()  # 跳转登录
        else:
            if self.member['balance'] < self.final_price:
                QMessageBox.warning(QWidget(), '警告', '余额不足')
                dialog = NewMemberDialog(self.db, member=self.member)
                # 只允许充值
                for i, edit in dialog.inputs.items():
                    edit.setReadOnly(True)
                    if i == 'balance':
                        edit.setReadOnly(False)
                if dialog.exec_() == QDialog.Accepted:
                    self.member = self.db.get_member(dialog.inputs['name'].text().strip())
                    self.holder.setText("当前会员：" + self.member["name"] + "\n余额：" + str(self.member["balance"]))
            else:
                # 已登录且余额足够
                self.member['balance'] -= self.final_price
                # 更新数据库
                query = "UPDATE Member SET balance = ? WHERE id = ?"
                params = (self.member['balance'], self.member['id'])
                self.db.execute_query(query, params)

                self.make_tip()
                self.member = {}; self.market.clear()
                self.holder.setText("当前会员：未选")
                QMessageBox.information(QWidget(), '成功', '购买成功')

    def make_tip(self):
        # 更新订单数据表，用户活跃时间
        current_date = datetime.now().date()
        query = "INSERT INTO Orders (member_id, total_price, create_date) VALUES (?, ?, ?)"
        params = (self.member['id'], self.final_price, current_date)
        order_id = self.db.execute_query(query, params)
        
        # 更新会员活跃时间
        query = "UPDATE Member SET last_date = ? WHERE id = ?"
        params = (current_date, self.member['id'])
        self.db.execute_query(query, params)

        # 生成订单信息
        order_info = f"会员姓名: {self.member['name']}\n电话: {self.member['phone']}\n\n购买商品清单:\n"
        for item in self.market:
            order_info += f"商品名称: {item['name']}\n价格: {item['price']} 元\n数量: {item['quantity']}\n小计: {item['total_price']} 元\n\n"
        order_info += f"订单总金额: {self.final_price} 元\n订单时间: {current_date}\n会员余额: {self.member['balance']} 元"

        # 保存订单信息到文本文件
        path = f"{APP}/tips/order{order_id}.txt"
        with open(path, "w", encoding='utf-8') as f:
            f.write(order_info)


class SellThread(QThread):
    def __init__(self, refresh_signal, market):
        super().__init__()
        self.refresh = refresh_signal
        self.market_context = market
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(100)  # 1000毫秒 = 1秒

    def on_timer(self):
        self.refresh.emit()