# Drosophila AML integration

Single-cell RNA-seq analysis of hemocytes from two *Drosophila* leukemia models (AML1-ETO and RasV12, with their
control), compared with seven published larval hemocyte datasets.

Paper: [title, authors, journal, DOI — to add]


## Notebooks
| # | notebook | function |
|---|---|---|
| 01 | `01_build_atlas.ipynb` | joins the published datasets and the leukemia dataset into one count matrix (FlyBase gene IDs); removes cells with 200 or fewer detected genes and cells without a published label; normalises |
| 02 | `02_integration.ipynb` | selects 2,000 highly variable genes from the unperturbed control cells; PCA, Harmony and UMAP of the circulating cells |
| 03 | `03_label_transfer.ipynb` | gives every other circulating cell the AML cluster it resembles most (vote of the 30 nearest AML cells, distance cutoff, refinement of split votes) |
| 04 | `04_cluster_profiles.ipynb` | correlates the expression profiles of the AML clusters with published cell types; finds the PM4 signature genes |
| 05 | `05_leukemia_vs_control.ipynb` | finds genes that differ between each leukemia arm and the control arm, for whole arms and within clusters |
| 06 | `06_figures.ipynb` | draws every figure and saves the plotted values |

`settings.py` holds what the notebooks share: where the data are, the names of the files passed from one notebook
to the next, the AML cluster names and the random seed.


## Data
The count data are not in this repository. Public datasets were placed as following:

```
data/
  raw/
    GSE325999/                            GSE325999_matrix_GEO.txt.gz, GSE325999_metadata_GEO.txt.gz
    GSE184781/                            GSE184781_matrix.mtx.gz, GSE184781_barcodes.tsv.gz, GSE184781_genes.tsv.gz
    yoon_integrated_figshare_24014010/    barcodes.tsv.gz, genes.tsv.gz, matrix.mtx.gz, metadata.txt
    yoon_w1118_10x_figshare_16585805/     metadata.txt
  reference/
    flybase_fb_2026_02/                   fbgn_annotation_ID_fb_2026_02.tsv.gz, fb_synonym_fb_2026_02.tsv.gz
```

| folder | source |
|---|---|
| `GSE325999` | leukemia dataset of this study (AML1-ETO, RasV12, control): https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE325999 |
| `GSE184781` | 10x *w1118* hemocytes of Yoon et al. 2023: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE184781 |
| `yoon_integrated_figshare_24014010` | Yoon et al. 2023, integrated larval hemocyte data of six published studies: https://doi.org/10.6084/m9.figshare.24014010 |
| `yoon_w1118_10x_figshare_16585805` | Yoon et al. 2023, metadata of the 10x *w1118* hemocytes (only `metadata.txt` is used): https://doi.org/10.6084/m9.figshare.16585805 |
| `flybase_fb_2026_02` | FlyBase release FB2026_02: https://s3ftp.flybase.org/releases/FB2026_02/precomputed_files/genes/fbgn_annotation_ID_fb_2026_02.tsv.gz and https://s3ftp.flybase.org/releases/FB2026_02/precomputed_files/synonyms/fb_synonym_fb_2026_02.tsv.gz |

Three small tables for result reproducibility are in `inputs/`:

| file | content |
|---|---|
| `samples.tsv` | each sample's library name in the Yoon et al. data, dataset, experiment, condition (control, wasp, injury, selected_uninfected, AML1-ETO, RasV12), compartment, technology, and the Harmony batch (the sample's matched control experiment) |
| `published_labels.tsv.gz` | the cluster label that each original study published for its cells, and where the label was taken from|
| `umap_start_positions.tsv.gz` | starting positions for the UMAP of notebook 02 used for coherent representation|



## Licence and citation

The code is released under the MIT licence (`LICENSE`). If you use it, please cite the paper above and the
datasets and packages it builds on (Yoon et al. 2023 and the six studies of its integrated data; Scanpy;
Harmony; scikit-learn).
