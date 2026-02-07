from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QComboBox()
        cb.addItems(['Spring', 'Summer', 'Fall', 'Winter'])

        cb.currentIndexChanged.connect(lambda: print(cb.currentText()))

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
