from hazm import POSTagger,Normalizer
import requests
from bs4 import BeautifulSoup, Comment
import re


def handle_ha(word_list,word):
    if word == 'ها' or word =='های' or word=='هایی':
        return word
    else:
        if word[len(word)-2:] == u'ها' and word[len(word)-3] != u'‌':
            if  word[:len(word)-2] + u'‌' + word[len(word)-2:] in word_list:
                return word[:len(word)-2] + u'‌' + word[len(word)-2:]
            else:
                return word
        elif word[len(word)-3:] == u'های' and word[len(word)-4] != u'‌':
            if  word[:len(word)-3] + u'‌' + word[len(word)-3:] in word_list:
                return word[:len(word)-3] + u'‌' + word[len(word)-3:]
            else:
                return word
        elif word[len(word)-4:] == u'هایی' and word[len(word)-5] != u'‌':
            if  word[:len(word)-4] + u'‌' + word[len(word)-4:] in word_list:
                return word[:len(word)-4] + u'‌' + word[len(word)-4:]
            else:
                return word
        else:
            return word



def handle_mi(word_list,word):
    if word=='می':
        return word
    else:
        if word[:2] == u'می' and  word[2] != u'‌':
            if word[:2] + u'‌' + word[2:] in word_list:
                return word[:2] + u'‌' + word[2:]
            elif u'نمی‌' + word[2:] in word_list:
                return word[:2] + u'‌' + word[2:]
            else:
                return word
        elif word[:3] == u'نمی' and  word[2] != u'‌':
            if word[:3] + u'‌' + word[3:] in word_list:
                return word[:3] + u'‌' + word[3:]
            elif u'می‌' + word[3:] in word_list:
                return word[:3] + u'‌' + word[3:]
            else:
                return word
        else:
            return word

def step1_tokenize(to_send):
    args = {}
    args['text'] = to_send
    args['dontCorrectInsideQuote'] = 'false'
    args['correctDelimOnly'] = 'false'
    args['goToSegmentor'] = 'false'
    args['firstCaseOnly'] = 'false'
    args['correctCompoundWords'] = 'true'
    r = requests.post("http://step1.nlp.sbu.ac.ir/services/Service.asmx/Tokenize", data=args)
    print(r.status_code)
    results = r.text
    tokens = []
    bs = BeautifulSoup(results,features='html5lib')
    word_tags = bs.find_all('word')
    morph_tags = bs.find_all('morph')
    for i in range(len(word_tags)):
        word = word_tags[i].text
        to_add = []
        if word.isspace():
            continue
        else:
            to_add.append(word)
            to_add.append(morph_tags[i].find('tag').text)
            tokens.append(to_add)
    return tokens



def sentences(token_and_tags):
    cut_pos = []
    for i in range(len(token_and_tags)):
        if re.match(r"V[0-9]+", token_and_tags[i][1]):
            if i + 1 < len(token_and_tags) and  token_and_tags[i + 1][1] == 'endDelim' and token_and_tags[i + 1][0] != "«" :
                cut_pos.append(i + 1)
            else:
                cut_pos.append(i)
        elif i == len(token_and_tags) - 1:
            cut_pos.append(i)
    return cut_pos
    
