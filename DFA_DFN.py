



#from functools import parcital







"""def DFA(transicoes, estado, terminais, st) -> bool:
   
    for c in st:
        try:
            estado = transicoes[estado, c]
        except KeyError:
            return False
    return estado in terminais

def DFN_DFA(transicoes, estados, terminais, st) -> bool:
    estados = estados.copy()
    for c in st:
        novos_estados = set()
        for estado in estados:
            novos_estados.update(transicoes.get((estado, c), ()))
        estados = novos_estados
            
    return bool(estados.intersection(terminais))


def receber_transica():
    t1 = {}
    while(True):
        palavra = input("DIGITE A TRASICAO:") 
        pal=palavra.replace("<", "")
        pal=pal.replace(">", "")
        pal=pal.replace("{", "")
        pal=pal.replace("}", "")
        pal = pal.split(",")

        tam = len(pal)
        if tam == 3:
            t1[pal[0],pal[1]] = {pal[2]}  
        elif tam == 4:
            t1[pal[0],pal[1]] = {pal[2],pal[3]}
        elif tam == 5:
            t1[pal[0],pal[1]] = {pal[2],pal[3],pal[4]}

        opcao = input("MAIS TRANSICOES?...  \n 1)-SIM   \n 2)-NAO  \n ->")
        
        if opcao == "2":
            break
    return t1

transicoes = receber_transica()

estado  = {input("QUAL E O SEU ESTADO INICIAL:")}


st = input("PALAVRA A TEXTAR:")

if DFN_DFA(transicoes,estadoin, estadofinal, st):
    print(" palavra aceite")
else:
    print(" pal nao aceite")

estado= input("QUAL E O SEU ESTADO FINAL:")
estado = estado.replace("{", "")
estado = estado.replace("}", "")
estado = estado.split(",")
if len(estado) == 2:
    estadofinal ={estado[0],estado[1]}
elif len(estado)== 3:
     estadofinal ={estado[0],estado[1],estado[2]}
else:
     estadofinal ={estado[0]}

print(estadofinal)"""

transicoes = {
    ("q0","a"): {"q1"},
    ("q1","b"): {"q3"},
    ("q2","c"): {"q4"},
   
}
arquivo = open("l.lfa", 'w')
i = 0
for v in transicoes:
    t = transicoes[v]
    for j in t:
        T= j
        arquivo.write('<'+v[i]+','+v[i+1] +','+'{'+T+'}'+'>'+'\n')

for v in transicoes:
     print(v)
