# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    split = min(pop_size-2, int(pop_size * elite_rate)) # (maximo pop_size-2)
    elite, non_elite = pop[:split], pop[split:] # Selecciona la elite
    progeny = []
    for i in elite:
        if random.random() < mutate_prob: mutate(i)
        else: progeny.append(crossover(i, roulette(non_elite)))
    return elite + roulette(non_elite + progeny, num_winners=pop_size - len(elite))


gpassword = ga(#pop_size=100, elite_rate=0.8, mutate_prob=0.2,
               fun_next_gen=next_generation)
print("\nFin version 3")
