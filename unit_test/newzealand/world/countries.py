class Country:
    def __init__(self, name) -> None:
        print("Country: {}".format(name))

    def get_visa(self, name: str) -> str:
        return "some day {}".format(name)


class NewZealand(Country):
    def __init__(self) -> None:
        self.name = "New Zealand"
        super().__init__(self.name)
