# Named Entity Recognition (NER) from News Articles

A complete end-to-end Jupyter Notebook for training and evaluating custom spaCy Named Entity Recognition (NER) models on news articles using the CoNLL-2003 style dataset. The project demonstrates data loading, preprocessing, formatting data for spaCy, training both small and medium spaCy models, evaluation on test sets, and visualization of extracted named entities using displaCy.

## Features
- Data loading and parsing from CoNLL-2003 style text files
- Conversion of BIO-tagged tokens to spaCy training format
- Training custom spaCy NER models (small and medium)
- Validation and test evaluation with entity-level accuracy
- Visualization of recognized entities with spaCy's displaCy tool
- Performance metrics presented for model comparison

## Project Structure
- `Named-Entity-Recognition-NER-from-News-Articles.ipynb` - Jupyter Notebook with full pipeline from data loading, preprocessing, training, evaluating, and visualization
- Saved custom models (small and medium) for inference and testing

## Installation
1. Create and activate a Python environment (recommended):
```powershell
conda create -n ner-env python=3.8
conda activate ner-env
```
2. Install dependencies:
```powershell
pip install -r requirements.txt
```
3. Download the dataset files and place them in the expected folder (data loading paths specified in the notebook).

## Usage
- Run the notebook to train NER models and evaluate their performance.
- Visualize sample entity extractions inline using spaCy's displaCy.
- Save and load custom trained models for prediction on new data.

## Dataset
This project uses the CoNLL-2003 style English dataset for Named Entity Recognition, downloaded via Kaggle from the alaakhaled/conll003-englishversion dataset.

***

Let me know if you want this shortened or expanded, or adapted to another style.

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/68559943/727997e0-8235-4888-9d7e-2b84354755f2/Named-Entity-Recognition-NER-from-News-Articles.ipynb)
