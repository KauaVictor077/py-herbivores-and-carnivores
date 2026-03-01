class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.name = name
        self._health = health
        self.hidden = hidden

class Herbivore(Animal):

    def hide(self: Animal) -> None: 
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(
            self,
            target: Animal) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
