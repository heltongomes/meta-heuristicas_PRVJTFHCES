# -*- coding: utf-8 -*-
"""
ESTRUTURAS DE VIZINHANÇA

@author: helton gomes
"""

# IMPORTAR BIBLIOTECA DEEPCOPY - USADO QUANDO TEMOS UMA LISTA DE LISTAS
from copy import deepcopy

import calcula_fo as CFO

def met_descida_interna(sol, fo, cid, veic, c, d, ts, ti, tf, cap, pic, dem):
    
    fo_viz = fo
    sol_viz = deepcopy(sol)
        
    fo_viz_melhor = fo
    sol_viz_melhor = deepcopy(sol)
    
    # ESTRUTURA DE VIZINHANÇA - TROCA DA ORDEM DE VISITAÇÃO DE DUAS CIDADES - MESMO VEÍCULO
    for i in range(veic):
        
         if len(sol_viz[i]) > 0:
             
             for j in range(len(sol_viz[i]) - 1):
                 for l in range(j + 1, len(sol_viz[i])):
                     
                     """"
                     aux = sol_viz[i][j]
                     sol_viz[i][j] = sol_viz[i][l]
                     sol_viz[i][l] = aux
                     """
                     
                     sol_viz[i][j], sol_viz[i][l] = sol_viz[i][l], sol_viz[i][j] 
                     
                     fo_viz = CFO.calc_fo(sol_viz, cid, veic, c, d, ts, ti, tf, cap, pic, dem)
                     
                     if fo_viz < fo_viz_melhor:
                         fo_viz_melhor = fo_viz
                         sol_viz_melhor = deepcopy(sol_viz)
                         
                     """    
                     aux = sol_viz[i][j]
                     sol_viz[i][j] = sol_viz[i][l]
                     sol_viz[i][l] = aux
                     """
                     
                     sol_viz[i][j], sol_viz[i][l] = sol_viz[i][l], sol_viz[i][j]
                     
                     #input("Precione <enter> para continuar ...")
    
    #print("Viz 1:", sol_viz_melhor, " - ", fo_viz_melhor)
    return sol_viz_melhor, fo_viz_melhor


def met_descida_interna2(sol, fo, cid, veic, c, d, ts, ti, tf, cap, pic, dem):
    
    fo_viz = fo
    sol_viz = deepcopy(sol)
        
    fo_viz_melhor = fo
    sol_viz_melhor = deepcopy(sol)
    
    # ESTRUTURA DE VIZINHANÇA - TROCA DA ORDEM DE VISITAÇÃO DE UMA CIDADE - MESMO VEÍCULO
    for i in range(veic):
        
         if len(sol_viz[i]) > 0:
             
             for j in range(len(sol_viz[i])):
                 for l in range(len(sol_viz[i])):
                     
                     if j != l:
                         
                         aux = sol_viz[i][j]
                         sol_viz[i].remove(aux)
                         sol_viz[i].insert(l, aux)
                     
                         fo_viz = CFO.calc_fo(sol_viz, cid, veic, c, d, ts, ti, tf, cap, pic, dem)
                     
                         if fo_viz < fo_viz_melhor:
                             fo_viz_melhor = fo_viz
                             sol_viz_melhor = deepcopy(sol_viz)
                             
                         sol_viz = deepcopy(sol)
                     
                     
                         #input("Precione <enter> para continuar ...")
    
    #print("Viz 2:", sol_viz_melhor, " - ", fo_viz_melhor)
    return sol_viz_melhor, fo_viz_melhor


def met_descida_externa(sol, fo, cid, veic, c, d, ts, ti, tf, cap, pic, dem):
    
    fo_viz = fo
    sol_viz = deepcopy(sol)
        
    fo_viz_melhor = fo
    sol_viz_melhor = deepcopy(sol)
    
    # ESTRUTURA DE VIZINHANÇA - TROCA DA ORDEM DE VISITAÇÃO DE DUAS CIDADES - VEÍCULOS DIFERENTES
    for i in range(veic):
        
        if len(sol_viz[i]) > 0:
            
            for j in range(veic):
                
                if (len(sol_viz[j]) > 0) and (i != j):
                    
                    for k in range(len(sol_viz[i])):
                        for l in range(len(sol_viz[j])):
                            
                            #print(sol_viz)
                            sol_viz[i][k], sol_viz[j][l] = sol_viz[j][l], sol_viz[i][k]
                            #print(sol_viz)
                            
                            fo_viz = CFO.calc_fo(sol_viz, cid, veic, c, d, ts, ti, tf, cap, pic, dem)
                            
                            if fo_viz < fo_viz_melhor:
                                fo_viz_melhor = fo_viz
                                sol_viz_melhor = deepcopy(sol_viz)
                            
                            #input("Precione <enter> para continuar ...")
                            sol_viz[i][k], sol_viz[j][l] = sol_viz[j][l], sol_viz[i][k]
                            
        
    return sol_viz_melhor, fo_viz_melhor

def met_descida_externa2(sol, fo, cid, veic, c, d, ts, ti, tf, cap, pic, dem):
    
    fo_viz = fo
    sol_viz = deepcopy(sol)
        
    fo_viz_melhor = fo
    sol_viz_melhor = deepcopy(sol)
    
    # ESTRUTURA DE VIZINHANÇA - TROCA DA ORDEM DE VISITAÇÃO DE UMA CIDADE - VEÍCULOS DIFERENTES
    for i in range(veic):
        
        if len(sol_viz[i]) > 0:
            
            for j in range(veic):
                
                if (len(sol_viz[j]) > 0) and (i != j):
                    
                    for k in range(len(sol_viz[i])):
                        for l in range(len(sol_viz[j]) + 1):
                            
                            #print(sol_viz)
                            aux = sol_viz[i][k]
                            sol_viz[i].remove(aux)
                            sol_viz[j].insert(l, aux)
                            #print(sol_viz)
                            
                            fo_viz = CFO.calc_fo(sol_viz, cid, veic, c, d, ts, ti, tf, cap, pic, dem)
                     
                            if fo_viz < fo_viz_melhor:
                                fo_viz_melhor = fo_viz
                                sol_viz_melhor = deepcopy(sol_viz)
                    
                            #input("Precione <enter> para continuar ...")
                            
                            sol_viz = deepcopy(sol)
        
    return sol_viz_melhor, fo_viz_melhor