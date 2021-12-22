# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    elite = pop[:int(pop_size * elite_rate)]  # Selecciona la elite
    progeny = elite
    while len(progeny) < pop_size:
        parent1, parent2 = roulette(elite), roulette(pop)
        # pop.remove(parent2)
        child = crossover(parent1, parent2)
        if random.random() < mutate_prob: child = mutate(child)
        progeny.append(child)
    return progeny


gpassword = ga(#pop_size=100, elite_rate=0.8, mutate_prob=0.2,
               fun_next_gen=next_generation)
print("Fin version 4")
