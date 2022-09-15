import pandas as pd

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
