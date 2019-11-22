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
#
# for i in vet_final:
#         if i in palavras_sem_stopwords:
#             aux+=1
#             vet1.append(aux)
#         else:
#             aux2 = 0
#             vet1.append(aux)
#
#         aux = 0
#
# for i in vet_final:
#     if i in palavras_sem_stopwords2:
#         vet2.append(1)
#     else:
#         vet2.append(0)
# frequencia = FreqDist(palavras_sem_stopwords)
# i = 0
# while i < len(vet_final):
#     for j in len(vet_final):
#         if j in palavras_sem_stopwords:
#             aux+=1
#     vet1.append(aux)
#     aux = 0
#     i+=1
# texts = [vet_final,palavras_sem_stopwords]
# vet1 = collections.Counter(word for words in texts for word in words)
texts = [vet_final, palavras_sem_stopwords]
count = 0
# for text in texts:
#     # print(Counter(text).values())
#     count =1
#     if count > 0:
#         vet1=(Counter(text).values())
# for i in vet1:
#     if vet1[i]<
#
# texts = [vet_final,palavras_sem_stopwords2]
# for text in texts:
#     print(Counter(text))
#     count =1
#     if count > 0:
#         vet2=(Counter(text).values())
# # print(vet_final)
# print(palavras_sem_stopwords)
# print(vet1)
#
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

print(vet_final)
print(palavras_sem_stopwords)
print(vet1)

print(vet_final)
print(palavras_sem_stopwords2)
print(vet2)
