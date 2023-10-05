'''
/***********************************/
/* Aluno: Helen Silva - N070498    */
/* TURMA: CC2A13                   */
/* Profa. Eliane                   */
/***********************************/
'''

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

print('|------------------- Processo Eleitoral -------------------|\n')
while True:
    idade = input('Digite sua idade: ')
    try:
        idade_int = int(idade)
        if idade_int >= 16:
            print(f'''
            |------------------------------|
            |  URNA ELETÔNICA - {cod_UE}  |
            |------------------------------|
            |   Eleitores esperados | {eleitores_esperados}    |
            |   Zona  | {zona}               |
            |   Seção | {secao}               |
            |------------------------------|
            ''')
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
            print('\n|------------------- Votação encerrada -------------------|\n')
            contador += 1
        else:
            print('Você não tem idade suficiente para votar.')

        if contador >= eleitores_esperados:
            break                   
    except ValueError:
        print('Digite uma idade válida (um número inteiro)!')

print('\n|------------------- Encerramento das Eleições -------------------|')
print(f'''
            |--------------------------------------------|
            |                TOTALIZAÇÃO                 |
            |--------------------------------------------|
            |                 PREFEITOS                  |
            |--------------------------------------------|
            |          PDB         |          PSB        |
            |--------------------------------------------|
            |        P1 = {P1}        |       P3 = {P3}        |
            |        P2 = {P2}        |       P4 = {P4}        |
            |--------------------------------------------|
            |                  VEREADORES                |
            |--------------------------------------------|
            |          PDB         |          PSB        |
            |--------------------------------------------| 
            |         V1 = {V1}       |      V3 = {V3}         |
            |         V2 = {V2}       |      V4 = {V4}         |
            |--------------------------------------------|
            |                  TOTAL VOTOS               |
            |--------------------------------------------|
            |          PARTIDO     |      CARGO          |
            |--------------------------------------------|
            |          PDB = {P1+P2+V1+V2}     |   Prefeito = {P1+P2+P3+P4}      |
            |          PSB = {P3+P4+V3+V4}     |   Vereador = {V1+V2+V3+V4}      |
            |          Nulos = {PN}   |   Em branco = {VB}     |
            |--------------------------------------------|
            |                TOTAL ELEITORES             |
            |--------------------------------------------|
            |       VOTARAM = {contador}   |   FALTAS = {eleitores_esperados - contador}         |
            |--------------------------------------------|


            |--------------------------------------------|
            |                 RESULTADO                  |
            |--------------------------------------------|
            |   Candidato a Prefeito mais votado = {''}      |
            |   Candidato a Vereador mais votado = {''}      |
            |--------------------------------------------|
''')
