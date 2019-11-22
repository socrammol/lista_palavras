from nltk import collections, Counter
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.util import ngrams
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

###stopword
stopwords = set(stopwords.words('portuguese') + list(punctuation))
# 1 arquivo

def setencas(texto):
    # sentencas = sent_tokenize(f)
    palavras = word_tokenize(f.lower())
    # montando um vetor com as palavras sem stopword
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]
    return palavras_sem_stopwords
dicionario = []
vetores_palavras = []


###lendo os arquivos
f = open('texto1.txt', 'r').read()
vetores_palavras.append(setencas(f))
#
# # 2 aquivo
f = open('texto3.txt', 'r').read()
vetores_palavras.append(setencas(f))
f = open('texto2.txt', 'r').read()
vetores_palavras.append(setencas(f))

for i in vetores_palavras:
    dicionario += i



dicionario = list(dict.fromkeys(dicionario))
print( dicionario)


def extract_ngrams(vetor, num):
    n_grams = ngrams(vetor,num)
    return [' '.join(grams) for grams in n_grams]
print(extract_ngrams(dicionario, 2))

vet1 = []
vet2 = []

vet_final = dicionario
tamanho_vet = len(vetores_palavras)


for m in vetores_palavras:
    palavras_sem_stopwords = m
    contador = []

    for i in range(0, len(vet_final), 1):
        aux1 = vet_final[i]
        for j in range(0, len(palavras_sem_stopwords), 1):
            aux2 = palavras_sem_stopwords[j]
            if aux1 == aux2:
                contador.append(1)
        vet1.append(sum(contador))
        contador = []
    vet2.append(vet1)
    vet1 = []




print(vet2)
print(vetores_palavras[0])
print(vetores_palavras[1])
print(vetores_palavras[2])




# vet1 = []
# contador = []
# for i in range(0, len(dicionario), 1):
#     aux1 = dicionario[i]
#     for m in vetores_palavras:
#         for j in range(0, len(m),1):
#             aux2 = m[j]
#             if aux1 == aux2:
#                 contador.append(1)
#
#         sum(contador)
#         vet1.append(contador)
#     contador = []
# print(vet1)
# print(vetores_palavras)

# ###separando as senteças e as palavras
# sentencas = sent_tokenize(f)
# palavras = word_tokenize(f.lower())
#
# ###montando um vetor com as palavras sem stopword
# palavras_sem_stopwords2 = [palavra for palavra in palavras if palavra not in stopwords]
#
#
# vet1 = []
# vet2 = []
# vet_final = palavras_sem_stopwords + palavras_sem_stopwords2
# vet_final = list(dict.fromkeys(vet_final))
# x = 0
# aux = 0
#
# texts = [vet_final, palavras_sem_stopwords]
# count = 0
#
# contador = []
# for i in range(0, len(vet_final), 1):
#     aux1 = vet_final[i]
#     for j in range(0, len(palavras_sem_stopwords), 1):
#         aux2 = palavras_sem_stopwords[j]
#         if aux1 == aux2:
#             contador.append(1)
#     vet1.append(sum(contador))
#     contador = []
#
# contador = []
# for i in range(0, len(vet_final), 1):
#     aux1 = vet_final[i]
#     for j in range(0, len(palavras_sem_stopwords2), 1):
#         aux2 = palavras_sem_stopwords2[j]
#         if aux1 == aux2:
#             contador.append(1)
#     vet2.append(sum(contador))
#     contador = []
#
# print('dicionario: ', vet_final)
# print('vet palavras: ', palavras_sem_stopwords)
# print(vet1)
#
#
# def extract_ngrams(vet_final):
#     n_grams = ngrams(vet_final,2)
#     return [' '.join(grams) for grams in n_grams]
# print(extract_ngrams(vet_final))
#
# # print(vet_final)
# # print(palavras_sem_stopwords2)
# # print(vet2)
###separando as senteças e as palavras


