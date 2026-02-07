from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QComboBox()
        cb.addItems(['Spring', 'Summer', 'Fall', 'Winter'])

        cb.currentIndexChanged.connect(lambda: print(cb.currentText()))

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(cb)
        self.setLayout(self.mainlayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
