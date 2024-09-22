"""
Z-score based anomaly detection for real-time data streams.
This module implements the Z-score algorithm for detecting anomalies in 
continuous data streams. The Z-score method is effective for its simplicity, 
efficiency, and adaptability to changing data patterns. By using a sliding 
window approach, this implementation maintains recent statistics (mean and 
standard deviation), making it suitable for dynamic environments with 
concept drift.
"""

import numpy as np
from collections import deque

class ZScoreAnomalyDetector:
    def __init__(self, window_size=100, threshold=3):
        """
        Initializes the Z-Score anomaly detector with a sliding window.

        :param window_size: The number of recent data points to consider in the window.
        :param threshold: The Z-score threshold above which a data point is considered an anomaly.
        """
        self.window_size = window_size
        self.threshold = threshold

        # A deque to store the most recent data points (sliding window)
        self.data_window = deque(maxlen=window_size)

        # Initialize mean and standard deviation for the sliding window
        self.mean = 0
        self.std = 0

    def update(self, value):
        """
        Updates the sliding window with a new data point and recalculates the statistics.

        :param value: The new data point to add to the sliding window.
        """
        # Append the new value to the sliding window
        self.data_window.append(value)

        # Recalculate the mean and standard deviation based on the current window
        self._recalculate_statistics()

    def is_anomaly(self, value):
        """
        Checks whether a given data point is an anomaly based on the Z-score.

        :param value: The data point to check for anomaly status.
        :return: True if the data point is an anomaly, False otherwise.
        """
        # Ensure there are enough data points in the window to calculate statistics
        if len(self.data_window) < self.window_size:
            return False
        
        # If the standard deviation is zero, anomaly detection is not possible
        if self.std == 0:
            return False
        
        # Calculate the Z-score for the current value
        z_score = abs(value - self.mean) / self.std

        # Return True if the Z-score exceeds the specified threshold
        return z_score > self.threshold

    def _recalculate_statistics(self):
        """
        Recalculates the mean and standard deviation for the current window.
        This ensures the statistics stay updated as new data points are added.
        """
        self.mean = np.mean(self.data_window)
        self.std = np.std(self.data_window)
