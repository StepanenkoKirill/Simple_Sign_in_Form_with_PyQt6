import sys
from PyQt6.QtWidgets import QApplication
from login_form import login_window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    log_win = login_window()
    log_win.show()
    sys.exit(app.exec())