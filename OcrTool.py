from PIL import Image
import sys
import pyocr

class OcrConverter():

    def __init__(self, lang='jpn_vert', layout=5):
        self.tool = self.get_ocr_tool()
        self.lang = lang
        self.layout = layout

    def get_ocr_tool(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found.")
            sys.exit(1)

        return tools[0]

    def get_text(self, src):

        if not (src.endswith(('.png', '.jpg', '.PNG', '.JPG'))):
            print("File type is not image.")
            exit()

        txt = self.tool.image_to_string(
            Image.open(src),
            lang=self.lang,
            builder=pyocr.builders.TextBuilder(tesseract_layout=self.layout))

        txt = txt.replace(' ', '')

        return txt


if __name__ == "__main__":

    src = 'sample.png'

    if not (src.endswith(('.png', '.jpg', '.PNG', '.JPG'))): exit()
    
    image_recog = OcrConverter(lang='jpn',layout=6)
    print(image_recog.get_text(src))
