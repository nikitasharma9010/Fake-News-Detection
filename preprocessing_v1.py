from imports import *

custom_stopwords = ['subject','from','re','use','edu']
customized_stopwords = stopwords.words('english') + custom_stopwords

def tokenize_v1(text):
    global customized_stopwords
    
    tokens = []
    
    # for every token in preprocessed text,
    for token in simple_preprocess(text):
        
        # donot add to list of tokens if token is a stopword
        if token not in STOPWORDS and len(token) > 3 and token not in customized_stopwords:
            tokens.append(token)
    
    return tokens

