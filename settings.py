"""Settings shared by every notebook: where the data are, and the names used throughout the pipeline.

Folders
    CODE_DIR        this folder (the notebooks, settings.py and inputs/).
    INPUT_DIR       inputs/: the sample sheet, the published cell labels and the UMAP start positions.
    ROOT            the folder that holds data/ (see README.md). By default this folder. If the data are
                    somewhere else, write that folder's path into data_root.txt (one line) next to this file.
    PROCESSED_DIR   large files written by the pipeline (the atlas, the integration).
    RESULTS_DIR     tables and figures written by the pipeline.

RUN_NAME is the name of the output folders (data/interim/<RUN_NAME>/ and results/<RUN_NAME>/).
Running a notebook again replaces its own outputs.
"""
import os
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
INPUT_DIR = CODE_DIR / "inputs"

data_root_file = CODE_DIR / "data_root.txt"

if data_root_file.exists():
    ROOT = Path(data_root_file.read_text().strip())
else:
    ROOT = CODE_DIR

RUN_NAME = os.environ.get("PIPELINE_RUN_NAME", "paper")

PROCESSED_DIR = ROOT / "data" / "interim" / RUN_NAME
RESULTS_DIR = ROOT / "results" / RUN_NAME

# Files that one notebook writes and later notebooks read
ATLAS_FILE = PROCESSED_DIR / "atlas.h5ad"                              # notebook 01
INTEGRATION_FILE = PROCESSED_DIR / "integration_circulating.h5ad"      # notebook 02
HVG_TABLE = RESULTS_DIR / "integration" / "integration_hvgs.tsv"       # notebook 02
LABEL_TABLE = RESULTS_DIR / "label_transfer" / "labels.tsv.gz"         # notebook 03

# Names used in every notebook
AML_DATASET = "AML1ETO_RasV12"                 # the leukemia dataset (AML1-ETO, RasV12 and control arms)
AML_CLUSTERS = ["PM1", "PM2", "PM3", "PM4", "PM5", "PM6", "PM7", "PM8", "PM9", "LM1", "LM2", "CC1", "CC2"]
UNASSIGNED = "unassigned"                      # label of cells that get no AML cluster label
SEED = 0                                       # random seed of every step that uses random numbers
