# -*- coding: utf-8 -*-
# Path: algorithms\abstractga.py

import random

from algorithms import roulette, stochastic_universal_sampling, tournament
from algorithms.abstractga import GeneticAlgorithm


class GeneticAlgorithmV1(GeneticAlgorithm):

    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        self.description = "Pure and extinguishing elitist crossover. All elites survive, and the rest die"
        self.version = 1

    def next_gen(self):
        """ Return the next generation """
        self.pop = self.pop[:max(2, int(self.pop_size * self.elite_rate))]  # Select the elite, minimum 2
        while len(self.pop) < self.pop_size:  # Cross the elite to complete the population
            couple = roulette(self.pop, 2)
            self.pop.append(self.crossover(couple[0], couple[1]))
        # Mutate the population according to the mutate_prob probability
        self.pop = [self.mutate(self.pop[i]) if random.random() < self.mutate_rate else self.pop[i] for i in range(len(self.pop))]
        return self.pop


class GeneticAlgorithmV2(GeneticAlgorithm):
    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        self.description = "Pure and preservative elitist crossover. All elites survive, crossover according to " \
                           "fitness, selection by roulette among non-elites and offspring"
        self.version = 2

    def next_gen(self):
        """ Return the next generation """
        split = min(self.pop_size - 2, int(self.pop_size * self.elite_rate))  # Select the elite (maximum pop_size-2)
        elite, non_elite = self.pop[:split], self.pop[split:]
        # Mutate among non-elite individuals
        for i in range(len(elite)):
            if random.random() < self.mutate_rate:
                elite[i] = self.mutate(elite[i])
        # Cross to generate offspring. Cross pairs in order to cross individuals with similar fitness
        progeny = [self.crossover(self.pop[i], self.pop[i + 1]) for i in range(0, self.pop_size, 2)]
        return elite + roulette(non_elite + progeny, num_winners=self.pop_size - len(elite))


class GeneticAlgorithmV3(GeneticAlgorithm):
    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        self.description = "Processes the elite and mutates chromosomes according to the mutate_prob. Chromosomes " \
                           "that do not mutate are crossed with another elite member chosen by roulette and generate " \
                           "a new chromosome"
        self.version = 3

    def next_gen(self):
        """ Return the next generation """
        split = min(self.pop_size - 2, int(self.pop_size * self.elite_rate))  # (maximum pop_size-2)
        elite, non_elite = self.pop[:split], self.pop[split:]  # Select the elite
        progeny = []
        for i in range(len(elite)):
            if random.random() < self.mutate_rate:
                elite[i] = self.mutate(elite[i])
            else:
                progeny.append(self.crossover(elite[i], roulette(non_elite)[0]))
        return elite + roulette(non_elite + progeny, num_winners=self.pop_size - len(elite))


class GeneticAlgorithmV4(GeneticAlgorithm):
    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        self.description = "This version is the closest to the real biological concept"
        self.version = 4

    def next_gen(self):
        """ Return the next generation """
        nextgen = list()
        parents = self.pop.copy()
        while len(nextgen) < self.pop_size:
            parent1, parent2 = roulette(parents, 2)
            child = self.crossover(parent1, parent2)
            nextgen.append(self.mutate(child) if random.random() < self.mutate_rate else child)
        return nextgen


class GeneticAlgorithmV5(GeneticAlgorithm):
    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        self.description = "Generates offspring through mutation"
        self.version = 5

    def next_gen(self):
        """ Return the next generation """
        split = int(self.pop_size * self.elite_rate)
        elite, non_elite = self.pop[:split], self.pop[split:]  # Select the elite
        nextgen = elite.copy()
        to_cross = []
        while len(elite) > 0:
            i = roulette(elite)[0]
            if random.random() < self.mutate_rate:
                nextgen.append(self.mutate(i))
            else:
                to_cross.append(i)
            elite.remove(i)
        if len(to_cross) % 2 == 1:  # If there is an odd number of chromosomes to cross, add another one
            to_cross.append(roulette(non_elite)[0])
        while len(to_cross) > 0:
            parent1, parent2 = roulette(to_cross, 2)
            nextgen.append(self.crossover(parent1, parent2))
            to_cross.remove(parent1)
            to_cross.remove(parent2)
        return nextgen + roulette(non_elite, self.pop_size - len(nextgen))


class GeneticAlgorithmV6(GeneticAlgorithm):
    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        self.description = "Preservative, pure non-elite"
        self.version = 6

    def next_gen(self):
        """ Return the next generation """
        split = int(self.pop_size * self.elite_rate)
        nextgen, non_elite = self.pop[:split], self.pop[split:]
        parents = self.pop.copy()
        while len(parents) > 2 and len(nextgen) < self.pop_size:
            parent1, parent2 = roulette(parents, 2)
            parents.remove(parent1)
            parents.remove(parent2)
            child = self.crossover(parent1, parent2)
            nextgen.append(self.mutate(child) if random.random() < self.mutate_rate else child)
        return nextgen + roulette(non_elite, self.pop_size - len(nextgen))


class GeneticAlgorithmV7(GeneticAlgorithm):
    """Generational GA using the operators presented in the course slides."""

    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.05,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        # The slides recommend Pm in [1%, 5%]. This version applies it once per child.
        self.mutate_rate = min(self.mutate_rate, 0.05)
        self.elite_rate = 0.0
        self.description = "Stochastic universal selection, one-point crossover, and one-gene mutation"
        self.version = 7

    def next_gen(self):
        """Select, cross, mutate descendants, and replace the whole population."""
        parents = stochastic_universal_sampling(self.pop, self.pop_size)
        nextgen = []
        for i in range(0, self.pop_size, 2):
            child1, child2 = self.crossover_pair(parents[i], parents[i + 1])
            for child in (child1, child2):
                nextgen.append(self.mutate_one_gene(child) if random.random() < self.mutate_rate else child)
        return nextgen


class GeneticAlgorithmV8(GeneticAlgorithmV7):
    """Generational GA with tournament selection of three participants."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = "Tournament selection (k=3), one-point crossover, and one-gene mutation"
        self.version = 8

    def next_gen(self):
        """Select with tournaments, cross, mutate descendants, and replace."""
        parents = tournament(self.pop, self.pop_size, tournament_size=3)
        nextgen = []
        for i in range(0, self.pop_size, 2):
            child1, child2 = self.crossover_pair(parents[i], parents[i + 1])
            for child in (child1, child2):
                nextgen.append(self.mutate_one_gene(child) if random.random() < self.mutate_rate else child)
        return nextgen
