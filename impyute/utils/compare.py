"""impyute.utils.compare.py"""
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# pylint: disable=too-many-locals
def compare(imputed, log_path="results.txt"):
    """ Given an imputed dataset, runs a bunch of machine learning algorithms

    Parameters
    ----------
    imputed: [(str, np.ndarray), (str, np.ndarray)...]
       List of tuples containing (imputation algorithm name, imputed data)

    Returns
    ------
    results.txt
        Classification results on imputed data

    """
    clfs = [["SVC", SVC()],
            ["KNeighbours", KNeighborsClassifier(2)],
            ["GaussianNB", GaussianNB()],
            ["RandomForestClassifier", RandomForestClassifier()]]

    results = {imputation_name: [] for imputation_name, _ in imputed}

    for imputation_name, data in imputed:
        X, y = data
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            test_size=0.33,
                                                            random_state=42)
        print("Imputation {} =========".format(imputation_name))
        for clf_name, clf in clfs:
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            results[imputation_name].append((clf_name, accuracy))
            print("...{}".format(clf_name))

    with open(log_path, 'w') as f:
        f.write(str(results))
    print("Results saved to {}".format(log_path))
