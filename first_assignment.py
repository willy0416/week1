from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, 
    QCheckBox, QSlider, QComboBox, QWidget, 
    QHBoxLayout, QVBoxLayout, QLineEdit
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    """Custom window meant to display a textbox, dropdown bar,
    yes/no checkboxes, slider from 0 to 100, and save button when
    viewed from top to bottom.
    """
    def __init__(self):
        """Window constructor."""
        # Declare instance variables required for YAML file
        self.text = ""
        self.yes, self.no = False, False
        self.choice = ""
        self.slider_level = 0

        super().__init__()

        self.setWindowTitle("Example GUI")

        # Set up overarching layouts
        outer_layout = QVBoxLayout()
        inner_layout = QHBoxLayout()    # will hold yes/no checkboxes

        # Add yes/no checkboxes to the same row
        # TODO: prevent both yes and no from being simultaneously checked
        self.yes_box = QCheckBox("Yes")
        self.no_box = QCheckBox("No")
        inner_layout.addWidget(self.yes_box)
        inner_layout.addWidget(self.no_box)

        # Connect checkboxes to slots
        self.yes_box.stateChanged.connect(self.on_yes_click)
        self.no_box.stateChanged.connect(self.on_no_click)

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

    def on_yes_click(self, value):
        if value == Qt.Checked:
            self.no_box.setCheckState(Qt.Unchecked)
            self.yes, self.no = True, False
        else:
            self.yes = False
        print(self.yes, self.no)
    
    def on_no_click(self, value):
        if value == Qt.Checked:
            print("working")
            self.yes_box.setCheckState(Qt.Unchecked)
            self.yes, self.no = False, True
        else:
            self.no = False
        print(self.yes, self.no)

app = QApplication([])

window = MainWindow()
window.show()

app.exec_()