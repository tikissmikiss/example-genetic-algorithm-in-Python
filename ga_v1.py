# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    pop = pop[:2] if pop_size*elite_rate<3 else pop[:int(pop_size*elite_rate)]  # Selecciona la elite
    while len(pop) < pop_size:  # Cruzar elite hasta completar la población
        couple = random.sample(pop, 2)
        pop.append(crossover(couple[0], couple[1]))
    # Mutar la poblacion segun la probabilidad de mutate_prob
    pop = [mutate(pop[i]) if random.random() < mutate_prob else pop[i]
           for i in range(len(pop))]
    return pop


gpassword = ga(#pop_size=100, elite_rate=0.2, mutate_prob=0.8,
               fun_next_gen=next_generation)
print("Fin version 1")
