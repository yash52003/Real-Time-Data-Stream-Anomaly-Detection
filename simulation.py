"""
Simulation script for anomaly detection without visualization.
This script runs the anomaly detection algorithm on simulated data and reports 
the detected anomalies. It's useful for testing the algorithm's performance 
or for batch processing of data streams. The Z-score algorithm is used here 
for its ability to adapt to changing data patterns in real-time streams.
"""

from data_stream_simulator import DataStreamSimulator
from zscore_anomaly_detection import ZScoreAnomalyDetector

def run_simulation(num_points=1000):
    simulator = DataStreamSimulator()
    detector = ZScoreAnomalyDetector()
    
    anomalies = []
    for i in range(num_points):
        value = next(simulator.generate_data())
        if detector.is_anomaly(value):
            anomalies.append((i, value))
        detector.update(value)
    
    return anomalies

if __name__ == "__main__":
    results = run_simulation()
    print(f"Detected {len(results)} anomalies")
    for i, value in results:
        print(f"Anomaly at point {i}: {value}")