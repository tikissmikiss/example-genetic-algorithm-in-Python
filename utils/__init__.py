# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse

from algorithms import _DEF_PASSWORD


def args() -> dict:
    parser = argparse.ArgumentParser(
        prog='\n\tpython ga.py',
        description='ga.py es una aproximación didáctica de un algoritmo genético. Desarrollado por José Herce para la '
                    'asignatura de Computación Bioinspirada del grado de ingeniería informática de UNIR. Este '
                    'algoritmo busca una cadena de caracteres que coincida con la contraseña dada. La función de '
                    'fitness es el número de caracteres que no coinciden con la contraseña. Los caracteres válidos '
                    'son las letras mayúsculas, las letras minúsculas, los números y los símbolos de puntuación. '
                    'Todos los parámetros pueden ser modificados por línea de comandos, tal como se indica en la '
                    'ayuda. Si no se especifica un parámetro, se utilizará el valor por defecto.',
        epilog='Aproximación didáctica de un algoritmo genético. Desarrollado por José Herce para la '
               'asignatura de Computación Bioinspirada del grado de ingeniería informática de UNIR.')
    # Agregar argumentos
    parser.add_argument('version', choices=['1', '2', '3', '4', '5', '6'], metavar='version',
                        help='Variante del algoritmo que se desea ejecutar. Afecta al como se genera la generación '
                             'siguiente. Valores posibles: 1, 2, 3, 4, 5, 6.')
    parser.add_argument('-g', '--max-generations', default=50000, dest='max_generations', action='store',
                        metavar='<int>', type=int, help='Establece el número máximo de generaciones. Valor por '
                                                        'defecto: 50000')
    parser.add_argument('-p', '--population', default=100, dest='pop_size', action='store', metavar='<int>', type=int,
                        help='Establece el tamaño de la población. Si el es impar, se establece al valor par '
                             'inmediatamente superior. Valor por defecto: 100')
    parser.add_argument('-e', '--elite-rate', default=0.2, dest='elite_rate', action='store', metavar='<float>',
                        type=float, help='Establece el porcentaje de la población que se considera élite, la cual '
                                         'esta formada por los mejores individuos. Valor por defecto: 0.3')
    parser.add_argument('-mR', '--mutate-rate', default=0.1, dest='mutate_rate', action='store', metavar='<float>',
                        type=float, help='Establece la probabilidad de que un individuo sea seleccionado para mutar. '
                                         'Valor por defecto: 0.1')
    parser.add_argument('-mP', '--mutate-prob', default=0.2, dest='mutate_prob', action='store', metavar='<float>',
                        type=float, help='Establece la probabilidad de mutación de cada gen de un individuo que ha '
                                         'sido seleccionado para mutar. Valor por defecto: 0.2')
    parser.add_argument('-d', '--delay', default=0, dest='delay', action='store', metavar='<int>', type=int,
                        help='Establece el tiempo de espera entre generaciones en milisegundos. Valor por defecto: 0')
    parser.add_argument('-P', '--password', default=_DEF_PASSWORD, dest='password', action='store', metavar='<str>',
                        type=str, help=f'Establece la contraseña que se debe de encontrar mediante el algoritmo. '
                                       f'Valor por defecto: {_DEF_PASSWORD}')
    group_v = parser.add_mutually_exclusive_group()
    group_v.add_argument('-v', '--verbose=true', dest='verbose', action='store_true', default=True,
                         help='Activa la salida detallada de información. Valor por defecto: Activo')
    group_v.add_argument('-V', '--verbose=false', dest='verbose', action='store_false', default=True,
                         help='Desactiva la salida detallada de información. Valor por defecto: Activo')
    group_a = parser.add_mutually_exclusive_group()
    group_a.add_argument('-f', '--fitness=true', dest='print_fits', action='store_true', default=True,
                         help='Activa la impresión de todos los fitness. Valor por defecto: Activo')
    group_a.add_argument('-F', '--fitness=false', dest='print_fits', action='store_false', default=True,
                         help='Desactiva la impresión de todos los fitness. Valor por defecto: Activo')
    group_s = parser.add_mutually_exclusive_group()
    group_s.add_argument('-s', '--static=true', dest='static_print', action='store_true', default=True,
                         help='Activa la impresión estática de la salida. Valor por defecto: Activo')
    group_s.add_argument('-S', '--static=false', dest='static_print', action='store_false', default=True,
                         help='Desactiva la impresión estática de la salida. Valor por defecto: Activo')
    group_m = parser.add_mutually_exclusive_group()
    group_m.add_argument('-b', '--bests=true', dest='print_solutions', action='store_true', default=True,
                         help='Activa la impresión de las, hasta 40, mejores soluciones. Valor por defecto: Activo')
    group_m.add_argument('-B', '--bests=false', dest='print_solutions', action='store_false', default=True,
                         help='Desactiva la impresión de las, hasta 40, mejores soluciones. Valor por defecto: Activo')
    parser.add_argument('-Fs', '--fits-size', default=40, dest='fits_size', action='store', metavar='<int>', type=int,
                        help='Establece el número de fitness que se imprimen. Valor por defecto: 40')
    parser.add_argument('-Ss', '--solutions-size', default=40, dest='solutions_size', action='store', metavar='<int>',
                        type=int, help='Establece el número de soluciones que se imprimen. Valor por defecto: 40')
    parse_args = parser.parse_args()
    # Validar y limitar los valores de los parámetros
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
