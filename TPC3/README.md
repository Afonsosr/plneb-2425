# TPC3 - Afonso Rodrigues, PG55831

## Introdução
A execução deste código permite ler um ficheiro de conceitos médicos ("dicionario_medico") em formato ".txt" (previamente convertido, pois o ficheiro original se encontrava no formato ".pdf"), proceder à sua organização e, com a informação, gerar um ficheiro ".html".

## Procedimento

## Abertura e limpeza do ficheiro

Inicialmente, o ficheiro é aberto e lido integralmente. Após isso, o primeiro processo consiste em eliminar os "form feeds" ("\f"), ou seja, marcadores de quebra de página, e marcar cada um dos diferentes conceitos individualmente, para que depois seja mais simples separar cada um dos conceitos. Seguidamente, esta separação é executada. Para tudo isto, são utilizadas expressões regulares. 


```python

```

## Organização e remoção de quebras de linha

Após isto, é criada uma lista de conceitos. Cada um dos elementos será, também, uma lista na forma [conceito,descrição] e, para isso, ainda há processamentos a serem executados em cada um dos conceitos. Em primeiro lugar, há uma iteração pelas descrições dos vários conceitos, em que o objetivo é eliminar quebras de linha ("\n") que estejam presentes. É também feita, em cada conceito, a separação entre o termo relativo ao conceito e a sua descrição.


```python
conceitos_texto = re.split(r"\n\n@",texto)

conceitos_list = []
for c in conceitos_texto:
    conceito = re.split(r"\n",c)
    elem = [conceito[0],""]
    for f in conceito[1:]:
        elem[1] = elem[1] + str(" ") + f
    
    conceitos_list.append(elem)
```

## Criação de ficheiro ".html"

Após tudo isto, é gerado um ficheiro ".html" que será aplicado ao "conceitos_list", que é a lista de conceitos onde toda a informação tratada está armazenada.


```python
def gera_html(conceitos):
    html_header = f"""
        <!DOCTYPE html>
            <head>
            </head>
            <body> 
            <h3>Dicionário de conceitos médicos</h3>
            <p>Este dicionário foi desenvolvido para a aula de PLNEB 2024/2025 <p>""" 


    html_conceitos = ""

    for designacao, descricao in conceitos:
                html_conceitos += f"""
                                <div>
                                <p><b>{designacao}</b></p>
                                <p>{descricao}</p>
                                </div>
                                <hr/> 
                            """


    html_footer = """              
                </body>
            </html> """
    
    return html_header + html_conceitos + html_footer

html = gera_html(conceitos_list)
f_out = open("dicionario_medicos.html","w")
f_out.write(html)

```

Por último, ambos os ficheiros são fechados (tanto o ficheiro ".txt" inicial como o ficheiro ".html").


```python
f_out.close()
file.close()
```
