import re
from collections import defaultdict

import nltk 
from nltk.util import ngrams


class MarkovChain(object):
    def __init__(self, ngram_size=2, divider_token='^'):
        self.n = ngram_size
        self.transition_probabilities = defaultdict(nltk.FreqDist)
        self.divider_token = divider_token
        
    def tokenize_sentence(self, sentence):
        sentence = sentence.lower()
        sentence = (self.divider_token + ' ') * self.n + sentence + (' ' + self.divider_token) * self.n
        word_tokenized = nltk.tokenize.word_tokenize(sentence)
        return list(ngrams(word_tokenized,  self.n))
    
    def train_sentence(self, sentence):
        tokenized = self.tokenize_sentence(sentence.decode('utf-8'))
        # Annoyting utf8 hijinx
        tokenized = map(lambda x: tuple(map(lambda y: y.encode('utf-8'), x)), tokenized)
        num_tokens = len(tokenized)
        for i, token in enumerate(tokenized):
            if i < num_tokens - 1:
                next_token = tokenized[i + 1]
                self.transition_probabilities[token][next_token[self.n - 1:]] += 1
    
    def _get_sentence_starter(self):
        return self.n * (self.divider_token,)
    
    def get_next(self, current, weighted_by_probability=False):
        
        next_freq = self.transition_probabilities[current]
        
        if weighted_by_probability:
            prob_dist = nltk.MLEProbDist(next_freq)
            return prob_dist.generate()
        else:
            prob_dist = nltk.UniformProbDist(next_freq)
            return prob_dist.generate()
    
    def _clean_sentence(self, generated_sentence):
        cleaned = ' '.join(generated_sentence[self.n:-self.n])
        cleaned = cleaned.capitalize()
        cleaned = re.sub(' (\W)', r'\1', cleaned) # Remove space before punct
        return cleaned
    
    def generate_sentence(self, max_words=100, weighted_by_probability=False):

        sentence = current = start = self._get_sentence_starter()
        count = 0
        while True:
            count += 1

            next_token = self.get_next(current)
            sentence = sentence + next_token
            current = sentence[-self.n:]            
            if current == start or count > max_words:
                break
        return self._clean_sentence(sentence)