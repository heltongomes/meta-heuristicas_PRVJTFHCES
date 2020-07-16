# Algortimo Simulated Annealing para PRVJTFHCES
# Data: 25/06/2019
# Última Atualização: 21/05/2020
# Autores: Aloísio Jr./Helton Gomes

from copy import deepcopy
import random
from numpy import exp
#from random import randint
import calcula_fo as CFO
import descida as MD

def met_sa(sol, fo, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap, pic, dem, ti, tf, fres, samax):
# método SA aplicado ao PRVJTFHCES
    # Passo Inicial
    temp_cor = ti
    fo_c = fo
    sol_c = deepcopy(sol)
    fo_best = fo
    sol_best = deepcopy(sol)

    # Passo iterativo
    while temp_cor > tf:
        iter = 0
        while iter < samax:
            iter += 1
            # gerar solução S vizinha a S'
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
     # atualiza melhor solução
    sol = deepcopy(sol_best)
    return sol_best, fo_best

def gera_vizinho(solucao):
# método utilizado para gerar um vizinho qualquer para uma solução
    N = len(solucao)
    # print(N)
    # Sorteia o primeiro elemento a ser trocado
    a = random.randint(0, N-1)
    # print("a=",a)
    while len(solucao[a]) == 0:
        a = random.randint(0, N - 1)
        # print(f"Novo valor de a ={a}")
    b = random.randint(0,len(solucao[a])-1)
    # print("b=",b)
    # print(f"Solucao[{a}][{b}] = {solucao[a][b]}")
    tmov = random.randint(1,2)
    # print(f"Tipo movimento = {tmov}")
    # Determina onde o elemento será alocado
    if tmov == 1:  # movimento de troca
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
            # print(f"Novo valor de c ={c}")
            if len(solucao[c]) == 0:
                condicao = True
            elif (c == a) and (len(solucao[a]) == 1):
                condicao = True
            else:
                condicao = False
        d = random.randint(0, len(solucao[c])-1)
        # print(f"d={d}")
        while solucao[a][b] == solucao[c][d]:
            d = random.randint(0, len(solucao[c]) - 1)
            # print(f"novo valor de d={d}")
        solucao[a][b], solucao[c][d] = solucao[c][d], solucao[a][b]
        # print(solucao)
    elif tmov == 2: # movimento de realocação
        # retira o elemento da lista
        elemento = solucao[a].pop(b)
        # print(solucao)
        # escolhe a nova posição para o elemento
        # essa posição deve ser diferente da inicial
        c = random.randint(0, N - 1) # sorteando o veículo
        # print(f"c={c}")
        if (a==c) and (len(solucao[a])==0):
            condicao = True
        else:
            condicao = False
        while condicao:
            c = random.randint(0, N - 1)
            # print(f"Novo valor de c ={c}")
            if (a == c) and (len(solucao[a]) == 0):
                condicao = True
            else:
                condicao = False
        d = random.randint(0,len(solucao[c]))
        # print(f"d={d}")
        if (a==c) and (b==d):
            condicao = True
        else:
            condicao = False
        while condicao:
            d = random.randint(0,len(solucao[c]))
            # print(f"Novo valor de d ={d}")
            if (a == c) and (b==d):
                condicao = True
            else:
                condicao = False
        solucao[c].insert(d, elemento)
        # print(solucao)
    #return solucao

    # Sorteia o segundo elemento a ser trocado

    #print(solucao[a][b])
    #elemento = solucao[a].pop(b) # remove item à partir do indice
    #print(solucao)
    #print(elemento)
    #solucao[4].insert(0, elemento)
    #print(solucao)
    #a = random.randint(0, N-1)
    #print(a)
    #a = random.randint(0, N-1)
    #print(a)
    #a = random.randint(0, N-1)
    #print(a)


