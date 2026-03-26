import re
import string 
import nltk
# nltk.download()
# nltk.download('stopwords')
# nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

def clean_data(text: str) -> str:
    '''
    Function takes in a string, 
    returns the cleaned string by convering to 
    lowercase, and removing punctuation and numbers.
    '''
    # Convert to lowercase
    text_lower = text.lower()

    # Remove punctuation and numbers 
    pattern = r'[0-9' + re.escape(string.punctuation) + r']'
    text_no_punc_no_nums = re.sub(pattern, '', text_lower)

    return text_no_punc_no_nums


def preprocess_data(text: str) -> list:
    '''
    Functionn takes in a string, 
    returns the pre-processed string by 
    performing tokenization, stopword removal, 
    and lemmatization.
    '''
    # Tokenization 
    text_tokenized = word_tokenize(text)

    # Stopword removal
    stop_words = set(stopwords.words('english'))
    stop_words.add('reuters') # Remove the common word in all real articles
    text_no_stopwords = [word for word in text_tokenized if word not in stop_words]

    # Lemmatization 
    lemmatizer = WordNetLemmatizer()
    text_lemmatized = [lemmatizer.lemmatize(word) for word in text_no_stopwords]
    final_cleaned = [word for word in text_lemmatized if len(word) > 1]
    return final_cleaned