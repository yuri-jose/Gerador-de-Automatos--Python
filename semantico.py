from sintatico import Sintatico
class Semantico:
    def __init__(self):
        pass

    objSintatico=Sintatico()

    Linhas_do_ficheiro = []
    Arquivo = 'file.lfa'
    with open(Arquivo) as ojct:
      for linha in ojct:
        Linhas_do_ficheiro.append(linha)

#*********** exex direita ***************************************************
        def DFN_DFA(self,transicoes, estados, terminais, st) -> bool:

            estados = estados.copy()
            for c in st:
                novos_estados = set()
                for estado in estados:
                    novos_estados.update(transicoes.get((estado, c), ()))
                estados = novos_estados
                    
            return bool(estados.intersection(terminais))

 #******************************************************************************

        def DFN_DFA_PASSO_APASSO(self,transicoes, estados, terminais, st) -> bool:

            estados = estados.copy()
            for c in st:
                novos_estados = set()
                for estado in estados:
                    novos_estados.update(transicoes.get((estado, c), ()))
                    print('\n',estado +" leu ",c)
                    print("transita para",novos_estados)
                    print("\n==========================")
    
                estados = novos_estados
                    
            return bool(estados.intersection(terminais))           

        def receber_transica(self):
            t1 = {}
            while(True):
                palavra = input("\n\tDIGITE A TRASICAO:") 
                verificacao=self.objSintatico.analise_sintaxe_auto(palavra)
                if verificacao == 0:
                    print("\tTransicao invalida!")
                    continue
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
 #****************************************************  
        def receber_transica_file(self,list):
            t1 = {}
            for x in list:    
                while(True):
                    palavra = x 
                    verificacao=self.objSintatico.analise_sintaxe_auto(palavra)
                    if verificacao == 0:
                        print("\tTransicao invalida!")
                        return t1
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
            return t1         
        
    