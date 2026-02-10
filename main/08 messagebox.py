from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("messagebox")
        self.btn.clicked.connect(self.btnClicked)

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.btn)
        self.setLayout(self.mainlayout)

    def btnClicked(self):
        reply = QMessageBox.information(self, 'title', 'message',
                                         QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel,
                                         QMessageBox.StandardButton.Ok)
        
        if reply == QMessageBox.StandardButton.Ok:
            print('Clicked Ok')
        elif reply == QMessageBox.StandardButton.Cancel:
            print('Clicked Cancel')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()