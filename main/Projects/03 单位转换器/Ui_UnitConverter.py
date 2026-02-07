# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UnitConverter.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(317, 297)
        self.verticalLayout_2 = QVBoxLayout(Main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Main)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_type = QComboBox(Main)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.horizontalLayout.addWidget(self.comboBox_type)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Main)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_input = QLineEdit(Main)
        self.lineEdit_input.setObjectName(u"lineEdit_input")

        self.horizontalLayout_3.addWidget(self.lineEdit_input)

        self.comboBox_input = QComboBox(Main)
        self.comboBox_input.addItem("")
        self.comboBox_input.addItem("")
        self.comboBox_input.addItem("")
        self.comboBox_input.addItem("")
        self.comboBox_input.addItem("")
        self.comboBox_input.setObjectName(u"comboBox_input")

        self.horizontalLayout_3.addWidget(self.comboBox_input)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Main)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_result = QLineEdit(Main)
        self.lineEdit_result.setObjectName(u"lineEdit_result")
        self.lineEdit_result.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_result)

        self.comboBox_result = QComboBox(Main)
        self.comboBox_result.addItem("")
        self.comboBox_result.addItem("")
        self.comboBox_result.addItem("")
        self.comboBox_result.addItem("")
        self.comboBox_result.addItem("")
        self.comboBox_result.setObjectName(u"comboBox_result")

        self.horizontalLayout_2.addWidget(self.comboBox_result)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_clear = QPushButton(Main)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout_4.addWidget(self.pushButton_clear)

        self.pushButton_swap = QPushButton(Main)
        self.pushButton_swap.setObjectName(u"pushButton_swap")

        self.horizontalLayout_4.addWidget(self.pushButton_swap)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Main)

        self.comboBox_result.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"\u5355\u4f4d\u8f6c\u6362\u5668", None))
        self.label.setText(QCoreApplication.translate("Main", u"\u7c7b\u578b", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("Main", u"\u957f\u5ea6", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("Main", u"\u8d28\u91cf", None))

        self.label_2.setText(QCoreApplication.translate("Main", u"\u6570\u636e", None))
        self.comboBox_input.setItemText(0, QCoreApplication.translate("Main", u"\u6beb\u7c73", None))
        self.comboBox_input.setItemText(1, QCoreApplication.translate("Main", u"\u5398\u7c73", None))
        self.comboBox_input.setItemText(2, QCoreApplication.translate("Main", u"\u5206\u7c73", None))
        self.comboBox_input.setItemText(3, QCoreApplication.translate("Main", u"\u7c73", None))
        self.comboBox_input.setItemText(4, QCoreApplication.translate("Main", u"\u5343\u7c73", None))

        self.label_3.setText(QCoreApplication.translate("Main", u"\u7ed3\u679c", None))
        self.comboBox_result.setItemText(0, QCoreApplication.translate("Main", u"\u6beb\u7c73", None))
        self.comboBox_result.setItemText(1, QCoreApplication.translate("Main", u"\u5398\u7c73", None))
        self.comboBox_result.setItemText(2, QCoreApplication.translate("Main", u"\u5206\u7c73", None))
        self.comboBox_result.setItemText(3, QCoreApplication.translate("Main", u"\u7c73", None))
        self.comboBox_result.setItemText(4, QCoreApplication.translate("Main", u"\u5343\u7c73", None))

        self.pushButton_clear.setText(QCoreApplication.translate("Main", u"\u6e05\u7a7a", None))
        self.pushButton_swap.setText(QCoreApplication.translate("Main", u"\u4ea4\u6362", None))
    # retranslateUi

