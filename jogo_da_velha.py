from os import system, name 
from time import sleep

def limpar_tela():
    system('cls' if name == 'nt' else 'clear')

def print_velha(velha):
    for i in range(len(velha)):
        for j in range(len(velha)):
            print('|', velha[i][j], end=' ')

        print('|')

def limite_de_jogo(limite):
    if limite == 0:
        print('Deu velha!')
        exit()

def menu():
    print('-' * 30)
    print('JOGO DA VELHA'.center(30))
    print('-' * 30)

def vitoria_vertical(matriz):
    for i in range(3):
        if matriz[i][0] == 'X' and matriz[i][1] == 'X' and matriz[i][2] == 'X': 
            print('jogador_1 venceu!')
            exit()

        if matriz[i][0] == 'O' and matriz[i][1] == 'O' and matriz[i][2] == 'O': 
            print('jogador_2 venceu!')
            exit()

def vitoria_horizontal(matriz):
    for i in range(3):
        if matriz[0][i] == 'X' and matriz[1][i] == 'X' and matriz[2][i] == 'X': 
            print('jogador_1 venceu!')
            exit() 

        if matriz[i][0] == 'O' and matriz[i][1] == 'O' and matriz[i][2] == 'O': 
            print('jogador_2 venceu!')
            exit()

def vitoria_diagonal(matriz):
    if matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X': 
        print('jogador_1 venceu!')
        exit()
    if matriz[0][2] == 'X' and matriz[1][1] == 'X' and matriz[2][0] == 'X':
        print('jogador_1 venceu!')
        exit()

    if matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O': 
        print('jogador_2 venceu!')
        exit()
    if matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == 'O':
        print('jogador_2 venceu!')
        exit()

def main():
    matriz = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
            ]
    
    jogador_1 = True
    jogador_2 = False 
    limite = 9 
    
    menu()
    while True:
    
        if jogador_1: print('Vez do jogador 1\n')
        else: print('Vez do jogador 2\n')
    
        if jogador_1:
            jogador_1 = False 
            jogador_2 = True 
            l = int(input('Linha: '))
            c = int(input('Coluna: '))
    
            while True:
                if l < 1 or l > 3 or c < 1 or c > 3 or matriz[c-1][l-1] != ' ':
                    print('\nMovimento invalido!\n')
                    sleep(1)
                    limpar_tela()
                    print('Vez do jogador 1\n')
    
                    l = int(input('Linha: '))
                    c = int(input('Coluna: '))      
                    continue
                break  
    
            matriz[c-1][l-1] = 'X'
    
        elif jogador_2:
            jogador_1 = True
            jogador_2 = False 
            l = int(input('Linha: '))
            c = int(input('Coluna: '))
    
            while True:
                if l < 1 or l > 3 or c < 1 or c > 3 or matriz[c-1][l-1] != ' ' :
                    print('\nMovimento invalido\n')
                    sleep(1)
                    limpar_tela()
                    print('Vez do jogador 2\n')
                    l = int(input('Linha: '))
                    c = int(input('Coluna: '))      
                    continue
                break  
            
    
            matriz[c-1][l-1] = 'O'
        
        limite -= 1 
    
        limpar_tela()
        print_velha(matriz)
        print()
    
        vitoria_vertical(matriz)
        vitoria_horizontal(matriz)
        vitoria_diagonal(matriz)
        limite_de_jogo(limite)
    
if _name_ == '_main_':
    main()
