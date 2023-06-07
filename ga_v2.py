# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    split = min(pop_size-2, int(pop_size * elite_rate)) # Selecciona la elite (maximo pop_size-2)
    elite, non_elite = pop[:split], pop[split:]
    # Mutar entre los no elite
    for i in non_elite:
        if random.random() > mutate_prob: mutate(i)
    # Cruzar para generar descendencia. Se cruza por parejas en orden para cruzar individuos de similar fitness
    progeny = [crossover(pop[i], pop[i+1]) for i in range(0, pop_size, 2)]
    return elite + roulette(non_elite + progeny, num_winners=pop_size - len(elite))


gpassword = ga(#pop_size=100, elite_rate=0.2, mutate_prob=0.8,
               fun_next_gen=next_generation)
print("\nFin version 2")
