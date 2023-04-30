import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits

class KMeansOnDigits:
    
    def __init__(self,n_clusters,random_state) -> None:
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = load_digits()

    def predict(self,n_clusters:int,random_state:int,digits):
        kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
        clusters = kmeans.fit_predict(digits.data,digits.target)
        self.clusters = clusters

    def get_labels(self,clusters:np.ndarray, digits):
        result = np.zeros(clusters.shape)
        for i in digits.target_names:
            mask = clusters == i
            modusz = mode(digits.target[mask]).mode
            result[mask]= modusz
        self.labels = result

    def calc_accuracy(self,target_labels:np.ndarray, predicted_labels:np.ndarray):
        self.accuracy = round(accuracy_score(target_labels,predicted_labels),2)

    def confusion_matrix(self,y_true, y_pred):
        self.mat = confusion_matrix(y_true,y_pred)
