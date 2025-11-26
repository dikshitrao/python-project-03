class BookItem:
    def _init_(self, name, writer, code, state="free"):
        self.name = name
        self.writer = writer
        self.code = code
        self.state = "FREE"

    def to_line(self):
        return f"{self.name}|{self.writer}|{self.code}|{self.state}"

    @staticmethod
    def from_line(text):
        name, writer, code, state = text.strip().split("|")
        return BookItem(name, writer, code, "FREE")