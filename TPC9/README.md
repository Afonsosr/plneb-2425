# TPC9 - Afonso Rodrigues, PG55831

## Introdução

Este trabalho tem como principal objetivo a análise do texto de um livro do Harry Potter, pela comparação e várias relações de similaridade entre as palavras do livro.

## Treino do Modelo

O ficheiro harry.txt começou por ser aberto e tokenizado. Após isso, foi inicializado o modelo de treino, como é possível verificar abaixo.

```python

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

