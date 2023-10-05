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

print('|----- Processo Eleitoral -----|\n')
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
            |--------------------------|
            |        PREFEITOS         |
            |--------------------------|
            |   P1  |  Prefeito 1      |
            |   P2  |  Prefeito 2      |
            |   P3  |  Prefeito 3      |
            |   P4  |  Prefeito 4      |
            |   PB  |  Voto Branco     |
            |   PN  |  Voto Nulo       |
            |--------------------------|
            ''')
            prefeito = input('Digite a sigla para candidato a prefeito: ')

            while (prefeito != 'P1' and prefeito != 'p1' and prefeito != 'P2' and prefeito != 'p2' and prefeito != 'P3' and prefeito != 'p3' and prefeito != 'P4' and prefeito != 'p4' and prefeito != 'PB' and prefeito != 'pb' and prefeito != 'Pb' and prefeito != 'pB' and prefeito != 'PN' and prefeito != 'pn' and prefeito != 'Pn' and prefeito != 'pN'):
                prefeito = input('Digite uma sigla válida (PREFEITO): ')

            if prefeito == 'P1' or prefeito == 'p1':
                P1 += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'P2' or prefeito == 'p2':
                P2 += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'P3' or prefeito == 'p3':
                P3 += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'P4' or prefeito == 'p4':
                P4 += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'PB' or prefeito == 'pb' or prefeito == 'Pb' or prefeito == 'pB':
                PB += 1
                print('Voto para prefeito confirmado!')
            elif prefeito == 'PN' or prefeito == 'pn' or prefeito == 'Pn' or prefeito == 'pN':
                PN += 1
                print('Voto para prefeito confirmado!')

            print('''
            |--------------------------|
            |        VEREADORES        |
            |--------------------------|
            |   V1  |  Vereador 1      |
            |   V2  |  Vereador 2      |
            |   V3  |  Vereador 3      |
            |   V4  |  Vereador 4      |
            |   VB  |  Voto Branco     |
            |   VN  |  Voto Nulo       |
            |--------------------------|
            ''')
            vereador = input('Digite a sigla para candidato a vereador: ')

            while (vereador != 'V1' and vereador != 'v1' and vereador != 'V2' and vereador != 'v2' and vereador != 'V3' and vereador != 'v3' and vereador != 'V4' and vereador != 'v4' and vereador != 'VB' and vereador != 'vb' and vereador != 'Vb' and vereador != 'vB' and vereador != 'VN' and vereador != 'vn' and vereador != 'Vn' and vereador != 'vN'):
                vereador = input('Digite uma sigla válida (VEREADOR): ')

            if vereador == 'V1' or vereador == 'v1':
                V1 += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'V2' or vereador == 'v2':
                V2 += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'V3' or vereador == 'v3':
                V3 += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'V4' or vereador == 'v4':
                V4 += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'VB' or vereador == 'vb' or prefeito == 'Vb' or prefeito == 'vB':
                VB += 1
                print('Voto para vereador confirmado!')
            elif vereador == 'VN' or vereador == 'vn' or prefeito == 'Vn' or prefeito == 'vN':
                VN += 1
                print('Voto para vereador confirmado!')
            contador += 1
        else:
            print('Você não tem idade suficiente para votar.')

        

        if contador >= eleitores_esperados:
            break           
        
    except ValueError:
        print('Digite uma idade válida (um número inteiro)!')

print(f'''
|--------------------------------------------|
|                TOTALIZAÇÃO                 |
|--------------------------------------------|
|        PREFEITOS    |    VEREADORES        |
|         P1 = {P1}      |      V1 = {V1}          |
|         P2 = {P2}      |      V2 = {V2}          |
|         P3 = {P3}      |      V3 = {V3}          |
|         P4 = {P4}      |      V4 = {V4}          |
|        TOTAL = {P1+P2+P3+P4}    |     TOTAL = {V1+V2+V3+V4}        |
|--------------------------------------------|
|       NULOS = {PN+VN}     |   EM BRANCOS = {PB+VB}     |
|--------------------------------------------|
|       VOTARAM = {contador}   |   FALTAS = {eleitores_esperados - contador}         |
|--------------------------------------------|
''')