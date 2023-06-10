# -*- coding: utf-8 -*-

import os
import random
import sys
import time
from math import ceil

import numpy as np

from algorithms.genetics import GeneticAlgorithmV3, GeneticAlgorithmV1, GeneticAlgorithmV2, GeneticAlgorithmV4, \
    GeneticAlgorithmV5, GeneticAlgorithmV6
from utils import args, separator_line

# ga = GeneticAlgorithmV1()
# ga = GeneticAlgorithmV3()
#
# ga.ga()


# def_password = "Laboratorio de algoritmos evolutivos. [ {Asignatura} :  Computación Bioinspirada ] <Dev. by José Herce>"

# ###############################################################################
# # Opciones de ejecución
# ###############################################################################
# _pop_size = 20
# _elite_rate = 0.2
# _mutate_prob = 0.8
# _max_generations = 10000
# _delay = 100
# _verbose, _print_all, _static_print, solutions, _help = True, True, True, True, False
# _version = 0 if os.path.split(__file__)[-1] == os.path.split(sys.argv[0])[-1] else sys.argv[0][-4]
# for arg in sys.argv[1:]:
#     if re.compile('^-[vasmVASM]+').search(arg):
#         if 'v' in arg: _verbose = True
#         if 'V' in arg: _verbose = False
#         if 'a' in arg: _print_all = True
#         if 'A' in arg: _print_all = False
#         if 's' in arg: _static_print = True
#         if 'S' in arg: _static_print = False
#         if 'm' in arg: solutions = True
#         if 'M' in arg: solutions = False
#     elif re.compile(r'^(--help|-h\b)').search(arg): _help = True
#     elif re.compile('^--pop-size=[-\+\d]+').search(arg): _pop_size = int(arg.split('=')[1])
#     elif re.compile('^--elite-rate=[-\+\d]+').search(arg): _elite_rate = float(arg.split('=')[1])
#     elif re.compile('^--mutate-prob=[-\+\d]+').search(arg): _mutate_prob = float(arg.split('=')[1])
#     elif re.compile('^--max-generations=[-\+\d]+').search(arg): _max_generations = int(arg.split('=')[1])
#     elif re.compile('^--password=.+').search(arg): _password = arg.split('=')[1]
#     elif re.compile('^[^-]{2}.+').search(arg): _password = arg
#     elif re.compile('^--verbose=[\d]+').search(arg): _verbose = bool(int(arg.split('=')[1]))
#     elif re.compile('^--all=[\d]+').search(arg): _print_all = bool(int(arg.split('=')[1]))
#     elif re.compile('^--static=[\d]+').search(arg): _static_print = bool(int(arg.split('=')[1]))
#     elif re.compile('^--delay=[\d]+').search(arg): _delay = int(arg.split('=')[1])
#     elif re.compile('^--version=[-\+\d]+').search(arg) and os.path.split(__file__)[-1] == os.path.split(sys.argv[0])[-1]: _version = arg.split('=')[1]
# if sum([1 for i in [_elite_rate, _mutate_prob, _pop_size, _max_generations] if i < 0]):
#     sys.exit("Error: Invalid parameters")


args = args()

if int(args['version']) == 1:
    ga = GeneticAlgorithmV1(vars=args)
elif int(args['version']) == 2:
    ga = GeneticAlgorithmV2(vars=args)
elif int(args['version']) == 3:
    ga = GeneticAlgorithmV3(vars=args)
elif int(args['version']) == 4:
    ga = GeneticAlgorithmV4(vars=args)
elif int(args['version']) == 5:
    ga = GeneticAlgorithmV5(vars=args)
elif int(args['version']) == 6:
    ga = GeneticAlgorithmV6(vars=args)
else:
    raise Exception("Error: Invalid version")

ga.run()

print(f"{separator_line()}\nFin version {ga.version}\n")
ga.print_stats()
print(f"{separator_line()}\n")

