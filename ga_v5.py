# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    split = max(10, int(pop_size*elite_rate)) 
    elite, non_elite = pop[:split], pop[split:]  # Selecciona la elite
    nextgen = elite.copy()
    to_cross = []
    while len(elite) > 0:
        i = roulette(elite)
        if random.random() < mutate_prob: nextgen.append(mutate(i.copy()))
        else: to_cross.append(i)
        elite.remove(i)
    if len(to_cross) % 2 == 1: to_cross.append(roulette(non_elite))
    while len(to_cross) > 0:
        parent1, parent2 = roulette(to_cross, 2)
        nextgen.append(crossover(parent1, parent2))
        to_cross.remove(parent1)
        to_cross.remove(parent2)
    return nextgen + roulette(non_elite, pop_size - len(nextgen))


gpassword = ga(fun_next_gen=next_generation)
print("\nFin version 5")
