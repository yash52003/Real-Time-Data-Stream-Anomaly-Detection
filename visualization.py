"""
Visualization module for real-time plotting of data streams and anomalies.
This module uses matplotlib to create an interactive plot that updates in 
real-time as new data points are processed. It visualizes the continuous 
data stream and highlights detected anomalies, providing an intuitive 
representation of the anomaly detection process.
"""

import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.anomaly_points, = self.ax.plot([], [], 'ro')
        self.data = []
        self.anomalies = []

    def update(self, value, is_anomaly):
        self.data.append(value)
        if is_anomaly:
            self.anomalies.append((len(self.data) - 1, value))

        self.line.set_data(range(len(self.data)), self.data)
        anomaly_x, anomaly_y = zip(*self.anomalies) if self.anomalies else ([], [])
        self.anomaly_points.set_data(anomaly_x, anomaly_y)

        self.ax.relim()
        self.ax.autoscale_view()
        plt.pause(0.01)

    def show(self):
        plt.ioff()
        plt.show()