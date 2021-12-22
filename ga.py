# -*- coding: utf-8 -*-

import os
import sys
import random
from math import sqrt
from math import ceil

# Opciones de ejecucion
verbose = False
print_all = False
if ('-v' or '--verbose') in sys.argv: verbose = True
if ('-a' or '--all') in sys.argv: print_all = True


_password = "Abre. Soy yo! Quién va a ser si no?"
# _password = "Python Random module is an in-built module of Python which is used to generate random numbers. These are pseudo-random numbers means these are not truly random. This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc."


def get_password_len():
    """ Return the length of the current password, for simulation purposes """
    return len(_password)


def get_fitness(guess):
    """ Return the number of caracters in guess string mismathing the same position of the password """
    return sum(1 for expected, actual in zip(_password, guess) if expected != actual)


def gene_set():
    """ Return the feasible characters of the password """
    return " 0123456789áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}"


def initial_population(pop_size, chromosome_len):
    """ Create a initial population """
    # return [random.sample(gene_set(), chromosome_len) for _ in range(pop_size)]
    # sample devuelve conjuntos de k elementos sin elementos repetidos
    return [[random.choice(gene_set()) for _ in range(chromosome_len)] for _ in range(pop_size)]


# Implemente la función mutate() que recibe un cromosoma y lo muta cambiando aleatoriamente un único gen por otro del gene_set().
def mutate(chromosome):
    """ Mutate randomly one gen of the chromosome, which is a string with the characters of the password """
    chromosome[random.randint(0, len(chromosome) - 1)] = random.choice(gene_set())
    return chromosome


# Implemente la función crossover() que recibe 2 cromosomas, realiza con ellos una hibridación de 1 punto aleatorio, y devuelve otro cromosoma con la hibridación realizada.
def crossover(chromosome1, chromosome2):
    """ Perform a one point crossover of the chromosomes """
    if random.random() < 0.5: chromosome1, chromosome2 = chromosome2, chromosome1
    split = random.randint(0, get_password_len() - 1)
    return chromosome1[:split] + chromosome2[split:]


def ga(pop_size=100, elite_rate=0.2, mutate_prob=0.8, max_generations=10000, fun_next_gen=None):
    """ Genetic Algorithm driving the search of the password """
    pop = initial_population(pop_size, get_password_len())
    for i in range(max_generations):
        pop.sort(key=get_fitness)
        print_generation(pop_size, elite_rate, mutate_prob, the_fitest=pop[0], generation=i, pop=pop)
        if get_fitness(pop[0]) == 0:
            return pop[0]
        pop = fun_next_gen(pop, pop_size, elite_rate, mutate_prob)
    print("Password not found")
    return False


def _clear():
    if os.name == "nt": os.system("cls") 
    else: os.system("clear")


def print_generation(pop_size, elite_rate, mutate_prob, the_fitest, generation, pop):
    if not print_all: _clear()
    print("Password length:", get_password_len(), "\npop_size:", len(pop),
          "\nelite_rate:", elite_rate, "\nmutate_prob:", mutate_prob,
          "\n\nGeneration:", generation, "fitness:", get_fitness(the_fitest),
          "\n", chromosome_to_string(the_fitest), "\n")
    if verbose: 
        print("Listado ordenado de fitness de toda la poblacion:")
        print(*['{0:{width}}'.format(get_fitness(i), width=2) for i in pop], sep=" ")


def chromosome_to_string(chromosome):
    """ Return the string representation of the chromosome """
    return "".join(chromosome)


def roulette_wheeling(players, num_winers):
    """ Return the winners of the roulette wheel selection """
    selection_mode = num_winers < len(players)/2
    players.sort(key=get_fitness, reverse=selection_mode)
    winners = [] if selection_mode else players
    for _ in range(num_winers if selection_mode else len(players) - num_winers):
        domain = gauss_form(len(players))
        tirada = random.randint(1, domain)
        if selection_mode:
            winners.append(players.pop(ceil(inverse_gauss_form(tirada))-1))
        else:
            winners.pop(ceil(inverse_gauss_form(tirada))-1)
    return winners


def gauss_form(n):
    """ Return the sum of 1..n natural numbers """
    return (n*(n+1)) // 2


def inverse_gauss_form(x):
    """ Return the inverse function of the gauss_sum """
    return ((8*x+1)**0.5 - 1) / 2


print("\nEjecute el archivo correspondiente de cada versión.\n> python3 ga_v?.py\n")
