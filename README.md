# ReviewSense — Customer Feedback Analysis

NLP pipeline built during my internship at Infosys Springboard. Processes large-scale customer review datasets and extracts product-level sentiment trends, keyword patterns, and business insights.

---

## What it does

Raw customer reviews are messy and unstructured. ReviewSense takes that raw text and turns it into something a product team or business analyst can actually use — sentiment scores by product, keyword frequency trends, and structured summaries organised by topic.

---

## Pipeline

```
Raw reviews (CSV)
      ↓
Text preprocessing (lowercasing, stopword removal, lemmatisation)
      ↓
TF-IDF keyword extraction
      ↓
Sentiment scoring (per review + aggregated per product)
      ↓
Topic modelling (LDA)
      ↓
Structured BI report output
```

---

## Tech stack

| Component | Technology |
|-----------|------------|
| Text preprocessing | NLTK · regex |
| Keyword extraction | TF-IDF (Scikit-learn) |
| Sentiment analysis | VADER · custom scoring |
| Topic modelling | LDA (Gensim) |
| Data handling | Pandas · NumPy |
| Output | Structured CSV + summary report |

---

## Run it

```bash
git clone https://github.com/SArora2712/Infosys_ReviewSense.git
cd Infosys_ReviewSense
pip install -r requirements.txt
python main.py --input data/reviews.csv --output results/
```

---

## Sample output

The pipeline produces:
- Sentiment score per review (positive / negative / neutral)
- Aggregated sentiment per product category
- Top-N keywords per category using TF-IDF
- Topic clusters with representative keywords
- Summary report in structured format

---

## Internship context

This was my core deliverable at Infosys Springboard. The goal was to give non-technical stakeholders a way to understand what customers were saying across thousands of reviews without reading them manually. The TF-IDF + sentiment approach works well for this — it's fast, interpretable, and doesn't need a GPU.

---

*Python · NLP · TF-IDF · Sentiment Analysis · Infosys Springboard Internship*
