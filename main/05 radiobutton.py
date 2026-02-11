from PySide6.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup, QGroupBox, QVBoxLayout, QHBoxLayout, QLabel

"""
QButtonGroup处理单选按钮优于QGroupBox
后者可以在Qt Designer中快捷设置
"""

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btnGroup = QButtonGroup(self)
        label1 = QLabel("Season")
        btn1 = QRadioButton("Spring")
        btn2 = QRadioButton("Summer")
        btn3 = QRadioButton("Fall")
        btn4 = QRadioButton("Winter")
        self.btnGroup.addButton(btn1)
        self.btnGroup.addButton(btn2)
        self.btnGroup.addButton(btn3)
        self.btnGroup.addButton(btn4)
        btn1.toggled.connect(self.selectSeason)
        btn2.toggled.connect(self.selectSeason)
        btn3.toggled.connect(self.selectSeason)
        btn4.toggled.connect(self.selectSeason)

        self.groupBox = QGroupBox(self) #groupBox默认存在边框
        #self.groupBox.setFlat(True) #设置其边框为一条线
        self.groupBox.setStyleSheet("border:0;") #隐藏其边框
        label2 = QLabel("Weather")
        btn5 = QRadioButton("Sunny", self.groupBox)
        btn6 = QRadioButton("Rainy", self.groupBox)
        btn7 = QRadioButton("Windy", self.groupBox)
        btn8 = QRadioButton("Snowy", self.groupBox)
        btn5.clicked.connect(self.selectWeather)
        btn6.clicked.connect(self.selectWeather)
        btn7.clicked.connect(self.selectWeather)
        btn8.clicked.connect(self.selectWeather)

        self.label3 = QLabel("Season: None")
        self.label4 = QLabel("Weather: None")

        itemList1 = [label1, btn1, btn2, btn3, btn4]
        itemList2 = [label2, btn5, btn6, btn7, btn8]
        itemList3 = [self.label3, self.label4]

        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.mainlayout = QVBoxLayout()

        layoutList = [self.layout1, self.layout2, self.layout3]

        for item in itemList1:
            self.layout1.addWidget(item)
        for item in itemList2:
            self.layout2.addWidget(item)
        for item in itemList3:
            self.layout3.addWidget(item)
        for item in layoutList:
            self.mainlayout.addLayout(item)
        self.setLayout(self.mainlayout)

    def selectSeason(self):
        print("selected season")
        self.label3.setText(f"Season: {self.btnGroup.checkedButton().text()}")
    
    def selectWeather(self):
        print("selected weather")
        print(self.groupBox.children())
        for child in self.groupBox.children():
            print(child.text())
            if isinstance(child, QRadioButton) and child.isChecked():
                self.label4.setText(f"Weather: {child.text()}")
        

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()