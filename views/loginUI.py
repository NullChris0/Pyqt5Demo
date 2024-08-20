from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QPainter
import ui.back
from json import dumps, loads
from ui.ui_login import Ui_LoginWindow
from controllers.database import Database

class LoginThread(QThread):
    # 按钮发来的登录信号
    deal = pyqtSignal(str)

    def __init__(self, db:Database, log_result):
        super().__init__()
        self.refer_db = db
        self.log_result = log_result

    def run(self):
        pass

    def read_admin(self, data: str):
        # 解析字符串json，变成dict
        data = loads(data)
        user_name = data.get("user_name")
        password = data.get("password")

        # 查询数据库验证用户名和密码
        query = "SELECT * FROM Admin WHERE username = ? AND password = ?"
        params = (user_name, password)
        account = self.refer_db.fetch_one(query, params)

        if account is None:
            print("Login failed: Invalid username or password")
            self.log_result.emit("FAILED")
        elif account[0] == 0:  # 管理员账号(id=0)
            print("Admin Login successful")
            self.log_result.emit("ADMIN")
        elif account:  # 其他账号
            print("Saler Login successful")
            self.log_result.emit("SALER")
       

class LoginUI(QWidget, Ui_LoginWindow):
    log_result = pyqtSignal(str)  # 登录结果信号
    
    def __init__(self, db:Database, sell=None, admin=None):
        super().__init__()
        self.setWindowIcon(QIcon(':back/icon.png'))
        self.setupUi(self)
        # 功能类的引用
        self.refer_sell = sell
        self.refer_admin = admin
        self.refer_db = db

        # 绑定槽函数(登录按钮)
        self.login_btn.clicked.connect(self.login)
        # 绑定槽函数(登录结果信号)
        self.log_result.connect(self.login_handler)
        # 返回登录的信号
        self.refer_admin.back_to_login.connect(lambda: self.show())
        self.refer_sell.back_to_login.connect(lambda: self.show())
        # 创建登录子线程
        self.logthread = LoginThread(self.refer_db, self.log_result)
        self.logthread.deal.connect(self.logthread.read_admin)  # 绑定子线程的槽函数
        self.logthread.start()

    def login(self):
        user_name = self.user_name.text()
        password = self.password.text()
        # 向子线程发送信号
        self.logthread.deal.emit(dumps({"user_name": user_name, "password": password}))

    def login_handler(self, result: str):
        self.user_name.clear()
        self.password.clear()
        if result == "ADMIN":
            self.refer_admin.show()
            self.close()
        elif result == "SALER":
            self.refer_sell.show()
            self.close()
        else:
            QMessageBox.information(self, "登录失败", "信息有误！")

    def paintEvent(self, event):
        background_image = QPixmap(':/back/0.png')
        painter = QPainter(self)
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