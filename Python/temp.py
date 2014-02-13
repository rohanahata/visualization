def dump_json(tokens_in,state,size):
    tokens_freq = FreqDist(tokens_in)
    tokens_table = [dict(word=w, freq=tokens_freq[w]) for w in tokens_freq]
    tokens_table_short = tokens_table[:size]

    with open("tokens_"+ state + str(size) + ".json",'w') as outfile:
        json.dump(tokens_table_short,outfile, sort_keys = True, indent = 4,
ensure_ascii=False)

raw_text = open('ofk.txt').read()
tokens_raw = nltk.word_tokenize(raw_text)

a=nltk.pos_tag(tokens_raw)
b=dict(a)
pos2=nltk.defaultdict(list)
for k, v in b.items:
	pos2[v].append(k)
for k in pos2:
	pos2[k]=list(set(pos2[k]))
temp = {'Pronoun': ['PRP','PRP$','WP', 'POS'], 'Verb':['VBG','VBN','VBD','VBZ','VB'], 'Determiner':['DT','WDT'], 'Adjective':['JJ','JJR','JJS'], 'Noun':['NNP','NNPS','NNS','NN'], 'Particle':['RP'], 'Adverb':['WRB','RB','RBR','RBS'],'Conjuction':['CC'], 'Numeral':['CD'], 'Preposition':['IN','TO']}
for k in temp:
    z=0
    for i in temp[k]:
            z+=len(pos2[i])
	print z, temp[k]

temp = {'Pronoun': ['PRP','PRP$','WP', 'POS'], 'Verb':['VBG','VBN','VBD','VBZ','VB'], 'Determiner':['DT','WDT'], 'Adjective':['JJ','JJR','JJS'], 'Noun':['NNP','NNPS','NNS','NN'], 'Particle':['RP'], 'Adverb':['WRB','RB','RBR','RBS'],'Conjuction':['CC'], 'Numeral':['CD'], 'Preposition':['IN','TO']}
for j in range(4):
	for k in temp:
		q=0
		for i in temp[k]:
			q+=len(position[j][i])
		print q, k, j