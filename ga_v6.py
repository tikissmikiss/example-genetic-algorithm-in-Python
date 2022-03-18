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


gpassword = ga(fun_next_gen=next_generation)
print(f"\033[5;33mVersion 6 finished\033[0;0m - \033[5;31mSolution: \033[5;32m"
      + gpassword + "\033[0;0m")
