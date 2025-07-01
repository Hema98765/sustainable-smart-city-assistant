import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    model = IsolationForest(contamination=0.1)
    data["anomaly"] = model.fit_predict(data[["energy_usage"]])
    return data

def plot_anomalies(data):
    plt.plot(data["energy_usage"])
    plt.scatter(data.index[data["anomaly"] == -1], data["energy_usage"][data["anomaly"] == -1], color='red')
    plt.title("Anomaly Detection in Energy Usage")
    plt.savefig("anomalies_plot.png")