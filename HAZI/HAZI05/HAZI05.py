
import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KNNClassifier:
    @staticmethod
    def load_csv(csv_path:str) ->Tuple[pd.DataFrame,pd.DataFrame]:
        #np.random.seed(42)
        df = pd.read_csv(csv_path,delimiter=',')
        df.sample(frac=1,random_state=42).reset_index(drop=True)
        x,y = df.iloc[:,:4],df.iloc[:,-1]
        return x,y


    def __init__(self,k:int,test_split_ratio:float)->None:
        self.k = k
        self.test_split_ratio = test_split_ratio
        

    @classmethod
    def k_neighbors(self)->int:
        return self.k

    def train_test_split(self,features:pd.DataFrame,labels:pd.DataFrame) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        x_train,y_train = features.iloc[:train_size,:],labels.iloc[:train_size]
        x_test,y_test = features.iloc[train_size:train_size+test_size,:], labels.iloc[train_size:train_size + test_size]
        #return (x_train,y_train,x_test,y_test)
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test


    def euclidean(self,element_of_x:pd.DataFrame) -> pd.DataFrame:
        return ((self.x_train - element_of_x).sum()**2).pow(1./2)

    def predict(self,x_test:np.ndarray) -> np.ndarray:
        labels_pred = []
        for x_test_element in x_test:
            distances = self.euclidean(x_test_element)
            distances = np.array(sorted(zip(distances,self.y_train)))
            label_pred = mode(distances[:self.k,1],keepdims=False).mode
            labels_pred.append(label_pred)
        self.y_preds = np.array(labels_pred,dtype=np.int32)

    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100

    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        return conf_matrix
