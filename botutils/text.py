import re

multiple_spaces = re.compile(ur'(\s)+', re.UNICODE)
space_before_punct = re.compile(ur' (\W)', re.UNICODE)

sent_detector = None

def tokenize_sentences(text):
    global sent_detector

    if not sent_detector:
        import nltk
        # TODO: what if this is not installed?
        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

    sentences = sentences = sent_detector.tokenize(text.strip())
    sentences = map(lambda x : x.encode('utf-8'), sentences)

    return sentences


def remove_trailing_punctuation(text):
    return re.sub(r'\W+$','', text)

def remove_leading_punctuation(text):
    return re.sub(r'^\W+','', text)

def remove_space_before_punctuation(text):
    return re.sub(space_before_punct, r'\1', text)

def collapse_multiple_whitespace(text):
    return re.sub(multiple_spaces, ' ', text.replace('\n', ' ').replace('\xc2\xa0', ' '))