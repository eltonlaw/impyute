## CHANGELOG

### v0.0.7

- `fast_knn`: Add parameters that can be passed to `scipy.spatial.KDTree` (`leafsize`) and `scipy.spatial.KDTree.query` (`eps`, `p`, `distance_upper_bound`). Add example usage for `fast_knn`. [(PR#38)](https://github.com/eltonlaw/impyute/pull/38)
- Support for Pandas DataFrame objects [(#PR36)](https://github.com/eltonlaw/impyute/pull/36)
- Support for python3.7 [(PR#34)](https://github.com/eltonlaw/impyute/pull/34)
- New time series imputation - Moving window imputation: `impyute.moving_window` [(PR#28)](https://github.com/eltonlaw/impyute/pull/28)
- Renamed some files/functions [(PR#23)](https://github.com/eltonlaw/impyute/pull/23)
    * `random_uniform` -> `randu`
    * `random_normal` -> `randn`
    * `impyute.deletions` -> `impyute.deletion`
    * `impyute.datasets` -> `impyute.dataset`
    * `impyute.imputations` -> `impyute.imputation`
    * `impyute.utils` -> `impyute.util`
- All imputations used to run on a pointer to the original array, changing the original. Changed behaviour run on a copy with the option of running on the original (`inplace=True`). Implementation of this is still buggy, because `inplace=True` only works if what's getting passed in truly is a pointer.  [(PR#22)](https://github.com/eltonlaw/impyute/pull/22)
