## 0.0.9

- Fix `fast_knn` incorrect weighting bug. Replaced distance weighting with inverse distance weighting and ability to swap in custom function (arg: 1D list of distances, ret: 1D list of weight percentages). New namespace created `impyute.util.inverse_distance_weighting` for functions that can be modified with custom args using `functool.partial` (check test for more details). 
- pybase dockerfile bug fixes
- 
