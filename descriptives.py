from nltk.corpus import wordnet
import nltk
import re


def synonyms(word):
    synons = set()
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synons.add(l.name())
    return synons


def get_adj(words):
    tagged = nltk.pos_tag(words)
    adjs = set()
    for t in tagged:
        descriptives = re.findall(r'\(\'(\w*?)\',\s\'JJ\w?\'', str(t))
        for d in descriptives:
            adjs.add(d)
    return adjs

adj_list = set()

def adjectives(word, category):
    global adj_list
    adj_list.add(word)
    f = open(category+'/words.txt', 'a')
    f.write(word+'\n')
    f.close()
    if (len(adj_list) % 10) == 0:
        print(len(adj_list))
    adjs = get_adj(synonyms(word))
    for adj in adjs:
        if adj not in adj_list:
            adjectives(adj, category)

##if __name__ == '__main__':
##    adjectives('good', 'pos') # len = 2464
##    adjectives('bad', 'neg')  # len = 2443
    
