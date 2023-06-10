# # -*- coding: utf-8 -*-
#
# import random
#
# from ga import ga, crossover, mutate, roulette
#
#
# def next_generation(pop, pop_size, elite_rate, mutate_prob):
#     """ Return the next generation """
#     pop = pop[:max(2, int(pop_size*elite_rate))]  # Selecciona la elite, mínimo 2
#     while len(pop) < pop_size:  # Cruzar elite hasta completar la población
#         couple = roulette(pop, 2)
#         pop.append(crossover(couple[0], couple[1]))
#     # Mutar la población según la probabilidad de mutate_prob
#     pop = [mutate(pop[i]) if random.random() < mutate_prob else pop[i] for i in range(len(pop))]
#     return pop
#
#
# gpassword = ga(  # pop_size=100, elite_rate=0.2, mutate_prob=0.8,
#                fun_next_gen=next_generation,
#                 description="Cruce elitista puro y extintivo. Todos los elite sobreviven y el resto muere",)
# print("\nFin version 1")
import random

from algorithms import roulette
from algorithms.abstractga import GeneticAlgorithm


class GeneticAlgorithmV1(GeneticAlgorithm):

    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        self.description = "Cruce elitista puro y extintivo. Todos los elite sobreviven y el resto muere"
        self.version = 1

    def next_gen(self):
        """ Return the next generation """
        self.pop = self.pop[:max(2, int(self.pop_size * self.elite_rate))]  # Selecciona la elite, mínimo 2
        while len(self.pop) < self.pop_size:  # Cruzar elite hasta completar la población
            couple = roulette(self.pop, 2)
            self.pop.append(self.crossover(couple[0], couple[1]))
        # Mutar la población según la probabilidad de mutate_prob
        self.pop = [self.mutate(self.pop[i]) if random.random() < self.mutate_rate else self.pop[i] for i in range(len(self.pop))]
        return self.pop


class GeneticAlgorithmV2(GeneticAlgorithm):
    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        self.description = "Cruce elitista puro y preservativo. Todos los elite sobreviven, cruce segun fitness, " \
                           "seleccion por ruleta entre no elites y descendencia"
        self.version = 2

    def next_gen(self):
        """ Return the next generation """
        split = min(self.pop_size - 2, int(self.pop_size * self.elite_rate))  # Selecciona la elite (maximo pop_size-2)
        elite, non_elite = self.pop[:split], self.pop[split:]
        # Mutar entre los no elite
        for i in range(len(elite)):
            if random.random() < self.mutate_rate:
                elite[i] = self.mutate(elite[i])
        # Cruzar para generar descendencia. Se cruza por parejas en orden para cruzar individuos de similar fitness
        progeny = [self.crossover(self.pop[i], self.pop[i + 1]) for i in range(0, self.pop_size, 2)]
        return elite + roulette(non_elite + progeny, num_winners=self.pop_size - len(elite))


class GeneticAlgorithmV3(GeneticAlgorithm):
    def __init__(self, pop_size: int = 100, elite_rate: float = 0.2, mutate_prob: float = 0.1, mutate_rate: float = 0.2,
                 max_generations: int = 10000, solutions_size: int = 10, fits_size: int = 10, delay: int = 0,
                 password: str = None, verbose: bool = True, print_solutions: bool = True, print_fits: bool = True,
                 static_print: bool = True, vars: dict = None):
        super().__init__(pop_size, elite_rate, mutate_prob, mutate_rate, max_generations, solutions_size, fits_size,
                         delay, password, verbose, print_solutions, print_fits, static_print, vars)
        self.description = "Procesa la elite y muta los cromosomas según el mutate_prob, los cromosomas que no mutan " \
                           "se cruzan con otro miembro de la elite elegido mediante la ruleta y generan un nuevo " \
                           "cromosoma"
        self.version = 3

    def next_gen(self):
        """ Return the next generation """
        split = min(self.pop_size - 2, int(self.pop_size * self.elite_rate))  # (maximo pop_size-2)
        elite, non_elite = self.pop[:split], self.pop[split:]  # Selecciona la elite
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
        self.description = "Esta versión es la mas se acerca al concepto biológico real"
        self.version = 4

    def next_gen(self):
        """ Return the next generation """
        # elite = self.pop[:max(2, int(self.pop_size * self.elite_rate))]  # Selecciona la elite, mínimo 2
        # nextgen = elite.copy()
        nextgen = list()
        parents = self.pop.copy()
        while len(nextgen) < self.pop_size:
            # parent1 = roulette(self.pop)[0]  # los élite tienen el doble de probabilidades de ser elegidos
            # rest_pop = self.pop.copy()
            # rest_pop.remove(parent1)  # Quita el elite seleccionado
            # parent2 = roulette(rest_pop)[0]  # Selecciona otro de entre el resto de la población
            # child = self.crossover(parent1, parent2)
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
        self.description = "Genera descendencia por mutación"
        self.version = 5

    def next_gen(self):
        """ Return the next generation """
        # split = max(10, int(self.pop_size * self.elite_rate))
        split = int(self.pop_size * self.elite_rate)
        elite, non_elite = self.pop[:split], self.pop[split:]  # Selecciona la elite
        nextgen = elite.copy()
        to_cross = []
        while len(elite) > 0:
            i = roulette(elite)[0]
            if random.random() < self.mutate_rate:
                nextgen.append(self.mutate(i))
            else:
                to_cross.append(i)
            elite.remove(i)
        if len(to_cross) % 2 == 1:  # Si hay un número impar de cromosomas para cruzar, se añade otro
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
        self.description = "Preservativo, no elitista puro"
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

