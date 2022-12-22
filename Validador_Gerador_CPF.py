import os
import random
import re


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



while True:
    opcao = input("Deseja validar ou Gerar um CPF? [V] validar, [G]Gerar, [S] Sair: ").upper().strip()[0]
    while opcao != 'S' and opcao != 'V' and opcao != 'G':
        opcao = input('Digite V, G ou S: ').upper().strip()[0]
    if opcao == 'V':
        entrada = input('CPF [xxx.xxx.xxx-xx]: ')
        cpf_enviado_usuario = re.sub(
            r'[^0-9]',
            '',
            entrada
        )
        entrada_e_sequencial = entrada == entrada[0] * len(entrada)
       
        while entrada_e_sequencial == True: 
            entrada = input('Não podem ser enviados dados sequenciais, informe seu cpf novamente: ') 
            entrada_e_sequencial = entrada == entrada[0] * len(entrada)

        nove_digitos = cpf_enviado_usuario[:9]
        contador_regressivo_1 = 10

        resultado_digito_1 = 0
        for digito in nove_digitos: 
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1 
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0 

        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11 

        
        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        tres = nove_digitos[:3]
        seis = nove_digitos[3:6]
        nove = nove_digitos[6:9]
        formata_cpf = tres+'.'+seis+'.'+nove+'-'

        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
        cpf_formatado = f'{formata_cpf}{digito_1}{digito_2}'

        print('Validando Seu CPF',end='')
        tempo()

        if cpf_enviado_usuario == cpf_gerado_pelo_calculo: 
            print(f'{cpf_formatado} é válido')
            continuar = input('Deseja continuar? ').upper().strip()[0]

            while continuar != 'S' and continuar != 'N':
                continuar = input(f'{continuar} não é valido! Digite Sim ou Não: ').upper().strip()[0]

            if continuar == 'S':
                print('Voltando para o incio',end='')
                tempo()
                os.system('cls')
                continue
            else:
                print('Saindo do Programa',end='')
                tempo()
                break

        else:
            print(f'{cpf_enviado_usuario} não é um CPF inválido')
            continuar = input('Deseja continuar? ').upper().strip()[0]

            while continuar != 'S' and continuar != 'N':
                continuar = input(f'{continuar} não é valido! Digite Sim ou Não: ').upper().strip()[0]

            if continuar == 'S':
                print('Voltando para o incio',end='')
                tempo()
                os.system('cls')
                continue
            else:
                print('Saindo do Programa',end='')
                tempo()
                break
    
    elif opcao == 'G':
        nove_digitos = ''
        print('Gerando seu CPF',end='')
        tempo()
        for i in range(9):
            nove_digitos += str(random.randint(0,9))


        contador_regressivo_1 = 10 

        resultado_digito_1 = 0 
        for digito in nove_digitos: 
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1 
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11


        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        tres = nove_digitos[:3]
        seis = nove_digitos[3:6]
        nove = nove_digitos[6:9]
        nove_digitos = tres+'.'+seis+'.'+nove+'-'

        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

        print(f'CPF Gerado: {cpf_gerado_pelo_calculo}')
        continuar = input('Deseja continuar? ').upper().strip()[0]
        while continuar != 'S' and continuar != 'N':
            continuar = input(f'{continuar} não é valido! Digite Sim ou Não: ').upper().strip()[0]
        if continuar == 'S':
            print('Voltando para o incio',end='')
            tempo()
            os.system('CLS')
            continue
        else:
            print('Saindo do Programa',end='')
            tempo()
            break

    else:
        print('saindo do programa',end='')
        tempo()
        break
print('FIM DO PROGRAMA!')
