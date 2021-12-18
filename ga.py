# -*- coding: utf-8 -*-

# import math
import random

import ga_aux

_password = "Abre. Soy yo! Quién va a ser si no?"
# _password = "El módulo estandariza un conjunto básico de herramientas rápidas y eficientes en memoria que son útiles por sí mismas o en combinación. Juntos, forman un álgebra iteradora que permite construir herramientas especializadas de manera sucinta y eficiente en Python puro."
# _password = "Este módulo implementa una serie de bloques de construcción de iteradores inspirados en construcciones de APL, \"Haskell\" y SML. Cada uno ha sido refundido en una forma adecuada para Python. El módulo estandariza un conjunto básico de herramientas rápidas y eficientes en memoria que son útiles por sí mismas o en combinación. Juntos, forman un álgebra iteradora que permite construir herramientas especializadas de manera sucinta y eficiente en Python puro. Por ejemplo, SML proporciona una herramienta de tabulación: que produce una secuencia . El mismo efecto se puede lograr en Python combinando map() y count() para formar .tabulate(f)f(0), f(1), ...map(f, count()) Estas herramientas y sus contrapartes integradas también funcionan bien con las funciones de alta velocidad en el módulo del operador. Por ejemplo, el operador de multiplicación se puede mapear a través de dos vectores para formar un producto de punto eficiente: .sum(map(operator.mul, vector1, vector2))Iteradores infinitos: "

''' Settings for the genetic algorithm
    aptitud:
        - proportional: Probabilidad de supervivencia proporcional al valor de la función fitness
        - ranked: Probabilidad de supervivencia proporcional a pa posicion en el ranking
    muestreo:
        - ruleta: Seleccion por ruleta
        - torneo: Seleccion por n torneos
        - elitista: Seleccion por elitismo (Mantener a los mejores para evitar perderlos)
    mutacion:
        - intercambio: Intercambia dos genes
        - incremento: Incrementa un gen
        - decremento: Decrementa un gen
    cruzamiento: (crossover)
        - 1_punto: Cruza un punto
        - 2_puntos: Cruza dos puntos
        - random: Cruza aleatoriamente

'''


def get_password_len():
    """ Return the length of the current password, for simulation purposes """
    return len(_password)


def get_fitness(guess):
    """ Return the number of caracters in guess string mismatching the same position of the password """
    # El objeto zip produce tuplas de n-longitud, donde n es el número de iterables pasados como argumentos posicionales a zip().
    # El elemento i-ésimo en cada tupla viene del argumento i-ésimo iterable a zip(). Esto continúa hasta que el argumento más corto se agota.
    return sum(1 for expected, actual in zip(_password, guess) if expected != actual)


def gene_set():
    """ Return the feasible characters of the password """
    return " 0123456789áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}"


def initial_population(pop_size, chromosome_len):
    """ Create a initial population """
    # return [random.sample(gene_set(), chromosome_len) for _ in range(pop_size)]
    return [[random.choice(gene_set()) for _ in range(chromosome_len)] for _ in range(pop_size)]


# Implemente la función mutate() que recibe un cromosoma y lo muta cambiando aleatoriamente un único gen por otro del gene_set().
def mutate(chromosome):
    """ Mutate randomly one gen of the chromosome, which is a string with the characters of the password """
    chromosome[random.randint(0, len(chromosome) - 1)
               ] = random.choice(gene_set())
    return chromosome


# Implemente la función crossover() que recibe 2 cromosomas, realiza con ellos una hibridación de 1 punto aleatorio, y devuelve otro cromosoma con la hibridación realizada.
def crossover(chromosome1, chromosome2):
    """ Perform a one point crossover of the chromosomes """
    p = random.randint(0, get_password_len() - 1)
    return chromosome1[:p] + chromosome2[p:]


"""
• pop_size el tamaño de la población (por defecto 100) que se mantiene fijo entre generaciones
• elite_rate la proporción de la población que se consideran buenas soluciones y que se usan para construir la siguiente población (por defecto es el 20%)
• mutate_prob la proporción de candidatos que mutan (por defecto es el 80%) de la población entera (incluida la élite). Los candidatos que no se mutan, se cruzan con otro
• max_generations el número máximo de generaciones que permitimos iterar en el
algoritmo (pode defecto 10.000)
"""


def ga(pop_size=1000, elite_rate=0.2, mutate_prob=0.8, max_generations=10000):
    """ Genetic Algorithm driving the search of the password """
    pop = initial_population(pop_size, get_password_len())
    for i in range(max_generations):
        pop.sort(key=get_fitness)
        ga_aux.clear()
        print("Password length:", get_password_len(), "\n\nGeneration:",
                    i, "fitness:", get_fitness(pop[0]), "\n", chromosome_to_string(pop[0]))
        if get_fitness(pop[0]) == 0: return pop[0]
        # pop = next_generation_roulette(pop, elite_rate, mutate_prob)
        pop = next_generation(pop, elite_rate, mutate_prob)
    print("Password not found")
    return False


def next_generation(pop, elite_rate, mutate_prob):
    """ Return the next generation """
    pop_size = len(pop)
    # Selecciona la elite
    pop = pop[:int(pop_size * elite_rate)]
    # Cruzar elite hasta completar la población
    while len(pop) < pop_size:
        pop.append(crossover(random.choice(pop), random.choice(pop)))
    # Mutar al mutate_prob de la poblacion
    pop = [pop[i] if random.random() > mutate_prob else mutate(pop[i]) for i in range(len(pop))]
    return pop


def next_generation_roulette(pop, elite_rate, mutate_prob):
    """ Return the next generation """
    pop_size = len(pop)
    # Selecciona la elite
    split = int(pop_size * elite_rate)
    elite, non_elite = pop[:split], pop[split:]
    # Mutar entre los no elite
    non_elite = [non_elite[i] if random.random() > mutate_prob else mutate(non_elite[i]) for i in range(len(non_elite))]
    # Cruzar para generar descendencia. Se cruza por parejas en orden para cruzar individuos de similar fitness
    progeny = [crossover(pop[i], pop[i+1]) for i in range(0, pop_size, 2)]
    return elite + roulette_wheeling(non_elite + progeny, num_winers=pop_size - len(elite))


def roulette_wheeling(players, num_winers):
    """ Return the winners of the roulette wheel selection """
    # Ordenar de modo que los mejores tengan mayor valor de indice
    players.sort(key=get_fitness, reverse=True)
    winners = []
    for _ in range(num_winers):
        domain = gauss_sum(len(players))
        tirada = random.randint(1, domain)
        winners.append(players.pop(int(inverse_gauss_sum(tirada))-1))
    return winners


def gauss_sum(n):
    """ Return the sum of 1..n natural numbers """
    return (n*(n+1)) // 2


def inverse_gauss_sum(x):
    """ Return the inverse function of the gauss_sum """
    # indice = (math.sqrt(8*tirada+1) - 1) / 2
    return ((8*x+1)**0.5 - 1) / 2


def chromosome_to_string(chromosome):
    """ Return the string representation of the chromosome """
    return "".join(chromosome)


# def clear():
#     if os.name == "nt": os.system("cls")
#     else: os.system("clear")


gpassword = ga()
