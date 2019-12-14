from typing import List

from service.model import StationaryModel, SeriesModel, SeriesWrapperModel


class NeutrinoMapper:

    @staticmethod
    def map_stationary(energy: float, distance: float, probability: float) -> StationaryModel:
        """map stationary values to model

        :param energy: float
        :param distance: float
        :param probability: float
        :return: StationaryModel
        """
        return StationaryModel(energy=energy, distance=distance, probability=probability)

    @staticmethod
    def map_series(distance_energy: List[float], probability: List[float]) -> SeriesWrapperModel:
        """map series values of distance/energy and their corresponding probabilities to model

        :param distance_energy: list of floats
        :param probability: list of floats
        :return: SeriesWrapperModel
        """
        series_wrapper_model = SeriesWrapperModel()
        for dist_energy, prob in zip(distance_energy, probability):
            series_wrapper_model.add_values(SeriesModel(distance_energy=dist_energy, probability=prob))
        return series_wrapper_model