# -*- coding: utf-8 -*-

import os
import sys
import random
import re
from math import ceil


_password = "Abre. Soy yo! Quién va a ser si no?"

###############################################################################
# Opciones de ejecución
###############################################################################
_pop_size = 100
_elite_rate = 0.2
_mutate_prob = 0.8
_max_generations = 10000
_verbose, _print_all, _static_print, _matrix = True, False, True, False
_version = 0 if os.path.split(__file__)[-1] == os.path.split(sys.argv[0])[-1] else sys.argv[0][-4]
for arg in sys.argv[1:]:
    if re.compile('^-[vasVAS]+').search(arg):
        if 'v' in arg: _verbose = True
        if 'V' in arg: _verbose = False
        if 'a' in arg: _print_all = True
        if 'A' in arg: _print_all = False
        if 's' in arg: _static_print = True
        if 'S' in arg: _static_print = False
        if 'm' in arg: _matrix = True
        if 'M' in arg: _matrix = False
    elif re.compile('^--pop-size=[-\+\d]+').search(arg): _pop_size = int(arg.split('=')[1])
    elif re.compile('^--elite-rate=[-\+\d]+').search(arg): _elite_rate = float(arg.split('=')[1])
    elif re.compile('^--mutate-prob=[-\+\d]+').search(arg): _mutate_prob = float(arg.split('=')[1])
    elif re.compile('^--max-generations=[-\+\d]+').search(arg): _max_generations = int(arg.split('=')[1])
    elif re.compile('^--password=.+').search(arg): _password = arg.split('=')[1]
    elif re.compile('^[^-]{2}.+').search(arg): _password = arg
    elif re.compile('^--verbose=[\d]+').search(arg): _verbose = bool(int(arg.split('=')[1]))
    elif re.compile('^--all=[\d]+').search(arg): _print_all = bool(int(arg.split('=')[1]))
    elif re.compile('^--static=[\d]+').search(arg): _static_print = bool(int(arg.split('=')[1]))
    elif re.compile('^--version=[-\+\d]+').search(arg) and os.path.split(__file__)[-1] == os.path.split(sys.argv[0])[-1]: _version = arg.split('=')[1]
if sum([1 for i in [_elite_rate, _mutate_prob, _pop_size, _max_generations] if i < 0]):
    sys.exit("Error: Invalid parameters")


###############################################################################
# Metodos aportados por el profesor (No se modifican)
###############################################################################

def get_password_len():
    """ Return the length of the current password, for simulation purposes """
    return len(_password)


def get_fitness(guess):
    """ Return the number of character's in guess string mismatching the same position of the password """
    return sum(1 for expected, actual in zip(_password, guess) if expected != actual)


def gene_set():
    """ Return the feasible characters of the password """
    return " 0123456789áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}"


###############################################################################
# Implementación metodos solicitados por el profesor
###############################################################################

def initial_population(pop_size, chromosome_len):
    """ Create a initial population """
    population = []
    for _ in range(pop_size):
        population.append( ''.join(random.choice(gene_set()) for _ in range(chromosome_len)))
    return [[i, get_fitness(i)] for i in population]


def mutate(chromosome):
    """ Mutate randomly one gen of the chromosome, which is a string with the characters of the password """
    pos = random.randint(0, get_password_len() - 1)
    chromosome[0] = chromosome[0][:pos] + random.choice(gene_set()) + chromosome[0][pos+1:]
    chromosome[1] = get_fitness(chromosome[0])
    return chromosome


def crossover(chromosome1, chromosome2):
    """ Perform a one point crossover of the chromosomes """
    if random.random() < 0.5: chromosome1, chromosome2 = chromosome2, chromosome1
    split = random.randint(0, get_password_len() - 1)
    hybrid = chromosome1[0][:split] + chromosome2[0][split:]
    return [hybrid, get_fitness(hybrid)]


def ga(pop_size=_pop_size, elite_rate=_elite_rate, mutate_prob=_mutate_prob, max_generations=_max_generations, fun_next_gen=None):
    """ Genetic Algorithm driving the search of the password """
    pop = initial_population(pop_size, get_password_len())
    for i in range(max_generations):
        pop.sort(key=lambda x: x[1])
        print_generation(elite_rate, mutate_prob, the_fitest=pop[0], generation=i+1, pop=pop)
        if pop[0][1] == 0:
            return pop[0][0]
        pop = fun_next_gen(pop, pop_size, elite_rate, mutate_prob)
    print("Password not found")
    return False


