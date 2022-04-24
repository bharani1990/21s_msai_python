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

class Composite_Structure:
    def __init__(self, classifier_list) -> None:
        """
        Initialize a class item with a list of classificators
        """
        self.classifier_list = classifier_list
        

    def fit(self, feature_matrix, response):
        """
        Fit classifiers from the initialization stage
        """
        for c in self.classifier_list:
            c.fit(feature_matrix, response)

    def predict(self, feature_matrix):
        
        """
        Get predicts from all the classifiers and return
        the most popular answers
        """
        y_pred_dict = {}
        for c in self.classifier_list:
            y_pred = c.predict(feature_matrix)
            y_pred_dict[c] = y_pred
        return y_pred_dict
        


if __name__ == "__main__":
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    3. Prepare classifiers to initialize <StructuralPatternName> class.
    4. Train the ensemble
    """
    dataset = datasets.load_iris()
    features = dataset.data
    targets = dataset.target
    X_train, X_test, y_train, y_test = train_test_split(features, targets)
    classifier_list = [
        DecisionTreeClassifier(max_depth=None, min_samples_split=2, random_state=0),
        RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=42),
        ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0),
        RandomForestClassifier(n_estimators=10)
    ]
    
    ensemble = Composite_Structure(classifier_list)    
    ensemble.fit(X_train, y_train)
    
    y_pred_dict = ensemble.predict(X_test)
    list_of_lists = []
    for k, v in y_pred_dict.items():
        list_of_lists.append(list(v))
    nume = np.array([sum(i) for i in zip(list_of_lists[0], list_of_lists[1], list_of_lists[2], list_of_lists[3])])
    deno = len(classifier_list)
    y_pred = np.floor(nume / deno)
    acc = accuracy_score(y_test, y_pred)
    print(f"Score with ensemble = {acc}")
