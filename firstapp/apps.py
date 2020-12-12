from django.apps import AppConfig
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib


class FirstappConfig(AppConfig):
    name = 'firstapp'

class ML:
    def __init__(self):
        self.vectorizer = joblib.load(r'C:\Users\duran\Python Projects\test_proj\hello\firstapp\models\vectorizer.pkl')
        self.classificator = joblib.load(r'C:\Users\duran\Python Projects\test_proj\hello\firstapp\models\RFC.pkl')

    def text_preprocessing(self, input_text):
        review = re.sub('[^a-zA-Z]', ' ', input_text)
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)

        return review

    