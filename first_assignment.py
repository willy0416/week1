from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QCheckBox, QSlider, QComboBox, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    """Custom window meant to display a textbox, dropdown bar,
    yes/no checkboxes, slider from 0 to 100, and save button when
    viewed from top to bottom.
    """
    def __init__(self):
        """Window constructor."""
        super().__init__()

        self.setWindowTitle("Example GUI")

        # Setting up overarching layouts
        outer_layout = QVBoxLayout()
        inner_layout = QHBoxLayout()    # will hold yes/no checkboxes

        # Adding yes/no checkboxes to the same row
        # TODO: prevent both yes and no from being simultaneously checked
        yes_box = QCheckBox("Yes")
        no_box = QCheckBox("No")
        inner_layout.addWidget(yes_box)
        inner_layout.addWidget(no_box)

        textbox = QLineEdit()

        dropdown = QComboBox()
        dropdown.addItems(["One", "Two", "Three"])

        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.valueChanged.connect(self.update_slider_label)

        self.slider_label = QLabel('0')
        self.slider_label.setAlignment(Qt.AlignCenter)
        self.slider_label.setMinimumWidth(80)

        save_button = QPushButton("Save")

        outer_layout.addWidget(textbox)
        outer_layout.addWidget(dropdown)
        outer_layout.addLayout(inner_layout)
        outer_layout.addWidget(slider)
        outer_layout.addWidget(self.slider_label)
        outer_layout.addWidget(save_button, alignment=Qt.AlignRight)

        dummy_widget = QWidget()
        dummy_widget.setLayout(outer_layout)

        self.setCentralWidget(dummy_widget)

    def update_slider_label(self, value):
        self.slider_label.setText(str(value))

app = QApplication([])

window = MainWindow()
window.show()

app.exec_()