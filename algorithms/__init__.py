from __future__ import annotations

import random
from math import ceil

###############################################################################
# Declaración de constantes
###############################################################################

DEF_PASSWORD = "Algoritmos evolutivos - {Computación Bioinspirada} <[by José Herce]>"

GEN_SET = " 0123456789áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>¿?@[" \
          "\\]^_`{|}"


###############################################################################
# Métodos propios
###############################################################################


def winner(value):
    """ Return the winner of the roulette wheel selection """
    return ceil(inverse_gauss_form(value)) - 1


def roulette(players: list, num_winners=1) -> list:
    """ Return the winners of the roulette wheel selection """
    selection_mode = num_winners < len(players) / 2  # True si es mejor seleccionar que eliminar
    # players = players.copy()  # Evitar modificar la lista original
    # players = np.array(players.copy(), dtype=object)  # Evitar modificar la lista original
    ordered_players = sorted(players, key=lambda x: x[1], reverse=selection_mode)
    # players.sort(key=lambda x: method_name(x), reverse=selection_mode)
    # players = players[np.argsort(players[:, 1].astype(int))[::-1]].tolist()
    winners = [] if selection_mode else ordered_players
    for _ in range(num_winners if selection_mode else len(players) - num_winners):
        domain = gauss_form(len(ordered_players))
        tirada = random.randint(1, domain)
        if selection_mode:
            winners.append(ordered_players.pop(winner(tirada)))
        else:
            winners.pop(winner(tirada))
    # return winners if num_winners != 1 else [winners[0]]
    return winners


def method_name(x):
    return x[1]


def gauss_form(n):
    """ Return the sum of 1..n natural numbers """
    return (n * (n + 1)) // 2


def inverse_gauss_form(a):
    """ Return the inverse function of the gauss_sum """
    return ((8 * a + 1) ** 0.5 - 1) / 2

