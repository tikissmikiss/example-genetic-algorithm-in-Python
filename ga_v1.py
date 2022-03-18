# -*- coding: utf-8 -*-

import random

from ga import ga, crossover, mutate, roulette


def next_generation(pop, pop_size, elite_rate, mutate_prob):
    """ Return the next generation """
    pop = pop[:max(2, int(pop_size*elite_rate))]  # Select the elite, minimum 2
    while len(pop) < pop_size:  # Cross elite to complete population
        couple = roulette(pop, 2)
        pop.append(crossover(couple[0], couple[1]))
    # Mutate the population according to the probability of mutate_prob
    pop = [mutate(pop[i]) if random.random() < mutate_prob else pop[i] for i in range(len(pop))]
    return pop


gpassword = ga(fun_next_gen=next_generation)
print(f"\033[5;33mVersion 1 finished\033[0;0m - \033[5;31mSolution: \033[5;32m"
      + gpassword + "\033[0;0m")
