from flask import Flask
from flask_restplus import Api, Resource

from neutrino.neutrino import NeutrinoOscillation
from neutrino.request_parser import stationary_parser, distance_series_parser, energy_series_parser


application = Flask(__name__)
api = Api(application, version='0.0', title='Neutrino Oscillation',
    description='A simple API to provide calculated neutrino oscillation metrics',
)

namespace = api.namespace('neutrinoOscillation', description='Neutrino Oscillation')


@namespace.route('/hello')
class Hello(Resource):
    def get(self):
        return {"Hello": "World"}


@namespace.route('/twoPhase/stationary')
@namespace.expect(stationary_parser)
class TwoPhase(Resource):

    def get(self):
        args = stationary_parser.parse_args()
        neutrino_type = args['type']
        energy = args['energy']
        distance = args['distance']

        neutrino_oscillation = NeutrinoOscillation(oscillation_type=neutrino_type)

        result = neutrino_oscillation.two_phase_oscillation_probability(energy=energy, distance=distance)
        return {"probability": result}


@namespace.route('/twoPhase/series/distance')
@namespace.expect(distance_series_parser)
class TwoPhaseDistance(Resource):

    def get(self):

        args = distance_series_parser.parse_args()
        neutrino_type = args['type']
        energy = args['energy']
        min_distance =args['minDistance'] or 0
        max_distance = args['maxDistance']
        distance_interval = args['distanceInterval']
        neutrino_oscillation = NeutrinoOscillation(oscillation_type=neutrino_type)
        distances, probabilities = neutrino_oscillation.two_phase_series(max_distance=max_distance,
                                                                         min_distance=min_distance,
                                                                         interval=distance_interval,
                                                                         energy_val=energy, distance=True)

        return {"distance": distances, "probability": probabilities}


@namespace.route('/twoPhase/series/energy')
@namespace.expect(energy_series_parser)
class TwoPhaseEnergy(Resource):

    def get(self):
        args = energy_series_parser.parse_args()
        neutrino_type = args['type']
        distance = args['distance']
        min_energy = args['minEnergy'] or 0
        max_energy = args['maxEnergy']
        energy_interval = args['energyInterval']
        neutrino_oscillation = NeutrinoOscillation(oscillation_type=neutrino_type)
        energies, probabilities = neutrino_oscillation.two_phase_series(max_energy=max_energy,
                                                                        min_energy=min_energy,
                                                                        interval=energy_interval,
                                                                        distance_val=distance, energy=True)

        return {"energy": energies, "probability": probabilities}

if __name__ == "__main__":
    application.run(host="0.0.0.0")
