from collections import namedtuple
from enum import Enum


two_phase = namedtuple('two_phase', 'sin_square_two_theta, delta_m_squared')

class TwoPhase(Enum):
    solar = two_phase(0.85, 7.9*10**-5)
    atmospheric = two_phase(0.093,2.5**10-3)
