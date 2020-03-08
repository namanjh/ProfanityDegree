#importing the libraries
import requests
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import pandas as pd

#downloading profane word list
def get_profane_list(url):
    req = requests.get(url, allow_redirects = False)
    open(r'profane_list.txt','wb').write(req.content)


#list of profanity list
def read_profane_list():
    list_file = open(r'profane_list.txt', 'r')
    profanity_list= []
    profanity = list_file.readlines()
    for each in profanity:
        profanity_list.append(each.strip())
    return profanity_list

#reading the comments file line by line
def get_facebook_comments():
    comment_file = open(r'facebook_comments.txt', 'r')
    lines = comment_file.read().splitlines()
    return lines
    
#function to remove punctutation from the text
def remove_punctuation(text):
    no_punctuation = "".join([c for c in text if c not in string.punctuation])
    return no_punctuation

#removing words that donot provide any meaningful sentiment
def remove_stopwords(text):
    words = [w for w in text if w not in stopwords.words('english')]
    return words

#generating root for of the word
def word_lemmatizer(text):
    lem_text = [lemmatizer.lemmatize(word) for word in text]
    return lem_text

def word_stemmer(text):
    stem_text = " ".join([stemmer.stem(i) for i in text])
    return stem_text

'''4 steps in clean comments:
    1. remove punctuations
    2. Tokenize the comments
    3. Remove stop words
    4. Stemming & lemmatizing'''
    
def clean_comments(raw_comments):
    raw_comments['comment'] = raw_comments['comment'].apply(lambda x: remove_punctuation(x))
    
    raw_comments['comment'] = raw_comments['comment'].apply(lambda x: tokenizer.tokenize(x))
    
    raw_comments['comment'] = raw_comments['comment'].apply(lambda x: remove_stopwords(x))
    
    raw_comments['comment'] = raw_comments['comment'].apply(lambda x: word_lemmatizer(x))
    raw_comments['comment'] = raw_comments['comment'].apply(lambda x: word_stemmer(x))
    
    return raw_comments

def calculate_degree(comment, profane_list):
    degree_of_profanity = sum(1 for word in comment if word in profane_list) / len(comment)
    return degree_of_profanity

def calculate_profanity_degree(clean_comments, profane_list):
    profanity_df = pd.DataFrame()
    profanity_df['comment'] = clean_comments['comment'].apply(lambda x: tokenizer.tokenize(x))
    profanity_df['degree'] = profanity_df['comment'].apply(lambda x: calculate_degree(x, profane_list))
    return profanity_df

url = 'https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt'
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'\w+')

get_profane_list(url)
profane_list = read_profane_list()
raw_comment_list = get_facebook_comments()
raw_comment_df = pd.DataFrame(raw_comment_list, columns = ['comment'])
clean_comments = clean_comments(raw_comment_df)

print(clean_comments.head())

final_df = pd.DataFrame()
final_df = calculate_profanity_degree(clean_comments, profane_list)

print(final_df.head())
