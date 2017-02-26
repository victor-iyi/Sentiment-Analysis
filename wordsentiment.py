import csv

negative_words = set()
positive_words = set()

def load_knowledgeBase():
    files = ['neg', 'pos']
    for f in files:
        with open(f+'/words.txt') as neg:
            neg_words = csv.reader(neg, delimiter='\n')

            for neg_row in neg_words:
                if f == 'neg':
                    negative_words.add(neg_row[0])
                if f == 'pos':
                    positive_words.add(neg_row[0])


def sentiment(file):
    f = open(file, 'r').read()
    sent_counter = 0

    for neg in negative_words:
        if neg in f:
            sent_counter += 1

    for pos in positive_words:
        if pos in f:
            sent_counter -= 1

    if sent_counter > 0:
        print('The review was positive')
    if sent_counter == 0:
        print('The review was neutral')
    if sent_counter < 0:
        print('The review was negative')

    print(sent_counter)


load_knowledgeBase()
sentiment('neg_review.txt')
sentiment('pos_review.txt')
count = 0
for n in positive_words:
    if n in negative_words:
        count +=1
print('No of pos in neg',count)

