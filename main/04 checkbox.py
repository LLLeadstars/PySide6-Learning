from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QCheckBox('是否被选择')
        cb.stateChanged.connect(self.showState)
        
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)

    def showState(self, state):
        print(state)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()