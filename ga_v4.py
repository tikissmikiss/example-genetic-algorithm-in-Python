# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    elite = pop[:max(2, int(pop_size*elite_rate))]  # Selecciona la elite, mínimo 2
    nextgen = elite
    while len(nextgen) < pop_size:
        parent1, parent2 = roulette(elite), roulette(pop)
        child = crossover(parent1, parent2)
        if random.random() < mutate_prob: mutate(child)
        nextgen.append(child)
    return nextgen


gpassword = ga(#pop_size=100, elite_rate=0.8, mutate_prob=0.2,
               fun_next_gen=next_generation)
print("Fin version 4")