# _pop_size = max(2, args._pop_size)
# _elite_rate = max(0, min(1, args._elite_rate))
# _mutate_prob = max(0, min(1, args._mutate_prob))
# _max_generations = max(0, args._max_generations)
# _delay = max(0, args._delay)
# _verbose = args._verbose
# _static_print = args._static_print
# _print_fits = args._print_all
# _print_solutions = args.solutions
# _fits_size = args._fits_size
# _solutions_size = args._solutions_size
# _password = args._password
# _version = args.version
#
# _start_time = time.time()
#
#
# ###############################################################################
# # Metodos aportados por el profesor (No se modifican)
# ###############################################################################
#
# def get_password_len():
#     """ Return the length of the current password, for simulation purposes """
#     return len(_password)
#
#
# def get_fitness(guess):
#     """ Return the number of character's in guess string mismatching the same position of the password """
#     return sum(1 for expected, actual in zip(_password, guess) if expected != actual)
#
#
# def gene_set():
#     """ Return the feasible characters of the password """
#     return " 0123456789áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}"
#
#
# ###############################################################################
# # Implementación metodos solicitados por el profesor
# ###############################################################################
#
# # def initial_population(pop_size, chromosome_len):
# #     """ Create a initial population """
# #     population = []
# #     for _ in range(pop_size):
# #         population.append( ''.join(random.choice(gene_set()) for _ in range(chromosome_len)))
# #     return [[i, get_fitness(i)] for i in population]
#
# def initial_population(pop_size, chromosome_len):
#     """ Create a initial population """
#     population = np.empty((pop_size, 2), dtype=object)
#     for i in range(pop_size):
#         chromosome = ''.join(random.choice(gene_set()) for _ in range(chromosome_len))
#         population[i] = (chromosome, get_fitness(chromosome))
#     return population
#
#
# def mutate(chromosome):
#     """ Mutate randomly one gen of the chromosome, which is a string with the characters of the password """
#     pos = random.randint(0, get_password_len() - 1)
#     chromosome[0] = chromosome[0][:pos] + random.choice(gene_set()) + chromosome[0][pos + 1:]
#     chromosome[1] = get_fitness(chromosome[0])
#     return chromosome
#
#
# def crossover(chromosome1, chromosome2):
#     """ Perform a one point crossover of the chromosomes """
#     if random.random() < 0.5: chromosome1, chromosome2 = chromosome2, chromosome1
#     split = random.randint(0, get_password_len() - 1)
#     hybrid = chromosome1[0][:split] + chromosome2[0][split:]
#     return [hybrid, get_fitness(hybrid)]
#
#
# def ga(pop_size=_pop_size, elite_rate=_elite_rate, mutate_prob=_mutate_prob, max_generations=_max_generations,
#        fun_next_gen=None, description=None):
#     """ Genetic Algorithm driving the search of the password """
#     pop_size = pop_size + (pop_size % 2)  # Asegúrese de que el tamaño de la población es par
#     pop = initial_population(pop_size, get_password_len())
#     for i in range(max_generations):
#         # Ordenar la población por su fitness
#         pop = pop[np.argsort(pop[:, 1].astype(int))]
#         print_generation(elite_rate, mutate_prob, the_fitest=pop[0], generation=i + 1, pop=pop, description=description)
#         if int(pop[0][1]) == 0:
#             return pop[0][0]
#         next_gen = fun_next_gen(pop.tolist(), pop_size, elite_rate, mutate_prob)
#         pop = np.array(next_gen)
#         if _delay: time.sleep(_delay / 1000)
#     print("Password not found")
#     return False
#
#
# ###############################################################################
# # Metodos propios
# ###############################################################################
#
# def roulette(players, num_winners=1):
#     """ Return the winners of the roulette wheel selection """
#     selection_mode = num_winners < len(players) / 2  # True si es mejor seleccionar que eliminar
#     players = np.array(players.copy())  # Evitar modificar la lista original
#     # players.sort(key=lambda x: x[1], reverse=selection_mode)
#     players = players[np.argsort(players[:, 1].astype(int))[::-1]].tolist()
#     winners = [] if selection_mode else players
#     for _ in range(num_winners if selection_mode else len(players) - num_winners):
#         domain = gauss_form(len(players))
#         tirada = random.randint(1, domain)
#         if selection_mode:
#             winners.append(players.pop(winner(tirada)))
#         else:
#             winners.pop(winner(tirada))
#     return winners if num_winners != 1 else winners[0]
#
#
# def gauss_form(n):
#     """ Return the sum of 1..n natural numbers """
#     return (n * (n + 1)) // 2
#
#
# def inverse_gauss_form(a):
#     """ Return the inverse function of the gauss_sum """
#     return ((8 * a + 1) ** 0.5 - 1) / 2
#
#
# def winner(value):
#     """ Return the winner of the roulette wheel selection """
#     return ceil(inverse_gauss_form(value)) - 1
#
#
# ###############################################################################
# # Metodos Impresion
# ###############################################################################
#
# def print_generation(elite_rate, mutate_prob, the_fitest, generation, pop, description):
#     msg = ""
#     if _static_print:
#         msg += "\033[1;1f"
#     if _verbose:
#         msg += _print_verbose(elite_rate, mutate_prob, the_fitest, generation, pop, description)
#     else:
#         msg += _print_non_verbose(the_fitest, generation)
#     if not _static_print and _verbose and not _print_fits: msg += _separator_line()
#     if _print_fits: msg += _str_print_all(pop)
#     if not _static_print and _print_fits: msg += _separator_line()
#     if _print_solutions: msg += _print_matrix(pop)
#     print(msg)
#
#
# def _str_print_all(pop):
#     lst = "\n\nOrdered fitness list of the entire population:\n\033[0;0m"
#     for i in range(min(_fits_size, len(pop))):
#         lst += str(f'\033[0;31m{pop[i][1]:4}\033[0;0m')
#         if (i + 1) % 20 == 0: lst += "\n\033[0;0m"
#     return lst
#
#
# def _separator_line():
#     return "\n" + "-" * 80 + "\n\033[0;0m"
#
#
# def _print_verbose(elite_rate, mutate_prob, the_fitest, generation, pop, description):
#     ret = "Version: \033[0K\033[5;33m" + str(_version) + (
#         f"\033[0;0m - \033[95m\033[1m\033[3m\033[4m{description}" if description else "") + "\033[0;0m"
#     # ret = "Version: \033[0K\033[5;33m" + str(_version)  + "\033[0;0m"
#     ret += "\nPassword length: \033[0K\033[5;33m" + str(get_password_len()) + "\033[0;0m"
#     ret += "\nPopulation Size: \033[0K\033[5;33m" + str(len(pop)) + "\033[0;0m"
#     ret += "\nElite Rate: \033[0K\033[5;33m" + str(elite_rate) + "\033[0;0m"
#     ret += "\nMutate Probability: \033[0K\033[5;33m" + str(mutate_prob) + "\033[0;0m"
#     ret += "\n\nGeneration: \033[0K\033[5;33m" + str(generation) + "\033[0;0m"
#     ret += "  best-fitness: \033[0K\033[5;33m" + str(the_fitest[1]) + "\033[0;0m"
#     ret += "  average-time: \033[0K\033[5;33m" + str(round((time.time() - _start_time) / generation, 3)) + "\033[0;0m"
#     ret += "  total-time: \033[0K\033[5;33m" + str(round(time.time() - _start_time, 2)) + "\033[0;0m"
#     ret += "\n\nBest solution:\n  \033[0K\033[5;32m" + str(the_fitest[0]) + "\033[0;0m"
#     return ret
#
#
# def _print_non_verbose(the_fitest, generation):
#     ret = "\033[0;0mGeneration: " + "\033[0K\033[5;33m" + str(generation) + "\033[0;0m"
#     ret += "\033[0;0m  best-fitness: " + "\033[0K\033[5;33m" + str(the_fitest[1]) + "\033[0;0m"
#     ret += "  \033[0K\033[5;32m" + str(the_fitest[0]) + "\033[0;0m"
#     return ret
#
#
# def _print_matrix(pop):
#     ret = "\n"
#     # for i in range(40 if len(pop) > 40 else len(pop)):
#     for i in range(min(_solutions_size, len(pop))):
#         ret += f"\033[5;33m{i + 1:3}\033[0;0m:\033[5;36m{pop[i][1]:4}\033[0;0m | \033[5;32m" \
#                + str(pop[i][0]) + "\n\033[0;0m"
#     return ret
#
#
# # ###############################################################################
# # # Selección de versión
# # ###############################################################################
# # Comprobar que el fichero coincide con el programa informado en los argumentos
# # if os.path.split(__file__)[-1] == os.path.split(sys.argv[0])[-1]:
# #     if _version:
# #         if _static_print: print("\033[2J\033[1;1f")
# #         exec(open('ga_v{}.py'.format(_version)).read())
# #     else:
# #         print("\nEjecute el archivo correspondiente de la versión, o indique la versión que dese ejecutar.",
# #               "Ejemplos:",
# #               "> python3 genetics.py",
# #               "> python3 ga.py --version=1\n", sep="\n")
# #     exit(0)
#
# # print("fin ga.py")
