# -*- coding: utf-8 -*-

from __future__ import annotations

import random
from math import ceil

###############################################################################
# Declaration of constants
###############################################################################

_DEF_PASSWORD = "MUIA : Genetic Algorithms - {Evolutionary Computation} <[by Group 1]>"

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


def stochastic_universal_sampling(players: list, num_winners: int) -> list:
    """Select individuals with replacement using stochastic universal sampling.

    The algorithm minimizes fitness, whereas roulette selection requires greater
    values for better individuals. Therefore, fitness is converted to a strictly
    positive adaptation value before constructing the roulette.
    """
    if not players or num_winners <= 0:
        return []

    worst_fitness = max(player[1] for player in players)
    sectors = [worst_fitness - player[1] + 1 for player in players]
    rulette_size = sum(sectors)
    marker_distance = rulette_size / num_winners
    position = random.uniform(0, marker_distance)

    winners = []
    accumulated_position = sectors[0]
    i = 0
    for _ in range(num_winners):
        while position > accumulated_position and i < len(players) - 1:
            i += 1
            accumulated_position += sectors[i]
        winners.append(players[i])
        position += marker_distance
    return winners


def tournament(players: list, num_winners: int, tournament_size: int = 3) -> list:
    """Select the best individual from random tournaments of k participants.

    Participants do not repeat within one tournament. Winners may repeat across
    tournaments, so the returned list can be used as a complete mating pool.
    """
    if not players or num_winners <= 0:
        return []

    size = min(tournament_size, len(players))
    return [min(random.sample(players, size), key=lambda player: player[1])
            for _ in range(num_winners)]


def _gauss_form(n):
    """ Return the sum of 1..n natural numbers """
    return (n * (n + 1)) // 2


def _inverse_gauss_form(a):
    """ Return the inverse function of the gauss_sum """
    return ((8 * a + 1) ** 0.5 - 1) / 2
