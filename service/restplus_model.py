from flask_restplus import Model, fields


stationary_model = Model('stationary_model',{
    'energy': fields.Integer(required=True, attribute='energy'),
    'distance': fields.Integer(required=True, attribute='distance'),
    'probability': fields.Float(required=True, attribute='probability')
})

series_single_model = Model('series_single_model', {
    'distanceOverEnergy': fields.Float(required=True, attribute='distance_energy'),
    'probability': fields.Float(required=True, attribute='probability')
})

series_model = Model('series_model',{
                     'series': fields.List(
                         fields.Nested(series_single_model)
                     )})
