# TPC3 - Afonso Rodrigues, PG55831

**Descrição:** 
A execução deste código permite ler um ficheiro de conceitos médicos ("dicionario_medico") em formato ".txt" (previamente convertido, pois o ficheiro original se encontrava no formato ".pdf"), proceder à sua organização e, com a informação, gerar um ficheiro ".html".

Inicialmente, o ficheiro é aberto e lido integralmente. Após isso, o primeiro processo consiste em eliminar os "form feeds" ("\f"), ou seja, marcadores de quebra de página, e marcar cada um dos diferentes conceitos individualmente, para que depois seja mais simples separar cada um dos conceitos. Seguidamente, esta separação é executada. Para tudo isto, são utilizadas expressões regulares. 

Após isto, é criada uma lista de conceitos. Cada um dos elementos será, também, uma lista na forma [conceito,descrição] e, para isso, ainda há processamentos a serem executados em cada um dos conceitos. Em primeiro lugar, há uma iteração pelas descrições dos vários conceitos, em que o objetivo é eliminar quebras de linha ("\n") que estejam presentes. É também feita, em cada conceito, a separação entre o termo relativo ao conceito e a sua descrição.

Após tudo isto, é gerado um ficheiro ".html" que será aplicado ao "conceitos_list", que é a lista de conceitos onde toda a informação tratada está armazenada.

Por último, ambos os ficheiros são fechados (tanto o ficheiro ".txt" inicial como o ficheiro ".html").




