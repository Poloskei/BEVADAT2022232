import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KNNClassifier:
    @staticmethod
    def load_csv(csv_path:str) ->Tuple[pd.DataFrame,pd.DataFrame]:
        df = pd.read_csv(csv_path,na_values='""',delimiter=',')
        df = df.sample(frac=1,random_state=42).reset_index(drop=True)
        x,y = df.iloc[:,:-1],df.iloc[:,-1]
        y = pd.DataFrame(y).reset_index(drop=True)
        return x,y


    def __init__(self,k:int,test_split_ratio:float)->None:
        self.k = k
        self.test_split_ratio = test_split_ratio
        self.y_preds = pd.DataFrame()
        
    @property
    def k_neighbors(self)->int:
        return self.k
    
    @k_neighbors.setter
    def k_neighbors(self,value):
        self.k=value
    

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
        return pd.DataFrame(((self.x_train - element_of_x)**2).sum(axis=1).pow(1./2))

    def predict(self,x_test:pd.DataFrame):
        labels_pred = []
        for i in range(len(x_test)):
            distances = self.euclidean(x_test.iloc[i])
            distances['y']=self.y_train
            distances.sort_values(by = [0],inplace=True)
            label_pred = distances.head(self.k)['y'].mode()[0]
            labels_pred.append(label_pred)

       
        self.y_preds = pd.DataFrame(labels_pred)

    def accuracy(self) -> float:
        self.y_test.reset_index(drop=True,inplace=True)
        self.y_preds.reset_index(drop=True,inplace=True)
        self.y_test.columns=['y']
        self.y_preds.columns=['y']
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100

    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test,self.y_preds)
        return conf_matrix
    
    def best_k(self)->Tuple[int,float]:
        bestk=0
        bestval=0.0
        for i in range(1,20):
            self.__init__(i,0.2)
            
            self.predict(self.x_test)

            acc = self.accuracy().item()
            if acc > bestval:
                bestval=acc
                bestk=i
        
        return bestk,bestval.__round__(2)
