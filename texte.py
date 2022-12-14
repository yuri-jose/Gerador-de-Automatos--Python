




def AFD():
        Transicoes = []
        print("==================================================================")
        estadoIn = input("QUAL E O SEU ESTADO INICIAL:")
        estadof = input("QUAL E O SEU ESTADO FINAL:")
        while(True):
            transi = input("DIGITE A TRASICAO:")
            Transicoes.append(transi)
            opcao = input("MAIS TRANSICOES?...  \n 1)-SIM   \n2)-NAO")
            if opcao == "2":
                break
            
        palavra = input("PALAVRA A SER TEXTADA:")
        palavra2 = ""
        b=0
        for x in Transicoes:
            b+=1
        ij=0
        fim =""
        str =""
        c=False
        ven =0
        for  i in palavra:
         for j in Transicoes:
            ij+=1
            str=j[1]+j[2]
            if estadoIn== str or c:
             c=True
            if i in j:
                palavra2+=i
            else:
                ven=1
            fim=j[6]+j[7]
        if palavra2 == palavra and fim == estadof and ven == 0:   
            print("==================================================================")
            print("PALAVRA ACEITE PARA O AUTOMATO")    
        else:
            print("==================================================================")
            print("PALAVRA INVALIDA PARA O AUTOMATO")

AFD()