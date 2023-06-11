# -*- coding: utf-8 -*-
# Path: algorithms\abstractga.py
#
from __future__ import annotations

import random
import time
from abc import ABC, abstractmethod

from algorithms import _DEF_PASSWORD, _GEN_SET
from utils import clear_screen, separator_line


class GeneticAlgorithm(ABC):
    """ Initialize the Genetic Algorithm
    :param pop_size: Size of the population
    :param elite_rate: Rate of the elite population
    :param mutate_rate: Probability of mutation
    :param max_generations: Maximum number of generations
    :param password: Password to guess
    :param delay: Delay between generations
    :param verbose: Print the description of the algorithm
    :param print_solutions: Print the solutions of the population
    :param solutions_size: Number of solutions to print
    :param fits_size: Number of fits to print
    :param print_fits: Print the fits of the population
    :param static_print: Print the solutions and fits in the same position
    """

    def __init__(
            self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
            max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
            password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
            static_print: bool = True, vars: dict = None
    ):
        self.description: str = "Genetic Algorithm"
        self.version: int = 0
        self.the_fittest: tuple | None = None
        self.generation: int = 0
        self.pop: list | None = None
        self.start_time: float | None = None
        self.solutions_size = solutions_size
        self.fits_size = fits_size
        self.print_solutions = print_solutions
        self.verbose = verbose
        self.print_fits = print_fits
        self.static_print = static_print
        self.delay = delay
        self.password = password if password else _DEF_PASSWORD
        self.pop_size = pop_size
        self.elite_rate = elite_rate
        self.mutate_prob = mutate_prob
        self.mutate_rate = mutate_rate
        self.max_generations = max_generations
        if vars:
            self.__dict__.update(vars)

    @property
    def gene_set(self):
        """ Return the feasible characters of the password """
        return _GEN_SET

    @property
    def get_best_solution(self):
        """ Return the best solution of the population """
        return max(self.pop, key=lambda x: x[1])

    @abstractmethod
    def next_gen(self):
        """ Return the next generation """
        pass

    def initial_population(self):
        """ Create an initial population """
        population = list()
        for i in range(self.pop_size):
            chromosome = ''.join(random.choice(self.gene_set) for _ in range(len(self.password)))
            population.append((chromosome, self.get_fitness(chromosome)))
        return population

    def get_fitness(self, guess) -> int:
        """ Return the number of characters in the guess string that mismatch the same position of the password """
        return sum(1 for expected, actual in zip(self.password, guess) if expected != actual)

    def mutate_old(self, chromosome) -> tuple:  # Previous version only mutated one chromosome
        """ Mutate randomly one gene of the chromosome, which is a string with the characters of the password """
        pos = random.randint(0, len(self.password) - 1)
        chain = chromosome[0][:pos] + random.choice(self.gene_set) + chromosome[0][pos + 1:]
        fitness = self.get_fitness(chain)
        return chain, fitness

    def mutate(self, chrom: tuple) -> tuple:  # All chromosomes have a probability of mutating
        """ Process the string of the chromosome and mutate the characters with a probability """
        chain = ''.join(random.choice(self.gene_set) if random.random() < self.mutate_prob else g for g in chrom[0])
        fitness = self.get_fitness(chain)
        return chain, fitness

    def crossover(self, chromosome1, chromosome2) -> tuple:
        """ Perform a one-point crossover of the chromosomes """
        if random.random() < 0.5:
            chromosome1, chromosome2 = chromosome2, chromosome1
        split = random.randint(0, len(self.password) - 1)
        hybrid = chromosome1[0][:split] + chromosome2[0][split:]
        return hybrid, self.get_fitness(hybrid)

    def run(self):
        """ Genetic Algorithm driving the search of the password """
        self.start_time = time.time()
        self.pop_size = self.pop_size + (self.pop_size % 2)  # Ensure population size is even
        self.pop = self.initial_population()
        if self.static_print:
            clear_screen()
        for i in range(self.max_generations):
            # Sort the population by fitness
            self.pop.sort(key=lambda x: x[1])
            self.the_fittest = self.pop[0]
            self.generation = i + 1
            self.print_generation()
            if int(self.pop[0][1]) == 0:
                return self.pop[0][0]
            self.pop = self.next_gen()
            if self.delay:
                time.sleep(self.delay / 1000)
        print("Password not found")
        return False

    ###############################################################################
    # Printing Methods
    ###############################################################################

    def print_stats(self):
        """ Print the statistics of the search """
        print(self._print_verbose())

    def print_generation(self):
        msg = ""
        if self.static_print:
            msg += "\033[1;1f"
        if self.verbose:
            msg += self._print_verbose()
        else:
            msg += self._print_non_verbose()
        if not self.static_print and self.verbose and not self.print_fits:
            msg += separator_line()
        if self.print_fits:
            msg += self._str_print_all()
        if not self.static_print and self.print_fits:
            msg += separator_line()
        if self.print_solutions:
            msg += self._print_matrix(self.pop)
        print(msg)

    def _str_print_all(self):
        lst = "\n\nOrdered fitness list of the entire population:\n\033[0;0m"
        for i in range(min(self.fits_size, len(self.pop))):
            lst += str(f'\033[0;31m{self.pop[i][1]:4}\033[0;0m')
            if (i + 1) % 20 == 0:
                lst += "\n\033[0;0m"
        return lst

    def _print_verbose(self):
        ret = "Version: \033[0K\033[5;33m" + str(self.version) + (
            f"\033[0;0m - \033[95m\033[1m\033[3m\033[4m{self.description}" if self.description else "") + "\033[0;0m"
        ret += "\nPassword length: \033[0K\033[5;33m" + str(len(self.password)) + "\033[0;0m"
        ret += "\nPopulation Size: \033[0K\033[5;33m" + str(len(self.pop)) + "\033[0;0m"
        ret += "\nElite Rate: \033[0K\033[5;33m" + str(self.elite_rate) + "\033[0;0m"
        ret += "\nMutate Rate: \033[0K\033[5;33m" + str(self.mutate_rate) + "\033[0;0m"
        ret += "\nMutate Probability: \033[0K\033[5;33m" + str(self.mutate_prob) + "\033[0;0m"
        ret += "\n\nGeneration: \033[0K\033[5;33m" + str(self.generation) + "\033[0;0m"
        ret += "  best-fitness: \033[0K\033[5;33m" + str(self.the_fittest[1]) + "\033[0;0m"
        ret += "  average-time: \033[0K\033[5;33m" + str(
            round((time.time() - self.start_time) / self.generation, 3)) + "\033[0;0m"
        ret += "  total-time: \033[0K\033[5;33m" + str(round(time.time() - self.start_time, 2)) + "\033[0;0m"
        ret += "\n\nBest solution:\n  \033[0K\033[5;32m" + str(self.the_fittest[0]) + "\033[0;0m"
        return ret

    def _print_non_verbose(self):
        ret = "\033[0;0mGeneration: " + "\033[0K\033[5;33m" + str(self.generation) + "\033[0;0m"
        ret += "\033[0;0m  best-fitness: " + "\033[0K\033[5;33m" + str(self.the_fittest[1]) + "\033[0;0m"
        ret += "  \033[0K\033[5;32m" + str(self.the_fittest[0]) + "\033[0;0m"
        return ret

    def _print_matrix(self, pop):
        ret = "\n"
        # for i in range(40 if len(self._pop) > 40 else len(self._pop)):
        for i in range(min(self.solutions_size, len(self.pop))):
            ret += f"\033[5;33m{i + 1:3}\033[0;0m:\033[5;36m{self.pop[i][1]:4}\033[0;0m | \033[5;32m" \
                   + str(self.pop[i][0]) + "\n\033[0;0m"
        return ret
