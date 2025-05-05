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

## Similaridade

Foi testada a similaridade entre as várias palavras que aparecem no livro. Começou-se por analisar o estudo do conjunto de palavras "mais próximas"/"com maior associação" ao termo de input. Foram testadas as palavras 'leviosa' e 'hagrid'. Abaixo estão, respetivamente, apresentados os outputs de cada uma das pesquisas

Input:
```python
model_wv.wv.most_similar('leviosa')
```
Output:
```txt
[('fantochinho', 0.3471190333366394),
 ('substituindo', 0.3336864113807678),
 ('precisaremos', 0.3290361762046814),
 ('formos', 0.32050657272338867),
 ('mundo', 0.31179478764533997),
 ('dias', 0.3085697889328003),
 ('chorando', 0.30578887462615967),
 ('perto', 0.30517101287841797),
 ('poderes', 0.29699182510375977),
 ('acidentara', 0.2967570424079895)]
```

Input:
```python
model_wv.wv.most_similar('hagrid')
```
Output:
```txt
[('edwiges', 0.3439558148384094),
 ('espalhar', 0.33714985847473145),
 ('piscaram', 0.3369746208190918),
 ('desengonçado', 0.3322811424732208),
 ('apanhando', 0.32884615659713745),
 ('meia', 0.3226913511753082),
 ('chapinhava', 0.31663644313812256),
 ('harry', 0.3039996922016144),
 ('training', 0.291799932718277),
 ('rouba', 0.29159069061279297)]
```

De seguida, foi testada a similaridade entre pares de termos. Par aisto, tentei pensar em termos que pudessem estar associados de uma forma mais próxima, tanto pelo contexto de toda a saga como do livro em questão, de uma forma mais específica. Os resultados obtidos foram os seguintes:

Input:
```python
print(model_wv.wv.similarity("harry","voldemort"))
print(model_wv.wv.similarity("filosofal","harry"))
print(model_wv.wv.similarity("hagrid","hermione"))
print(model_wv.wv.similarity("harry","snape"))
```
Output:
```txt
0.13185275
0.12981871
0.035221413
-0.0152964955
```

## Intruso

De uma lista de conceitos, queriamos agora saber qual é o termo intruso. Foram feitos alguns testes. 

Input:
```python
model_wv.wv.doesnt_match(["harry","rony","hermione"])
```
Output:
```txt
'hermione'
```

Aqui, por exemplo, o intruso corresponder a 'hermione' deve-se, provavelmente, ao caso de este ser um nome feminino, enquanto que o nome 'harry' e 'rony' correspondem a nomes masculinos.

Input:
```python
model_wv.wv.doesnt_match(["draco","harry","hermione","rony"])
```
Output:
```txt
'draco'
```

Já neste caso, a exclusão de 'draco' pode-se dever mais ao contexto da própria história e à relação entre as personagens. Como se sabe, o Draco (Slytherin) faz parte de uma "casa" diferente das de Harry, Ron e Hermione (Gryffindor), ou seja, também não faz parte do núcleo de amigos de Harry, visto até como um opositor/inimigo ao grupo de amigos. 

## Analogias

O estudo de analogias permite ver relações/possíveis sinónimos que podem ser inferidos a partir de conjuntos de palavras. Apesar de alguns dos conceitos testados terem retornado palavras menos óbvias, ou descontextualizadas, houve um conjunto de termos que retornou algo interessante:

Input:
```python
def analogy( x2, y1, x1):
    result = model_wv.wv.most_similar(positive=[y1, x2], negative=[x1])
    return result[0][0]

analogy('harry', 'rony', 'hagrid')
```
Output:
```txt
'seguidores'
```

O modelo, aqui, é capaz de reconhecer/identificar Harry e Ron como "seguidores" de Hagrid, uma personagem muito próxima de ambos e que tanto lhes ensina ao longo de todos os livros.

## Visualização gráfica

Foi analisado um conjunto de palavras com recurso a representação gráfica. É utilizada uma redução da dimensionalidade dos conceitos e é feita a sua representação. Assim, é possível ver de uma forma mais simples, a proximidade entre os vários termos presentes na lista de teste.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def display_pca_scatterplot(model, words=None):
    word_vectors = []
    valid_words = []

    for w in words:
        if w in model:
            word_vectors.append(model[w])
            valid_words.append(w)
        else:
            print(f"Aviso: '{w}' não está no vocabulário do modelo.")

    word_vectors = np.array(word_vectors)
    twodim = PCA(n_components=2).fit_transform(word_vectors)

    plt.figure(figsize=(10, 10))
    plt.scatter(twodim[:, 0], twodim[:, 1], edgecolors='k', c='skyblue', s=100)

    for word, (x, y) in zip(valid_words, twodim):
        plt.text(x, y, word, fontsize=12, ha='left', va='bottom')

    plt.title("Palavras no espaço PCA (2D)", fontsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

palavras =  ['sirius','draco','malfoy', 'snape', 'mcgonagall','harry', 'rony', 'hermione', 'dumbledore','hagrid']
display_pca_scatterplot(model_wv.wv,palavras)

palavras2 =  ['hogwarts','escola','varinha','magia','grifinória','sirius','draco','malfoy', 'snape', 'mcgonagall','harry', 'rony', 'hermione', 'dumbledore','hagrid']
display_pca_scatterplot(model_wv.wv,palavras2)
```
No notebook é possível ver a representação gráfica de ambas as listas de palavras.

## Tensorflow - nuvem de conceitos

Abaixo está representada a nuvem de conceitos obtida no tensorflow, bem como o conjunto de palavras mais próximas a 'harry'.

<img src="nuvem.png">

