Suspicious Fake News Analyzer(SUFNA)

Data source : Kaggle

Tools and Libraries : Jupyter notebook, Pandas, numpy, sklearn(Logistic Model, Vectorizer(TfidfVectorizer),metrics)

Execution

A machine learning system  was built to detect the likelihood of a news being fake using Natural Language Processing(NLP).

First, each news article was converted into numerical features using TF-IDF, which measures how important each word is in a document relative to the dataset.
TF-IDF measures how important a word is in a document relative to the whole dataset.
Words that appear frequently in one article but not across many articles get higher weights, allowing the model to focus on meaningful signals instead of common words.

The vocabulary was limited to the most informative 5000 words to reduce noise and improve efficiency.

Then Logistic Regression classifier was trained on the dataset to learn how strongly each word indicates fake or real news.

For example, words like “said” strongly indicate real news, while sensational words like “video” or “just” tend to indicate fake news.

By combining these weighted signals, the model predicts whether an article is fake or real.

The model achieved around 97.71% accuracy, showing that linguistic patterns can effectively distinguish reliable reporting from misinformation.

Summary
* TF-IDF converts articles into numerical features
* Logistic Regression learns which words indicate fake or real news
* Each word contributes a weighted vote toward the final prediction

