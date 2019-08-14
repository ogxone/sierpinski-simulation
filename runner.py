import getopt
import sys

from drawer.turtle import Drawer
from simulator import SierpinskiSimulation


def get_opts():
    opts = {
        'depth': 2
    }

    input_opts, _ = getopt.getopt(sys.argv[1:], '', ['depth='])
    for opt_name, opt_val in input_opts:
        if opt_name == '--depth':
            opt_val = int(opt_val)
            if 1 <= opt_val <= 5:
                opts['depth'] = opt_val
                continue
            raise ValueError(f'disk-num should be an integer between 3 and 8, `{opt_val}` given')

    return opts


if __name__ == '__main__':
    opts = get_opts()
    SierpinskiSimulation(Drawer(opts['depth']), opts['depth']).show_simulation()
