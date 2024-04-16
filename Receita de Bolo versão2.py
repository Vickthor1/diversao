#Rceita de Bolo
#ENTRADA -> PROCESSAMENTO ->SAIDA
#Problema: fazer um bolo chocolate
#IDE vscode LP Python

#Passo 1: Identificação do problema. 
#Passo 2: Escolha das Ferramentas
#Passo 3: Implementação, Testes, Validações ... 

###Entradas###
#Ingredientes 
#uma colher de chá fermento
#3 xícaras de farinha
#3 ovos
#2 xicaras cacau em pó(chocolate)
#1 xicara leite
#1/2 xicara margarina
#uma lata chatilly
#3 xícaras açucar
#meia colher de chá de sal

###Processamento###
#seprar uma vasilha para misturar os ingredientes
#acrescentar os ingredientes na vasilha
#misturar os ingedientes na vasilha ate ficar homogeneo
#untar um forma com margarina e colocar os ingedientes misturados
#ligar o forno 180 graus por 10 minutos
#colocar a vasilha no forno pré-aquecido
#esperar 45 minutos para assar (Verificar!!)
#retirar o bolo do forno, apenas se tiver pronto
#colocar o bolo na mesa para esfriar
#prepara a cobertura
#servir 
#Fim
while True:
    def fazer_bolo():
            # fermento =  1
            # ovos = 3 
            # farinha = 3
            # chocolate = 2
            # leite = 1
            # margarina = 0.5
            # chantilly = 1
            # acucar = 3
            # sal = 0.05
        
        ingredientes = {
            "fermento":   1,
            "ovos": 3, 
            "farinha":  3,
            "chocolate": 2,
            "leite": 1,
            "margarina":  0.5,
            "chantilly": 1,
            "acucar": 3,
            "sal": 0.05
        }

    #modo de preparo
    
    print("Separe uma vasilha para misturar os ingredientes")
    
    print("Acrescentar os ingredientes na vasilha")
    
    mistura_massa = ["fermento", "ovos", "farinha", "chocolate", "leite", "acucar","sal"]
    
    print("Misturar os ingedientes na vasilha ate ficar homogeneo")
    
    print("Unte a forma e coloque os ingredientes")

    #temperatura = 180
    while True:
        temperatura = int(input("Digite a temperatura do forno "))
        if temperatura == 180:
            break
        elif temperatura > 180:
            print('Muito quente!!!')
            pass
        elif temperatura < 180:
            print('Muito frio!!!')
            pass
    #tempo = 10
    while True:
     print('')
     tempo_pre = int(input("Entre com o tempo de pre-aquecimento "))

     if tempo_pre == 10:
         break
     
     elif tempo_pre > 10:
         print('')
         print('Pouco tempo')
         pass
     
     elif tempo_pre < 10:
         print('')
         print('Muito tempo')
         pass
    
    print('')

    print(f"Aqueça o forno em {temperatura} por {tempo_pre}")
    
    print('')

    print("Coloque a vasilha no forno pré-aquecido")

    print('')

    #tempo_preparo = 45
    
    #verificar se o bolo esta assado
     
    print("Verificando se o bolo esta assado")

    print('')
    
    while True:
     tempo_preparo = int(input("Digite o tempo de preparo "))
     print('')
     if tempo_preparo >= 45:
            print("Bolo Assado! Pode retirar do forno e colocar na mesa")
            print('')
            print("Colocar a cobertura e Servir!!")
            break
     else:
      print("Bolo está cru, apressado! Espere")
      pass

    break
