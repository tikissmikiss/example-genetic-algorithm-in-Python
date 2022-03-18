# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    split = min(pop_size-2, int(pop_size * elite_rate)
                )  # Select the elite (max pop_size-2)
    elite, non_elite = pop[:split], pop[split:]
    # Mutate among the non-elite
    for i in non_elite:
        if random.random() > mutate_prob: mutate(i)
    # Cruzar para generar descendencia. Se cruza por parejas en orden para cruzar individuos de similar fitness
    progeny = [crossover(pop[i], pop[i+1]) for i in range(0, pop_size, 2)]
    return elite + roulette(non_elite + progeny, num_winners=pop_size - len(elite))


gpassword = ga(fun_next_gen=next_generation)
print(f"\033[5;33mVersion 2 finished\033[0;0m - \033[5;31mSolution: \033[5;32m"
      + gpassword + "\033[0;0m")
