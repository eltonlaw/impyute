"""test_compare.py"""
import ast
import numpy as np
import impyute as impy

SHAPE = (5, 5)


def test_output_file_exists(test_data, results_path):
    data = test_data(SHAPE)
    labels = np.array([1, 0, 1, 1, 0])
    imputed_mode = []
    imputed_mode.append(["mode", (impy.mode(np.copy(data)), labels)])
    imputed_mode.append(["mean", (impy.mean(np.copy(data)), labels)])

    impy.util.compare(imputed_mode, log_path=results_path)
    with open(results_path, 'r') as fin:
        expected = {'mode': [('SVC', 0.0)], 'mean': [('SVC', 0.0)]}
        assert ast.literal_eval(next(fin)) == expected