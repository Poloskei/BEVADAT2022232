
import numpy as np
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KNNClassifier:
    @staticmethod
    def load_csv(csv_path:str) ->Tuple[np.ndarray,np.ndarray]:
        np.random.seed(42)
        dataset = np.genfromtxt(csv_path,delimiter=',')
        np.random.shuffle(dataset,)
        x,y = dataset[:,:4],dataset[:,-1]
        return x,y


    def __init__(self,k:int,test_split_ration:float)->None:
        self.k = k
        self.test_split_ratio = test_split_ratio
        


    def k_neighbors()->int:
        return self.k

    def train_test_split(features:np.ndarray,labels:np.ndarray,) -> None:
        test_size = int(len(features) * test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        x_train,y_train = features[:train_size,:],labels[:train_size]
        x_test,y_test = features[train_size:train_size+test_size,:], labels[train_size:train_size + test_size]
        #return (x_train,y_train,x_test,y_test)
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test

    def euclidean(element_of_x:np.ndarray) -> np.ndarray:
        return np.sqrt(np.sum((self.x_train - element_of_x)**2,axis=1))

    def predict(x_test:np.ndarray) -> np.ndarray:
        labels_pred = []
        for x_test_element in x_test:
            distances = euclidean(x_test_element)
            distances = np.array(sorted(zip(distances,y_train)))
            label_pred = mode(distances[:k,1],keepdims=False).mode
            labels_pred.append(label_pred)
        self.y_preds = np.array(labels_pred,dtype=np.int32)

    def accuracy() -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100

    def plot_confusion_matrix():
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        sns.heatmap(conf_matrix,annot=True) 