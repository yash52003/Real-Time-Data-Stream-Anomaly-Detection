"""
Simulation script for anomaly detection without visualization.
This script runs the Z-score anomaly detection algorithm on simulated data points 
and logs the detected anomalies. It is useful for testing the performance of the 
anomaly detection algorithm or for batch processing large streams of data without 
the overhead of real-time visualization.

The Z-score algorithm dynamically adjusts to changes in the data, making it well-suited 
for real-time anomaly detection in streams with non-stationary patterns.
"""

from data_stream_simulator import DataStreamSimulator
from zscore_anomaly_detection import ZScoreAnomalyDetector

def run_simulation(num_points=1000):
    """
    Run the anomaly detection simulation over a specified number of data points.

    :param num_points: The number of data points to simulate (default: 1000).
    :return: A list of detected anomalies, each represented as a tuple (index, value).
    """
    # Initialize the data simulator and anomaly detector
    simulator = DataStreamSimulator()
    detector = ZScoreAnomalyDetector()

    # List to store detected anomalies
    anomalies = []

    # Simulate data stream and perform anomaly detection
    for i in range(num_points):
        # Generate the next data point from the simulator
        value = next(simulator.generate_data())

        # Check if the current data point is an anomaly based on Z-score
        if detector.is_anomaly(value):
            anomalies.append((i, value))  # Store the anomaly with its index

        # Update the anomaly detector with the new value for future calculations
        detector.update(value)

    return anomalies


if __name__ == "__main__":
    # Run the simulation and capture detected anomalies
    results = run_simulation()

    # Print a summary of the number of detected anomalies
    print(f"Detected {len(results)} anomalies")

    # Print details of each detected anomaly
    for index, value in results:
        print(f"Anomaly at point {index}: {value}")
