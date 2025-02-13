# 1)

def reverse(s):
    f = ""
    cont = -1
    while abs(cont) <= len(s):
        f = f + s[cont]
        cont -= 1
    return f


# 2) 
# 2.1)
# opção mais simples

def procura_aA(s):
    c = 0
    s = s.lower()
    for l in s:
        if l == "a":
            c += 1
    return c

# 2.2)
# outra opção

def procura_aA_2(s):
    c1 = 0
    c2 = 0
    for l in s:
        if l == "a":
            c1 += 1
        elif l == "A":
            c2 += 1
    return (f"Número de A presentes:"+ str(c2) +"; Número de a presentes: "+ str(c1))


# 3)

def vogais(s):
    c = 0
    s = s.upper()
    for l in s:
        if l == "A" or l == "E" or l == "I" or l == "O" or l == "U":
            c += 1
    return c

# 4)

def minusculo(s):
    res = s.lower()
    return res


# 5)

def maiusculo(s):
    res = s.upper()
    return res



# 6)

def capicua(s):
    r = True
    s1 = s
    s2 = reverse(s)
    if s1 != s2:
        r = False
    return r


# 7)

def verificacao_caracteres(s1,s2):
    l_s1 = []
    l_s2 = []
    r = True
    for l in s1:
        if l not in l_s1:
            l_s1.append(l)
    for l in s2:
        if l not in l_s2:
            l_s2.append(l)
    for elem in l_s1:
        if elem not in l_s2:
            r = False
    return r


# 8)
# 8.1)
# opcao por letras

def ocorrencias1(s1,s2):
    l_s1 = []
    l_s2 = []
    cont = {}
    for l in s1:
        if l not in l_s1:
            l_s1.append(l)
    for l in s2:
        l_s2.append(l)
    for l in l_s1:
        for elem in l_s2:
            if l == elem:
                if elem not in cont:
                    cont[elem] = 1
                else:
                    cont[elem] += 1
         
    return cont

# 8.2)
# opcao por expressões

def ocorrencias2(s1,s2):
    res = s2.count(s1)
    return res


# 9) 

def anagrama(s1,s2):
    r = True
    a = sorted(s1)
    b = sorted(s2)
    if a != b:
        r = False
    return r


# 10)

def tabela_classes(lista_palavras):
    dicionario = {}
    for elem in lista_palavras:
        chave = ''.join(sorted(elem))
        if chave not in dicionario:
            dicionario[chave] = [elem]
        else:
            dicionario[chave].append(elem)

    return print(dicionario)


# TESTES:

print(reverse("afonso"))
print(procura_aA("abAnanado"))
print(procura_aA_2("abAnAnado"))
print(vogais("AlfabEto"))
print(minusculo("ISSO"))
print(maiusculo("exatamente"))
print(capicua("ovo"))
print(verificacao_caracteres("amanha esta sol","amanha vai estar sol no parque "))
print(verificacao_caracteres("amamha esta sol","amanha"))
print(ocorrencias1("data","datado"))
print(ocorrencias2("brinca","brincadeirabrinbrincar"))
print(anagrama("silent","listen"))
print(anagrama("hello","world"))
tabela_classes(["samba","roma","amor","ambas","maro","maratona","anotaram"])
