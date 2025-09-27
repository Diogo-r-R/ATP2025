#TPC2
#jogo dos fósforos

    input("carrega para começar o jogo")
    print("jogo do fosforo")
    
    jogador=input("escreve 1 para jogar em primeiro ou 2 para começar em segundo: ")
    if  jogador == "1":
        print("És o jogador 1")
        numero_inicial=21
        while numero_inicial>=1:
            print(numero_inicial)
            retirados=int(input(f"escolhe um número entre 1 e 4 para retirar a {numero_inicial}: "))
            numero_inicial= numero_inicial - retirados
            print(numero_inicial)
            numero_computador= 5 - retirados
            numero_inicial= numero_inicial - numero_computador
            print(f"o computador retirou {numero_computador}")
            if numero_inicial == 1:
                print("sobrou apenas 1 fósforo")
                print("o computador ganhou")
                break 
    else:
        print("És o jogador 2")
        numero_inicial=21
        
        while numero_inicial>=1:
            print(numero_inicial)
            numero_computador=1
            numero_inicial=numero_inicial-numero_computador
            print("O computador retirou 1")
            print(numero_inicial)
            retirados=int(input(f"escolhe um número entre 1 e 4 para retirar a {numero_inicial}: "))
            numero_inicial-=retirados
    
            while numero_computador + retirados == 5:
                print(numero_inicial)
                numero_computador=1
                numero_inicial=numero_inicial-numero_computador
                print("O computador retirou 1")
                print(numero_inicial)
                retirados=int(input(f"escolhe um número entre 1 e 4 para retirar a {numero_inicial}: "))
                numero_inicial-=retirados
                if numero_inicial == 1:
                        print("sobrou apenas 1 fósforo")
                        print("Você ganhou")
                        break 
            else:
                numero_computador= 4-retirados
                numero_inicial=numero_inicial-numero_computador
                print(f"O computador retirou {numero_computador}")
                while numero_inicial>=1:
                    print(numero_inicial)
                    retirados=int(input(f"escolhe um número entre 1 e 4 para retirar a {numero_inicial}: "))
                    numero_inicial= numero_inicial - retirados
                    print(numero_inicial)
                    numero_computador= 5 - retirados
                    numero_inicial= numero_inicial - numero_computador
                    print(f"o computador retirou {numero_computador}")
                    if numero_inicial == 1:
                        print("sobrou apenas 1 fósforo")
                        print("o computador ganhou")
                        break 
            if numero_inicial==1:
                break
