import textract


class DocParser:
    def __init__(self, file_name, location):
        self.file_name = file_name
        self.location = location

    def parse(self):
        try:
            text = textract.process(self.location + '/' + self.file_name)
            return text.decode("utf-8").split('\n')
        except:
            return []
