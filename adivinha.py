print("jogo do adivinha")
jogador=int(input('Escreve "1" para seres a escolher um número e o computador a adivinhar e "2" para ser o computador a escolher e tu a adivinhares: '))



if jogador==1:
    print('''REGRAS:
      -Indica se o número que pensaste é menor "<" ou maior ">" do que o número que o computador adivinhou;
      -Caso seja igual escreve "=". ''')
    from math import ceil
    num=50
    div=25
    input("""
            -pensa num número entre 1 e 100. """)
    valor=input("O teu número é 50? ")
    num_adv=1   
    while valor!="=":
        num_adv+=1
        if valor=="<":
            num=int(num-div)
            div=ceil((div/2))
            valor=input(f"o teu número é {num}? ")
        elif num==99 and valor==">":
            num+=1
            num_adv-=1
            break
        elif valor==">":
            num=int(num+div)
            div= ceil((div/2))
            valor=input(f"o teu número é {num}? ")
        else:
            print(f"{valor} é invalido")
            valor=input("O teu número é 50? ")
    
    print(f"o teu número é {num}!")
    if num_adv==1:
        print(f"O computador adivinhou em {num_adv} jogada")
    else:
        print(f"O computador adivinhou em {num_adv} jogadas")
elif jogador==2:
    print("""REGRAS:
          -tenta adivinhar o número que o computador escolheu, estando este compreendido entre 1 e 100;
          -O computador vai indicar se o número que escolheste é igual maior ou menor que o número que o computador escolheu.""")
    from random import randint
    num=randint(1,100)
    print("O computador pensou numn número.")
    adv=int(input("""tenta adivinhar qual o número que o computador escolheu!
          Escreve um número entre 1 e 100: """))
    num_adv=1
    while adv!=num:
        num_adv+=1
        if adv<num:
            print(f"O número que o computador escolheu é maior que {adv}.")
            adv=int(input("escolhe outro número: "))
        elif adv>num:
            print(f"O número que o computador escolheu é menor que {adv}.")
            adv=int(input("escolhe outro número: "))
        elif adv!=(1,101):
            print(f"{adv} é um número invalido!")
            adv=int(input("""tenta adivinhar qual o número que o computador escolheu!
          Escreve um número entre 1 e 100: """))
    if num_adv==1:
        print(f"""Acertaste em {num_adv} jogada!
          O número que o computador pensou é {adv}""")
    else:
        print(f"""Acertaste em {num_adv} jogadas!
          O número que o computador pensou é {adv}""")

    
elif jogador!=(1,3):
    print(f"{jogador} é inválido")




                
            
