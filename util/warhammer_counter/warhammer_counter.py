__author__ = 'schrecknetuser'

from target import *
from tau_models import *


def main():

    targets_list = [
        Guardsman(),
        Ork(),
        Marine(),
        Terminator(),
        Bike(),
        Piranha(),
        Harpy(),
        Manticore(),
        Rhino(),
        LandRaider()
    ]

    models = [
        Broadside(),
        RiptideIaNovaPlasma(),
        RiptideBurstNovaPlasma(),
        RiptideIaNovaSms(),
        RiptideBurstNovaSms(),
        StormsurgeBlastCannonShort(),
        StormsurgeBlastCannonMedium(),
        StormsurgeBlastCannonLong(),
        StormsurgePulseDriver(),
        StormsurgePulseDriverAnchored()
    ]

    ranges = [8, 20, 30, 72]

    with open('output.html', 'w') as f:
        f.write('<html>')
        f.write('<body>')

        for range_value in ranges:
            f.write('<h3>Range %d</h3>' % range_value)

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
                    f.write('<td>%f</td>' % (model.wound_count(target, range_value)/model.divider()))
                f.write('</tr>')

            f.write('</table>')
        f.write('</body>')
        f.write('</html>')


if __name__ == '__main__':
    main()