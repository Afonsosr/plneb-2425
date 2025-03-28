# TPC7 - Afonso Rodrigues, PG55831

## Introdução

Este trabalho tem como objetivo a criação de uma tabela dinâmica dentro de uma página web, e integrada nos trabalhos das últimas aulas, onde seja possível fazer uma pesquisa de conceitos.

## conceitos.js

No script conceitos.js inicializamos a tabela. É também aí que é ativada/permitida a pesquisa por conceitos e termos a partir de expressões regulares.

```python
$(document).ready( function () {
    $('#tabela_conceitos').DataTable({
    search: {
        regex: true
        }
    });
});
```

## tabela.html

Foi criado um ficheiro .html para a configuração da tabela. è aqui que conseguimos organizar toda a informação e escolher o tipo de tabela que pretendemos utilizar.

```html
class="table table-bordered table-striped"
```
De notar que caso o utilizador clique no conceito ou designação desejada, é redirecionado para a página conceito.html, onde terá apenas informação sobre o conceito selecionado.

```html
{% extends 'layout.html' %}

{% block head %}
    <title> Tabela </title>    <!-- Isto é o nome da página que aparece em cima no separador-->
{% endblock %}

{% block body %}

<table id="tabela_conceitos" class="table table-bordered table-striped">
    
    <thead>
        <tr>
            <th scope="col">Conceitos</th>
            <th scope="col">Descrições</th>
        </tr>
    </thead>
    <tbody>
        {% for designacao, descricao in db.items() %}
        <tr>
            <!--<td>{{designacao}}</td>-->
            <td><a href="/conceitos/{{designacao}}" class="list-group-item list-group-item-action">{{designacao}}</a></td>
            <!--<td>{{descricao}}</td>-->
            <td><a href="/conceitos/{{designacao}}" class="list-group-item list-group-item-action">{{descricao}}</a></td>
        </tr>
        {% endfor %}
    </tbody>
</table>


{% endblock %}
```

## @app.get("/conceitos/tabela")

Aqui, vemos a inicialização da rota que levará à página da tabela (tabela.html), no ficheiro tpc7.py.

```python
@app.get("/conceitos/tabela")
def conceitos_tabela():
    return render_template("tabela.html",db=db)
```

## layout.html

No ficheiro layout.html é feito o import do script em javascript referente aos templates de tabela do DataTable.

```html
<script src="https://cdn.datatables.net/2.2.2/js/dataTables.js"></script>
```

Tabém é adicionado, no navegador, um botão com ligação para a página da tabela.

```python
<a class="nav-link" href="/conceitos/tabela">Tabela</a>
```

## home.html

Foi adicionada à página home.html um botão com acesso direto à tabela. 

```html
<a href="/conceitos/tabela" class="btn btn-outline-secondary btn-lg px-4">Tabela</a>
```




