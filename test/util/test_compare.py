"""test_compare.py"""
import numpy as np
import impyute as impy

mask = np.zeros((5, 5), dtype=bool)
mask[0][0] = True
data_m = impy.dataset.test_data(mask=mask)
labels = np.array([1, 0, 1, 1, 0])
imputed_mode = []
imputed_mode.append(["mode", (impy.mode(np.copy(data_m)), labels)])
imputed_mode.append(["mean", (impy.mean(np.copy(data_m)), labels)])

def test_output_file_exists():
    """ Small test to just check that it runs without fialing"""
    path = "./results.txt"
    impy.util.compare(imputed_mode, log_path=path)
