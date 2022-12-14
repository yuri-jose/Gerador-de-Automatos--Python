import os
from Lexico import Lexico
from sintatico import Sintatico
from semantico import Semantico
class main:
    def __init__(self):
        pass
    obj=Lexico()
    obj2=Sintatico()
    obj3=Semantico()

    def abre_o_automato_no_ficheiro(Nome_do_arquivo):
     Recebe_as_Linhas_e_poe_nalista=[]
     with open(Nome_do_arquivo) as novo_objecto_do_tipo_filr:
        for pegacada_linha in novo_objecto_do_tipo_filr:
            Recebe_as_Linhas_e_poe_nalista.append(pegacada_linha)
        return Recebe_as_Linhas_e_poe_nalista

   
    opcao_Digitada = ""
    transicoes = {}

    while(opcao_Digitada != "5"):
        os.system("clear")
        print("========================+========================")
        print(" |           AFD-AFND-INTERPRETER  (2021)      |")
        print("========================+========================")
        print("\t1)-ABRIR                     ")
        print("=================================================")
        print("\t2)-INTERPRETAR                         | ")
        print("================================================")
        print("\t3)-GUARDAR                             | ")
        print("================================================")
        print("\t4)-CARREGAR                            |")
        print("================================================")
        print("\t5)-SAIR                                |")
        print("================================================")
        opcao_Digitada =input("OPCAO:")
        if opcao_Digitada == "1":
            os.system("clear")
            print("=============================================")
            print("  |     THE AUTOMAT FOR INTERPRET          | ")
            print("=============================================")
            novo_ficheiro =input("DIGITE O NOME DO FICHEIRO. ex filename.lfa:")
            arquivo =""
            try:
                arquivo =open(novo_ficheiro,'r')
                x = arquivo.read()
                print(x) 
                type(x)
            except FileNotFoundError:
                print(" arquivo inexistente")
               
            print("===============================================")
            x=input("QUALQUER TECLA PRA VOLTAR: ")
        elif opcao_Digitada == "2":

            
            if 0 == 0 :
                os.system("clear")
                transicoes = obj3.receber_transica()

                op = ""
                while op != "3":
                    os.system("clear")
                    
                    print("===============================================")
                    print("                INTERPRETAR                  ")
                    print("===============================================")
                    print("\t1)-EXECUTAR")
                    print("===============================================")
                    print("\t2)-EXECUTAR PASSO A PASSO")
                    print("===============================================")
                    print("\t3)-SAIR")
                    print("===============================================")
                
                    op = input("\topcao:")
                    if op == "1":
                        os.system("clear")
                        print("\n\nTRANSICOES = ",transicoes)
                        print("\t===============================================")
                        print("\t             EXECUSAO DIREITA")
                        print("\t===============================================")
                        
                        
                        estado = input("\tQUAL E O SEU ESTADO INICIAL: ")
                        estado = estado.replace("{", "")
                        estado = estado.replace("}", "")
                        estado = estado.split(",")
                        if len(estado) == 2:
                            estadoin ={estado[0],estado[1]}
                        elif len(estado)== 3:
                            estadoin ={estado[0],estado[1],estado[2]}
                        else:
                            estadoin ={estado[0]}

                        estado = input("\tQUAL E O SEU ESTADO FINAL:")
                        
                        estado = estado.replace("{", "")
                        estado = estado.replace("}", "")
                        estado = estado.split(",")
                        if len(estado) == 2:
                            estadofinal ={estado[0],estado[1]}
                        elif len(estado)== 3:
                            estadofinal ={estado[0],estado[1],estado[2]}
                        else:
                            estadofinal ={estado[0]}

                        while True:
                            palavra= input(" \n\tPALAVRA A TEXTAR: ")

                            if obj3.DFN_DFA(transicoes,estadoin,estadofinal,palavra):
                                print("\t\n= PALAVRA ACEITE =\n")
                            else:
                                print("\t\n= PALAVRA NAO ACEITE =\n")
                            
                            op = input("\n\tTEXTAR MAIS PALAVRA? \n 1)-SIM   \n 2)-NAO  \n ->")
                            
                            if op == "2":
                                break

                    elif op == "2": 
                        os.system("clear")  
                        print("\n\nTRANSICOES = ",transicoes)
                        print("===============================================")
                        print("             PASSO A PASSO")
                        print("===============================================")

                        estado = input("\tQUAL E O SEU ESTADO INICIAL: ")
                        estado = estado.replace("{", "")
                        estado = estado.replace("}", "")
                        estado = estado.split(",")
                        if len(estado) == 2:
                            estadoin ={estado[0],estado[1]}
                        elif len(estado)== 3:
                            estadoin ={estado[0],estado[1],estado[2]}
                        else:
                            estadoin ={estado[0]}

                        estado = input("\tQUAL E O SEU ESTADO FINAL:")
                        
                        estado = estado.replace("{", "")
                        estado = estado.replace("}", "")
                        estado = estado.split(",")
                        if len(estado) == 2:
                            estadofinal ={estado[0],estado[1]}
                        elif len(estado)== 3:
                            estadofinal ={estado[0],estado[1],estado[2]}
                        else:
                            estadofinal ={estado[0]}

                        while True:
                            palavra= input(" \n\tPALAVRA A TEXTAR: ")

                            if obj3.DFN_DFA_PASSO_APASSO(transicoes,estadoin,estadofinal,palavra):
                                print("\t\n= PALAVRA ACEITE =\n")
                            else:
                                print("\t\n= PALAVRA NAO ACEITE =\n")
                            
                            op = input("\n\tTEXTAR MAIS PALAVRA? \n 1)-SIM   \n 2)-NAO  \n ->")
                            
                            if op == "2":
                                break                   
                
        if opcao_Digitada == "3":
            os.system("clear")
            print("\n\ntTRANSICOES = ",transicoes)
            novo_ficheiro =input("DIGITE O NOME DO FICHEIRO. ex filename.lfa:")
            arquivo = open(novo_ficheiro , 'w')
            i = 0
            for v in transicoes:
                t = transicoes[v]
                for j in t:
                    T= j
                    arquivo.write('<'+v[i]+','+v[i+1] +','+'{'+T+'}'+'>'+'\n')
            arquivo.close()    
            
            print("GUARDADO COM SUCESSO")
            input("esperando")
        elif opcao_Digitada == "4":
            os.system("clear")
            print("==========»======================================")
            print("  (ESCOLHEU A OPCAO DE CARREGAR UM NOVO FICHEIRO)  ")
            print("=================================================")
            novo_ficheiro =input("DIGITE O NOME DO FICHEIRO A CARREGAR:")
            try:
              v =  abre_o_automato_no_ficheiro(novo_ficheiro)
              print(v)
              transicoes = obj3.receber_transica_file(v)
              input("esperando")
            except FileNotFoundError:
                print(" arquivo inexistente")
