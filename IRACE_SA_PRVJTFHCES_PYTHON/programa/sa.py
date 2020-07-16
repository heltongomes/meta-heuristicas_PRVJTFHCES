# -*- coding: utf-8 -*-
"""
SIMULATED ANNEALING PARA O PRVJTFHCES

@author: Helton Gomes
"""

# IMPORTANDO BIBLIOTECAS
from copy import deepcopy
import random
from numpy import exp
import calcula_fo as CFO
import descida as MD

# META-HEURÍSTICA SIMULATED ANNEALING
def met_sa(sol, fo, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap, pic, dem, ti, tf, fres, samax):
    # Passo Inicial
    temp_cor = ti
    fo_c = fo
    sol_c = deepcopy(sol)
    fo_best = fo
    sol_best = deepcopy(sol)

    # PASSO ITERATIVO
    while temp_cor > tf:
        iter = 0
        while iter < samax:
            iter += 1

            # GERAÇÃO DE UMA SOLUÇÃO s VIZINHA DE s'
            nova_sol = deepcopy(sol_c)
            gera_vizinho(nova_sol)
            fo_nova = CFO.calc_fo(nova_sol, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap, pic, dem)
            delta = fo_nova - fo_c
            if delta < 0:
                fo_c = fo_nova
                sol_c = deepcopy(nova_sol)
                if fo_c < fo_best:
                    fo_best = fo_c
                    sol_best = deepcopy(sol_c)
            else:
                x = random.random()
                if x < exp(-delta/temp_cor):
                    fo_c = fo_nova
                    sol_c = deepcopy(nova_sol)
        temp_cor *= fres

     # ATUALIZAÇÃO DA MELHOR SOLUÇÃO
    sol = deepcopy(sol_best)
    return sol_best, fo_best

# MÉTODO PARA GERAR UM VIZINHO QUALQUER DE UMA SOLUÇÃO
def gera_vizinho(solucao):
    N = len(solucao)
    
    # SORTEIA O PRIMEIRO ELEMENTO A SER TROCADO
    a = random.randint(0, N-1)
    
    while len(solucao[a]) == 0:
        a = random.randint(0, N - 1)
        
    b = random.randint(0,len(solucao[a])-1)
    
    tmov = random.randint(1,2)
    
    # DETERMINA ONDE O ELEMENTO SERÁ ALOCADO
    if tmov == 1:  # MOVIMENTO DE TROCA
        c = random.randint(0, N-1)
        # print(f"c={c}")
        if len(solucao[c]) == 0:
            condicao = True
        elif (c == a) and (len(solucao[a]) == 1):
            condicao = True
        else:
            condicao = False
        while condicao:
            c = random.randint(0, N - 1)

            if len(solucao[c]) == 0:
                condicao = True
            elif (c == a) and (len(solucao[a]) == 1):
                condicao = True
            else:
                condicao = False
        d = random.randint(0, len(solucao[c])-1)

        while solucao[a][b] == solucao[c][d]:
            d = random.randint(0, len(solucao[c]) - 1)

        solucao[a][b], solucao[c][d] = solucao[c][d], solucao[a][b]

    elif tmov == 2: # MOVIMENTO DE REALOCAÇÃO
        # RETIRA O ELEMENTO DA LISTA
        elemento = solucao[a].pop(b)
        
        # ESCOLHE A NOVA POSIÇÃO PARA O ELEMENTO (ESSA POSIÇÃO DEVE SER DIFERENTE DA INICIAL)
        c = random.randint(0, N - 1) # SORTEANDO O VEÍCULO
        
        if (a==c) and (len(solucao[a])==0):
            condicao = True
        else:
            condicao = False
        while condicao:
            c = random.randint(0, N - 1)
            
            if (a == c) and (len(solucao[a]) == 0):
                condicao = True
            else:
                condicao = False
        d = random.randint(0,len(solucao[c]))
        
        if (a==c) and (b==d):
            condicao = True
        else:
            condicao = False
        while condicao:
            d = random.randint(0,len(solucao[c]))
            
            if (a == c) and (b==d):
                condicao = True
            else:
                condicao = False
        solucao[c].insert(d, elemento)