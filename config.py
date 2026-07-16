from pathlib import Path

# =============================================================================
# Project Root
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent

# =============================================================================
# Data Directories
# =============================================================================

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = DATA_DIR / "outputs"

# =============================================================================
# Project Directories
# =============================================================================

NOTEBOOKS_DIR = BASE_DIR / "notebooks"
SCRIPTS_DIR = BASE_DIR / "scripts"
DOCS_DIR = BASE_DIR / "docs"
IMAGES_DIR = BASE_DIR / "images"