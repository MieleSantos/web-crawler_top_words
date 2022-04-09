import re
from typing import List

import nltk
import requests
from bs4 import BeautifulSoup

from wordcloud_wc import create_wordcloud

nltk.download("punkt")
nltk.download("stopwords")
"""
Pegando as palavras mais usadas no site e faz um top 10
"""


def start(url):
    """_summary_
        Função para fazer a requisição no site e extrair as palavras
    Args:
        url (String): url do site a ser requisitado
    """
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, "html.parser")

    for each_text in soup.find_all("div", {"class": "entry-content"}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist: list):
    """
        Função para remover pontuações e criar lista de palavras
    Args:
        wordlist (list): Lista com todas as palavras encontradas no site
    """
    clean_list = []

    for word in wordlist:
        symbols = '!@#$%^&*()_–-+={[}]|\;:"<>?/., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")

        if len(word) > 0:
            clean_list.append(word)

    # removendo stopwords
    clean_list = remover_stop_word(clean_list)
    create_dictionary(clean_list)


def create_dictionary(clean_list: list):
    """
        Função para conta a ocorrencia das palavras
    Args:
        clean_list (list): Lista de palavras, com stopwords removidas
    """
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # criando wordcloud
    create_wordcloud(word_count)


def remover_stop_word(clean_list: list) -> List:
    """
        Função para remover as stopwords, números e palavras que contem algum
        número junto
    Args:
        clean_list (List): Lista com todas as palavras extraidas do site

    Returns:
        List: lsita com as stopwords removidas
    """
    # definindo stopwords do idioma english
    stopwords = nltk.corpus.stopwords.words("english")
    print("Total de palavras com stopwords: ", len(clean_list))
    # removendo stopwords
    tokens = [palavra for palavra in clean_list if palavra not in stopwords]
    print("Total sem stopswords: ", len(tokens))
    # removendo palavras que contem alguum numero
    tokens = [elemento for elemento in tokens if not re.search(r"\d+", elemento)]
    print("Total sem stopswords e numeros: ", len(tokens))

    return tokens


if __name__ == "__main__":
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
