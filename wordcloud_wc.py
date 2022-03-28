import matplotlib
from wordcloud import WordCloud

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def create_wordcloud(data):
    """
        Função para gera um wordcloud de palavras
    Args:
        data (List): Lista de tuplas com as palavras e as quantidades
    """
    # Gerando nuvem de palavras
    wc = WordCloud(
        background_color="white",
        max_words=2000,
        max_font_size=256,
        random_state=42,
        width=1000,
        height=500,
    )
    # Transformando (de lista para dicionário) pois a função que utilizaremos
    # nesse caso requer um dicionário
    data = dict(data)

    # ajuste do tamanho das palavras
    wc.generate_from_frequencies(data)
    plt.figure(figsize=[20, 10])
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
