"""This .py file preps incoming data"""

import pandas as pd
import re
import string

from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ' '.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def preprocess(text):
    text = strip_tags(text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text