###############################################################################
# Metodos propios
###############################################################################

def roulette(players, num_winners=1):
    """ Return the winners of the roulette wheel selection """
    selection_mode = num_winners < len(players)/2 # True si es mejor seleccionar que eliminar
    players = players.copy() # Evitar modificar la lista original
    players.sort(key=lambda x: x[1], reverse=selection_mode)
    winners = [] if selection_mode else players
    for _ in range(num_winners if selection_mode else len(players) - num_winners):
        domain = gauss_form(len(players))
        tirada = random.randint(1, domain)
        if selection_mode: winners.append(players.pop( winner(tirada) ))
        else: winners.pop( winner(tirada) )
    return winners if num_winners != 1 else winners[0]


def gauss_form(n):
    """ Return the sum of 1..n natural numbers """
    return (n*(n+1)) // 2


def inverse_gauss_form(a):
    """ Return the inverse function of the gauss_sum """
    return ((8*a+1)**0.5 - 1) / 2


def winner(value):
    """ Return the winner of the roulette wheel selection """
    return ceil( inverse_gauss_form(value) ) - 1


###############################################################################
# Metodos Impresion
###############################################################################

def print_generation(elite_rate, mutate_prob, the_fitest, generation, pop):
    msg = ""
    if _static_print:
        msg += "\033[1;1f"
    if _verbose: msg += _print_verbose(elite_rate, mutate_prob, the_fitest, generation, pop)
    else: msg += _print_non_verbose(the_fitest, generation)
    if not _static_print and _verbose and not _print_all: msg += _separator_line()
    if _print_all: msg += _str_print_all(pop)
    if not _static_print and _print_all: msg += _separator_line()
    if _matrix: msg += _print_matrix(pop)
    print(msg)

def _str_print_all(pop):
    lst = "\n\nListado ordenado de fitness de toda la población:\n\033[0;0m"
    for i in range(len(pop)):
        lst += str(f'\033[0;31m{pop[i][1]:4}\033[0;0m')
        if (i+1) % 20 == 0: lst += "\n\033[0;0m"
    return lst

def _separator_line():
    return "\n" + "-"*80 + "\n\033[0;0m"

def _print_verbose(elite_rate, mutate_prob, the_fitest, generation, pop):
    ret = "Version: \033[0K\033[5;33m" + str(_version)  + "\033[0;0m"
    ret += "\nPassword length: \033[0K\033[5;33m" + str(get_password_len())  + "\033[0;0m"
    ret += "\nPopulation Size: \033[0K\033[5;33m" + str(len(pop)) + "\033[0;0m"
    ret += "\nElite Rate: \033[0K\033[5;33m" + str(elite_rate) + "\033[0;0m"
    ret += "\nMutate Probability: \033[0K\033[5;33m" + str(mutate_prob) + "\033[0;0m"
    ret += "\n\nGeneration: \033[0K\033[5;33m" + str(generation) + "\033[0;0m"
    ret += "  best-fitness: \033[0K\033[5;33m" + str(the_fitest[1]) + "\033[0;0m"
    ret += "\n  \033[0K\033[5;32m" + str(the_fitest[0]) + "\033[0;0m"
    return ret

def _print_non_verbose(the_fitest, generation):
    ret = "\033[0;0mGeneration: " + "\033[0K\033[5;33m" + str(generation) + "\033[0;0m"
    ret += "\033[0;0m  best-fitness: " + "\033[0K\033[5;33m" + str(the_fitest[1]) + "\033[0;0m"
    ret += "  \033[0K\033[5;32m" + str(the_fitest[0]) + "\033[0;0m"
    return ret

def _print_matrix(pop):
    ret = "\n"
    for i in range(40):
        ret += f"  \033[5;33m{i:3}\033[0;0m:\033[5;36m{pop[i][1]:4}\033[0;0m | \033[5;32m" \
            + str(pop[i][0]) + "\n\033[0;0m"
    return ret


###############################################################################
# Selección de versión
###############################################################################

if os.path.split(__file__)[-1] == os.path.split(sys.argv[0])[-1]:
    if _version: 
        if _static_print: print("\033[2J\033[1;1f")
        exec(open('ga_v{}.py'.format(_version)).read())
    else:
        print("\nEjecute el archivo correspondiente de la versión, o indique la versión que dese ejecutar.", 
              "Ejemplos:",
              "> python3 ga_v1.py",
              "> python3 ga.py --version=1\n", sep="\n")
    exit(0)

# print("fin ga.py")
