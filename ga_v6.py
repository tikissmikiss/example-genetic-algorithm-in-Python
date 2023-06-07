# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    nextgen = pop[:int(pop_size*elite_rate)]  # Selecciona la elite
    parents = roulette(pop, random.randint(0, pop_size))
    while len(parents) > 2:
        parent1, parent2 = roulette(parents, 2)
        parents.remove(parent1)
        parents.remove(parent2)
        child = crossover(parent1, parent2)
        if random.random() < mutate_prob: mutate(child)
        nextgen.append(child)
    return nextgen + roulette(pop, pop_size - len(nextgen))


gpassword = ga(  # pop_size=100, elite_rate=0.2, mutate_prob=0.8,
                fun_next_gen=next_generation)
print("\nFin version 6")
