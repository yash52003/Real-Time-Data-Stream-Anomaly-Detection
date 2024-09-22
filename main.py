"""
This is the main  script for real-time anomaly detection in data streams.
This script orchestrates the data simulation, anomaly detection, and visualization.
It uses the Z-score algorithm for anomaly detection due to its simplicity and 
effectiveness for real-time processing. The script generates a continuous data 
stream, applies the anomaly detection algorithm, and visualizes the results in 
real-time, providing a comprehensive demonstration of the system's capabilities.
"""

from zscore_anomaly_detection import ZScoreAnomalyDetector
from data_stream_simulator import DataStreamSimulator
from visualization import Visualizer

def main():
    # Initialize components
    data_simulator = DataStreamSimulator()
    anomaly_detector = ZScoreAnomalyDetector(window_size=100, threshold=3)
    visualizer = Visualizer()

 # Run simulation
    for _ in range(1000):# Simulating 1000 data points
        value = next(data_simulator.generate_data())
        is_anomaly = anomaly_detector.is_anomaly(value)
        anomaly_detector.update(value)
        visualizer.update(value, is_anomaly)

    visualizer.show()

if __name__ == "__main__":
    main()