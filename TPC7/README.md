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



