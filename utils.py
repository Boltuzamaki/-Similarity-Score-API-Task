import pandas
import numpy as np
import nltk 
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def process_sentence(sentence):
    """
    Function to clean senetence by removing stopwords and lowercasing all words 
    Args:
        sentence: A string (sentence)
    Output:
        returns cleaned sentence 
    """
    word_list = word_tokenize(sentence)
    filtered_words = [word.lower() for word in word_list if word not in stopwords.words('english')]
    return ' '.join(filtered_words)

def cosine_similarity_calc(vector_1,vector_2):
    """
    Function to find cosine similarity
    Args:
        vector_1: Sentence vector one sentence 
        vector_2: Sentence vector of second sentence
    Output:
        Returns co-sine similarity of two sentence 
    """
    similarity = np.dot(vector_1,vector_2)/(np.linalg.norm(vector_1)*np.linalg.norm(vector_2))
    return round(similarity, 3)

def avg_feature_vector(sentence, embedding_dict, num_features):
    """
    Function which use word2vec and create sentence vector by averaging word vector of all words in a sentence 
    Args:
        sentence: A string(sentence)
        embeddin_dict: A dictionary of pretrained embedding 
        num_features: Number of features present in the embedding 
    Output:
        Return sentence vector
    """
    sentence = process_sentence(sentence)
    words = word_tokenize(sentence)
    feature_vec = np.zeros((num_features, ), dtype='float32')
    n_words = 0
    word_list = list(embedding_dict.keys())
    for word in words:
        if word in word_list:
            n_words += 1
            feature_vec = np.add(feature_vec, embedding_dict[word])
    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec