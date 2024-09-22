"""
Z-score based anomaly detection for data streams.
This module implements the Z-score algorithm for detecting anomalies in 
real-time data streams. The Z-score method is chosen for its simplicity, 
efficiency, and ability to adapt to changing data patterns. It uses a 
sliding window approach to maintain recent statistics, making it suitable 
for continuous data streams with potential concept drift.
"""

import numpy as np
from collections import deque

class ZScoreAnomalyDetector:
    def __init__(self, window_size=100, threshold=3):
        self.window_size = window_size
        self.threshold = threshold
        self.data_window = deque(maxlen=window_size)
        self.mean = 0
        self.std = 0

    def update(self, value):
        self.data_window.append(value)
        
        # Recalculate mean and standard deviation
        self.mean = np.mean(self.data_window)
        self.std = np.std(self.data_window)

    def is_anomaly(self, value):
        if len(self.data_window) < self.window_size:
            return False
        if self.std == 0:
            return False
        z_score = abs(value - self.mean) / self.std
        return z_score > self.threshold