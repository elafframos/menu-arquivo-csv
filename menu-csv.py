import csv

def menu():     #Função menu para 
    print('''\n[1]Leia o arquivo
[2]Modifique
[3]Sair''')



def leia():     #Função para ler um arquivo csv que o usúario escolher!
    if escolha == 1:
        arquivo = input('''\nDigite qual arquivo você quer ler: ''')
        
        with open(arquivo, 'r') as file:  # Para ler um arquivo csv
            reader  = csv.reader(file)
            for row in reader:
                print('\n',row)


def modifique():    #Função para modificar um arquivo csv que o usúario escolher!
    if escolha == 2:
        pergunta = input('\nDigite o arquivo você quer modificar: ')
        pergunta1 = input('\nDigite um nome: ')

        with open(pergunta, 'a', newline='') as file:    #Para adicionar algo a esse arquivo csv!
            file.write(pergunta1)

def encerrar():     #Função para fechar o programa!
    if escolha == 3:
        print('\nPrograma encerrado com sucesso!\n')


while menu:     #Laço de repetição

    menu()
    escolha = int(input('\nEscolha uma das opções acima: '))
    if escolha == 1:
        leia()
        continue
    if escolha == 2:
        modifique()
        continue
    if escolha == 3:
        encerrar()
        break
