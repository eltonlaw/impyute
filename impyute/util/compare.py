"""impyute.util.compare.py"""
import importlib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# pylint: disable=too-many-locals
# pylint: disable=dangerous-default-value


def compare(imputed, classifiers=["sklearn.svm.SVC"], log_path=None):
    """
    Given an imputed dataset with labels and a list of supervised machine
    learning model, find accuracy score of all model/imputation pairs.

    Parameters
    ----------
    imputed: [(str, np.ndarray), (str, np.ndarray)...]
        List of tuples containing (imputation_name, imputed_data) where
        `imputation_name` is a string and `imputed_data` is a tuple where
        `imputed_data`[0] is the data, X and `imputed_data`[1] is the label, y
    classifiers: [str, str...str] (optional)
        Provide a list of classifiers to run imputed data sets on. Right now,
        it ONLY works with sklearn, the format should be like so:
        `sklearn.SUBMODULE.FUNCTION`. More generally its
        'MODULE.SUBMODULE.FUNCTION'. If providing a custom classifier, make
        sure to add the file location to sys.path first and the classifier
        should also be structured like sklearn (with a `fit` and `predict`
        method).
    log_path: str (optional)
        To write results to a file, provide a relative path

    Returns
    -------
    results.txt
        Classification results on imputed data

    """
    clfs = []
    for clf_name in classifiers:
        mod_name, smod_name, fn_name = clf_name.split(".")
        try:
            mod = importlib.import_module("{}.{}".format(mod_name, smod_name))
            fn = getattr(mod, fn_name)
            clfs.append([fn_name, fn])
        except ModuleNotFoundError:
            print("Cannot import '{}' from '{}.{}'".format(fn_name,
                                                           mod_name,
                                                           smod_name))

    results = {imputation_name: [] for imputation_name, _ in imputed}

    for imputation_name, data in imputed:
        X, y = data
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            test_size=0.33,
                                                            random_state=0)
        print("Imputation {} =========".format(imputation_name))
        for clf_name, clf in clfs:
            clf = clf()
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            results[imputation_name].append((clf_name, accuracy))
            print("...{}".format(clf_name))

    # If not None, write to path
    if log_path:
        with open(log_path, 'w') as f:
            f.write(str(results))
        print("Results saved to {}".format(log_path))

    return results
