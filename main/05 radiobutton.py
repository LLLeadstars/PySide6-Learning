from PySide6.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup, QGroupBox, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget()
        self.setLayout(self.mainlayout)
        

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()