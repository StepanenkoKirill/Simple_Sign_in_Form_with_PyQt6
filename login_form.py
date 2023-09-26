from PyQt6.QtWidgets import (QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QPushButton, QWidget,
                             QLabel, QPushButton, QApplication)
from PyQt6.QtCore import Qt

class login_window(QWidget):
    base = {"John Smith": "123", "Kirill Stepanenko": "1924"}
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login form")
        screen_resolution = QApplication.primaryScreen().geometry()
        window_width = 400
        window_height = 100
        self.setGeometry((screen_resolution.width() - window_width) // 2,
                         (screen_resolution.height() - window_height) // 2,
                         window_width, window_height)

        # making labels
        labels = {"Password": QLabel("Password"), "User": QLabel("User")}

        # making lineedit objects
        self.lineEdits = {"Password": QLineEdit(), "User": QLineEdit()}

        # making Login button
        self.Login = QPushButton("Login")
        self.Login.setDefault(True)

        # make unseen pswd entering
        self.lineEdits["Password"].setEchoMode(QLineEdit.EchoMode.Password)

        # make status bar
        self.status = QLabel("Hello to my form. Please log in.")
        self.status.setStyleSheet('font-size: 12px; color: red;')

        # move illustrate
        # edits = {"Password": QLineEdit(self), "User": QLineEdit(self)}
        # new_labels = {"Password": QLabel("Password", self), "User": QLabel("User", self)}
        # login = QPushButton("Login", self)
        # login.move(130,60)
        # new_labels["User"].move(10, 10)
        # new_labels["Password"].move(10, 35)
        # edits["User"].move(70, 10)
        # edits["Password"].move(70, 35)

        # setting layout
        layout = QGridLayout()
        self.setLayout(layout)

        # adding widgets to the layout
        layout.addWidget(labels["User"], 0, 0, 1, 1)
        layout.addWidget(self.lineEdits["User"], 0, 1, 1, 3)

        layout.addWidget(labels["Password"], 1, 0, 1, 1)
        layout.addWidget(self.lineEdits["Password"], 1, 1, 1, 3)

        layout.addWidget(self.Login, 2, 3, 1, 1)
        layout.addWidget(self.status, 3, 0, 1, 3)

        # create signal to handle the button click
        self.Login.clicked.connect(self.check_the_user)

    def check_the_user(self):
        user = self.lineEdits['User'].text()
        password = self.lineEdits['Password'].text()

        if user in self.base.keys():
            if self.base[user] == password:
                self.window = logged_window(user)
                self.window.show()
                self.close()
            else:
                self.status.setText("Password is incorrect")
        else:
            self.status.setText("There is no such a user")

class logged_window(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setWindowTitle("Logged window")
        fixed_size = 300
        self.setFixedHeight(fixed_size)
        self.setFixedWidth(fixed_size)

        self.status = QLabel("Congratulations, " + name)
        self.status.setStyleSheet('font-size: 16px; color: red;')

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.status, 0, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)