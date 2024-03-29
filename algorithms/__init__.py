# -*- coding: utf-8 -*-

from __future__ import annotations

import random
from math import ceil

###############################################################################
# Declaration of constants
###############################################################################

_DEF_PASSWORD = "Evolutionary Algorithms - {Bioinspired Computing} <[by José Herce]>"

_GEN_SET = " 0123456789áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>¿?@[" \
          "\\]^_`{|}"


###############################################################################
# Custom methods
###############################################################################


def _winner(value):
    """ Return the winner of the roulette wheel selection """
    return ceil(_inverse_gauss_form(value)) - 1


def roulette(players: list, num_winners=1) -> list:
    """ Return the winners of the roulette wheel selection """
    selection_mode = num_winners < len(players) / 2  # True if it's better to select than eliminate
    ordered_players = sorted(players, key=lambda x: x[1], reverse=selection_mode)
    winners = [] if selection_mode else ordered_players
    for _ in range(num_winners if selection_mode else len(players) - num_winners):
        domain = _gauss_form(len(ordered_players))
        spin = random.randint(1, domain)
        if selection_mode:
            winners.append(ordered_players.pop(_winner(spin)))
        else:
            winners.pop(_winner(spin))
    return winners


def _gauss_form(n):
    """ Return the sum of 1..n natural numbers """
    return (n * (n + 1)) // 2


def _inverse_gauss_form(a):
    """ Return the inverse function of the gauss_sum """
    return ((8 * a + 1) ** 0.5 - 1) / 2
