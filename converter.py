from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QComboBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys


class ConverterWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Google Converter")
        self.setGeometry(200, 200, 650, 220)
        self.setFixedSize(650, 220)
        self.setStyleSheet("background-color: white")
        self.setContentsMargins(5, 15, 5, 15)

        # initial states of combo box
        self.combo_box_states = ["Celsius", "Fahrenheit"]
        self.line_edit_values = ["0", "32"]

        self.init_window()

    def init_window(self):

        self.converter_combo_box = QComboBox()
        self.converter_combo_box.setFixedSize(450, 30)
        self.converter_combo_box.setFont(QFont("Arial", 10))
        self.converter_combo_box.addItem("Temperature")
        self.converter_combo_box.setStyleSheet("background-color: light gray")

        # LEFT SIDE
        self.left_line_edit = QLineEdit()
        self.left_line_edit.setAlignment(Qt.AlignCenter)
        self.left_line_edit.setText("0")
        self.left_line_edit.setFixedSize(210, 40)
        self.left_line_edit.setFont(QFont("Arial", 19))
        self.left_line_edit.textEdited.connect(self.line_edit_state_changed)

        self.left_combo_box = QComboBox()
        self.left_combo_box.setFont(QFont("Arial", 10))
        self.left_combo_box.setFixedSize(210, 32)
        self.left_combo_box.setStyleSheet("background-color: light gray")
        self.left_combo_box.addItem("Celsius")
        self.left_combo_box.addItem("Fahrenheit")
        self.left_combo_box.addItem("Kelvin")
        self.left_combo_box.setCurrentText(self.combo_box_states[0])
        self.left_combo_box.activated.connect(self.combo_box_state_changed)

        self.equal_label = QLabel("=")
        self.equal_label.setFont(QFont("Arial", 20))
        self.equal_label.setStyleSheet("color: gray")

        # RIGHT
        self.right_line_edit = QLineEdit()
        self.right_line_edit.setText("32")
        self.right_line_edit.setAlignment(Qt.AlignCenter)
        self.right_line_edit.setFixedSize(210, 40)
        self.right_line_edit.setFont(QFont("Arial", 19))
        self.right_line_edit.textEdited.connect(self.line_edit_state_changed)

        self.right_combo_box = QComboBox()
        self.right_combo_box.setFont(QFont("Arial", 10))
        self.right_combo_box.setFixedSize(210, 32)
        self.right_combo_box.addItem("Celsius")
        self.right_combo_box.addItem("Fahrenheit")
        self.right_combo_box.addItem("Kelvin")
        self.right_combo_box.setCurrentText(self.combo_box_states[1])
        self.right_combo_box.setStyleSheet("background-color: light gray")
        self.right_combo_box.activated.connect(self.combo_box_state_changed)

        self.grid = QGridLayout()
        self.grid.addWidget(self.left_line_edit, 0, 0)
        self.grid.addWidget(self.left_combo_box, 1, 0)
        self.grid.addWidget(self.equal_label, 0, 1)
        self.grid.addWidget(QLabel(), 1, 1)
        self.grid.addWidget(self.right_line_edit, 0, 2)
        self.grid.addWidget(self.right_combo_box, 1, 2)
        self.grid.setVerticalSpacing(0)
        self.grid.setHorizontalSpacing(7)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.grid)
        self.hbox.addStretch()

        self.formula_font = QFont("Arial", 9)

        self.formula_label = QLabel("Formula")
        self.formula_label.setFont(self.formula_font)
        self.formula_label.setStyleSheet("background-color: orange; color: white; padding: 2; border-radius: 2")
        self.formula_label.setFixedHeight(16)

        self.formula_answer_label = QLabel("(0°C × 9/5) + 32 = 32°F")
        self.formula_answer_label.setFont(QFont("Arial", 10))

        self.formula_hbox = QHBoxLayout()
        self.formula_hbox.addWidget(self.formula_label)
        self.formula_hbox.addSpacing(10)
        self.formula_hbox.addWidget(self.formula_answer_label)
        self.formula_hbox.addStretch()

        self.main_vbox = QVBoxLayout()
        self.main_vbox.addWidget(self.converter_combo_box)
        self.main_vbox.addSpacing(15)
        self.main_vbox.addLayout(self.hbox)
        self.main_vbox.addSpacing(10)
        self.main_vbox.addLayout(self.formula_hbox)

        self.center_widget = QWidget()
        self.center_widget.setLayout(self.main_vbox)
        self.setCentralWidget(self.center_widget)

    def combo_box_state_changed(self):
        """
        switches both combo boxes' text if user sets the same for both
        by storing the current texts of both in a list variable
        :return:
        """

        left_unit = self.left_combo_box.currentText()
        right_unit = self.right_combo_box.currentText()

        if left_unit == right_unit:
            self.combo_box_states.reverse()
            self.left_combo_box.setCurrentText(self.combo_box_states[0])
            self.right_combo_box.setCurrentText(self.combo_box_states[1])

        else:
            self.combo_box_states = [left_unit, right_unit]

        # TODO: in the future, clean this code pls
        left_text = self.left_line_edit.text()

        if self.is_number(left_text):
            value = float(left_text)

            if value.is_integer():
                value = int(value)

            answer = self.convert_temperature(value, self.combo_box_states[0], self.combo_box_states[1])

            if answer.is_integer():
                answer = int(answer)

            self.right_line_edit.setText(str(answer))
            self.line_edit_values = [str(value), str(answer)]

        elif left_text == "":
            self.right_line_edit.setText("")
            self.line_edit_values = ["", ""]

        else:
            self.right_line_edit.setText("")
            self.line_edit_values = [left_text, ""]
        # TODO: until here

        self.set_formula_label(self.line_edit_values[0], self.combo_box_states[0],
                               self.line_edit_values[1], self.combo_box_states[1])

    def line_edit_state_changed(self):

        left_text = self.left_line_edit.text().strip()
        right_text = self.right_line_edit.text().strip()

        left_unit = self.left_combo_box.currentText()
        right_unit = self.right_combo_box.currentText()

        if left_text != self.line_edit_values[0]:
            # left line edit was changed

            if self.is_number(left_text):
                value = float(left_text)

                if value.is_integer():
                    value = int(value)

                answer = self.convert_temperature(value, left_unit, right_unit)

                if answer.is_integer():
                    answer = int(answer)

                self.right_line_edit.setText(str(answer))
                self.line_edit_values = [str(value), str(answer)]

            elif left_text == "":
                self.right_line_edit.setText("")
                self.line_edit_values = ["", ""]

            else:
                self.right_line_edit.setText("")
                self.line_edit_values = [left_text, ""]

        elif right_text != self.line_edit_values[1]:
            # right line edit was changed

            if self.is_number(right_text):
                value = float(right_text)

                if value.is_integer():
                    value = int(value)

                answer = self.convert_temperature(value, right_unit, left_unit)

                if answer.is_integer():
                    answer = int(answer)

                self.left_line_edit.setText(str(answer))
                self.line_edit_values = [str(answer), str(value)]

            elif right_text == "":
                self.left_line_edit.setText("")
                self.line_edit_values = ["", ""]

            else:
                self.left_line_edit.setText("")
                self.line_edit_values = ["", right_text]

        self.set_formula_label(self.line_edit_values[0], left_unit, self.line_edit_values[1], right_unit)

    @staticmethod
    def is_number(string):

        try:
            value = float(string)
            return True
        except ValueError:
            return False

    def set_formula_label(self, value, unit, answer, to_unit):

        if unit == "Celsius":
            if to_unit == "Fahrenheit":
                self.formula_answer_label.setText(f"({value}°C × 9/5) + 32 = {answer}°F")
            elif to_unit == "Kelvin":
                self.formula_answer_label.setText(f"{value}°C + 273.15 = {answer}K")

        elif unit == "Fahrenheit":
            if to_unit == "Celsius":
                self.formula_answer_label.setText(f"({value}°F − 32) × 5/9 = {answer}°C")
            if to_unit == "Kelvin":
                self.formula_answer_label.setText(f"({value}°F − 32) × 5/9 + 273.15 = {answer}K")

        elif unit == "Kelvin":
            if to_unit == "Celsius":
                self.formula_answer_label.setText(f"{value}K − 273.15 = {answer}°C")
            elif to_unit == "Fahrenheit":
                self.formula_answer_label.setText(f"({value}K − 273.15) × 9/5 + 32 = {answer}°F")

    @staticmethod
    def convert_temperature(value, unit, to_unit):

        decimal_places = 4
        answer = 0

        if unit == "Celsius":
            if to_unit == "Fahrenheit":
                answer = value * 9/5 + 32
            elif to_unit == "Kelvin":
                answer = value + 273.15

        elif unit == "Fahrenheit":
            if to_unit == "Celsius":
                answer = (value - 32) * 5/9
            if to_unit == "Kelvin":
                answer = (value - 32) * 5/9 + 273.15

        elif unit == "Kelvin":
            if to_unit == "Celsius":
                answer = value - 273.15
            elif to_unit == "Fahrenheit":
                answer = (value - 273.15) * 9/5 + 32

        if answer == 0:
            return 0.0

        return round(answer, decimal_places)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ConverterWindow()
    widget.show()
    sys.exit(app.exec())

