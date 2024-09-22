import numpy as np

class DataStreamSimulator:
    def __init__(self, anomaly_probability=0.01, anomaly_magnitude_range=(10, 20), noise_std=1):
        """
        Initialize the data stream simulator.
        
        :param anomaly_probability: Probability of an anomaly being injected.
        :param anomaly_magnitude_range: Range of anomaly magnitude.
        :param noise_std: Standard deviation for noise generation.
        """
        self.t = 0
        self.anomaly_probability = anomaly_probability
        self.anomaly_magnitude_range = anomaly_magnitude_range
        self.noise_std = noise_std

    def _base_signal(self, t):
        """Generate the base sine wave signal."""
        return 10 * np.sin(0.1 * t)

    def _seasonal_component(self, t):
        """Generate the seasonal sine wave component."""
        return 5 * np.sin(0.01 * t)

    def _add_noise(self):
        """Add random noise to the signal."""
        return np.random.normal(0, self.noise_std)

    def _inject_anomaly(self):
        """Inject anomalies with a specified probability."""
        if np.random.random() < self.anomaly_probability:
            return np.random.choice([-1, 1]) * np.random.uniform(*self.anomaly_magnitude_range)
        return 0

    def generate_data(self):
        """Continuously generate data points with base, seasonal components, noise, and occasional anomalies."""
        while True:
            base_signal = self._base_signal(self.t)
            seasonal_component = self._seasonal_component(self.t)
            noise = self._add_noise()
            anomaly = self._inject_anomaly()

            # Combine all components to form the final value
            value = base_signal + seasonal_component + noise + anomaly

            yield value
            self.t += 1
