import os
from colorama import Fore, Back, Style, init
import pickle
import shutil
import time

init(autoreset=True)

while True:
    # Limpa a tela do CMD
    os.system('cls' if os.name == 'nt' else 'clear')
    

    # Opções do menu
    print(Style.BRIGHT + Fore.RED + "=" * 30)
    print(Fore.YELLOW + "             MENU         ")
    print(Style.BRIGHT + Fore.RED + "=" * 30)
    print(Style.BRIGHT + Fore.GREEN + "[ 1 ] Criar conta")
    print(Style.BRIGHT + Fore.GREEN + "[ 2 ] Login")
    print(Style.BRIGHT + Fore.GREEN + "[ 3 ] Gerenciamento")
    print(Style.BRIGHT + Fore.GREEN + "[ 0 ] Sair do programa")
    print(Style.BRIGHT + Fore.RED + "=" * 30)
    
    opcao = input(Style.BRIGHT + Fore.GREEN + "\nEscolha uma opção: ")

    os.system('cls' if os.name == 'nt' else 'clear')
    
    #ok
    if opcao == "1":
        print(Style.DIM + Fore.YELLOW + "\n-> Preencha os campos e pressione enter")
        usuario = input(Fore.LIGHTCYAN_EX + "\nUsuario: ")
        senha = input(Fore.LIGHTCYAN_EX + "\nSenha: ")

        os.system('cls' if os.name == 'nt' else 'clear')

        user = {
        "usuario": [usuario],
        "senha": [senha]
        }

        with open(f"usuario_{usuario}.pkl", "wb") as arquivo:
         pickle.dump(user, arquivo)

        print(Style.BRIGHT + Fore.GREEN + "\nUSUARIO CRIADO!")
        time.sleep(1)
        print(Style.DIM + Fore.YELLOW + "\nRETORNANDO AO MENU...")
        time.sleep(1)

    #a criar 
    if opcao == "2":
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Style.BRIGHT + Fore.YELLOW + "\nFaça seu login")
            
            login_user = input(Style.BRIGHT + Fore.GREEN + "\nUSUARIO:")
            login_senha = input(Style.BRIGHT + Fore.GREEN + "\nSENHA:")

            buscar_user = login_user 
            buscar_senha = login_senha

            arquivo_buscar = f"usuario_{buscar_user}.pkl"

            try:
                with open(arquivo_buscar, "rb") as dado:
                 dado_valido = pickle.load(dado)

            except FileNotFoundError:
               print(Style.BRIGHT + Fore.RED + "\nUSUARIO OU SENHA INVALIDOS""\nTente novamente")
               time.sleep(2)
               break
                
            else:
                if buscar_user in dado_valido["usuario"]:

                    if buscar_senha in dado_valido["senha"]:

                        print(Style.BRIGHT + Fore.GREEN + "\nLOGIN REALIZADO COM SUCESSO!")
                        time.sleep(2)
                        break
                    if buscar_senha not in dado_valido["senha"]:
                        print(Style.BRIGHT + Fore.RED + "\nUSUARIO OU SENHA INVALIDOS""\nTente novamente")
                        time.sleep(2)
                    break
                if buscar_user not in dado_valido["usuario"]:

                    print(Style.BRIGHT + Fore.RED + "\nUSUARIO OU SENHA INVALIDOS""\nTente novamente")
                    time.sleep(2)
                    break
                break


         

    #ok
    if opcao == "3":
        while True:
            
            print(Style.DIM + Fore.YELLOW + "\n-> Qual usuario deseja editar?")

            usuario_search = input(Fore.LIGHTCYAN_EX + "\nDigite um nome de usuario ou insira ""R"" para retornar:")
            os.system('cls' if os.name == 'nt' else 'clear')

            if usuario_search == "R":
               print(Style.DIM + Fore.YELLOW + "\nRETORNANDO AO MENU...")
               time.sleep(3)
               break

            arquivo_buscar = f"usuario_{usuario_search}.pkl"

            try:
                with open(arquivo_buscar, "rb") as dado:
                 dado_valido = pickle.load(dado)

            except FileNotFoundError:
               print(Style.BRIGHT + Fore.RED + "\nUSUARIO OU SENHA INVALIDOS""\nTente novamente")
               time.sleep(2)
               break    
            else:
  
        
                print(Style.DIM + Fore.YELLOW + f"\nO que deseja editar em {usuario_search}?")
                print(Style.BRIGHT + Fore.RED + "=" * 30)
                print(Style.BRIGHT + Fore.GREEN + "[ E ] Editar")
                print(Style.BRIGHT + Fore.GREEN + "[ D ] Deletar")
                print(Style.BRIGHT + Fore.GREEN + "[ R ] Retornar")
                print(Style.BRIGHT + Fore.RED + "=" * 30)

                select_edition = input(Fore.LIGHTCYAN_EX + "\nSelecione:")
                os.system('cls' if os.name == 'nt' else 'clear')

            

                # Sessão de alteração de dados
                if select_edition == "E":

                    novo_user = input(Fore.LIGHTCYAN_EX + "\nNovo nome de usuario:")
                    nova_senha = input(Fore.LIGHTCYAN_EX + "\nNova senha:")

                    os.system('cls' if os.name == 'nt' else 'clear')

                    antigo_arquivo = f"usuario_{usuario_search}.pkl"
                    novo_arquivo = f"usuario_{novo_user}.pkl"

                    
                    with open(antigo_arquivo, "rb") as arquivo:
                        dados = pickle.load(arquivo)
                        dados["usuario"] = novo_user
                        dados["senha"] = nova_senha

                    time.sleep(1)

                    # se o nome mudar apaga o antigo e substitui
                    if antigo_arquivo != novo_arquivo:
                        #salva os dados no arquivop novo
                        with open(novo_arquivo, "wb") as arquivo:
                            pickle.dump(dados, arquivo)
                        
                        # apaga o antigo
                        if os.path.exists(antigo_arquivo):
                            os.remove(antigo_arquivo)
                    else:
                        #se o nome e igual vai reultilizar
                        with open(antigo_arquivo, "wb") as arquivo:
                            pickle.dump(dados, arquivo)

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "\nUSUARIO ALTERADO!")

                    break     

               
                elif select_edition == "D":
                    
                    nome_delete = f"usuario_{usuario_search}.pkl"

                    if os.path.exists(nome_delete):
                     os.remove(nome_delete)
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Style.BRIGHT + Fore.RED + "USUARIO DELETADO")
                    time.sleep(3)
                    break
                elif select_edition == "R":
                    break
                
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Style.BRIGHT + Fore.RED + "\nERRO - TENTE NOVAMENTE")

        

    if opcao == "0":
        print(Style.BRIGHT + Fore.YELLOW + "\nEncerrando o programa!")
        break 
    else:
        # print(Fore.RESET + "\nOpção inválida! Tente novamente.")
        input("\nPressione Enter para continuar...")
