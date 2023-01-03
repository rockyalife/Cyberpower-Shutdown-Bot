import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDateTimeEdit, QLabel
from PyQt5.QtCore import QTime
from scraper import MainBot

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_bot()
        self.init_ui()

    def init_bot(self):
        self.bot = MainBot()

    def init_ui(self):
        # Create a QLineEdit for the user to enter their name
        self.time_input = QDateTimeEdit(self)
        self.time_input.move(50, 50)
        self.time_input.resize(200, 30)
        self.time_input.setDisplayFormat("HH:mm")
        self.time_input.setTime(QTime.fromString(self.bot.config["DEFAULT_RESTORE_TIME"]))
        self.time_input.setCalendarPopup(True)

        # Create a QPushButton to submit the name
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.move(50, 100)
        self.submit_button.resize(200, 30)
        self.submit_button.clicked.connect(self.on_submit_button_clicked)

        # Create a QLabel to display the name
        self.name_label = QLabel(self)
        self.name_label.move(50, 150)
        self.name_label.resize(200, 30)

        # Set the window properties
        self.setGeometry(100, 100, 300, 250)
        self.setWindowTitle("Cyberpower Shutdown Options")

    def on_submit_button_clicked(self):
        self.bot.check_restore_option(self.time_input.text())
        
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
