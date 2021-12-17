# -*- coding: utf-8 -*-

import random

_password = "Abre. Soy yo! Quién va a ser si no?"


def get_password_len():
    """ Return the length of the current password, for simulation purposes """
    return len(_password)


def get_fitness(guess):
    """ Return the number of caracters in guess string mismatching the same position of the password """
    # El objeto zip produce tuplas de n-longitud, donde n es el número de iterables pasados como argumentos posicionales a zip(). 
    # El elemento i-ésimo en cada tupla viene del argumento i-ésimo iterable a zip(). Esto continúa hasta que el argumento más corto se agota.
    return sum(1 for expected, actual in zip(_password, guess) if expected != actual)


def gene_set():
    """ Return the feasible characters of the password """
    return " 0123456789áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}"


def initial_population(pop_size, chromosome_len):
    """ Create a initial population """
    pass


def mutate(chromosome):
    """ Mutate randomly one gen of the chromosome, which is a string with the characters of the password """
    pass


def crossover(chromosome1, chromosome2):
    """ Perform a one point crossover of the chormosomes """
    pass


def ga(pop_size=100, elite_rate=0.2, mutate_prob=0.8, max_generations=10000):
    """ Genetic Algorithm driving the search of the password """
    pass


guess = "Abre"
a = list()
a = [1 for expected, actual in zip(_password, guess) if expected != actual]
b = [(expected, actual) for expected, actual in zip(_password, guess)]

print(a)


gpassword = ga()
