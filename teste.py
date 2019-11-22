from nltk import collections, Counter
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
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
for i in vet_final:
    for j in palavras_sem_stopwords:
        if i == j:
            aux +=1
            vet1.append(aux)
        else:
            vet1.append(0)
        aux = 0

for i in vet_final:
    if i in palavras_sem_stopwords2:
        vet2.append(1)
    else:
        vet2.append(0)
frequencia = FreqDist(palavras_sem_stopwords)

# print(vet_final)
# print(palavras_sem_stopwords)
# print(vet1)
#
# print(vet_final)
# print(palavras_sem_stopwords2)
# print(vet2)

print('-----------')
print(vet1)
