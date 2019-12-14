import math
import numpy as np
from typing import List

from service.constants import TwoPhase


class NeutrinoOscillation:

    def __init__(self, oscillation_type):
        self.oscillation_type = oscillation_type

    def two_phase_oscillation_probability(self, distance_energy: float) -> float:
        """calculate the two-phase probability of neutrino oscillation given the distance/energy (in km/GeV) of a
        particle

        :param distance_energy: float
        :return: float, probability of oscillation
        """
        sin_s_t_theta, delta_m = [i for i in TwoPhase[self.oscillation_type].value]
        return sin_s_t_theta * (math.sin(1.27 * delta_m * distance_energy)) ** 2

    def two_phase_series(self, min_val: float, max_val:float, interval:float) -> (List[float], List[float]):
        """for a given distance/energy range of values, calculate the assocayed probabilities of two-phase oscillation

        :param min_val: float
        :param max_val: float
        :param interval: float
        :return: list of floats, list of floats -> list of requested distance energy values and list of their associated
        probabilities
        """

        dynamic_list = np.arange(min_val, max_val, interval)
        probability_list = [self.two_phase_oscillation_probability(dist_en) for dist_en in dynamic_list]

        return dynamic_list, probability_list