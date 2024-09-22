"""
Visualization module for real-time plotting of data streams and detected anomalies.
This module uses matplotlib to create an interactive, real-time plot that updates 
as new data points are processed. It visualizes the continuous data stream and 
highlights detected anomalies, providing an intuitive view of the anomaly detection process.
"""

import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        """
        Initialize the visualizer for real-time data plotting.
        This sets up the figure and axes for the plot, and initializes empty datasets 
        for storing data points and anomalies.
        """
        # Enable interactive mode in matplotlib for real-time plotting
        plt.ion()
        
        # Create the plot figure and axis
        self.fig, self.ax = plt.subplots()

        # Line for the data stream
        self.line, = self.ax.plot([], [], label='Data Stream')

        # Red circles for anomalies
        self.anomaly_points, = self.ax.plot([], [], 'ro', label='Anomalies')

        # Containers for data and anomalies
        self.data = []  # Stores the continuous data stream
        self.anomalies = []  # Stores detected anomalies (as tuples of index and value)

    def update(self, value, is_anomaly):
        """
        Update the plot with a new data point and check if it is an anomaly.

        :param value: The new data point to be added to the stream.
        :param is_anomaly: A boolean indicating whether the data point is an anomaly.
        """
        # Append the new value to the data stream
        self.data.append(value)

        # If the data point is an anomaly, store its index and value
        if is_anomaly:
            self.anomalies.append((len(self.data) - 1, value))

        # Update the line plot with the new data stream
        self._update_data_line()

        # Update the anomaly markers if any are detected
        self._update_anomaly_markers()

        # Adjust the axis limits and refresh the plot
        self._refresh_plot()

    def _update_data_line(self):
        """
        Update the line plot with the current data stream.
        This adjusts the line to include the new data points as they arrive.
        """
        # Update the data stream line with the current data
        self.line.set_data(range(len(self.data)), self.data)

    def _update_anomaly_markers(self):
        """
        Update the plot with markers for the detected anomalies.
        This adds red circles to the plot at positions where anomalies were detected.
        """
        # If there are any anomalies, extract their positions (x: index, y: value)
        if self.anomalies:
            anomaly_x, anomaly_y = zip(*self.anomalies)
        else:
            anomaly_x, anomaly_y = [], []  # No anomalies

        # Update the anomaly markers on the plot
        self.anomaly_points.set_data(anomaly_x, anomaly_y)

    def _refresh_plot(self):
        """
        Adjust the axis limits and refresh the plot in real-time.
        This ensures that the plot dynamically scales to fit the new data points 
        and anomalies, and then pauses briefly to allow for updates.
        """
        # Recompute the axis limits based on the new data and anomalies
        self.ax.relim()
        self.ax.autoscale_view()

        # Pause to allow real-time updates (this is necessary in interactive mode)
        plt.pause(0.01)

    def show(self):
        """
        Finalize and display the plot after all data points are processed.
        This turns off interactive mode and shows the static plot.
        """
        # Turn off interactive mode to finalize the plot
        plt.ioff()

        # Show the final plot with all data points and anomalies
        plt.show()
