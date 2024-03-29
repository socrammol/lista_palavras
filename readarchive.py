from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.util import ngrams
from flask import Flask, flash, request, redirect, render_template
from app import app

stopwords = set(stopwords.words('portuguese') + list(punctuation))

@app.route('/visualizar', methods=['POST'])
def visulizar_dados():
    return render_template('dados.html')

def inicia(caminho , op):
    opcao= op
    # vetores
    dicionario = []
    vetores_palavras = []
    vet_2andic = []
    vet_2anpala = []

    def verifica_frequencia(arr1, arr2):
        vetores_palavras = arr1
        vet_final = arr2
        vet1 = []
        vet2 = []
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
        return vet2

    def extract_ngrams(vetor, num):
        n_grams = ngrams(vetor, num)
        return [' '.join(grams) for grams in n_grams]

    def setencas(texto):
        # sentencas = sent_tokenize(f)
        palavras = word_tokenize(f.lower())
        # montando um vetor com as palavras sem stopword
        palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]
        return palavras_sem_stopwords

    try:
        for i in caminho:
            f = open(i, 'r').read()
            vetores_palavras.append(setencas(f))
    except OSError:
        return "Caminho especificado esta invalido valide se possui \\ entre os diretorios"

    # preenchendo os vetorers
    for i in vetores_palavras:
        dicionario += i
        vet_2anpala.append(extract_ngrams(i, 2))
    vet_2andic = list(extract_ngrams(dicionario, 2))
    vet_2andic = list(dict.fromkeys(vet_2andic))
    dicionario = list(dict.fromkeys(dicionario))
    vetor_freq = verifica_frequencia(vetores_palavras,dicionario)
    vetor_freq_2an = verifica_frequencia(vet_2anpala,vet_2andic)
    # redirect('/visualizar')

    if op == "1":
        return dicionario
    if op == "2":
        return vet_2andic
    if op == "3":
        return vetor_freq
    if op == "4":
        return vetor_freq_2an
