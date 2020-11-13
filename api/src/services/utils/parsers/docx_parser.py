import docx
import os


class DocxParser:
    def __init__(self, file_name, location):
        self.base_dir = os.getcwd()
        self.file_name = file_name
        self.location = location

    def parse(self):
        os.chdir(self.location)
        document = docx.Document(self.file_name)
        os.chdir(self.base_dir)
        return [paragraph.text for paragraph in document.paragraphs]
