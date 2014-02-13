from __future__ import division
import nltk
import json
import re, pprint
import random
#from nltk.book import *
from nltk.corpus import PlaintextCorpusReader

def dump_json(dictz,position):
	tokens_table = []
	temp = {'Pronoun': ['PRP','PRP$','WP', 'POS'], 'Verb':['VBG','VBN','VBD','VBZ','VB'], 'Determiner':['DT','WDT'], 'Adjective':['JJ','JJR','JJS'], 'Noun':['NNP','NNPS','NNS','NN'], 'Particle':['RP'], 'Adverb':['WRB','RB','RBR','RBS'],'Conjuction':['CC'], 'Numeral':['CD'], 'Preposition':['IN','TO']}
	for j in range(4):
		for k in temp:
			q=0
			for i in temp[k]:
				q+=len(position[j][i])
			tokens_table.append(dict(catalog = q*100, name=k+" in Chapter "+str(j+1), percentage=(j+1)*24))

	with open("tokens.json",'w') as outfile:
		json.dump(tokens_table,outfile, sort_keys = True, indent = 4, ensure_ascii = False)


raw1 = open('ofk_chap_b.txt').read()
raw2 = open('ofk_chap_c.txt').read()
raw3 = open('ofk_chap_d.txt').read()
raw4 = open('ofk_chap_e.txt').read()



tokens_raw1 = nltk.word_tokenize(raw1)
tokens_raw2 = nltk.word_tokenize(raw2)
tokens_raw3 = nltk.word_tokenize(raw3)
tokens_raw4 = nltk.word_tokenize(raw4)

tokens_text = [tokens_raw1,tokens_raw2, tokens_raw3, tokens_raw4]
z = []
for i in range(4):
	z.append(nltk.pos_tag(tokens_text[i]))

dictz = []
position = []

for i in range(4):
	dictz.append(dict(z[i])) #analogous to b
	position.append(nltk.defaultdict(list))

for i in range(4):
	for k, v in dictz[i].iteritems():
		position[i][v].append(k)
	for k in dictz[i]:
		dictz[i][k]=list(set(dictz[i][k]))

#temp = {'Pronoun': ['PRP','PRP$','WP', 'POS'], 'Verb':['VBG','VBN','VBD','VBZ','VB'], 'Determiner':['DT','WDT'], 'Adjective':['JJ','JJR','JJS'], 'Noun':['NNP','NNPS','NNS','NN'], 'Particle':['RP'], 'Adverb':['WRB','RB','RBR','RBS'],'Conjuction':['CC'], 'Numeral':['CD'], 'Preposition':['IN','TO']}


dump_json(dictz,position)