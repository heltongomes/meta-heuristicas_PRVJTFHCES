# python main.py -i Instancias/Inst1501.txt --arqsaida TabRes.txt --tempinicial 1000 --tempcritica 0.01 --taxa 0.99 --samax 2
# python main.py -i Instancias/Inst1501.txt --tempinicial 1000 --tempcritica 0.01 --taxa 0.99 --samax 2

# -*- coding: utf-8 -*-
"""
PROGRAMA PRINCIPAL

SA - PRVJTFHCES

@author: helton gomes
"""

#from copy import deepcopy

#import le_dados as LD
import le_dados as LD
import solucao_inicial as SI
import calcula_fo as CFO
#import descida as MD
#import vns
import sa

import time
import sys

qtd_cid = qtd_veic = 0 
cap_veic = []
pickup = []
demanda = []
t_serv = []
t_ini = []
t_fim = []
custo = []
dist = []

if ( len(sys.argv) != 11):
    print('\n\n\t--------------- ERRO ---------------', len(sys.argv))
    #print('\n\n\t--------------- ERRO ---------------')
#    print('\n\tPasse os comandos da seguinte forma:')
#    print('\n\tpython3 main.py --instancia nomearq.txt --replicacao replicacao --samax samax --tempinicial ti --tempcritica tc --taxa tx \n\n')
    exit(1)

for i in range(1, len(sys.argv), 1):
    if (sys.argv[i] == '-i'):
        instancia = (sys.argv[i+1])
    #if (sys.argv[i] == '--arqsaida'):
    #    nomearqsaida = (sys.argv[i+1])
    elif (sys.argv[i] == '--tempinicial'):
        ti = int(sys.argv[i+1])
    elif (sys.argv[i] == '--tempcritica'):
        tc = float(sys.argv[i+1])
    elif (sys.argv[i] == '--taxa'):
        tx = float(sys.argv[i+1])
    elif (sys.argv[i] == '--samax'):
        samax = int(sys.argv[i+1])

#print('\nInstancia = ', instancia)
#print('SAMAX = ', samax)
#print('Temperatura Inicial = ', ti)
#print('Temperatura Critica = ', tc)
#print('Taxa = ', tx)

# LEITURA DOS DADOS/PARAMETROS DO PROBLEMA

#qtd_cid, qtd_veic, cap_veic, pickup, demanda, t_serv, t_ini, t_fim, custo, dist = LD.leitura_dados()
qtd_cid, qtd_veic, cap_veic, pickup, demanda, t_serv, t_ini, t_fim, custo, dist = LD.ler_dados(instancia)

inicio = time.time()

sol_corrente = []
fo_corrente = 0

sol_viz = []
fo_viz = 0


#s = [[1, 4, 3], [5, 10, 12, 8, 6], [11, 7, 9, 2]]
#fo = CFO.calc_fo(s, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap_veic, pickup, demanda)
#print(fo)


# DETERMINAÇÃO DA SOLUÇÃO INICIAL

sol_corrente = SI.sol_ini(qtd_cid, qtd_veic, cap_veic, pickup, demanda)
#print("Solução Inicial:", sol_corrente)
fo_corrente = CFO.calc_fo(sol_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap_veic, pickup, demanda)
#print("FO Inicial:", fo_corrente)

# VALOR DA FUNÇÃO OBJETIVO DA SOLUÇÃO INICIAL - PARA CALCULAR O GAP DE MELHORA

fo_ini = fo_corrente

# BUSCA LOCAL - VNS

r = 4 # NUMERO DE ESTRUTURAS DE VIZINHANÇA
    
# sol_corrente, fo_corrente = vns.met_vns(sol_corrente, fo_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap_veic, pickup, demanda, r)

sol_corrente, fo_corrente = sa.met_sa(sol_corrente, fo_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap_veic, pickup, demanda, ti, tc, tx, samax)

fim = time.time()

#print("Melhor Solução:", sol_corrente)
#print("FO Melhor:", fo_corrente)

print(sol_corrente)
print(fo_corrente)

#fo_corrente = CFO.calc_fo(sol_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap_veic, pickup, demanda)

#gap = ((fo_ini - fo_corrente)/fo_ini)*100
#print(f'GAP = {gap: 5.2f}%')

#gap = ((fo_corrente - fo)/fo)*100
#print(f'GAP = {gap: 5.2f}%')

#print(f'Tempo: {fim - inicio: 5.3f} segundos')

# Impresão da solução final em um txt
#LD.imprimir_dados(nomearqsaida, instancia, qtd_cid, qtd_veic, fo_ini, fo_corrente, fim - inicio)