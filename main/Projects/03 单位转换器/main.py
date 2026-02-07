from PySide6.QtWidgets import QApplication, QWidget
from Ui_UnitConverter import Ui_Main

class MyWindow(QWidget, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #存储数据类型
        self.lengthVar = {'毫米':1, '厘米':10, '分米':100, '米':1000, '千米':1000000}
        self.weightVar = {'毫克':1, '克':1000, '千克':1000000, '吨':1000000000}
        self.TypeDict = {'长度':self.lengthVar, '质量':self.weightVar}

        self.bind()

    def bind(self):
        self.comboBox_type.currentTextChanged.connect(self.typeUpdate)
        self.comboBox_input.currentTextChanged.connect(self.calculate)
        self.comboBox_result.currentTextChanged.connect(self.calculate)
        self.lineEdit_input.textChanged.connect(self.calculate)
        self.pushButton_clear.clicked.connect(self.valueClear)
        self.pushButton_swap.clicked.connect(self.swap)

    def typeUpdate(self, text):
        self.comboBox_input.clear()
        self.comboBox_result.clear()
        self.valueClear()

        self.comboBox_input.addItems(self.TypeDict[text].keys())
        self.comboBox_result.addItems(self.TypeDict[text].keys())
        self.comboBox_result.setCurrentIndex(1)

    def calculate(self):
        value = self.lineEdit_input.text()
        if value == '':
            self.lineEdit_result.setText('')
            return
        
        unitType = self.comboBox_type.currentText()
        inputUnit = self.comboBox_input.currentText()
        resultUnit = self.comboBox_result.currentText()

        result = float(value) * self.TypeDict[unitType][inputUnit] / self.TypeDict[unitType][resultUnit]
        self.lineEdit_result.setText(str(result))

    def valueClear(self):
        self.lineEdit_input.setText('')
        self.lineEdit_result.setText('')

    def swap(self):
        temp = self.lineEdit_input.text()
        self.lineEdit_input.setText(self.lineEdit_result.text())
        self.lineEdit_result.setText(temp)

        temp = self.comboBox_input.currentIndex()
        self.comboBox_input.setCurrentIndex(self.comboBox_result.currentIndex())
        self.comboBox_result.setCurrentIndex(temp)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()