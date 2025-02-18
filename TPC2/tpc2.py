import re

# 1)
# 1.1)

def hello_inicio(s):
    a = re.match(r'hello',s)
    f = False
    if a != None:
        f = True
    return f


# 1.2)

def hello_search(s):
    a = re.search(r'hello',s)
    f = False
    if a != None:
        f = True
    return f


# 1.3)

def hello_findall(s):
    a = re.findall(r'[hH][eE][lL][lL][oO]',s)
    f = False

    if a != []:
        f = True
    return print(f'{f} - {a}')


# 1.4)

def hello_sub(s):
    a = re.sub(r'[hH][eE][lL][lL][oO]','*YEP*',s)
    return a


# 1.5)

def hello_split(s):
    a = re.split(r',',s)
    return a


# 2)

def palavra_magica(frase):
    a = re.findall(r'por favor[!?.]$',frase)
    print(a)
    f = False
    if a != []:
        f = True
    return f


# 3)

def narcisismo(s):
    a = re.findall(r'[eE][uU]',s)
    return print(f'Frequência da palavra "eu" - {len(a)}')


# 4)

def troca_de_curso(s, novo_curso):
    a = re.sub(r'LEI',novo_curso,s)
    return print(a)


# 5)

def soma_string(s):
    a = re.split(r',',s)
    final = 0
    for elem in a:
        final += int(elem)
    return print(f'Soma da linha = {final}')


# 6)

def pronomes(s):
    lista = re.split(r' ',s)
    final = []
    for elem in lista:
        a = re.match(r'\b[eEtTnNvV][uUlLoO][eEaAsS]?s?\b',elem)
        if a != None:
            final.append(elem)
    return print(final)


# 7)

def variavel_valida(s):
    a = re.match(r'[a-zA-Z]\w*',s)
    if a != None:
        f = True
    else:
        f = False
    
    return print(f)


# 8)

def inteiros(s):
    final = []
    lista = re.split(r' ',s)
    for elem in lista:
        a = re.fullmatch(r'-?\d+',elem)
        if a != None:
            final.append(elem)
    return print(final)


# 9)

def underscores(s):
    a = re.sub(r' +','_',s)
    return print(a)


# 10)

def codigo_postal(lista):
    final = []
    for elem in lista:
        a = re.match(r'\d{4}-\d{3}',elem)
        if a != None:
            b = re.split(r'-',a[0])
            final.append(tuple(b))
    return print(final)



# TESTES:

print(hello_inicio("world hello"))
print(hello_inicio("hello world"))
print(hello_search("world"))
print(hello_search("world hello, please globe"))
hello_findall("world hello,Hello please globe")
hello_findall("world please globe")
hello_findall("Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!")
print(hello_sub("Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"))
print(hello_split("bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."))
print(palavra_magica("Posso ir à casa de banho, por favor?"))
print(palavra_magica("Preciso de um favor."))
narcisismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou.")
troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", "Biomédica")
soma_string("4,-6,2,3,8,-3,0,2,-5,1")
pronomes("eu tu nos vozes voces vos voz")
pronomes("amanha vamos ao cinema, eu e eles")    
variavel_valida("Olá")
variavel_valida("2+3=5")
variavel_valida("1pessoa")
variavel_valida("p_e_s_s_o_a_")
inteiros("vou comprar 3 pecas de fruta, e 3.3 euros em doces e 2,4 euros em macas")
underscores("Eu    não sei se   eu quero continuar .")
codigo_postal(["4700-000","1234-567","8541-543","4123-974","9481-025"])
