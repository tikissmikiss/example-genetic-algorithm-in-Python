# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    split = int(pop_size * elite_rate) # Selecciona la elite
    elite, non_elite = pop[:split], pop[split:]
    # Mutar entre los no elite
    non_elite = [non_elite[i] if random.random() > mutate_prob else mutate(non_elite[i]) for i in range(len(non_elite))]
    # Cruzar para generar descendencia. Se cruza por parejas en orden para cruzar individuos de similar fitness
    progeny = [crossover(pop[i], pop[i+1]) for i in range(0, pop_size, 2)]
    return elite + roulette(non_elite + progeny, num_winers=pop_size - len(elite))


gpassword = ga(#pop_size=100, elite_rate=0.2, mutate_prob=0.8,
               fun_next_gen=next_generation)
print("Fin version 2")
