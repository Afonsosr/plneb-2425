# TPC9 - Afonso Rodrigues, PG55831

## Introdução

Este trabalho tem como principal objetivo a análise do texto de um livro do Harry Potter, pela comparação e várias relações de similaridade entre as palavras do livro.

## Treino do Modelo

O ficheiro harry.txt começou por ser aberto e tokenizado. Após isso, foi inicializado o modelo de treino, como é possível verificar abaixo.

```python
# Carregar documento (arquivo .txt)
with open("harry.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Tokenizar em palavras
tokens = word_tokenize(texto)

frases = [
    [token.lower() for token in word_tokenize(a, language='portuguese') if token.isalpha()]
    for a in tokens
]


model = Word2Vec(frases, vector_size=100, window=5, min_count=1, sg=1, epochs=5, workers=3)
```


Após isto, foram feitos testes e foi também criada a função get_word(), que verifica se a palavra em questão está presente no documento.

```python
def get_word(word):
    try:
        return model.wv[word]
    except KeyError:
        print("The word '"+word+"' does not appear in this model")
```

## Saving and Coding

## Similaridade

## Intruso

## Analogias

## Tensorflow - nuvem de conceitos

<img src="nuvem.png">

