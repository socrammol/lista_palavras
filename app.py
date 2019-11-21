from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest


f = open('texto1.txt', 'r')
f2 = open('texto2.txt', 'r')
texto = f = open('texto1.txt', 'r').read()

sentencas = sent_tokenize(f)
palavras = word_tokenize(f.lower())


stopwords = set(stopwords.words('portuguese') + list(punctuation))
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

frequencia = FreqDist(palavras_sem_stopwords)



sentencas_importantes = defaultdict(int)
vet = []

for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
        if palavra in frequencia:
            sentencas_importantes[i] += frequencia[palavra]

    vet.append(frequencia)


idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)




for i in sorted(idx_sentencas_importantes):
    print(sentencas[i])

print(vet)
