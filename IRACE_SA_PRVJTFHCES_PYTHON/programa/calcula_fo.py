# -*- coding: utf-8 -*-
"""
CALCULA VALOR DA FUNÇÃO OBJETIVO

@author: helton gomes
"""

def calc_fo(sol, cid, veic, c, d, ts, ti, tf, cap, pic, dem):
    
    fo = 0
    di = [] # INSTANTE DE INICIO DO ATENDIMENTO DOS CLIENTES
    di_aux = []
    alpha = 100 # PENALIDADE POR VIOLAÇÃO DA JANELA DE TEMPO
    beta = 100 # PENALIDADE POR VIOLAÇÃO DA CAPACIDADE DOS VEÍCULOS 
    
    # CALCULO DA DISTÂNCIA TOTAL (SOMATÓRIO) PERCORRIDA PELOS VEÍCULOS
    for i in range(veic):
        
        
        if len(sol[i]) > 0:
            fo += c[0][sol[i][0]]
            
            for j in range(len(sol[i]) - 1): 
                fo += c[sol[i][j]][sol[i][j+1]]
            
            fo += c[sol[i][len(sol[i])-1]][0]
            
    #print(fo)
    # DETERMINAÇÃO DAS "DATAS" INICIAIS DOS ATENDIMENTOS DAS CIDADES
    for i in range(veic):
        
        if len(sol[i]) > 0:
            
            for j in range(len(sol[i])):
                if j == 0:
                    di_aux.append(max(d[0][sol[i][j]], ti[sol[i][j]]))                
                else:
                    di_aux.append(max(di_aux[j-1] + ts[sol[i][j-1]] + d[sol[i][j-1]][sol[i][j]], ti[sol[i][j]]))
                    
        
        di.append(di_aux[:])
        di_aux.clear()
        
    #print(di)

    # VERIFICAÇÃO DO ATENDIMENTO DAS JANELAS DE TEMPO - PENALIZAÇÃO DA VIOLAÇÃO 
    for i in range(veic):
        for j in range(len(di[i])):
            
            #print(di[i][j])
            #print(ti[sol[i][j]])
            #input("Precione <enter> para continuar ...")
            
            if di[i][j] < ti[sol[i][j]]:
                fo += alpha*(abs(di[i][j] - ti[sol[i][j]]))
               
            elif di[i][j] > tf[sol[i][j]]:
                fo += alpha*(abs(di[i][j] - tf[sol[i][j]]))
                
    # VERIFICAÇÃO DO ATENDIMENTO DAS CAPACIDADES DOS VEÍCULOS - PENALIZAÇÃO DA VIOLAÇÃO
    
    # DETERMINAÇÃO DA QUANTIDADE DE ITESN A SEREM ENTREGUES E CADA ROTA (DEMANDAS DE ENTREGA)
    dem_entrega = [0]*veic
    for i in range(veic):
        if len(sol[i]) > 0:
            for j in range(len(sol[i])):
                dem_entrega[i] += dem[sol[i][j]]
                
    # VERIFICAÇÃO SE A CAPACIDADE DE CADA VEÍCULO É ULTRAPASSADA
    cap_ultra = [0]*veic
    for i in range(veic):
        if len(sol[i]) > 0:
            capacidade = dem_entrega[i]
            if capacidade > cap[i]:
                cap_ultra[i] += (capacidade-cap[i])
            for j in range(len(sol[i])):
                capacidade = capacidade - dem[sol[i][j]] + pic[sol[i][j]]
                if capacidade > cap[i]:
                    cap_ultra[i] += (capacidade - cap[i])
                    
    #print(cap_ultra)
    
    # PENALIZAÇÃO DA VIOLAÇÃO DAS CAPACIDADES DOS VEÍCULOS
    for i in range(veic):
        if cap_ultra[i] > 0:
            fo += cap_ultra[i]*beta

    return fo