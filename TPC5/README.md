# TPC5 - Afonso Rodrigues, PG55831

## Introdução

Este trabalho de casa tem como objetivo a criação de um percurso entre ficheiros html, partindo de uma lista de conceitos. O objetivo é que, em cada conceito, seja possível criar uma hiperligaão para uma página individual onde aparecerá a descrição do termo em questão.

Abaixo, serão apenas descritos os trabalhos feitos no sentido de realizar o que foi pedido, ou seja, a criação de rotas entre ficheiros html para páginas individuais de conceitos e não todo o trabalho executado durante a aula em conjunto com os professores.

## conceito_unico.html

Foi criado um ficheiro conceito_unico.html, que será o responsável pelo layout da página individual de cada termo. Este, apresentará como título a designação em questão, seguida da sua descrição.
```python
<!DOCTYPE html>
<html>

<head>
    <title>Conceito único</title>
</head>  

<body>
    <h2>{{designacao}}</h2>
    <p>{{db[designacao]}}</p>
</body>
</html>
```

## Adaptação no ficheiro conceitos.html
Esta página é aquela onde aparecem todos os conceitos listados. Foi necessário fazer uma alteração ao código desta, de forma a que cada um dos termos seja acompanhado da hiperligação já descrita acima. Assim, cada termo, passa a ter uma hiperligação associada, que levará á página individual de cada um.

Adaptação feita:
```python
 <a href="/conceitos/{{designacao}}" target="_blank" title="{{ db[designacao] }}">
          {{designacao}}
</a>
```

## Routes

Este trabalho baseia-se, principalmente, no uso de duas routes, que são as responsáveis por fazer a transição entre páginas html, e a compilação dos vários materiais, de forma a chegar-se ao resultado final.

```python
@app.route("/conceitos")
def conceitos():
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos",db=db)


@app.route("/conceitos/<designacao>")
def api_conceito(designacao):
    if designacao in db:        
        return render_template("conceito_unico.html", designacao=designacao, descricao=db[designacao], title="Conceito",db=db)


```
