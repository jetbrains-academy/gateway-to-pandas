import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def process_ted_talks(filename):
    df = pd.read_csv(filename)
    df = df.fillna('')

    df['content'] = df['description'] + ' ' + df['event'] +\
        ' ' + df['main_speaker'] + ' ' + df['name'] + \
        ' ' + df['speaker_occupation'] + \
        ' ' + df['tags'] + ' ' + df['title']

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['content'])

    return X
