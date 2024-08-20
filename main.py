from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication, Qt
import sys
from views import loginUI, sellUI, adminUI
from controllers.database import Database
import app_path
APP = app_path.get_app_path()

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 初始化app对象(只能有一个)

    # 初始化数据库
    db = Database(f'{APP}/eyeshop.db', f'{APP}/models/CREATE.sql')

    sell = sellUI.SellUI(db)
    admin = adminUI.AdminUI(db)
    login = loginUI.LoginUI(db, sell, admin)
    login.show()

    # 程序运行，循环
    sys.exit(app.exec_())
