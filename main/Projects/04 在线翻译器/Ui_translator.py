# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translator.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(539, 437)
        self.verticalLayout_4 = QVBoxLayout(Main)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Main)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit_key = QLineEdit(Main)
        self.lineEdit_key.setObjectName(u"lineEdit_key")

        self.horizontalLayout_4.addWidget(self.lineEdit_key)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Main)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_secret = QLineEdit(Main)
        self.lineEdit_secret.setObjectName(u"lineEdit_secret")
        self.lineEdit_secret.setDragEnabled(False)

        self.horizontalLayout_5.addWidget(self.lineEdit_secret)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Main)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_auto = QRadioButton(self.groupBox)
        self.radioButton_auto.setObjectName(u"radioButton_auto")
        self.radioButton_auto.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_auto)

        self.radioButton_cn = QRadioButton(self.groupBox)
        self.radioButton_cn.setObjectName(u"radioButton_cn")

        self.horizontalLayout.addWidget(self.radioButton_cn)

        self.radioButton_en = QRadioButton(self.groupBox)
        self.radioButton_en.setObjectName(u"radioButton_en")

        self.horizontalLayout.addWidget(self.radioButton_en)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.plainTextEdit_input = QPlainTextEdit(Main)
        self.plainTextEdit_input.setObjectName(u"plainTextEdit_input")

        self.verticalLayout_2.addWidget(self.plainTextEdit_input)

        self.pushButton_login = QPushButton(Main)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.verticalLayout_2.addWidget(self.pushButton_login)

        self.pushButton_translate = QPushButton(Main)
        self.pushButton_translate.setObjectName(u"pushButton_translate")

        self.verticalLayout_2.addWidget(self.pushButton_translate)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Main)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(Main)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)

        self.verticalLayout.addWidget(self.comboBox)

        self.plainTextEdit_output = QPlainTextEdit(Main)
        self.plainTextEdit_output.setObjectName(u"plainTextEdit_output")

        self.verticalLayout.addWidget(self.plainTextEdit_output)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"api key", None))
        self.label_3.setText(QCoreApplication.translate("Main", u"api secret", None))
        self.groupBox.setTitle(QCoreApplication.translate("Main", u"\u8f93\u5165\u8bed\u8a00", None))
        self.radioButton_auto.setText(QCoreApplication.translate("Main", u"\u81ea\u52a8\u8bc6\u522b", None))
        self.radioButton_cn.setText(QCoreApplication.translate("Main", u"\u4e2d\u6587", None))
        self.radioButton_en.setText(QCoreApplication.translate("Main", u"\u82f1\u8bed", None))
        self.plainTextEdit_input.setPlainText("")
        self.pushButton_login.setText(QCoreApplication.translate("Main", u"\u767b\u5f55API", None))
        self.pushButton_translate.setText(QCoreApplication.translate("Main", u"\u7ffb\u8bd1", None))
        self.label.setText(QCoreApplication.translate("Main", u"\u76ee\u6807\u8bed\u8a00", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Main", u"\u4e2d\u6587", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Main", u"\u82f1\u8bed", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Main", u"\u5fb7\u8bed", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Main", u"\u6cd5\u8bed", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Main", u"\u8bf7\u9009\u62e9\u76ee\u6807\u8bed\u8a00", None))
    # retranslateUi

