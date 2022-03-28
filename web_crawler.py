import requests
from bs4 import BeautifulSoup

from wordcloud_wc import create_wordcloud

"""
Pegando as palavras mais usadas no site e faz um top 10
"""


def start(url):

    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, "html.parser")

    for each_text in soup.find_all("div", {"class": "entry-content"}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    clean_list = []

    for word in wordlist:
        symbols = '!@#$%^&*()_–-+={[}]|\;:"<>?/., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # criando wordcloud
    create_wordcloud(word_count)


if __name__ == "__main__":
    start(
        "https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar"
    )
