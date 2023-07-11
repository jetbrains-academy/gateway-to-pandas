# Preprocessing 
Let's discuss the general concept of a content-based recommendation system. It uses the content of items to recommend other items that are similar. In our case, we are going to recommend TED Talks based on the similarity of their content, such as speaker, tags, themes and etc. To accomplish this, we need to compute similarities and then rank TED Talks based on these similarities. We will then write a function that outputs recommendations for a given TED Talk.

So the first task is converting the content of the items (in our case, `TED Talks`) into a form that the algorithm can understand. 
For instance, we could convert the tags, themes, and speaker's name into a string for each TED Talk and then convert the strings into vectors.

## How to convert text into numbers?
One of the original and straightforward methods for transforming texts into numerical values is `TF-IDF`. It's used to convert a collection of raw documents to a matrix of `TF-IDF` features. Let's break this down:
 - TF (Term Frequency): this summarizes how often a given word appears within a document
 - IDF (Inverse Document Frequency): this downscales words that appear a lot across documents. A word that appears in many documents will not be a good keyword to categorize these documents because it does not help differentiate them

`TF-IDF` are word frequency scores that try to highlight words that are more interesting, such as frequent in a document but not across documents. The `TF-IDF` value increases proportionally to the number of times a word appears in the document, but is offset by the frequency of the word in the corpus, which helps to adjust for the fact that some words appear more frequently in general.

In `sklearn` the TfidfVectorizer converts a collection of raw documents into a matrix of TF-IDF features. It's equivalent to CountVectorizer followed by TfidfTransformer.

Here's a simple usage of TfidfVectorizer:
```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.shape)
```
Output:
```python
['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
(4, 9)
```
The resulting matrix `X` is a sparse matrix where each row corresponds to a document and each column corresponds 
to a word in all the documents. The value in each cell in the matrix is the `TF-IDF` value of the word 
in the corresponding document.

# Task
Use the `TfidfVectorizer` to fit the vectorizer on the `df['content']`. 

**Important Note:** Please ensure that you have successfully downloaded the `ted_main.csv` data file in the previous task.
