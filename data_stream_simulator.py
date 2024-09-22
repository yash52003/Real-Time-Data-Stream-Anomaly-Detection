"""
Data stream simulator for testing anomaly detection algorithms.
This module generates a continuous stream of simulated data points, 
incorporating regular patterns, seasonal components, and random noise. 
It also injects occasional anomalies to test the detection capabilities 
of the anomaly detection algorithm. This approach provides a controlled 
environment for evaluating the performance of the Z-score method in 
various scenarios.
"""

import numpy as np

class DataStreamSimulator:
    def __init__(self):
        self.t = 0

    def generate_data(self):
        while True:
            # Base signal: sine wave
            base = 10 * np.sin(0.1 * self.t)
            
            # Add seasonal component
            seasonal = 5 * np.sin(0.01 * self.t)
            
            # Add noise
            noise = np.random.normal(0, 1)
            
            # Combine components
            value = base + seasonal + noise
            
            # Occasionally inject anomalies
            if np.random.random() < 0.01:
                value += np.random.choice([-1, 1]) * np.random.uniform(10, 20)
            
            yield value
            self.t += 1