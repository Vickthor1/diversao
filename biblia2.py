import random
print('---Cadastro da Biblioteca---')
usuarios = ['adm']
senhas = ["2023202420232024"]
a = "!@#$%¨&*"
V = [mascarada.replace("1","V")
     .replace("2",(random.choice(a)))
     .replace('3',(random.choice(a)))
     .replace('4',(random.choice(a)))
     .replace('5',(random.choice(a)))
     .replace('6',(random.choice(a)))
     .replace('7',(random.choice(a)))
     .replace('8',(random.choice(a)))
     .replace('9',(random.choice(a)))
     .replace("0",(random.choice(a)))
     for mascarada in senhas]
def registro():
    while True:
        print("Se deseja adicionar um novo usuário digite 1")
        print("Se deseja fazer login 2")
        print("Se deseja acessar a lista de usuários 3")
        print("Se deseja sair digite 4")
        escolha = input("Digite sua escolha: ")
        print("")

        if escolha == "1":
            print('-Adicionar usuário-')
            nome = str(input(' '))
            print("")
            usuarios.append(nome)
            
            senha = int(input(' '))
            print("")
            senhas.append(senha)
            print("Cadastro finalizado. Usuários cadastrados!")
            print("")
            x = int(input("Deseja sair? 1-Sim/2-Não "))
            if x == 1:
                break
            if x == 2:
                pass
        
        elif escolha == "2":
            nome = str(input("Digite o Nome do usuário: "))
            print("")
            if nome in usuarios:
                x = usuarios.index(nome)
                senha = str(input("Digite a senha do usuário: "))
                print("")
                if senha in senhas[x]:
                    print('Login efetuado com sucesso!')
                    print("")
                    print("Deseja sair? 1-Sim/2-Não")
                    resp = int(input(" "))
                    if resp == 1:
                        break
                    if resp == 2:
                        pass
                else:
                    print("Senha de usuário incorreta")
                    pass
                
            else:
                print('Usuário não encontrado!')
            pass
        elif escolha == "3":
            print("Usuários:")
            for user in usuarios:
                print(user)
            
            print("")    
            print("Deseja sair? 1-Sim/2-Não")
            x = int(input(" "))
            if x == 1:
                break
            if x == 2:
                pass
            
        if escolha == "4":
            print('Até brave!')
            break
        
        else:
            print("")
            print("Opção inválida. Tente novamente.")
            pass

registro()

for i in range(len(usuarios)):
    print("usuário: ",usuarios[i],"/ Senha: ",V[i])
