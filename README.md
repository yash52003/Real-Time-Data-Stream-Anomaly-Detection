# Real-Time Anomaly Detection in Data Streams  
### Yash Choudhary (Admission No: 21JE1066)  
#### Cobblestone Research Project

## Project Overview  
This project implements a **real-time anomaly detection system** for continuous data streams using the **Z-score algorithm**. The system is designed to detect unusual patterns or outliers in streaming data, which can represent various metrics such as financial transactions, system performance indicators, or sensor readings. The solution emphasizes real-time detection, efficient processing, and adaptability to changing data patterns.

## Key Features  
- **Real-time anomaly detection** using Z-score algorithm  
- **Simulated data stream generation** with injected anomalies  
- **Live visualization** of the data stream and detected anomalies  
- **Adaptability** to concept drift and seasonal variations  

## Project Structure  
The project consists of the following Python files:  
- **`main.py`**: The entry point of the application. Orchestrates the data simulation, anomaly detection, and visualization.  
- **`simulation.py`**: A standalone script to run the simulation without visualization, useful for testing or batch processing.  
- **`visualization.py`**: Handles real-time plotting of the data stream and detected anomalies.  
- **`zscore_anomaly_detection.py`**: Implements the Z-score algorithm for detecting anomalies.  
- **`data_stream_simulator.py`**: Generates a simulated data stream with occasional injected anomalies.

## Requirements  
- **Python 3.x**  
- **NumPy**  
- **Matplotlib**

### Installation  
Ensure you have **Python 3.x** installed on your system.  

Install the required libraries:  
```bash
pip install numpy matplotlib

### To run the main application with visualization:
This will start the data stream simulation and open a `matplotlib` window that shows the real-time data stream and detected anomalies.
```bash
python main.py

## Customization
You can adjust the parameters of the Z-score algorithm in `zscore_anomaly_detection.py`:

- **`window_size`**: Number of recent data points to consider (default: 100).
- **`threshold`**: Z-score threshold for anomaly detection (default: 3).

You can modify the data generation process in `data_stream_simulator.py` to simulate different types of data streams with varying levels of anomalies.

## How It Works
1. The **`DataStreamSimulator`** generates a continuous stream of data points, occasionally injecting anomalies.
2. The **`ZScoreAnomalyDetector`** processes each data point, calculating its Z-score based on the most recent data window.
3. If a data point's Z-score exceeds the specified threshold, it is flagged as an anomaly.
4. The **Visualizer** plots the data stream in real-time, highlighting detected anomalies on the plot.

## Why Z-Score?
The **Z-score method** was chosen for its simplicity, efficiency, and effectiveness in identifying outliers. It adapts well to changes in data patterns, making it ideal for real-time anomaly detection in dynamic data streams.
