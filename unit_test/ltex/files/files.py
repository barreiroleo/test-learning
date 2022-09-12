class File:
    def __init__(self, filename, body) -> None:
        self.filename = filename
        self.body     = body

    def create_dictionary(self):
        f = open(self.filename, "w+")
        f.write(self.body)
        f.close()

    def read_dictionary(self) -> str:
        f = open(self.filename, "r")
        content = f.read()
        f.close()
        return content


class Dictionary(File):
    def __init__(self) -> None:
        self.filename = "dictionary.esAR"
        self.body     = '{"es-AR": ["palabra, palabrita"], "en-US": ["<word>", "test"]}\n'
        super().__init__(self.filename, self.body)

