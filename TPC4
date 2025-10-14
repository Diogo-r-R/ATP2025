sala1=[200, [90,91,92,95,96,97,98,99,102,103,104,105,112,119,120,121,122], 'Good will hunting']
sala2=[150, [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
              76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], 'Matrix']
sala3=[150, [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
              76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], 'Whiplash']
sala4=[150, [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 
             65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 
             96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 
             122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 
             147, 148, 149, 150], 'inside out']
sala5=[150, [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
              76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], 'Pirates of the Caribbean']
cinema=[sala1,sala2,sala3,sala4,sala5]
filme=()
lugar=0

def listarsala(cinema):
        print("" \
        "FILMES EM EXIBIÇÃO:")
        i=0
        for s in cinema:
              print(f"{s[2]} / Sala {i+1} / {s[0]} lugares")
              i= i+1
    
def lugaresocupados():
    lug=int(input("De que sala quer ver a lista de lugares ocupados?"))
    i=0
    while i<1:
        if lug==1:
            print(sala1[1])
        elif lug==2:
            print(sala2[1])
        elif lug==3:
            print(sala3[1])
        elif lug==4:
            print(sala4[1])
        elif lug==5:
            print(sala5[1])
        else:
            print("Esta sala não existe...")
        i=i+1
    return

def venderbilhete():
    bilhetesala=int(input("Para que sala quer comprar o bilhete?"))
    bilhete= int(input("Insira o lugar que deseja comprar?"))
    var=[]
    if bilhetesala == 1:
        sala1[1].append(bilhete)==var
    elif bilhetesala == 2:
        sala2[1].append(bilhete)==var
    elif bilhetesala == 3:
        sala3[1].append(bilhete)==var
    elif bilhetesala == 4:
        sala4[1].append(bilhete)==var
    elif bilhetesala == 5:
        sala5[1].append(bilhete)==var
    else:
        print("Esta sala não existe")
    return var

def disponivelsala(cinema, filme, lugar):
    j = -1
    filme=input("Para que filme quer comprar o bilhete?")
    lugar=int(input("Que lugar quer comprar?")) 
    for i in range(len(cinema)):
        if filme == cinema[i][2]:
            j = i
            break
    if j == -1:
        print("Este filme não está em exibição! :c")
        return False
    if lugar in cinema[j][1]:
        print("Este lugar não está disponível. :C")
        return False
    else:
        print(f"O lugar {lugar} está disponível. c:")
        return True

def inserirsala():
    novalista=[]
    lugares=int(input("Quantos lugares tem a sala?"))
    i=0
    while i<1:
        if lugares>0 and lugares<=200:
            novalista.append(lugares)
            i=i+1
        else:
            print("Número inválido. Tente novamente.")
            lugares=int(input("Quantos lugares tem a sala?"))
    ocupados=[]
    novalista.append(ocupados)
    filme=input("Qual o filme em exibição?")
    novalista.append(filme)
    cinema.append(novalista)
    print("Sala adicionada! c:")
    return cinema

def cinema_menu():
    x=True
    print(" Cinema App ")
    print("Ver salas e detalhes [1]")
    print("Ver lugares ocupados [2]")
    print("Verificar lugar disponível [3]")
    print("Comprar bilhete [4]")
    print("Inserir sala [5]")
    print("Sair [0]")
    while x==True:
        pergunta=int(input("O que deseja fazer?"))
        if pergunta==1:
            listarsala(cinema)
        elif pergunta==2:
            lugaresocupados()
        elif pergunta==3:
            disponivelsala(cinema,filme,10)
        elif pergunta==4:
            venderbilhete()
        elif pergunta==5:
            inserirsala() 
        elif pergunta==0:
            print("Até à próxima! c:")
            x=False
            exit()




cinema_menu()
