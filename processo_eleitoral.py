'''
/***********************************/
/* Aluno: Helen Silva - N070498    */
/* TURMA: CC2A13                   */
/* Profa. Eliane                   */
/***********************************/
'''
import os 
import time

zona = '0237'
secao = '0986'
cod_UE = '874639576'
eleitores_esperados = 3
contador = 0

prefeito = ''
P1 = 0
P2 = 0
P3 = 0
P4 = 0
PB = 0
PN = 0

vereador = ''
V1 = 0
V2 = 0
V3 = 0
V4 = 0
VB = 0
VN = 0

def limpar_terminal():
    if os.name == 'posix':  #Linux e macOS
        os.system('clear')
    elif os.name == 'nt':  #Windows
        os.system('cls')

while True:
    print('|------------------- Processo Eleitoral -------------------------|\n')
    time.sleep(2)

    idade = input('Digite sua idade: ')
    try:
        idade_int = int(idade)
        if idade_int >= 16 and idade_int <= 115:
            print(f'''
|------------------------------|
|  URNA ELETÔNICA - {cod_UE}  |
|------------------------------|
|   Eleitores esperados | {eleitores_esperados}    |
|   Zona  | {zona}               |
|   Seção | {secao}               |
|------------------------------|
            ''')
            time.sleep(2)

            print('''
|---------------------------------|
|           PREFEITOS             |
|---------------------------------|
| SIGLA |   CANDIDATO   | PARTIDO |
|---------------------------------|
|   P1  |   Prefeito 1  |   PDB   |
|   P2  |   Prefeito 2  |   PDB   |
|   P3  |   Prefeito 3  |   PSB   | 
|   P4  |   Prefeito 4  |   PSB   |
|   PB  |   Voto Branco |   ***   |
|   PN  |   Voto Nulo   |   ***   |
|---------------------------------|
            ''')
            time.sleep(2)

            prefeito = input('Digite a sigla para candidato a prefeito: ').upper()

            while (prefeito != 'P1'  and prefeito != 'P2' and prefeito != 'P3' and prefeito != 'P4'  and prefeito != 'PB'  and prefeito != 'PN'):
                prefeito = input('Digite uma sigla válida (PREFEITO): ')

            if prefeito == 'P1':
                P1 += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'P2':
                P2 += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'P3':
                P3 += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'P4':
                P4 += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'PB':
                PB += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'PN':
                PN += 1
                print('Voto para prefeito confirmado!')
            time.sleep(2)
            print('''
|---------------------------------|
|           VEREADORES            |
|---------------------------------|
| SIGLA |   CANDIDATO   | PARTIDO |
|---------------------------------|
|   V1  |  Vereador 1   |   PDB   |
|   V2  |  Vereador 2   |   PDB   |
|   V3  |  Vereador 3   |   PSB   |
|   V4  |  Vereador 4   |   PSB   | 
|   VB  |  Voto Branco  |   ***   |
|   VN  |  Voto Nulo    |   ***   |
|---------------------------------|
            ''')
            time.sleep(2)
            
            vereador = input('Digite a sigla para candidato a vereador: ').upper()

            while (vereador != 'V1' and vereador != 'V2' and vereador != 'V3' and vereador != 'V4' and vereador != 'VB' and vereador != 'VN'):
                vereador = input('Digite uma sigla válida (VEREADOR): ')

            if vereador == 'V1':
                V1 += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'V2':
                V2 += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'V3':
                V3 += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'V4':
                V4 += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'VB':
                VB += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'VN':
                VN += 1
                print('Voto para vereador confirmado!')

            print('\n|-------------------- Votação encerrada -------------------------|\n')
            time.sleep(3)

            contador += 1

            limpar_terminal()

        elif idade_int == 2763:
            break
        else:
            print('Você não tem idade suficiente para votar.')

        if contador >= eleitores_esperados:
            break                   
    except ValueError:
        print('Digite uma idade válida (um número inteiro)!')

