import sklearn.utils
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
import sklearn.metrics as metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

class Builder_Creation:
    
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def get_subsample(self, df_share):
        """
        1. Copy train dataset
        2. Shuffle data (don't miss the connection between X_train and y_train)
        3. Return df_share %-subsample of X_train and y_train
        """
        n_samples = int(df_share / 100 * len(self.X_train))
        print("number of observations used for training = ", n_samples)
        X_train_sub, y_train_sub = shuffle(self.X_train, self.y_train, random_state=42, n_samples=n_samples)
        return X_train_sub, y_train_sub

    
if __name__ == "__main__":
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    """

    dataset = datasets.load_iris()
    features = dataset.data
    targets = dataset.target
    X_train, X_test, y_train, y_test = train_test_split(features, targets)
    pipe_lr = make_pipeline(StandardScaler(), LinearRegression())
    
    pattern_item = Builder_Creation(X_train, y_train)
    
    for df_share in range(10, 101, 10):
        """
        1. Preprocess curr_X_train, curr_y_train in the way you want
        2. Train Linear Regression on the subsample
        3. Save or print the score to check how df_share affects the quality
        """
        curr_X_train, curr_y_train = pattern_item.get_subsample(df_share)
        pipe_lr = LinearRegression().fit(curr_X_train, curr_y_train)
        pipe_lr.fit(curr_X_train, curr_y_train)
        y_pred_test = pipe_lr.predict(X_test)
        mse = metrics.mean_squared_error(y_test, y_pred_test)        
        print(f'Score for {df_share}%: {mse}')
        

