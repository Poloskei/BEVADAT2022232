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
        kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        clusters = kmeans.fit_predict(self.digits.data,self.digits.target)
        self.clusters = clusters

    def get_labels(self):
        result = np.zeros(self.clusters.shape)
        for i in self.digits.target_names:
            mask = self.clusters == i
            modusz = mode(self.digits.target[mask]).mode
            result[mask]= modusz
        self.labels = result

    def calc_accuracy(self):
        self.accuracy = round(accuracy_score(self.digits.target,self.labels),2)

    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target,self.labels)
