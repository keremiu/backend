import numpy as np
'''Z = (x - μ) / σ
Burada:
Z, Z-puanını temsil eder.
x, veri noktasının değeridir.
μ, veri setinin ortalamasıdır.
σ, veri setinin standart sapmasıdır.'''
#[2.5, 3.0, 2.2, 2.8, 1.5, 1.2, 1.8, 1.3, 3.7, 3.5, 3.6, 5.0]
#Anomali tespiti:
#[False False False False False False False False False False False True]
import numpy as np
class AnomalyDetector2:#IQR
    def __init__(self, iqr_threshold=1):
        self.iqr_threshold = iqr_threshold
        self.lower_bound = None
        self.upper_bound = None

    def fit(self, data):
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        self.lower_bound = q1 - (self.iqr_threshold * iqr)
        self.upper_bound = q3 + (self.iqr_threshold * iqr)

    def detect_anomalies(self, data):
        if self.lower_bound is None or self.upper_bound is None:
            raise Exception("Fit method should be called before detecting anomalies.")
        print(data)
        anomalies = np.logical_or(data < self.lower_bound, data > self.upper_bound)
        return anomalies
    
class AnomalyDetector:
    def __init__(self, threshold=1.5):
        self.threshold = threshold
        self.mean = None
        self.std_dev = None

    def fit(self, data):
        self.mean = np.mean(data)
        self.std_dev = np.std(data)

    def detect_anomalies(self, data):
        z_scores = (data - self.mean) / self.std_dev
        anomalies = np.abs(z_scores) > self.threshold
        return anomalies