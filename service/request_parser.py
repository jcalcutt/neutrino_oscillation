from flask_restplus import reqparse

from service.constants import TwoPhase


stationary_parser = reqparse.RequestParser()
stationary_parser.add_argument('type', type=str, choices=[osc_type.name for osc_type in TwoPhase], required=True,
                               help='Solar or atmospheric')
stationary_parser.add_argument('energy', type=float, required = True, help='Energy in GeV')
stationary_parser.add_argument('distance', type=float, required = True, help='Distance from source, in km')

de_series_parser = reqparse.RequestParser()
de_series_parser.add_argument('type', type=str, choices=[osc_type.name for osc_type in TwoPhase], required=True,
                               help='Solar or atmospheric')
de_series_parser.add_argument('maxDistanceEnergy', type=float, required=True, help='Max distance/energy')
de_series_parser.add_argument('minDistanceEnergy', type=float, required=False, help='Min distance/energy, default=0')
de_series_parser.add_argument('distanceEnergyInterval', type=float, required=True, help='Distance/Energy Interval')