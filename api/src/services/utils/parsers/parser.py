from src.services.utils.parsers.docx_parser import DocxParser
from src.services.utils.parsers.doc_parser import DocParser
from src.services.utils.parsers.pdf_parser import PdfParser
from src.services.utils.parsers.pptx_parser import PptxParser


class Parser:
    def __init__(self, file_name, location):
        self.file_name = file_name
        self.location = location

    def __file_name_extension__(self):
        return self.file_name.split('.')[-1].lower()

    @staticmethod
    def __get_parser__(extension):
        if extension == "docx":
            return DocxParser
        if extension == "doc":
            return DocParser
        if extension == "pdf":
            return PdfParser
        return PptxParser

    def parse(self):
        parser = self.__get_parser__(self.__file_name_extension__())
        return parser(self.file_name, self.location).parse()
