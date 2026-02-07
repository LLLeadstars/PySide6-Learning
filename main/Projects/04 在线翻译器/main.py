from PySide6.QtWidgets import QApplication, QWidget, QRadioButton
from Ui_translator import Ui_Main
from translateAPI import YoudaoTranslator

#the translator needs a Youdao Api key and secret to run

class MyWindow(QWidget, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.langDict = {'自动识别':'auto', '中文':'zh-CHS', '英语':'en', '德语':'de', '法语':'fr'}
        self.translator = YoudaoTranslator()
        self.bind()
      
    def setup_api_credentials(self):
        """从用户输入获取API凭证"""
        app_key = self.lineEdit_key.text()
        app_secret = self.lineEdit_secret.text()
        self.translator.set_credentials(app_key, app_secret)
    
    def translate(self):
        self.plainTextEdit_output.setPlainText(self.translate_text()) 

    def translate_text(self):
        """执行翻译"""
        if not self.translator.has_credentials():
            return "错误：请先设置API凭证"
        
        from_lang = 'auto'
        to_lang = 'auto'

        text = self.plainTextEdit_input.toPlainText()
        from_lang = self.langDict[self.get_selected_radio(self.groupBox)]
        to_lang = self.langDict[self.comboBox.currentText()]

        result = self.translator.translate(text, from_lang=from_lang, to_lang=to_lang)
        if result["success"]:
            return result["result"]["translated"]
        else:
            return f"翻译失败: {result['error']}"
    
    def get_selected_radio(self, groupBox):
         for child in groupBox.children():
            if isinstance(child, QRadioButton) and child.isChecked():
                return child.text()

    def bind(self):
        self.pushButton_login.clicked.connect(self.setup_api_credentials)
        self.pushButton_translate.clicked.connect(self.translate)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()