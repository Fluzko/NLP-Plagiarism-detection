class PlagiarismResult:
    def __init__(self, may_be_plagiarism=False, plagiarism_percentage=0, plagiarised_sentences=None, file_name=None):
        self.may_be_plagiarism = may_be_plagiarism
        self.plagiarism_percentage = plagiarism_percentage
        self.plagiarised_sentences = plagiarised_sentences
        self.file_name = file_name
