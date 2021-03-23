from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QComboBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

from quantities import Quantity


class ConverterWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Google Converter")
        self.setGeometry(200, 200, 650, 220)
        self.setFixedSize(650, 220)
        self.setStyleSheet("background-color: white")
        self.setContentsMargins(5, 15, 5, 15)

        self.initialize_values()
        self.create_window_widgets()

    def initialize_values(self):

        # CURRENT QUANTITY TO BE CONVERTED
        # TEMPERATURE IS THE INITIAL QUANTITY
        self.current_quantity = Quantity("Area")

        # initial states of combo boxes and line edits
        self.combo_box_states = self.current_quantity.initial_units
        self.line_edit_values = self.current_quantity.initial_values

        self.quantities_list = ["Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency",
                                "Fuel Economy", "Length", "Mass", "Plane Angle", "Pressure", "Speed",
                                "Temperature", "Time", "Volume"]

    def create_window_widgets(self):
        """
        creates the window and all widgets inside including the widgets' signal
        and slots and designs
        :return:
        """

        # QUANTITY COMBO BOX
        self.converter_combo_box = QComboBox()
        self.converter_combo_box.setFixedSize(450, 30)
        self.converter_combo_box.setFont(QFont("Arial", 10))
        self.converter_combo_box.setStyleSheet("background-color: light gray")
        self.converter_combo_box.activated.connect(self.converter_combo_box_state_changed)

        # LEFT UNIT LINE EDIT AND COMBO BOX
        self.left_line_edit = QLineEdit()
        self.left_line_edit.setAlignment(Qt.AlignCenter)
        self.left_line_edit.setFixedSize(210, 40)
        self.left_line_edit.setFont(QFont("Arial", 19))
        self.left_line_edit.textEdited.connect(self.line_edit_state_changed)

        self.left_combo_box = QComboBox()
        self.left_combo_box.setFont(QFont("Arial", 10))
        self.left_combo_box.setFixedSize(210, 32)
        self.left_combo_box.setStyleSheet("background-color: light gray")
        self.left_combo_box.activated.connect(self.combo_box_state_changed)

        self.equal_label = QLabel("=")
        self.equal_label.setFont(QFont("Arial", 20))
        self.equal_label.setStyleSheet("color: gray")

        # RIGHT UNIT LINE EDIT AND COMBO BOX
        self.right_line_edit = QLineEdit()
        self.right_line_edit.setAlignment(Qt.AlignCenter)
        self.right_line_edit.setFixedSize(210, 40)
        self.right_line_edit.setFont(QFont("Arial", 19))
        self.right_line_edit.textEdited.connect(self.line_edit_state_changed)

        self.right_combo_box = QComboBox()
        self.right_combo_box.setFont(QFont("Arial", 10))
        self.right_combo_box.setFixedSize(210, 32)
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

        # FORMULA LABEL AND SOLUTION LABEL
        self.formula_font = QFont("Arial", 9)

        self.formula_label = QLabel("Formula")
        self.formula_label.setFont(self.formula_font)
        self.formula_label.setStyleSheet("background-color: orange; color: white; padding: 2; border-radius: 2")
        self.formula_label.setFixedHeight(16)

        self.solution_label = QLabel()
        self.solution_label.setFont(QFont("Arial", 10))

        self.formula_hbox = QHBoxLayout()
        self.formula_hbox.addWidget(self.formula_label)
        self.formula_hbox.addSpacing(10)
        self.formula_hbox.addWidget(self.solution_label)
        self.formula_hbox.addStretch()

        # MAIN LAYOUT
        self.main_vbox = QVBoxLayout()
        self.main_vbox.addWidget(self.converter_combo_box)
        self.main_vbox.addSpacing(15)
        self.main_vbox.addLayout(self.hbox)
        self.main_vbox.addSpacing(10)
        self.main_vbox.addLayout(self.formula_hbox)

        self.center_widget = QWidget()
        self.center_widget.setLayout(self.main_vbox)
        self.setCentralWidget(self.center_widget)

        self.set_init_window_states()

    def set_init_window_states(self):
        """
        sets initial values of widgets in the window
        :return:
        """

        # sets initial value for quantity combo box widget
        for quantity in self.quantities_list:
            self.converter_combo_box.addItem(quantity)
        self.converter_combo_box.setCurrentText(self.current_quantity.name)

        # sets initial value for all other widgets
        self.set_window_states()

    def set_window_states(self):
        """
        sets all values of widgets in the window according to the chosen quantity
        inside the quantity combo box, and doesn't set quantity combo box value
        :return:
        """

        self.left_line_edit.setText(self.current_quantity.initial_values[0])

        for unit in self.current_quantity.units:
            self.left_combo_box.addItem(unit)
        self.left_combo_box.setCurrentText(self.combo_box_states[0])

        self.right_line_edit.setText(self.current_quantity.initial_values[1])

        for unit in self.current_quantity.units:
            self.right_combo_box.addItem(unit)
        self.right_combo_box.setCurrentText(self.combo_box_states[1])

        solution_text = self.current_quantity.get_solution_text(self.current_quantity.initial_values[0],
                                                                self.current_quantity.initial_units[0],
                                                                self.current_quantity.initial_values[1],
                                                                self.current_quantity.initial_units[1])
        self.solution_label.setText(solution_text)

    def clear_combo_box_items(self):
        self.left_combo_box.clear()
        self.right_combo_box.clear()

    def converter_combo_box_state_changed(self):
        """
        changes current_quantity attribute to user's input in converter combo box
        and immediately changes all the available units and initial values of the
        chosen quantity
        :return:
        """

        quantity_name = self.converter_combo_box.currentText()

        self.current_quantity = Quantity(quantity_name)
        self.combo_box_states = self.current_quantity.initial_units
        self.line_edit_values = self.current_quantity.initial_values

        self.clear_combo_box_items()
        self.set_window_states()

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

        # When combo box values are changed, left line edit's value must be converted to
        # right line edit's unit since self.line_edit_state_changed() can't do it for this
        # kind of signal
        left_text = self.left_line_edit.text()

        if self.is_number(left_text):
            value = float(left_text)

            if value.is_integer():
                value = int(value)

            answer = self.current_quantity.convert(value, self.combo_box_states[0], self.combo_box_states[1])
            answer = float(answer)

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
        # # # # # # #

        self.set_solution_label(self.line_edit_values[0], self.combo_box_states[0],
                                self.line_edit_values[1], self.combo_box_states[1])

    def line_edit_state_changed(self):

        # GETS LINE EDIT TEXT
        left_text = self.left_line_edit.text().strip()
        right_text = self.right_line_edit.text().strip()

        # GETS COMBO BOX UNITS TEXT
        left_unit = self.left_combo_box.currentText()
        right_unit = self.right_combo_box.currentText()

        # CHECKS IF .textChanged() signal came from LEFT OR RIGHT
        if left_text != self.line_edit_values[0]:
            # left line edit was changed

            if self.is_number(left_text):
                value = float(left_text)

                if value.is_integer():
                    value = int(value)

                answer = self.current_quantity.convert(value, left_unit, right_unit)

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

        # CHECKS IF .textChanged() signal came from LEFT OR RIGHT
        elif right_text != self.line_edit_values[1]:
            # right line edit was changed

            if self.is_number(right_text):
                value = float(right_text)

                if value.is_integer():
                    value = int(value)

                answer = self.current_quantity.convert(value, right_unit, left_unit)

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

        self.set_solution_label(self.line_edit_values[0], left_unit, self.line_edit_values[1], right_unit)

    def set_solution_label(self, value, unit, answer, to_unit):

        solution_text = self.current_quantity.get_solution_text(value, unit, answer, to_unit)
        self.solution_label.setText(solution_text)

    @staticmethod
    def is_number(string):

        try:
            value = float(string)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ConverterWindow()
    widget.show()
    sys.exit(app.exec())

