import pandas as pd
import string
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

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

def preprocess_text(text) : 
    # Removing the punctuation 
    text = text.translate(str.maketrans('', '', string.punctuation))
    print(text)
    # Changing to lowercase
    text = text.lower()

    # Removing the stop words 
    text = remove_stopwords(text, stopwords)
    
    return text    

def remove_stopwords(text, stopWords):
    words = word_tokenize(text)
    wordsFiltered = [w for w in words if w not in stopWords]
    return " ".join(wordsFiltered)
