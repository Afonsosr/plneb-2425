# TPC8 - Afonso Rodrigues, PG55831

## Introdução

Este trabalho tem como objetivo a formatação de toda a informação presente no campo "content" do ficheiro doencas__.json criado durante a aula 8. 
Todo este trabalho tem como base o dicionário de doenças presente no site [Atlas da Saúde](https://www.atlasdasaude.pt/doencasaaz/).

## doencas__.json

Este é o ficheiro .json inicial, a partir do qual iniciamos o processo de leitura e tratamento dos dados. Este ficheiro é composto por um conjunto de características/especificações de cada um dos conceitos (o url que leva à sua página individual, o "content", que será o campo a trabalhar, e um pequeno resumo do conceito).
Abaixo, é apresentado o exemplo de um dos conceitos presente neste ficheiro:

```json
 "Acne": {
        "url": "https://www.atlasdasaude.pt/acne-causas-sintomas-diagnostico-tratamento",
        "content": "<div class=\"ds-1col node node-doencas node-full view-mode-full clearfix\">\n<div class=\"field field-name-post-date field-type-ds field-label-hidden\">\n<div class=\"field-items\">\n<div class=\"field-item even\">20/02/2013 - 18:57</div>\n</div>\n</div>\n<div class=\"field field-name-body field-type-text-with-summary field-label-hidden\">\n<div class=\"field-items\">\n<div class=\"field-item even\"> <p>Atinge cerca de 80% da população com idade compreendida entre os 12 e os 24 anos, pelo que se pode dizer que esta é a doença inflamatória da pele mais frequente em todo o mundo. Caracterizada por um processo inflamatório que resulta da produção excessiva de sebo pelas glândulas sebáceas, esta afeta sobretudo o sexo feminino.</p>\n<p>Pode ainda surgir na <strong>infância</strong> – entre os 1 a 7 anos de idade -, o que pode querer indicar algum problema subjacente, como é o caso da puberdade precoce.</p>\n<p>Por outro lado, também a mulher adulta pode ter acne (depois dos 25 anos, mantendo-se até aos 40 ou mais anos), na maioria dos casos persistindo desde a adolescência ou então surgindo “de novo” nessa fase da vida.</p>\n<h2><strong>Acne na adolescência</strong></h2>\n<p>A acne na adolescência pode afetar a face e o tronco (ombros, zona V do decote e dorso), é mais precoce nas mulheres, mas mais grave nos homens. Caracteriza-se pela presença de hiperseborreia, comedões abertos e fechados (“<strong>pontos negros</strong>” e “<strong>pontos brancos</strong>”) e lesões inflamatórias (<strong>pápulas</strong>, <strong>pústulas</strong>, <strong>nódulos</strong>, <strong>quistos</strong>).</p>\n<p><strong>Acne na idade adulta</strong></p>\n<p>A acne na mulher adulta atinge a metade inferior do rosto e o pescoço, com lesões inflamatórias características. Com maior frequência, nesta faixa etária, há manipulação das lesões, o que acarreta cicatrizes hiperpigmentadas (acastanhadas). Nesta fase da vida, os fatores que contribuem para a acne são diversos, pelo que a resposta ao tratamento é mais demorada, podendo ser necessário manter um cuidado “preventivo” ao longo da vida.</p>\n<h2><strong>Causas </strong></h2>\n<p>As alterações hormonais são apontadas como as principais responsáveis pelo aparecimento da acne. As hormonas envolvidas neste processo são os “andrógenos”, com ação sobre as glândulas de gordura da pele, em determinadas localizações – face, tronco, couro cabeludo. Elas atuam aumentando a produção de sebo na pele e contribuindo para a condição de “hiperseborreia” que, associada a outros fatores, como a proliferação de bactérias, inflamação ou alterações no processo de queratinização da pele, conduzem ao aparecimento das lesões iniciais de acne – os comedões (vulgarmente designados por “pontos negros” ou “pontos brancos”). Quanto maior a inflamação que se observa, mais graves são as suas manifestações.</p>\n<p>O stress é, no entanto, outro dos fatores que pode estar na sua origem (já que promove uma maior atividade das glândulas sebáceas) ou agravá-la, uma vez que aumenta a tendência do indivíduo para espremer ou coçar borbulhas.</p>\n<p>Ao contrário do que se possa pensar, chocolates, azeitonas, marisco, gorduras ou bolos não são responsáveis por esta doença cutânea.</p>\n<h2><strong>Sintomas</strong></h2>\n<ul>\n<li>Pontos negros</li>\n<li>Pontos brancos</li>\n<li>Pápulas</li>\n<li>Pústulas</li>\n<li>Nódulos</li>\n<li>Quistos</li>\n</ul>\n<h2><strong>Diagnóstico </strong></h2>\n<p>O diagnóstico da acne é feito após exame da pele. Neste, os médicos procuram determinados sintomas, como cravos ou comedões, para determinar se a pessoa tem acne e não outra doença de pele, como rosácea.</p>\n<p>Após o diagnóstico, e com base no número e tipo de lesões, a acne é definida como: <strong>leve</strong>, <strong>moderada</strong> e <strong>grave</strong>.</p>\n<h2><strong>Tratamento </strong></h2>\n<p>O seu tratamento vai depender da gravidade da doença. No entanto, este permite reduzir a inflamação tornando a pele mais saudável.</p>\n<p>Podem ser utilizados cremes, géis, sabonetes e antibióticos para controlar a proliferação bacteriana, de aplicação tópica (diretamente na zona afetada), ou, em situações mais graves, medicação oral.</p>\n<p>O dermatologista pode ainda recomendar outros tratamentos complementares como a extração de comedões, punção ou drenagem de pústulas, nódulos e quistos. Peeling, laser ou dermobrasão podem ser necessários para o tratamento de marcas associadas às lesões provocadas pela acne.</p>\n<p>Quanto às manchas, estas podem ser tratadas em casa com recurso a cremes ou em consultório com recurso a fototerapia de luz azul.</p>\n<h2><span style=\"color:#00cc00;\">Artigos Relacionados </span></h2>\n<h3><a href=\"https://www.atlasdasaude.pt/publico/content/acne-principais-mitos\" target=\"_blank\">Acne: principais mitos </a></h3>\n<h3><a href=\"https://www.atlasdasaude.pt/publico/content/acne-solar\" target=\"_blank\">Acne solar</a></h3>\n<h3><a href=\"https://www.atlasdasaude.pt/publico/content/nova-pilula-contracetiva-no-combate-acne\" target=\"_blank\">Nova pílula contracetiva no combate à acne</a></h3>\n</div>\n</div>\n</div>\n<div class=\"field field-name-field-nota field-type-text field-label-inline clearfix\">\n<div class=\"field-label\"><div class=\"label-inner\">Nota: </div></div>\n<div class=\"field-items\">\n<div class=\"field-item even\">As informações e conselhos disponibilizados no Atlas da Saúde não substituem o parecer/opinião do seu Médico e/ou Farmacêutico.</div>\n</div>\n</div>\n<div class=\"field field-name-field-addthis field-type-addthis field-label-hidden\">\n<div class=\"field-items\">\n<div class=\"field-item even\"><a addthis:title=\"Acne - Atlas da Saúde\" addthis:url=\"https://www.atlasdasaude.pt/acne-causas-sintomas-diagnostico-tratamento\" class=\"addthis_button\"><img alt=\"Share page with AddThis\" src=\"https://s7.addthis.com/static/btn/sm-share-en.gif\"/>\n</a>\n</div>\n</div>\n</div>\n</div>",
        "resumo": "Atinge cerca de 80% da população com idade compreendida entre os 12 e os 24 anos, pelo que se pode dizer que esta é a doença inflamatória da pele mais frequente em todo o mundo."
    }
```

## tpc8.py

Inicialmente são feitos os imports das bibliotecas necessárias e, depois, é feita a abertura e load do ficheiro "doencas__.json"

```python
from bs4 import BeautifulSoup
import json

db_file = open("doencas__.json",encoding="utf-8")
db = json.load(db_file)
db_file.close()
```

Nota: Todo este processo acontece de forma iterativa.

É feito o parse, pela biblioteca BeautifulSoup, do conteúdo que é value da key "content", dentro do elemento.

Após isso, são pesquisadas as ocorrências de "h2","p" e "ul", que são, após análise, os vários tipos de elementos presentes e necessários para este trabalho no conteúdo de cada uma das doenças.

- **`<h2>`** → Títulos de subsecções
```python
if conteudo_div.name == "h2":
   if tex:
       info.append((titu,tex.strip()))
   strong_tag = conteudo_div.find("strong")
   titu = strong_tag.text.strip() if strong_tag else "Untitled"
   tex = ""
```
- **`<p>`** → Parágrafos de texto
```python
elif conteudo_div.name == "p":
   tex += conteudo_div.text.strip() + " "
```
- **`<ul>`** → Listas (ex.: sintomas, conjuntos de fatores)
```python
elif conteudo_div.name == "ul":
   list_items = [li.get_text(strip=True) for li in conteudo_div.find_all("li")]
   tex += ", ".join(list_items) + " "
```


Depois de encontrados, cada uma das informações é colocada no devido local, associado ao respetivo subtítulo na forma de tuplo. Este tuplo é adicionado à lista info.

```python
info.append((titu,tex.strip()))
```

A lista, por fim, é convertida para dicionário, o campo "content" é apagado e substituído pelos campos criados, e toda esta informação é escrita num novo ficheiro doencas_tpc.json, abaixo explicado.

```python
    del db[elem]["content"]
    d_info = dict(info)
    db[elem].update(d_info)
a = open("doencas_tpc.json","w",encoding="utf-8")
json.dump(db,a,indent=4,ensure_ascii=False)
a.close()
```

## doencas_tpc.json

Ficheiro final com todas as informações devidamente tratadas e associadas a cada um dos conceitos.

```json
"Acne": {
        "url": "https://www.atlasdasaude.pt/acne-causas-sintomas-diagnostico-tratamento",
        "resumo": "Atinge cerca de 80% da população com idade compreendida entre os 12 e os 24 anos, pelo que se pode dizer que esta é a doença inflamatória da pele mais frequente em todo o mundo.",
        "Intro": "Atinge cerca de 80% da população com idade compreendida entre os 12 e os 24 anos, pelo que se pode dizer que esta é a doença inflamatória da pele mais frequente em todo o mundo. Caracterizada por um processo inflamatório que resulta da produção excessiva de sebo pelas glândulas sebáceas, esta afeta sobretudo o sexo feminino. Pode ainda surgir na infância – entre os 1 a 7 anos de idade -, o que pode querer indicar algum problema subjacente, como é o caso da puberdade precoce. Por outro lado, também a mulher adulta pode ter acne (depois dos 25 anos, mantendo-se até aos 40 ou mais anos), na maioria dos casos persistindo desde a adolescência ou então surgindo “de novo” nessa fase da vida.",
        "Acne na adolescência": "A acne na adolescência pode afetar a face e o tronco (ombros, zona V do decote e dorso), é mais precoce nas mulheres, mas mais grave nos homens. Caracteriza-se pela presença de hiperseborreia, comedões abertos e fechados (“pontos negros” e “pontos brancos”) e lesões inflamatórias (pápulas, pústulas, nódulos, quistos). Acne na idade adulta A acne na mulher adulta atinge a metade inferior do rosto e o pescoço, com lesões inflamatórias características. Com maior frequência, nesta faixa etária, há manipulação das lesões, o que acarreta cicatrizes hiperpigmentadas (acastanhadas). Nesta fase da vida, os fatores que contribuem para a acne são diversos, pelo que a resposta ao tratamento é mais demorada, podendo ser necessário manter um cuidado “preventivo” ao longo da vida.",
        "Causas": "As alterações hormonais são apontadas como as principais responsáveis pelo aparecimento da acne. As hormonas envolvidas neste processo são os “andrógenos”, com ação sobre as glândulas de gordura da pele, em determinadas localizações – face, tronco, couro cabeludo. Elas atuam aumentando a produção de sebo na pele e contribuindo para a condição de “hiperseborreia” que, associada a outros fatores, como a proliferação de bactérias, inflamação ou alterações no processo de queratinização da pele, conduzem ao aparecimento das lesões iniciais de acne – os comedões (vulgarmente designados por “pontos negros” ou “pontos brancos”). Quanto maior a inflamação que se observa, mais graves são as suas manifestações. O stress é, no entanto, outro dos fatores que pode estar na sua origem (já que promove uma maior atividade das glândulas sebáceas) ou agravá-la, uma vez que aumenta a tendência do indivíduo para espremer ou coçar borbulhas. Ao contrário do que se possa pensar, chocolates, azeitonas, marisco, gorduras ou bolos não são responsáveis por esta doença cutânea.",
        "Sintomas": "Pontos negros, Pontos brancos, Pápulas, Pústulas, Nódulos, Quistos",
        "Diagnóstico": "O diagnóstico da acne é feito após exame da pele. Neste, os médicos procuram determinados sintomas, como cravos ou comedões, para determinar se a pessoa tem acne e não outra doença de pele, como rosácea. Após o diagnóstico, e com base no número e tipo de lesões, a acne é definida como: leve, moderada e grave.",
        "Tratamento": "O seu tratamento vai depender da gravidade da doença. No entanto, este permite reduzir a inflamação tornando a pele mais saudável. Podem ser utilizados cremes, géis, sabonetes e antibióticos para controlar a proliferação bacteriana, de aplicação tópica (diretamente na zona afetada), ou, em situações mais graves, medicação oral. O dermatologista pode ainda recomendar outros tratamentos complementares como a extração de comedões, punção ou drenagem de pústulas, nódulos e quistos. Peeling, laser ou dermobrasão podem ser necessários para o tratamento de marcas associadas às lesões provocadas pela acne. Quanto às manchas, estas podem ser tratadas em casa com recurso a cremes ou em consultório com recurso a fototerapia de luz azul."
    }
```
 
