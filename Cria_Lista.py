'''
Fça uma lista de compras com listas
o usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
nao permita que o programa quebre com erros de indices na lista
'''
import os


def tempo():
    from time import sleep
    sleep(0.5)
    print('.',end='')
    sleep(0.5)
    print('.',end='')
    sleep(0.5)
    print('.',end='')
    sleep(0.5)
    print('.',end='')
    sleep(0.5)
    print('.')
    sleep(0.5)



qtd = 0
lista_comp = []
lista = []
opcao = ''
salvar = ''

while True:
    try:
        opcao = input('O que deseja fazer? [i]inserir [a]apagar [l]listar [s]sair: ').upper().strip()[0]
    except:
        print('Para continuar, voce precisa digitar I, A, L ou S! ', end='')


                            #se a opção for para inserir itens
    if opcao == 'I':
        #validando a quantidade de itens que sera adicionado
        qtd_str = input('Quantos itens quer adicionar? ').strip()
        try:
            qtd = int(qtd_str)
        except:
            if qtd_str == '':
                print('este campo não pode ficar vazio!')
            else:
                print(f'"{qtd_str}" não é um numero valido' )
            continue

        #digitando o valor e adicionando na lista
        for i in range(qtd):
            item = input('Digite o item: ').strip()
            lista.append(item)
        
        #verificando se a lista esta vazia
        if len(lista) <=0 or lista == ['']:
            print('Sua lista está vazia! Voltando para o incio',end='')
            lista.clear()
            tempo()
            continue
        
        #Salvar arquivo txt
        salvar = input('Deseja salvar essa lista? [S][N] ').upper().strip()[0]

        if salvar == 'S':
            nome_arquivo = input('Digite o nome do arquivo: ')
            try:
                arquivo = open(nome_arquivo, 'r+')
            except:
                arquivo = open(nome_arquivo, 'a')
                for i in lista:
                    arquivo.write(f'{i}\n')
                arquivo.close()
        elif salvar == 'N':
            continuar = input('Deseja sair do Programa? ').upper().strip()
            if continuar == 'N':
                continue
            elif continuar == 'S':
                print('Saindo', end='')
                tempo()
                break
        if salvar != 'N' and salvar != 'S':
            while salvar != 'N' and salvar != 'S' and salvar =='':
                salvar = input('Esse valor não é valido! Digite [S] ou [N]').upper().strip()[0]
        elif len(salvar)==0:
            print('a lista não pode ficar vazia!!, voltando para o inico')


     
                            #Se a opção for para apagar:
    elif opcao == 'A':
        apgar_toda_lista = input('Deseja apagar todos os itens da lista? ').upper().strip()[0]

#verifica se quer apagar todos os itens da lista
        if apgar_toda_lista == 'S':
        #pergunta o nome do arquivo que deseja apagar
            deleta_nome_arquivo = input('Digite o nome do arquivo que deseja apagar: ')
            tem_certeza = input(f'Tem certeza que deseja apagar o arquivo "{deleta_nome_arquivo.upper()}"? '
                'Essa ação não podera ser desfeita! ').upper().strip()[0]
            
            #caso deseja apagar o arquivo inteiro
            if tem_certeza == 'S':
                try:
                    os.remove(deleta_nome_arquivo)
                    print('Arquivo apagado!')
                except:
                    print('Arquivo Não existe')
            #apaga a lista salva na memoria
            elif tem_certeza == 'N':
                lista.clear()
            #caso digite alguma coisa diferente de S ou N
            else:
                print('Comando invalido!!! Voltando para o inicio',end='')
                tempo()
            continuar = input('Deseja continuar? ').upper().strip()[0]
            
            #Caso não queria continuar, o sistema vai parar
            if continuar == 'N':
                print('Saindo',end='')
                tempo()
                break
            # caso queira continuar, o sistema vai voltar para o inico!
            elif continuar == 'S':
                continue
            #caso digite algo diferente de S ou N
            else:
                while continuar != 'S' and continuar <= 'N':
                    continuar = input('Voce precisa digitar S ou N: ')
        
        #caso deseje apagar pelo menos um item da lista.
        elif apgar_toda_lista == 'N':
            #verifica se a lista esta vazia
            #if len(lista)<=0 or lista == ['']:
            abre_arquivo = input('deseja abrir algum arquivo? ').upper().strip()[0]
            
            #caso deseje abrir algum arquivo
            if abre_arquivo == 'S':
                try:
                    nome_arquivo = input('digite o nome do arquivo: ')
                    arquivo = open(nome_arquivo,'r')
                    linhas = arquivo.readlines()
                    for i,e in enumerate(linhas):
                        e = e.rstrip('\n') #isso tira a quebra de linha que vem do arquivo
                        lista_comp.append(e)
                    arquivo.close()
                except:
                    print(f'{nome_arquivo} não existe!!voltando para o inicio')
                    tempo()
                    continue

                qtd_apagar = int(input(f'sua lista possui {len(lista_comp)} itens, quantos deseja apagar: '))
                for item in range(qtd_apagar):
                    for i,e in enumerate(lista_comp):
                        print(f'{i+1} - {e}')
                    apagar = int(input('digite o numero do item que deseja apagar: '))
                    apagar -= 1
                    try:
                        lista_comp.pop(apagar)
                    except:
                        while apagar.isalpha():
                            apagar = input('Digite um numero: ')
                try:
                    os.remove(nome_arquivo)
                    arquivo = open(nome_arquivo, 'r+')
                except:
                    arquivo = open(nome_arquivo, 'w+')
                    for i in lista_comp:
                        arquivo.writelines(f'{i}\n')
                    arquivo.close()
            #caso nao deseje abrir nenhum arquivo, o sistema irá parar
            elif abre_arquivo == 'N':
                break
            #Caso digite algo diferente de S ou N
            else:
                while abre_arquivo != 'S' and abre_arquivo != 'N':
                    abre_arquivo = input('Digite N ou S: ')
            
            
            print('sua lista ficaou assim: ')
            for i, e in enumerate(lista_comp):
                print(f'{i+1} - {e}')             
                        

                            #se a opção for Listar:
    elif opcao == 'L':
        try:
            nome_arquivo = input('digite o nome do arquivo: ')
            arquivo = open(nome_arquivo,'r')
            linhas = arquivo.readlines()
            for linha in linhas:
                linha = linha.rstrip('\n') #isso tira a quebra de linha que vem do arquivo
                lista_comp.append(linha)
            arquivo.close()
        except:
            print(f'{nome_arquivo} não existe!!voltando para o inicio')
            tempo()
            continue
        for i,e in enumerate(lista_comp):
            print(f'{i} - {e}')
    
    #Se a opção for sair
    elif opcao == 'S':
        print('Saindo',end='')
        tempo()
        break

    #Caso não digite I,A,L ou S
    else:
        print('Para continuar, voce precisa digitar I, A, L ou S! ', end='')


#fim do programa
print('Fim do programa!')




'''codigo feito pelo instrutor: 

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')'''