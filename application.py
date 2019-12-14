from flask import Flask
from flask_restplus import Api, Resource

from service.neutrino import NeutrinoOscillation
from service.request_parser import stationary_parser, de_series_parser
from service.restplus_model import stationary_model, series_model, series_single_model
from service.mapper import NeutrinoMapper

application = Flask(__name__)
api = Api(application, version='0.0', title='Neutrino Oscillation',
          description='A simple API to provide calculated service oscillation metrics',
          )

namespace = api.namespace('neutrinoOscillation', description='Neutrino Oscillation')

restplus_models = [stationary_model, series_model, series_single_model]

for model in restplus_models:
    api.models[model.name] = model


@namespace.route('/twoPhase')
@namespace.expect(stationary_parser)
class TwoPhase(Resource):
    @api.marshal_with(stationary_model)
    def get(self):
        args = stationary_parser.parse_args()
        neutrino_type = args['type']
        energy = args['energy']
        distance = args['distance']

        neutrino_oscillation = NeutrinoOscillation(oscillation_type=neutrino_type)

        probability = neutrino_oscillation.two_phase_oscillation_probability(distance_energy=distance / energy)
        result = NeutrinoMapper.map_stationary(energy=energy, distance=distance, probability=probability)
        return result


@namespace.route('/twoPhase/series')
@namespace.expect(de_series_parser)
class TwoPhaseDistanceEnergy(Resource):
    @api.marshal_with(series_model)
    def get(self):
        args = de_series_parser.parse_args()
        neutrino_type = args['type']
        min_distance_energy = args['minDistanceEnergy'] or 0
        max_distance_energy = args['maxDistanceEnergy']
        distance_energy_interval = args['distanceEnergyInterval']
        neutrino_oscillation = NeutrinoOscillation(oscillation_type=neutrino_type)
        distances, probabilities = neutrino_oscillation.two_phase_series(max_val=max_distance_energy,
                                                                         min_val=min_distance_energy,
                                                                         interval=distance_energy_interval)

        return NeutrinoMapper.map_series(distance_energy=distances, probability=probabilities)


if __name__ == "__main__":
    application.run(debug=True, port=8003)
    # host="0.0.0.0"
