## 0.0.9

- Fix `fast_knn` incorrect weighting bug. Replaced distance weighting with inverse distance weighting and ability to swap in custom function (arg: 1D list of distances, ret: 1D list of weight percentages). New namespace created `impyute.util.inverse_distance_weighting` for functions that can be modified with custom args using `functool.partial` (check test for more details). 
- pybase dockerfile bug fixes
- New `contrib` folder created and some of the utilities from `util` moved there:
    * `impyute.util.compare -> `impyute.contrib.compare`
    * `impyute.util.count_missing` -> `impyute.contrib.count_missing`
    * `impyute.util.describe` -> `impyute.contrib.describe`
- Util namespace breaking changes
    * impyute.util.find_null->impyute.ops.matrix.nan_indices
    * impyute.util.preprocess->impyute.ops.wrapper.wrappers
    * impyute.util.checks->impyute.ops.wrapper.checks
    * impyute.util.BadInputError -> impyute.ops.errors.BadInputError
    * impyute.util.BadOutputError -> impyute.ops.errors.BadOutputError
