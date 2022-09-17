import pandas as pd
from nltk.tokenize import word_tokenize

def remove_punctuation(df, column="text"):
    import string
    df[column] = df[column].apply(lambda review: review.translate(str.maketrans('', '', string.punctuation)))
    return df

def to_lowercase(df, column="text"):
    df[column] = df[column].apply(lambda review: review.lower())
    return df

def preprocess_df(df, column="text"):
    # TODO: remove stopwords, HTML tags, URLs and non-alphanumeric characters from the dataset using regex
    return to_lowercase(remove_punctuation(df, column), column)


def remove_stopwords(text, stopWords):
    words = word_tokenize(text)
    wordsFiltered = [w for w in words if w not in stopWords]
    return " ".join(wordsFiltered)
