__author__ = 'schrecknetuser'

import typing

dice_side_count = 6

class Target:
    def __init__(self, name: str, toughness: int, save: int, wounds: int):
        self.name = name
        self.toughness = toughness
        self.save = save
        self.wounds = wounds

class Weapon:
    def __init__(self, name: str, strength: int, shots: float, ap: int, damage: float, cost: int):

        self.strength = strength
        self.name = name
        self.shots = shots
        self.ap = ap
        self.damage = damage
        self.cost = cost


class Model:
    def __init__(self, ballistic: int, name: str, weapons: typing.List[Weapon], base_cost: int):
        self.ballistic = ballistic
        self.name = name
        self.weapons = weapons
        self.base_cost = base_cost

    def hundreds_of_points(self):
        total_cost = self.base_cost
        total_cost += sum([x.cost for x in self.weapons])
        return float(total_cost)/100

def damage_probability(strength: int, toughness: int) -> float:
    if strength*2 <= toughness:
        return float(1)/6
    if strength < toughness:
        return float(2)/6
    if strength == toughness:
        return float(1)/2
    if strength >= toughness*2:
        return float(5)/6
    if strength > toughness:
        return float(2)/3

def unsaved_wound_probability(ap: int, save:int) -> float:
    if save + ap > dice_side_count:
        return 1.0
    return float(save + ap - 1)/dice_side_count

def hit_probability(ballistic):
    return float(dice_side_count + 1 - ballistic)/dice_side_count

def wound_count(model: Model, target: Target) -> float:

    result = 0.0
    for weapon in model.weapons:
        wound_probability = damage_probability(weapon.strength, target.toughness)
        unsaved_probability = unsaved_wound_probability(weapon.ap, target.save)
        expected_dmg = min(weapon.damage, target.wounds)
        result += wound_probability*unsaved_probability*expected_dmg*weapon.shots*hit_probability(model.ballistic)
    return result


targets_list = [
        Target('guardsman', 3, 5, 1),
        Target('ork', 4, 6, 1),
        Target('marine', 4, 3, 1),
        Target('terminator', 4, 2, 2),
        Target('piranha', 5, 4, 6),
        Target('harpy', 6, 4, 12),
        Target('manticore', 7, 3, 11),
        Target('rhino', 8, 3, 12),
        Target('land raider', 8, 2, 16)
    ]

def sms() -> Weapon:
    return Weapon('sms', 5, 4, 0, 1, 20)

def hymp() -> Weapon:
    return Weapon('hymp', 7, 4, 1, 2, 41)

def ia_nova() -> Weapon:
    return Weapon('IA nova', 9, 3.5, 3, 3, 107)

def hvy_burst_cannon_nova() -> Weapon:
    return Weapon('Heavy burst cannon nova', 6, 12, 2, 1, 55)

def plasma_12_inches() -> Weapon:
    return Weapon('tau plasma', 6, 2, 3, 1, 11)

def plasma_24_inches() -> Weapon:
    return Weapon('tau plasma', 6, 1, 3, 1, 11)

def flamer() -> Weapon:
    return Weapon('flamer', 4, 3.5, 0, 1, 9)

def cluster_rocket_system() -> Weapon:
    return Weapon('cluster rocket system', 5, 14, 0, 1, 61)

def pulse_blastcannon_short() -> Weapon:
    return Weapon('pulse blastcannon short', 14, 2, 4, 6, 43)

def pulse_blastcannon_medium() -> Weapon:
    return Weapon('pulse blastcannon short', 12, 4, 2, 3, 43)

def pulse_blastcannon_long() -> Weapon:
    return Weapon('pulse blastcannon short', 10, 6, 0, 1, 43)

def pulse_driver() -> Weapon:
    return Weapon('pulse driver', 10, 2, 3, 3.5, 97)

def broadside() -> Model:
    return Model(4, 'broadside', [sms(), sms(), hymp(), hymp()], 80)

def riptide_nova_ia_plasma_12_inches() -> Model:
    return Model(4, 'riptide ia nova plasma 12 inches', [ia_nova(), plasma_12_inches(), plasma_12_inches()], 209)

def riptide_nova_ia_plasma_24_inches() -> Model:
    return Model(4, 'riptide ia nova plasma 24 inches', [ia_nova(), plasma_24_inches(), plasma_24_inches()], 209)

def riptide_nova_ia_sms() -> Model:
    return Model(4, 'riptide ia nova sms', [ia_nova(), sms(), sms()], 209)

def riptide_nova_burst_plasma_12_inches() -> Model:
    return Model(4, 'riptide burst nova plasma 12 inches', [hvy_burst_cannon_nova(), plasma_12_inches(), plasma_12_inches()], 209)

def riptide_nova_burst_plasma_24_inches() -> Model:
    return Model(4, 'riptide burst nova plasma 24 inches', [hvy_burst_cannon_nova(), plasma_24_inches(), plasma_24_inches()], 209)

def riptide_nova_burst_sms() -> Model:
    return Model(4, 'riptide burst nvoa sms', [hvy_burst_cannon_nova(), sms(), sms()], 209)

def stormsurge_blastcannon_short() -> Model:
    return Model(4, 'stormsurge blastcannon short', [cluster_rocket_system(), sms(), sms(), flamer(), flamer(), pulse_blastcannon_short()], 180 + 40)

def stormsurge_blastcannon_medium() -> Model:
    return Model(4, 'stormsurge blastcannon medium', [cluster_rocket_system(), sms(), sms(), flamer(), flamer(), pulse_blastcannon_medium()], 180 + 40)

def stormsurge_blastcannon_long() -> Model:
    return Model(4, 'stormsurge blastcannon long', [cluster_rocket_system(), sms(), sms(), flamer(), flamer(), pulse_blastcannon_long()], 180 + 40)

def stormsurge_pulse_driver() -> Model:
    return Model(4, 'stormsurge pulse driver', [cluster_rocket_system(), sms(), sms(), flamer(), flamer(), pulse_driver()], 180 + 40)

def stormsurge_pulse_driver_anchored() -> Model:
    return Model(3, 'stormsurge pulse driver anchored', [cluster_rocket_system(), sms(), sms(), pulse_driver()], 180 + 40 + 18)

def divider(model):
    #return 1
    return model.hundreds_of_points()

def main():

    models = [
        broadside(),
        riptide_nova_ia_plasma_12_inches(),
        riptide_nova_burst_plasma_12_inches(),
        riptide_nova_ia_plasma_24_inches(),
        riptide_nova_burst_plasma_24_inches(),
        riptide_nova_ia_sms(),
        riptide_nova_burst_sms(),
        stormsurge_blastcannon_short(),
        stormsurge_blastcannon_medium(),
        stormsurge_blastcannon_long(),
        stormsurge_pulse_driver(),
        stormsurge_pulse_driver_anchored()
    ]

    with open('output.html', 'w') as f:
        f.write('<html>')
        f.write('<body>')
        f.write('<table border=1>')
        f.write('<tr>')
        f.write('<td>name</td>')
        for target in targets_list:
            f.write('<td>%s</td>' % target.name)
        f.write('</tr>')

        for model in models:
            f.write('<tr>')
            f.write('<td>%s</td>' % model.name)
            for target in targets_list:
                f.write('<td>%f</td>' % (wound_count(model, target)/divider(model)))
            f.write('</tr>')

        f.write('</table>')
        f.write('</body>')
        f.write('</html>')


if __name__ == '__main__':
    main()