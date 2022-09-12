from files import Dictionary

class CommandHandler:
    def addToLanguageSpecificSettings(self, uri, type, data):
        pass

    def uriParser(self, args) -> list[str, str]:
        uri, data = ""
        return [uri, data]

    def addToDictionary(self, params) -> None:
        uri, data = self.uriParser(params)
        self.addToLanguageSpecificSettings(uri, "dictionary", data)
        pass
    
    def disableRules(self, params) -> None:
        uri, data = ""
        self.addToLanguageSpecificSettings(uri, "disabledRules", data)
        pass

    def hideFalsePositives(self, params) -> None:
        uri, data = ""
        self.addToLanguageSpecificSettings(uri, "hiddenFalsePositives", data)
        pass

arguments = {
    'uri' : 'file:///home/leonardo/.config/nvim/lua/test/latex/main.tex',
    'words' : { "en-US" : "Errorr" }
}
lsp = CommandHandler()
lsp.addToDictionary(arguments)
