from PyQt6 import QtGui, QtWidgets, QtCore


class BaseWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

    @staticmethod
    def message_box(title=None, message=None):
        """This method generates the message box with given title and messase.
        Args:
            title (str): Title of the messageBox window.
            message (str): Text to display in messageBox Window,

        Returns:
            None
        """
        if message:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            if not title:
                msgBox.setWindowTitle('Info')
            else:
                msgBox.setWindowTitle(title)
            msgBox.setText(message)
            msgBox.exec()

    def confirm_box(self, title=None, msg=None):
        """This method opens a confirmDialogBox with given titles and message.
        Args:
            title (str): Title of the messageBox window.
            msg (str): Text to display in messageBox Window,

        Returns:
            bool

        """
        choice = QtWidgets.QMessageBox.question(
            self, title, msg,
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            return True

    def center(self):
        """This method centers the application window on screen."""
        frame_geometry = self.frameGeometry()
        screen = QtWidgets.QApplication.primaryScreen()
        center_point = screen.availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())
