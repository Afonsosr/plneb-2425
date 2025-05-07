# TPC10 - Afonso Rodrigues, PG55831

## Introdução

Este trabalho tem como objetivo a extração e formatação de informações, tendo como base edições da revista da [Sociedade Portuguesa de Medicina Interna](https://revista.spmi.pt/index.php/rpmi/issue/archive).

## Modelo de dados

No ficheiro JSON, os dados são estruturados tal como podemos ver no exemplo abaixo:

```json
{
    "titulo": "Comportamento do Utilizador do Serviço de Urgência do Hospital da Horta-Açores",
    "autores": "Ana Simas, Nuno Amorim, Catarina Cabrita, Ricardo Veloso, Juvenal Morais, Rui Suzano",
    "url": "https://revista.spmi.pt/index.php/rpmi/article/view/2582",
    "resumo": {
      "Introdução": "O uso inapropriado dos serviços de urgência,com todas as consequências negativas para os sistemas desaúde, é um fenómeno generalizado multifactorial e com tendência crescente.",
      "Métodos": "Para conhecer a nossa realidade fizemos um estudo do comportamento do utilizador do serviço de urgência do Hospital da Horta através de um inquérito, tendo sido analisados 463 casos, representando 6,5% de todos os episódios do período de estudo, dos quais 44% eram do género masculino e 56% feminino e dois terços dos quais tinham idades entre 24 e os 66 anos.",
      "Resultados": "Com base na triagem de Manchester 60% dos inquiridos foram classificados não urgentes (Verdes, Azuise Brancos). Apenas 5% tinha contactado a linha Saúde24 e só 12% tentou consulta no médico de família.",
      "Conclusão": "Os motivos principais pela opção hospitalar foram a auto percepção de urgência clínica, a busca na celeridade do Serviço de Urgência para resolução do problema, o menor tempo de espera no atendimento, a maior probabilidade de acesso a um especialista hospitalar e/ou a exames diagnósticos e a uma expectativa de maior qualidade no serviço prestado."
    },
    "doi": "https://doi.org/10.24950/rspmi.2582",
    "palavras_chave": [
      "Açores",
      "Inquéritos e Questionários",
      "Mau Uso de Serviços de Saúde/estatísticas e dados numéricos",
      "Serviço de Urgência Hospitalar/estatística e dados numéricos"
    ],
    "data_publicacao": "2025-03-31"
  }
```
Se algum dos campos não tiver informação, este fica em branco.

## Barra de Progresso

De forma a que possa ser feito um acompanhamento do estado do processo em tempo real, foi adicionada uma barra de progresso que permite ver tanto qual a revista/volume que está a ser processada, bem como o artigo em análise da respetiva revista.

## Armazenamento dos dados

Os dados, depois de processados, são guardados num ficheiro JSON (info_artigos.json), criado para o efeito.

