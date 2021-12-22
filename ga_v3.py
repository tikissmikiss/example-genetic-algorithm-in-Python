# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette_wheeling


# def next_generation(pop, pop_size, elite_rate, mutate_prob):
#     """ Return the next generation """
#     split = int(pop_size * elite_rate)
#     elite, non_elite = pop[:split], pop[split:] # Selecciona la elite
#     progeny = [mutate(i.copy()) if random.random() < mutate_prob 
#         else crossover(i, elite[random.randint(0, len(elite) - 1)]) 
#         for i in elite]
#     return elite + progeny + roulette_wheeling(non_elite, num_winers=pop_size - len(elite) - len(progeny))


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    split = int(pop_size * elite_rate)
    elite, non_elite = pop[:split], pop[split:] # Selecciona la elite
    progeny = []
    for i in elite:
        if random.random() < mutate_prob: mutate(i)
        else: progeny.append(crossover(i, elite[random.randint(0, len(elite) - 1)]))
    return elite + roulette_wheeling(non_elite + progeny, num_winers=pop_size - len(elite))


gpassword = ga(pop_size=100, elite_rate=0.8, mutate_prob=0.2,
               fun_next_gen=next_generation)
