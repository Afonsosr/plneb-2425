import re

file = open("dicionario_medico.txt", encoding="utf8")

texto = file.read()


texto = re.sub(r"\n\n\f","\n\n",texto)
texto = re.sub(r"\n\n","\n\n@",texto)


conceitos_texto = re.split(r"\n\n@",texto)

conceitos_list = []
for c in conceitos_texto:
    conceito = re.split(r"\n",c)
    elem = [conceito[0],""]
    for f in conceito[1:]:
        elem[1] = elem[1] + str(" ") + f
    
    conceitos_list.append(elem)


# gerar html

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
f_out.close()

file.close()
