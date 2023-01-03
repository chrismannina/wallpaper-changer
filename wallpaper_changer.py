import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

class WallpaperChanger(QtWidgets.QWidget):
    def __init__(self):
        """
        Initialize the wallpaper changer widget.
        """
        super().__init__()

        # The directory containing the wallpaper images
        self.dir = r"C:\Users\chris\Pictures\Wallpapers"

        # The list of wallpaper images
        self.images = os.listdir(self.dir)

        # The index of the current image
        self.current_index = 0

        # The delay between wallpaper changes (in seconds)
        self.delay = 60

        # Set up the user interface
        self.init_ui()

    def init_ui(self):
        """
        Set up the user interface.
        """
        # Create a label to display the current image file name
        self.label = QtWidgets.QLabel(self)
        self.label.setText(self.images[self.current_index])

        # Create a spin box to control the delay between wallpaper changes
        self.spin_box = QtWidgets.QSpinBox(self)
        self.spin_box.setRange(1, 3600)  # Set the range from 1 to 3600 seconds
        self.spin_box.setSingleStep(1)  # Set the step size to 1 second
        self.spin_box.setValue(self.delay)  # Set the initial value to the current delay
        self.spin_box.valueChanged.connect(self.set_delay)  # Connect the valueChanged signal to the setDelay slot

        # Create a line edit widget to allow the user to enter the wallpaper directory
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setText(self.dir)
        self.line_edit.editingFinished.connect(self.set_dir)  # Connect the editingFinished signal to the setDir slot

        # Create a push button to start the wallpaper changing
        self.button = QtWidgets.QPushButton('Start', self)
        self.button.clicked.connect(self.start)

        # Create a horizontal layout to hold the label, spin box, line edit, and button
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.spin_box)
       
    def init_ui(self):
        """
        Set up the user interface.
        """
        # Create a label to display the current image file name
        self.label = QtWidgets.QLabel(self)
        self.label.setText(self.images[self.current_index])

        # Create a spin box to control the delay between wallpaper changes
        self.spin_box = QtWidgets.QSpinBox(self)
        self.spin_box.setRange(1, 3600)  # Set the range from 1 to 3600 seconds
        self.spin_box.setSingleStep(1)  # Set the step size to 1 second
        self.spin_box.setValue(self.delay)  # Set the initial value to the current delay
        self.spin_box.valueChanged.connect(self.set_delay)  # Connect the valueChanged signal to the setDelay slot

        # Create a line edit widget to allow the user to enter the wallpaper directory
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setText(self.dir)
        self.line_edit.editingFinished.connect(self.set_dir)  # Connect the editingFinished signal to the setDir slot

        # Create a push button to start the wallpaper changing
        self.button = QtWidgets.QPushButton('Start', self)
        self.button.clicked.connect(self.start)

        # Create a horizontal layout to hold the label, spin box, line edit, and button
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.spin_box)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setWindowTitle('Wallpaper Changer')
        self.show()

    def set_delay(self, value):
        """
        Set the delay between wallpaper changes.

        Parameters
        ----------
        value : int
            The delay in seconds.
        """
        self.delay = value

    def set_dir(self):
        """
        Set the wallpaper directory.
        """
        self.dir = self.line_edit.text()
        self.images = os.listdir(self.dir)

    def start(self):
        """
        Start the wallpaper changing.
        """
        self.change_wallpaper()

    def change_wallpaper(self):
        """
        Change the wallpaper to the current image.
        """
        # Change the wallpaper to the current image
        ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{self.dir}\\{self.images[self.current_index]}", 0)

        # Update the label to show the current image file name
        self.label.setText(self.images[self.current_index])

        # Increment the index
        self.current_index += 1
        if self.current_index >= len(self.images):
            self.current_index = 0  # Reset the index to 0

        # Schedule the next wallpaper change
        QtCore.QTimer.singleShot(self.delay * 1000, self.change_wallpaper)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wallpaper_changer = WallpaperChanger()
    sys.exit(app.exec_())
