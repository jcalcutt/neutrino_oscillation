class StationaryModel:
    def __init__(self, energy, distance, probability):
        self.energy = energy
        self.distance = distance
        self.probability = probability


class SeriesModel:
    def __init__(self, distance_energy, probability):
        self.distance_energy = distance_energy
        self.probability = probability


class SeriesWrapperModel:
    def __init__(self):
        self.series = []

    def add_values(self, singular_series):
        self.series.append(singular_series)
