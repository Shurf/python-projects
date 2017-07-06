__author__ = 'schrecknetuser'

from model import *
from tau_weapons import *

class Broadside(Model):
    def __init__(self):
        super().__init__('Broadside', 4, [Sms(), Sms(), Hymp(), Hymp()], 80)


class Riptide(Model):
    def __init__(self, name_addon:str, weapons):
        super().__init__('Riptide ' + name_addon, 4, weapons, 209)


class RiptideIaNovaPlasma(Riptide):
    def __init__(self):
        super().__init__('ia nova plasma', [IANova(), Plasma(), Plasma()])


class RiptideIaNovaSms(Riptide):
    def __init__(self):
        super().__init__('ia nova sms', [IANova(), Sms(), Sms()])


class RiptideBurstNovaPlasma(Riptide):
    def __init__(self):
        super().__init__('burst nova plasma', [HvyBurstCannon(), Plasma(), Plasma()])


class RiptideBurstNovaSms(Riptide):
    def __init__(self):
        super().__init__('burst nova sms', [HvyBurstCannon(), Sms(), Sms()])


class Stormsurge(Model):

    def bs(self):
        return 4

    def preset_weapons(self):
        return [ClusterRocketSystem(), Sms(), Sms()]

    def name(self):
        return 'Stormsurge '

    def __init__(self, name_addon:str, weapons_addon):
        super().__init__(self.name() + name_addon, self.bs(), self.preset_weapons() + weapons_addon, 180 + 40)


class StormsurgeAnchored(Stormsurge):

    def bs(self):
        return 3

    def name(self):
        return 'Stormsurge (anchored) '


class StormsurgeBlastCannonShort(Stormsurge):
    def __init__(self):
        super().__init__('blastcannon short', [PulseBlastcannonShort(), Flamer(), Flamer()])


class StormsurgeBlastCannonMedium(Stormsurge):
    def __init__(self):
        super().__init__('blastcannon medium', [PulseBlastcannonMedium(), Flamer(), Flamer()])


class StormsurgeBlastCannonLong(Stormsurge):
    def __init__(self):
        super().__init__('blastcannon long', [PulseBlastcannonLong(), Flamer(), Flamer()])


class StormsurgePulseDriver(Stormsurge):
    def __init__(self):
        super().__init__('pulse driver', [PulseDriverCannon(), Flamer(), Flamer()])

class StormsurgePulseDriverAnchored(StormsurgeAnchored):
    def __init__(self):
        super().__init__('pulse driver', [PulseDriverCannon(), Flamer(), Flamer()])
