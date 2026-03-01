class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
