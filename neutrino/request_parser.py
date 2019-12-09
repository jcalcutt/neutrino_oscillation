from flask_restplus import reqparse

from neutrino.constants import TwoPhase


stationary_parser = reqparse.RequestParser()
stationary_parser.add_argument('type', type=str, choices=[osc_type.name for osc_type in TwoPhase], required=True,
                               help='Solar or atmospheric')
stationary_parser.add_argument('energy', type=float, required = True, help='Energy in GeV')
stationary_parser.add_argument('distance', type=float, required = True, help='Distance from source, in km')

distance_series_parser = stationary_parser.copy()
distance_series_parser.remove_argument('distance')
distance_series_parser.add_argument('maxDistance', type=int, required=True, help='Max distance')
distance_series_parser.add_argument('minDistance', type=int, required=False, help='Min distance')
distance_series_parser.add_argument('distanceInterval', type=int, required=True, help='Distance Interval')

energy_series_parser = stationary_parser.copy()
energy_series_parser.remove_argument('energy')
energy_series_parser.add_argument('maxEnergy', type=int, required=True, help='Max energy')
energy_series_parser.add_argument('minEnergy', type=int, required=False, help='Min energy')
energy_series_parser.add_argument('energyInterval', type=int, required=True, help='Energy Interval')