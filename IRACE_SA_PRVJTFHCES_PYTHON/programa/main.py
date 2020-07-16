# python main.py -i Instancias/Inst1501.txt --tempinicial 1000 --tempcritica 0.01 --taxa 0.99 --samax 2

# -*- coding: utf-8 -*-
"""
PROGRAMA PRINCIPAL

SIMULATED ANNEALING PARA O PRVJTFHCES

@author: Helton Gomes
"""

# IMPORTANDO FUNÇÕES 
import le_dados as LD
import solucao_inicial as SI
import calcula_fo as CFO
import sa

# IMPORTANDO BIBLIOTECAS
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
    exit(1)

for i in range(1, len(sys.argv), 1):
    if (sys.argv[i] == '-i'):
        instancia = (sys.argv[i+1])
    elif (sys.argv[i] == '--tempinicial'):
        ti = int(sys.argv[i+1])
    elif (sys.argv[i] == '--tempcritica'):
        tc = float(sys.argv[i+1])
    elif (sys.argv[i] == '--taxa'):
        tx = float(sys.argv[i+1])
    elif (sys.argv[i] == '--samax'):
        samax = int(sys.argv[i+1])

# LEITURA DOS DADOS/PARAMETROS DO PROBLEMA
qtd_cid, qtd_veic, cap_veic, pickup, demanda, t_serv, t_ini, t_fim, custo, dist = LD.ler_dados(instancia)

inicio = time.time()

sol_corrente = []
fo_corrente = 0

sol_viz = []
fo_viz = 0

# DETERMINAÇÃO DA SOLUÇÃO INICIAL
sol_corrente = SI.sol_ini(qtd_cid, qtd_veic, cap_veic, pickup, demanda)
fo_corrente = CFO.calc_fo(sol_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap_veic, pickup, demanda)

# VALOR DA FUNÇÃO OBJETIVO DA SOLUÇÃO INICIAL - PARA CALCULAR O GAP DE MELHORA
fo_ini = fo_corrente

# BUSCA LOCAL - VNS
r = 4 # NUMERO DE ESTRUTURAS DE VIZINHANÇA
sol_corrente, fo_corrente = sa.met_sa(sol_corrente, fo_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap_veic, pickup, demanda, ti, tc, tx, samax)

# DETERMINAÇÃO DO TEMPO CUMPUTACIONAL GASTO PARA A OBTENÇÃO DA SOLUÇÃO
fim = time.time()

# IMPRESSÃO DA SOLUÇÃO EMCONTRADA
print(sol_corrente)
print(fo_corrente)