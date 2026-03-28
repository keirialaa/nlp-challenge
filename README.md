# NLP Challenge: Fake News Detector

## Overview
This project classifies news articles as **Real (1)** or **Fake (0)**. The goal was to build a model that understands journalistic style rather than just memorizing keywords.

## Technical Stack
- **Language:** Python 3.13
- **Environment:** Virtual Environment (`.venv`)
- **Libraries:** Pandas, Scikit-Learn, NLTK, Seaborn

## Methodology
1. **Cleaning:** Removed 'Reuters' tags to ensure the model learned linguistic patterns, not just publisher names.
2. **Feature Engineering:** Used TF-IDF to weigh the importance of words across the 40k+ article dataset.
3. **Training:** Utilized Logistic Regression, achieving a final accuracy of ~98%.

## How to Run
1. Activate the environment: `source .venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the notebook: `jupyter notebook main.ipynb`

## Key Findings
The model successfully identified that formal news relies heavily on **attribution** (the word "said"), while fake news relies on **urgency** (the word "breaking").
