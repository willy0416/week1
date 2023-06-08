from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, 
    QCheckBox, QSlider, QComboBox, QWidget, 
    QHBoxLayout, QVBoxLayout, QLineEdit, QMessageBox
)
from PyQt5.QtCore import Qt
import os, yaml

class MainWindow(QMainWindow):
    """Custom window meant to display a textbox, dropdown bar,
    checkboxes, slider from 0 to 100, and save button when
    viewed from top to bottom.
    """
    def __init__(self):
        """Window constructor."""
        super().__init__()

        self.setWindowTitle("Example GUI")

        # Set up overarching layouts
        outer_layout = QVBoxLayout()
        inner_layout = QHBoxLayout()    # will hold yes/no checkboxes

        # Add yes/no checkboxes to the same row
        self.first_option = QCheckBox("Option 1")
        self.second_option = QCheckBox("Option 2")
        self.options = [self.first_option, self.second_option]
        inner_layout.addWidget(self.first_option)
        inner_layout.addWidget(self.second_option)

        # Connect checkboxes to slots
        self.first_option.stateChanged.connect(self.on_first_option_click)
        self.second_option.stateChanged.connect(self.on_second_option_click)

        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("Type here")

        self.dropdown = QComboBox()
        self.dropdown.addItems(["One", "Two", "Three"])

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)

        # Connect slider to slot
        self.slider.valueChanged.connect(self.update_slider_label)

        self.slider_label = QLabel("0")
        self.slider_label.setAlignment(Qt.AlignCenter)
        self.slider_label.setMinimumWidth(80)

        save_button = QPushButton("Save")
        
        # Connect save button to slot
        save_button.clicked.connect(self.on_save_click)

        # Add all components to the outermost layout
        outer_layout.addWidget(self.textbox)
        outer_layout.addWidget(self.dropdown)
        outer_layout.addLayout(inner_layout)
        outer_layout.addWidget(self.slider)
        outer_layout.addWidget(self.slider_label)
        outer_layout.addWidget(save_button, alignment=Qt.AlignRight)

        dummy_widget = QWidget()
        dummy_widget.setLayout(outer_layout)

        self.setCentralWidget(dummy_widget)

    def update_slider_label(self, value):
        """Display slider value."""
        self.slider_label.setText(str(value))

    def on_first_option_click(self, value):
        """Slot for first checkbox."""
        if value == Qt.Checked:
            self.second_option.setCheckState(Qt.Unchecked)
    
    def on_second_option_click(self, value):
        """Slot for second checkbox."""
        if value == Qt.Checked:
            self.first_option.setCheckState(Qt.Unchecked)

    def on_save_click(self):
        """Slot for the save button. Grabs pertinent values 
        and writes current window status to test.yaml (WIP).
        Creates pop-up window to indicates that data has been 
        saved. Resets fields to default values.
        """
        dict = {}
        
        # Ask user to choose a checkbox if none are selected
        if not any(map(lambda x: x.isChecked(), self.options)):
            QMessageBox.warning(self, "Cannot save!", "You must select an option.")
            return
        
        # Grab text from text box
        dict["text"] = self.textbox.text()

        # Grab option from checkboxes
        for i, checkbox in enumerate(self.options):
            if checkbox.isChecked():
                dict["option"] = i + 1
                break
        
        # Grab choice from self.dropdown
        dict["choice"] = self.dropdown.currentText()

        # Grab value from slider
        dict["slider"] = int(self.slider_label.text())
        
        # Indicate to the user that their data has been saved
        dialog = QMessageBox(self)
        dialog.setText("Your information has been saved.")
        dialog.exec_()

        # Reset fields to initial values
        self.textbox.setText("")
        for option in self.options:
            option.setCheckState(Qt.Unchecked)
        self.dropdown.setCurrentIndex(0)
        self.slider.setTracking(True)
        self.slider.setValue(0)
        self.slider.setSliderPosition(0)
        self.slider.update()
        self.slider.repaint()

        # Write status to test.yaml
        if not os.path.isfile("test.yaml"):
            with open("test.yaml", "w") as file:
                yaml.dump({0: dict}, file)
        else:
            with open("test.yaml", "r") as file:
                previous_entries = yaml.safe_load(file)
                index = len(previous_entries)
            with open("test.yaml", "a") as file:
                yaml.dump({index: dict}, file)

app = QApplication([])

window = MainWindow()
window.show()

app.exec_()