<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# \# News Category Classification

A complete end-to-end notebook for classifying news articles into four categories (World, Sports, Business, Sci/Tech) using the AG News dataset. The project demonstrates data loading, preprocessing (cleaning + lemmatization), TF‑IDF feature extraction, classical ML (Logistic Regression, LightGBM) with hyperparameter search, and a feed‑forward neural network (TensorFlow/Keras). Visualizations (word clouds, coefficient bar chart) and evaluation reports are included.

Live demo : [https://news-category-classification-zzmfsj23xhyrlthxynyet8.streamlit.app/](https://news-category-classification-zzmfsj23xhyrlthxynyet8.streamlit.app/)

## Features

- Data cleaning and lemmatization using NLTK
- TF‑IDF feature extraction
- Model selection and hyperparameter tuning (Logistic Regression, LightGBM)
- Feed‑forward neural network with TF‑IDF input
- Word clouds and feature importance visualization
- Classification reports and evaluation utilities
- Streamlit UI demo for interactive sentiment analysis


## Project Structure

- `model.pkl` `vectorizer.pkl` - model and vectorizer files
- `News Category Classification.ipynb` - Jupyter Notebook containing preprocessing, training, and evaluation pipeline
- `app.py` - Streamlit application script for live sentiment analysis
- `requirements.txt` - Required Python packages
- `README.md` - Project overview and usage instructions


## Installation

1. Clone the repository:
``` powershell
git clone [https://github.com/MohamedGamal04/News-Category-Classification.git](https://github.com/MohamedGamal04/News-Category-Classification.git)
cd News-Category-Classification
```

2. Create a Python environment and activate it (recommended):
``` powershell
conda create -n classify-env python=3.8
conda activate classify-env
```

3. Install dependencies:
``` powershell
pip install -r requirements.txt
```

4. Download necessary NLTK data resources:
``` python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
```

Run required NLTK downloads in the notebook (cells include downloads for punkt, stopwords, wordnet, averaged_perceptron_tagger).

## Usage

- Train the model and evaluate using the Jupyter Notebook.
- To use the Streamlit app (once created and set up), run:

``` terminal
streamlit run app.py
```

- The Streamlit UI allows you to enter reviews manually or upload CSV files for batch prediction.


## Dataset

This project uses the [AG news classification dataset](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset).

edit this to match my NER project

Here is an edited version of the news category classification project description, tailored to match your Named Entity Recognition (NER) project:

***

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

1. Clone the repository:
```powershell
git clone <your-repo-url>
cd <your-repo-folder>
```

2. Create and activate a Python environment (recommended):
```powershell
conda create -n ner-env python=3.8
conda activate ner-env
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Download the dataset files and place them in the expected folder (data loading paths specified in the notebook).

## Usage

- Run the notebook to train NER models and evaluate their performance.
- Visualize sample entity extractions inline using spaCy's displaCy.
- Save and load custom trained models for prediction on new data.


## Dataset

This project uses the CoNLL-2003 style English dataset for Named Entity Recognition, downloaded via Kaggle from the alaakhaled/conll003-englishversion dataset.

***

Let me know if you want this shortened or expanded, or adapted to another style.
<span style="display:none">[^1]</span>

<div align="center">⁂</div>

[^1]: Named-Entity-Recognition-NER-from-News-Articles.ipynb

