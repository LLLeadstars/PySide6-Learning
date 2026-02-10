from PySide6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        lb = QLabel("当前滑条数值: 0")

        slider = QSlider(Qt.Orientation.Horizontal) #设置滑条为水平
        slider.setTickPosition(QSlider.TickPosition.TicksBelow) #设置刻度在下方
        slider.setTickInterval(10) #刻度间隔为10
        slider.setRange(0,100)
        '''
        slider.setMinimum(0)
        slider.setMaximum(100)
        '''
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(lb)
        self.mainlayout.addWidget(slider)
        self.setLayout(self.mainlayout)

        slider.valueChanged.connect(lambda: lb.setText(f"当前滑条数值: {slider.value()}"))

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()