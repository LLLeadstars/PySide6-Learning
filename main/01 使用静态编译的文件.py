from PySide6.QtWidgets import QApplication, QWidget
#from Ui_LoginFrame import Ui_Form
from Ui_example import Ui_Form

'''
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
'''

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
