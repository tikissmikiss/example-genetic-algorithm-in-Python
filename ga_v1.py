# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    pop = pop[:max(2, int(pop_size*elite_rate))]  # Selecciona la elite, mínimo 2
    while len(pop) < pop_size:  # Cruzar elite hasta completar la población
        couple = roulette(pop, 2)
        pop.append(crossover(couple[0], couple[1]))
    # Mutar la población según la probabilidad de mutate_prob
    pop = [mutate(pop[i]) if random.random() < mutate_prob else pop[i] for i in range(len(pop))]
    return pop


gpassword = ga(fun_next_gen=next_generation)
print("\nFin version 1")
