__author__ = 'schrecknetuser'

from weapon import *

class Sms(Weapon):
    def __init__(self):
        super().__init__('sms',
                         20,
                         [Profile(min_range=0, max_range=30, strength=5, shots=4, ap=0, damage=1)])


class Hymp(Weapon):
    def __init__(self):
        super().__init__('hymp',
                         41,
                         [Profile(min_range=0, max_range=36, strength=7, shots=4, ap=1, damage=2)])


class IANova(Weapon):
    def __init__(self):
        super().__init__('ion accelerator (nova)',
                         107,
                         [Profile(min_range=0, max_range=72, strength=9, shots=3.5, ap=3, damage=3)])



class HvyBurstCannon(Weapon):
    def __init__(self):
        super().__init__('heavy burst cannon (nova)',
                         55,
                         [Profile(min_range=0, max_range=36, strength=6, shots=12, ap=2, damage=1)])


class Plasma(Weapon):
    def __init__(self):
        super().__init__('plasma rifle',
                         11,
                         [
                            Profile(min_range=0, max_range=12, strength=6, shots=2, ap=3, damage=1),
                            Profile(min_range=12, max_range=24, strength=6, shots=1, ap=3, damage=1)
                         ])


class Flamer(Weapon):
    def __init__(self):
        super().__init__('flamer',
                         9,
                         [Profile(min_range=0, max_range=12, strength=4, shots=3.5, ap=0, damage=1)])



class ClusterRocketSystem(Weapon):
    def __init__(self):
        super().__init__('cluster rocket system',
                         61,
                         [Profile(min_range=0, max_range=48, strength=5, shots=14, ap=0, damage=1)])



class PulseBlastcannonShort(Weapon):
    def __init__(self):
        super().__init__('pulse blastcannon (short)',
                         43,
                         [Profile(min_range=0, max_range=10, strength=14, shots=2, ap=4, damage=6)])



class PulseBlastcannonMedium(Weapon):
    def __init__(self):
        super().__init__('pulse blastcannon (medium)',
                         43,
                         [Profile(min_range=0, max_range=20, strength=12, shots=4, ap=2, damage=3)])


class PulseBlastcannonLong(Weapon):
    def __init__(self):
        super().__init__('pulse blastcannon (long)',
                         43,
                         [Profile(min_range=0, max_range=30, strength=10, shots=6, ap=0, damage=1)])



class PulseDriverCannon(Weapon):
    def __init__(self):
        super().__init__('pulse driver cannon',
                         97,
                         [Profile(min_range=0, max_range=72, strength=10, shots=2, ap=3, damage=3.5)])


