from __future__ import division
import nltk
import json
import re, pprint
import random
from nltk.book import FreqDist
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import random

raw = []

raw.append(open('ofk_chap_b.txt').read())
raw.append(open('ofk_chap_c.txt').read())
raw.append(open('ofk_chap_d.txt').read())
raw.append(open('ofk_chap_e.txt').read())


tokens_text = []
tokens_imp = []
toptokens = []
z = []
fin=[]
for i in range(4):
	tokens_text.append(nltk.word_tokenize(raw[i]))
	tokens_text[i] = [w for w in tokens_text[i] if w.isalpha()]
	tokens_imp.append([w for w in tokens_text[i] if not w in stopwords.words('english')])
	tokens_imp[i]=FreqDist(tokens_imp[i])
	toptokens.append([token for token in tokens_imp[i]])
	toptokens[i]=toptokens[i][:10]

for i in range(4):
	z.append([])
	fin.append([])
	for j in range(10):
		z[i].append(wn.synsets(toptokens[i][j]))
		z[i][j]=z[i][j][:4]
		fin[i].append([])
		for k in z[i][j]:
			fin[i][j].append(dict(size=random.randint(1,10000),name=str(k)[str(k).index('\'')+1:str(k).index('.')]))

abc=[]
for i in range(4):
	abc.append([dict(name=toptokens[i][j], children = fin[i][j]) for j in range (0,10)])

chap_title = ['CHP 1', 'CHP 2', 'CHP 3', 'CHP 4']
table_final = [dict(name=chap_title[i], children=abc[i]) for i in range(0,4)]
tab = dict(name="Once and Future King",children = table_final)

with open("final" + ".json",'w') as outfile:
	json.dump(tab, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
