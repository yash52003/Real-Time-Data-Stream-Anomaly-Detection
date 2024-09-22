from zscore_anomaly_detection import ZScoreAnomalyDetector
from data_stream_simulator import DataStreamSimulator
from visualization import Visualizer

class RealTimeAnomalyDetectionSystem:
    def __init__(self, num_data_points=1000, window_size=100, threshold=3):
        """
        Initialize the real-time anomaly detection system.
        
        :param num_data_points: Number of data points to simulate.
        :param window_size: Window size for Z-score anomaly detection.
        :param threshold: Z-score threshold to flag anomalies.
        """
        self.num_data_points = num_data_points
        self.data_simulator = DataStreamSimulator()
        self.anomaly_detector = ZScoreAnomalyDetector(window_size=window_size, threshold=threshold)
        self.visualizer = Visualizer()

    def run(self):
        """Run the anomaly detection system for the specified number of data points."""
        data_stream = self.data_simulator.generate_data()

        for _ in range(self.num_data_points):
            value = next(data_stream)
            is_anomaly = self.anomaly_detector.is_anomaly(value)
            self.anomaly_detector.update(value)
            self.visualizer.update(value, is_anomaly)

        self.visualizer.show()

def main():
    # Initialize and run the anomaly detection system
    anomaly_detection_system = RealTimeAnomalyDetectionSystem(
        num_data_points=1000, 
        window_size=100, 
        threshold=3
    )
    anomaly_detection_system.run()

if __name__ == "__main__":
    main()
