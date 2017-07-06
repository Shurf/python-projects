__author__ = 'schrecknetuser'


class Target:
    def __init__(self, name: str, toughness: int, save: int, wounds: int):
        self.name = name
        self.toughness_value = toughness
        self.save_value = save
        self.wounds_value = wounds

    def toughness(self):
        return self.toughness_value

    def save(self):
        return self.save_value

    def wounds(self):
        return self.wounds_value


class Guardsman(Target):
    def __init__(self):
        super().__init__(name='guardsman', toughness=3, save=5, wounds=1)


class Ork(Target):
    def __init__(self):
        super().__init__(name='ork', toughness=4, save=6, wounds=1)


class Marine(Target):
    def __init__(self):
        super().__init__(name='marine', toughness=4, save=3, wounds=1)


class Terminator(Target):
    def __init__(self):
        super().__init__(name='terminator', toughness=4, save=2, wounds=2)


class Bike(Target):
    def __init__(self):
        super().__init__(name='bike', toughness=5, save=3, wounds=2)


class Piranha(Target):
    def __init__(self):
        super().__init__(name='piranha', toughness=5, save=4, wounds=6)


class Harpy(Target):
    def __init__(self):
        super().__init__(name='harpy', toughness=6, save=4, wounds=12)


class Manticore(Target):
    def __init__(self):
        super().__init__(name='manticore', toughness=7, save=3, wounds=11)


class Rhino(Target):
    def __init__(self):
        super().__init__(name='rhino', toughness=8, save=3, wounds=12)


class LandRaider(Target):
    def __init__(self):
        super().__init__(name='land raider', toughness=8, save=2, wounds=16)
