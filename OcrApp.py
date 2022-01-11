import sys
from PySide2 import QtWidgets
from OcrForm import Ui_form_OCR
from OcrTool import OcrConverter
import os

class OcrUi(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(OcrUi, self).__init__(parent)
        self.ui = Ui_form_OCR()
        self.ui.setupUi(self)

    def add(self):
        fileNames = self.get_filenames()
        self.ui.listWidget.addItems(fileNames)

    def get_filenames(self):
        fileInfos = QtWidgets.QFileDialog.getOpenFileNames(
            filter="Images (*.jpg *.png)")
        return fileInfos[0]

    def get_directory(self):
        dirName = QtWidgets.QFileDialog.getExistingDirectory(
            options=QtWidgets.QFileDialog.ShowDirsOnly)
        return dirName

    def remove(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def clearAll(self):
        self.ui.listWidget.clear()

    def get_list(self):
        lst = []
        for index in range(self.ui.listWidget.count()):
            lst.append(self.ui.listWidget.item(index).text())
        return lst

    def convert(self):
        
        dirName = self.get_directory()

        lang = self.get_ocr_lang(self.ui.comboBox_config.currentText())
        builder = self.get_ocr_builder(self.ui.comboBox_config.currentText())
        image_recog = OcrConverter(lang, builder)

        image_filter = ('.png', '.jpg', '.PNG', '.JPG')
        to_txt_mode = 'w'
        to_txt_encode = 'cp932'

        for src in self.get_list():

            if not (src.endswith(image_filter)):
                continue

            print("Converting... "+format(src))
            txt = image_recog.get_text(src)
            print(txt+'\n')

            filename = dirName+"\\"+os.path.splitext(os.path.basename(src))[0]+".txt"
            with open(filename, mode=to_txt_mode, encoding=to_txt_encode) as f:
                f.write(txt)

        self.clearAll()
        print("All images were converted.")

            # リストにしなくても選択させればよいのでは？
            # ターミナルへの出力をGUIにも出したい

    def get_ocr_lang(self, method):
        if method == "JP vert":
            return 'jpn_vert'
        elif method == 'JP hor':
            return 'jpn'
        elif method == 'ENG':
            return 'eng'
        else:
            print("This OCR language is not available.")
            exit()

    def get_ocr_builder(self, method):
        if method == "JP vert":
            return 5
        elif method == 'JP hor':
            return 6
        elif method == 'ENG':
            return 6  # fix
        else:
            print("This OCR builder is not available.")
            exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = OcrUi()
    window.show()
    sys.exit(app.exec_())
