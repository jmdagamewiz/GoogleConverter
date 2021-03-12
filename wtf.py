from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QMainWindow
import sys


class Widget(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_widget()

    def init_widget(self):
        self.left_line_edit = QLineEdit()
        self.left_line_edit.setFixedSize(210, 40)

        self.left_combo_box = QComboBox()
        self.left_combo_box.setFixedSize(210, 32)
        self.left_combo_box.addItem("Celsius")
        self.left_combo_box.addItem("Fahrenheit")
        self.left_combo_box.addItem("Kelvin")
        self.left_combo_box.setCurrentText("Celsius")

        self.equal_label = QLabel("=")

        self.right_line_edit = QLineEdit()
        self.right_line_edit.setFixedSize(210, 40)

        self.right_combo_box = QComboBox()
        self.right_combo_box.setFixedSize(210, 32)
        self.right_combo_box.addItem("Celsius")
        self.right_combo_box.addItem("Fahrenheit")
        self.right_combo_box.addItem("Kelvin")
        self.right_combo_box.setCurrentText("Fahrenheit")

        self.grid = QGridLayout()
        self.grid.addWidget(self.left_line_edit, 0, 0)
        self.grid.addWidget(self.equal_label, 0, 1)
        self.grid.addWidget(self.right_line_edit, 0, 2)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid)
        self.setCentralWidget(self.central_widget)


app = QApplication(sys.argv)
window = Widget()
window.show()
sys.exit(app.exec())
