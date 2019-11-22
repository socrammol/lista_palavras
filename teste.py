from nltk import collections, Counter
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.util import ngrams
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

###lendo os arquivos
f = open('texto1.txt', 'r').read()

# 1 arquivo
###separando as senteças e as palavras
sentencas = sent_tokenize(f)
palavras = word_tokenize(f.lower())

###stopword
stopwords = set(stopwords.words('portuguese') + list(punctuation))
###montando um vetor com as palavras sem stopword
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

# 2 aquivo
f = open('texto2.txt', 'r').read()

###separando as senteças e as palavras
sentencas = sent_tokenize(f)
palavras = word_tokenize(f.lower())

###montando um vetor com as palavras sem stopword
palavras_sem_stopwords2 = [palavra for palavra in palavras if palavra not in stopwords]
vet_final = []
vet_final.append(palavras_sem_stopwords[0])

vet1 = []
vet2 = []
vet_final = palavras_sem_stopwords + palavras_sem_stopwords2
vet_final = list(dict.fromkeys(vet_final))
x = 0
aux = 0

texts = [vet_final, palavras_sem_stopwords]
count = 0

contador = []
for i in range(0, len(vet_final), 1):
    aux1 = vet_final[i]
    for j in range(0, len(palavras_sem_stopwords), 1):
        aux2 = palavras_sem_stopwords[j]
        if aux1 == aux2:
            contador.append(1)
    vet1.append(sum(contador))
    contador = []

contador = []
for i in range(0, len(vet_final), 1):
    aux1 = vet_final[i]
    for j in range(0, len(palavras_sem_stopwords2), 1):
        aux2 = palavras_sem_stopwords2[j]
        if aux1 == aux2:
            contador.append(1)
    vet2.append(sum(contador))
    contador = []

print('dicionario: ', vet_final)
print('vet palavras: ', palavras_sem_stopwords)
print(vet1)


def extract_ngrams(vet_final):
    n_grams = ngrams(vet_final,2)
    return [' '.join(grams) for grams in n_grams]
print(extract_ngrams(vet_final))

# print(vet_final)
# print(palavras_sem_stopwords2)
# print(vet2)
