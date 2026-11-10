# Dependencies

The analysis was run with the versions below (Linux, CPU only). Packages were installed from conda-forge, except
harmonypy and scikit-misc, which were installed from PyPI.

| package | version | used for |
|---|---|---|
| Python | 3.12.14 | |
| scanpy | 1.12.3 | normalisation, highly variable genes, PCA, neighbour graph, UMAP, Wilcoxon test, gene scores, dot plot |
| anndata | 0.13.2 | data objects (`.h5ad` files) |
| harmonypy | 2.0.0 | Harmony batch correction |
| scikit-misc | 0.5.2 | needed by scanpy for the `seurat_v3` highly-variable-gene method |
| scikit-learn | 1.9.0 | nearest-neighbour label transfer |
| umap-learn | 0.5.12 | UMAP (through scanpy) |
| pynndescent | 0.6.0 | neighbour search (through scanpy) |
| numba | 0.67.0 | used by umap-learn and pynndescent |
| numpy | 2.5.2 | arrays |
| pandas | 3.0.5 | tables |
| scipy | 1.18.0 | sparse matrices, Spearman correlation, Wilcoxon signed-rank test, Benjamini–Hochberg adjustment |
| h5py | 3.16.0 | reading and writing `.h5ad` files |
| matplotlib | 3.11.1 | figures |
| seaborn | 0.13.2 | figures |
| jupyterlab | 4.6.3 | running the notebooks |
| ipykernel | 7.3.0 | running the notebooks |

Reference data: FlyBase release FB2026_02 (gene identifiers and synonyms).
