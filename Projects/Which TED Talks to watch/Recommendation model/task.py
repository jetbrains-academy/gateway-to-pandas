import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def load_data(path):
    df = pd.read_csv(path)
    df = df.fillna('')
    df['content'] = df['description'] + ' ' + df['event'] + \
                    ' ' + df['main_speaker'] + ' ' + df['name'] + \
                    ' ' + df['speaker_occupation'] + \
                    ' ' + df['tags'] + ' ' + df['title']
    return df


def compute_cosine_similarities(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['content'])
    cosine_similarities = linear_kernel(X, X)
    return cosine_similarities


def get_recommendations(title, df, cosine_similarities):
    # Get the index of the TED Talk
    idx = df[df['title'] == title].index[0]
    # Get the pairwise similarity scores
    sim_scores = list(enumerate(cosine_similarities[idx]))
    # Sort the TED Talks based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar TED Talks
    sim_scores = sim_scores[1:11]
    # Get the TED Talk indices
    talk_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[talk_indices]  # Return the top 10 most similar TED Talks


if __name__ == "__main__":
    df = load_data('../Introduction/ted_main.csv')
    cosine_similarities = compute_cosine_similarities(df)
    print(get_recommendations('The power of vulnerability', df, cosine_similarities))
