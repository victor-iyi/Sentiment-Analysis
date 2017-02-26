neg_words = []
pos_words = []

def loadAdjectives():
    global neg_words, pos_words
    for path in ['neg','pos']:
        read_adj = open(path+'/words.txt', 'r').read()
        adj = read_adj.split('\n')
        if path == 'neg':
            neg_words = [w for w in adj]
        if path == 'pos':
            pos_words = [w for w in adj]
            

loadAdjectives()

sentence_load = open('example.txt', 'r')
sentence = sentence_load.read()
print(sentence)
