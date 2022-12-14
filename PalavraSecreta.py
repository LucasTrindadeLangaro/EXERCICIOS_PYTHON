"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os
import random
from time import sleep

palavras = {'teste':'é um teste', 'amor':'é amor','alegria':'é alegria','bolsonaro':'é o presidente'
            ,'presidente':'cargo do bolsonaro','lula':'ladrao','cadeia':'lugar do lula'}
palavra_secreta = random.choice(list(palavras.items()))
letras_acertadas = ''
numero_tentativas = 0
limite = 0
print("JOGO DE ADIVINHA")
print(f"VOCE DEVE ADIVINHAR QUAL É A PALAVRA. VOCE TERA {len(palavra_secreta[0])+3} chances para acertar")
sleep(0.5)
print('VAMOS COMEÇAR!!')
sleep(1)
print(f'a dica é: {palavra_secreta[1]}')
while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    limite = numero_tentativas

    '''if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue'''

    if letra_digitada in palavra_secreta[0]:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta[0]:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    if limite > (len(palavra_secreta[0])+2):
        print('Que pena, você não acertou ):!!')
        print(f'A palavra era: {palavra_secreta[0]}')
        break


    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta[0]:
        print('A palavra era', palavra_secreta[0])
        if numero_tentativas == len(palavra_secreta[0]):
            print('PARABENS! VOCE ACERTOU DE PRIMEIRA')
        else:
            print('VOCÊ GANHOU!! PARABÉNS!')
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        desejo = input('Deseja continuar? ').upper().strip()[0]
        if desejo == 'S':
            os.system('cls')
            continue
        else:
            break

print('Fim de Jogo!')



'''
        CODDIGO ORIGINAL
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0'''
