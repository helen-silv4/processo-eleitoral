'''
/***********************************/
/* Aluno: Helen Silva - N070498    */
/* TURMA: CC2A13                   */
/* Profa. Eliane                   */
/***********************************/
'''
# Imports para limpar o terminal e temporizador
import os 
import time

# Variável contador para contar quantos loops ocorrerá (Quantos eleitores votaram)
contador = 0

# Variáveis para prefeito
prefeito = ''
P1 = 0
P2 = 0
P3 = 0
P4 = 0
PB = 0
PN = 0

# Variáveis para vereadores
vereador = ''
V1 = 0
V2 = 0
V3 = 0
V4 = 0
VB = 0
VN = 0

# Função para limpar terminal 
def limpar_terminal():
    if os.name == 'posix':  #Linux e macOS
        os.system('clear')
    elif os.name == 'nt':  #Windows
        os.system('cls')

# Inputs para cadastro da Urna Eletônica
print('|------------------- Cadastro da Urna -------------------------|\n')      
zona = input('Digite a Zona Eleitoral: ')
secao = input('Digite a Seção: ')
cod_UE = input('Digite o código da Urna Eletrônica: ')

eleitores_esperados = input('Digite a quantidade de eleitores esperados: ')

# Verifica se eleitores_esperados é um valor numérico
while not eleitores_esperados.isdigit():
    eleitores_esperados = input('Digito inválido! Digite a quantidade de eleitores esperados : ')

while True:
    print('\n|------------------- Processo Eleitoral -------------------------|\n')
    time.sleep(2)

# Mostra os dados cadastrados na urna
    print(f'''
|------------------------------|
|  URNA ELETÔNICA - {cod_UE}  |
|------------------------------|
|   Eleitores esperados | {eleitores_esperados}    |
|   Zona  | {zona}               |
|   Seção | {secao}               |
|------------------------------|
''')
    
    idade = input('Digite sua idade: ')
    # Tenta usar o bloco try para caso capture um erro ao usuário digitar um dado inválido para idade
    try:
        idade_int = int(idade)
        # Se a idade estiver entre 16 e 115 anos inicia-se o processo de votação
        if idade_int >= 16 and idade_int <= 115:
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
            # Verifica se a entrada de dados é válida
            prefeito = input('Digite a sigla para candidato a prefeito: ').upper()

            while (prefeito != 'P1'  and prefeito != 'P2' and prefeito != 'P3' and prefeito != 'P4'  and prefeito != 'PB'  and prefeito != 'PN'):
                prefeito = input('Digite uma sigla válida (PREFEITO): ').upper()

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
            # Verifica se a entrada de dados é válida
            vereador = input('Digite a sigla para candidato a vereador: ').upper()

            while (vereador != 'V1' and vereador != 'V2' and vereador != 'V3' and vereador != 'V4' and vereador != 'VB' and vereador != 'VN'):
                vereador = input('Digite uma sigla válida (VEREADOR): ').upper()

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
            time.sleep(2)
            
            # Após terminar a votação incrementa + 1 no contador e chama a função para limpar o terminal
            contador += 1
            limpar_terminal()

        # Chave para caso o administrador queira parar o processo de votação
        elif idade_int == 2763:
            break
        # Caso idade for menor que 16 ou maior que 115
        else:
            print('Você não tem idade suficiente para votar.')
        # Encerra o processo de votação quando o contador por maior ou igual a quantidade de eleitores esperados
        if contador >= int(eleitores_esperados):
            break 
    # Captura de erro
    except ValueError:
        print('Digite uma idade válida (um número inteiro)!')

# Função para verificar o Prefeito vencedor ou empate
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
    elif (P1 == P2):
        return 'Empate Prefeitos! Haverá um novo turno.'
    elif (P1 == P3):
        return 'Empate Prefeitos! Haverá um novo turno.'
    elif (P1 == P4):
        return 'Empate Prefeitos! Haverá um novo turno.'
    elif (P2 == P3):
        return 'Empate Prefeitos! Haverá um novo turno.'
    elif (P2 == P4):
        return 'Empate Prefeitos! Haverá um novo turno.'
    elif (P3 == P4):
        return 'Empate Prefeitos! Haverá um novo turno.'
    else:
        return 'Houve um equívoco! Haverá um novo turno.'

# Função para verificar o Vereador vencedor ou empate
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
    elif (V1 == V2):
        return 'Empate Vereadores! Haverá um novo turno.'
    elif (V1 == V3):
        return 'Empate Vereadores! Haverá um novo turno.'
    elif (V1 == V4):
        return 'Empate Vereadores! Haverá um novo turno.'
    elif (V2 == V3):
        return 'Empate Vereadores! Haverá um novo turno.'
    elif (V2 == V4):
        return 'Empate Vereadores! Haverá um novo turno.'
    elif (V3 == V4):
        return 'Empate Vereadores! Haverá um novo turno.'
    else:
        return 'Houve um equívoco! Haverá um novo turno.'

# Armazena o resultado das função em variáveis
resultado_prefeito = prefeitoVencedor(P1, P2, P3, P4)
resultado_vereador = vereadorVencedor(V1, V2, V3, V4)

# Resultado

print('|------------------- Encerramento das Eleições ------------------|')
time.sleep(2)

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
|         VOTARAM = {contador}           |           FALTAS = {int(eleitores_esperados) - contador}           |
|----------------------------------------------------------------|


|----------------------------------------------------------------|
|                           RESULTADO                            |
|----------------------------------------------------------------|
|   Candidato a Prefeito mais votado = {resultado_prefeito}      | 
|   Candidato a Vereador mais votado = {resultado_vereador}      |
|----------------------------------------------------------------|
''')