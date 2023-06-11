# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse

from algorithms import _DEF_PASSWORD


def args() -> dict:
    parser = argparse.ArgumentParser(
        prog='\n\tpython ga.py',
        description='ga.py is a didactic approximation of a genetic algorithm. Developed by José Herce for the '
                    'Computational Bioinspiration subject of the computer engineering degree at UNIR. This algorithm '
                    'searches for a string that matches the given password. The fitness function is the number of '
                    'characters that do not match the password. Valid characters are uppercase letters, lowercase '
                    'letters, numbers, and punctuation symbols. All parameters can be modified via command line, as '
                    'indicated in the help. If a parameter is not specified, the default value will be used.',
        epilog='Didactic approximation of a genetic algorithm. Developed by José Herce for the Computational '
               'Bioinspiration subject of the computer engineering degree at UNIR.')
    # Add arguments
    parser.add_argument('version', choices=['1', '2', '3', '4', '5', '6'], metavar='version',
                        help='Variant of the algorithm to be executed. It affects how the next generation is '
                             'generated. Possible values: 1, 2, 3, 4, 5, 6.')
    parser.add_argument('-g', '--max-generations', default=50000, dest='max_generations', action='store',
                        metavar='<int>', type=int, help='Set the maximum number of generations. Default value: 50000')
    parser.add_argument('-p', '--population', default=100, dest='pop_size', action='store', metavar='<int>', type=int,
                        help='Set the population size. If it is odd, it is set to the next higher even value. '
                             'Default value: 100')
    parser.add_argument('-e', '--elite-rate', default=0.2, dest='elite_rate', action='store', metavar='<float>',
                        type=float, help='Set the percentage of the population considered elite, composed of the best '
                                         'individuals. Default value: 0.3')
    parser.add_argument('-mR', '--mutate-rate', default=0.1, dest='mutate_rate', action='store', metavar='<float>',
                        type=float, help='Set the probability that an individual is selected for mutation. Default '
                                         'value: 0.1')
    parser.add_argument('-mP', '--mutate-prob', default=0.2, dest='mutate_prob', action='store', metavar='<float>',
                        type=float, help='Set the mutation probability of each gene of an individual that has been '
                                         'selected for mutation. Default value: 0.2')
    parser.add_argument('-d', '--delay', default=0, dest='delay', action='store', metavar='<int>', type=int,
                        help='Set the delay between generations in milliseconds. Default value: 0')
    parser.add_argument('-P', '--password', default=_DEF_PASSWORD, dest='password', action='store', metavar='<str>',
                        type=str, help=f'Set the password to be found by the algorithm. Default value: {_DEF_PASSWORD}')
    group_v = parser.add_mutually_exclusive_group()
    group_v.add_argument('-v', '--verbose=true', dest='verbose', action='store_true', default=True,
                         help='Activate detailed information output. Default value: Active')
    group_v.add_argument('-V', '--verbose=false', dest='verbose', action='store_false', default=True,
                         help='Deactivate detailed information output. Default value: Active')
    group_a = parser.add_mutually_exclusive_group()
    group_a.add_argument('-f', '--fitness=true', dest='print_fits', action='store_true', default=True,
                         help='Activate printing of all fitness values. Default value: Active')
    group_a.add_argument('-F', '--fitness=false', dest='print_fits', action='store_false', default=True,
                         help='Deactivate printing of all fitness values. Default value: Active')
    group_s = parser.add_mutually_exclusive_group()
    group_s.add_argument('-s', '--static=true', dest='static_print', action='store_true', default=True,
                         help='Activate static output printing. Default value: Active')
    group_s.add_argument('-S', '--static=false', dest='static_print', action='store_false', default=True,
                         help='Deactivate static output printing. Default value: Active')
    group_m = parser.add_mutually_exclusive_group()
    group_m.add_argument('-b', '--bests=true', dest='print_solutions', action='store_true', default=True,
                         help='Activate printing of the best solutions, up to 40. Default value: Active')
    group_m.add_argument('-B', '--bests=false', dest='print_solutions', action='store_false', default=True,
                         help='Deactivate printing of the best solutions, up to 40. Default value: Active')
    parser.add_argument('-Fs', '--fits-size', default=40, dest='fits_size', action='store', metavar='<int>', type=int,
                        help='Set the number of fitness values to print. Default value: 40')
    parser.add_argument('-Ss', '--solutions-size', default=40, dest='solutions_size', action='store', metavar='<int>',
                        type=int, help='Set the number of solutions to print. Default value: 40')
    parse_args = parser.parse_args()
    # Validate and limit parameter values
    parse_args.pop_size = max(2, parse_args.pop_size)
    parse_args.elite_rate = max(0, min(1, parse_args.elite_rate))
    parse_args.mutate_rate = max(0, min(1, parse_args.mutate_rate))
    parse_args.mutate_prob = max(0, min(1, parse_args.mutate_prob))
    parse_args.max_generations = max(0, parse_args.max_generations)
    parse_args.delay = max(0, parse_args.delay)
    return vars(parse_args)


def clear_screen():
    """ Clear the screen """
    print("\033c\033[2J\033[1;1f")


def separator_line():
    return "\n" + "-" * 80 + "\n\033[0;0m"