def prefeitoVencedor(P1, P2, P3, P4):
    if (P1 == 0) and (P2 == 0) and (P3 == 0) and (P4 == 0):
        return 'Votos nulos ou brancos! Haverá um novo turno.'
    elif (P1 > P2) and (P1 > P3) and (P1 > P4):
        return 'Prefeito 1 Vencedor!'
    elif (P2 > P1) and (P2 > P3) and (P2 > P4):
        return 'Prefeito 2 Vencedor!'
    elif (P3 > P1) and (P3 > P2) and (P3 > P4):
        return 'Prefeito 3 Vencedor!'
    elif (P4 > P1) and (P4 > P2) and (P4 > P3):
        return 'Prefeito 4 Vencedor!'
    elif (P1 == P2) or (P2 == P1):
        return 'Empate Prefeitos 1 e 2! Haverá um novo turno.'
    elif (P1 == P3) or (P3 == P1):
        return 'Empate Prefeitos 1 e 3! Haverá um novo turno.'
    elif (P1 == P4) or (P4 == P1):
        return 'Empate Prefeitos 1 e 4! Haverá um novo turno.'
    elif (P2 == P3) or (P3 == P2):
        return 'Empate Prefeitos 2 e 3! Haverá um novo turno.'
    elif (P2 == P4) or (P4 == P2):
        return 'Empate Prefeitos 2 e 4! Haverá um novo turno.'
    elif (P3 == P4) or (P4 == P3):
        return 'Empate Prefeitos 3 e 4! Haverá um novo turno.'
    else:
        return 'Houve um equívoco! Haverá um novo turno.'

def vereadorVencedor(V1, V2, V3, V4):
    if (V1 == 0) and (V2 == 0) and (V3 == 0) and (V4 == 0):
        return 'Votos nulos ou brancos! Haverá um novo turno.'
    elif (V1 > V2) and (V1 > V3) and (V1 > V4):
        return 'Vereador 1 Vencedor!'
    elif (V2 > V1) and (V2 > V3) and (V2 > V4):
        return 'Vereador 2 Vencedor!'
    elif (V3 > V1) and (V3 > V2) and (V3 > V4):
        return 'Vereador 3 Vencedor!'
    elif (V4 > V1) and (V4 > V2) and (V4 > V3):
        return 'Vereador 4 Vencedor!'
    elif (V1 == V2) or (V2 == V1):
        return 'Empate Vereadores 1 e 2! Haverá um novo turno.'
    elif (V1 == V3) or (V3 == V1):
        return 'Empate Vereadores 1 e 3! Haverá um novo turno.'
    elif (V1 == V4) or (V4 == V1):
        return 'Empate Vereadores 1 e 4! Haverá um novo turno.'
    elif (V2 == V3) or (V3 == V2):
        return 'Empate Vereadores 2 e 3! Haverá um novo turno.'
    elif (V2 == V4) or (V4 == V2):
        return 'Empate Vereadores 2 e 4! Haverá um novo turno.'
    elif (V3 == V4) or (V4 == V3):
        return 'Empate Vereadores 3 e 4! Haverá um novo turno.'
    else:
        return 'Houve um equívoco! Haverá um novo turno.'

resultado_prefeito = prefeitoVencedor(P1, P2, P3, P4)
resultado_vereador = vereadorVencedor(V1, V2, V3, V4)

print('|------------------- Encerramento das Eleições ------------------|')
time.sleep(3)

print(f'''
|----------------------------------------------------------------|
|                           TOTALIZAÇÃO                          |
|----------------------------------------------------------------|
|            PREFEITOS           |          VEREADORES           |
|----------------------------------------------------------------|
|      PDB      |      PSB       |       PDB    |      PSB       |
|----------------------------------------------------------------|
|     P1 = {P1}    |     P3 = {P3}     |     V1 = {V1}    |     V3 = {V3}    |   
|     P2 = {P2}    |     P4 = {P4}     |     V2 = {V2}    |     V4 = {V4}    |
|----------------------------------------------------------------|
|                          TOTAL VOTOS                           |
|----------------------------------------------------------------|
|           PARTIDO              |            CARGO              |
|----------------------------------------------------------------|
|           PDB = {P1+P2+V1+V2}              |          Prefeito = {P1+P2+P3+P4}         |
|           PSB = {P3+P4+V3+V4}              |          Vereador = {V1+V2+V3+V4}         |
|----------------------------------------------------------------|
|            NULOS               |           BRANCOS             |
|----------------------------------------------------------------|
|              {PN+VN}                 |              {PB+VB}                |
|----------------------------------------------------------------|
|                         TOTAL ELEITORES                        |
|----------------------------------------------------------------|
|         VOTARAM = {contador}           |           FALTAS = {eleitores_esperados - contador}           |
|----------------------------------------------------------------|


|----------------------------------------------------------------|
|                           RESULTADO                            |
|----------------------------------------------------------------|
|   Candidato a Prefeito mais votado = {resultado_prefeito}      | 
|   Candidato a Vereador mais votado = {resultado_vereador}      |
|----------------------------------------------------------------|
''')