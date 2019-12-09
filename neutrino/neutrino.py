import math

from neutrino.constants import TwoPhase


class NeutrinoOscillation:

    def __init__(self, oscillation_type):
        self.oscillation_type = oscillation_type

    def two_phase_oscillation_probability(self, energy, distance):
        sin_s_t_theta, delta_m = [i for i in TwoPhase[self.oscillation_type].value]
        return sin_s_t_theta * (math.sin(1.27 * delta_m * (distance / energy))) ** 2

    def two_phase_series(self, interval, **kwargs):
        if kwargs.get('distance'):
            dynamic_list = [i for i in range(kwargs.get('min_distance'), kwargs.get('max_distance'), interval)]
            probability_list = [self.two_phase_oscillation_probability(kwargs.get('energy_val'), dist) for dist in dynamic_list]
        elif kwargs.get('energy'):
            dynamic_list = [i for i in range(kwargs.get('min_energy'), kwargs.get('max_energy'), interval)]
            probability_list = [self.two_phase_oscillation_probability(energy, kwargs.get('distance_val')) for energy in
                                dynamic_list]
        else:
            raise ValueError

        return dynamic_list, probability_list