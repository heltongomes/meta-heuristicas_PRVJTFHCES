# -*- coding: utf-8 -*-
"""
ESTRUTURAS DE VIZINHANÇA

@author: Helton Gomes
"""

# IMPORTANDO BIBLIOTECA
from copy import deepcopy

# IMPORTANDO FUNÇÕES
import calcula_fo as CFO

def met_descida_interna(sol, fo, cid, veic, c, d, ts, ti, tf, cap, pic, dem):
    
    fo_viz = fo
    sol_viz = deepcopy(sol)
        
    fo_viz_melhor = fo
    sol_viz_melhor = deepcopy(sol)
    
    # ESTRUTURA DE VIZINHANÇA - TROCA DA ORDEM DE VISITAÇÃO DE DOIS CLIENTES - MESMO VEÍCULO
    for i in range(veic):
        
         if len(sol_viz[i]) > 0:
             
             for j in range(len(sol_viz[i]) - 1):
                 for l in range(j + 1, len(sol_viz[i])):
                     
                     sol_viz[i][j], sol_viz[i][l] = sol_viz[i][l], sol_viz[i][j] 
                     
                     fo_viz = CFO.calc_fo(sol_viz, cid, veic, c, d, ts, ti, tf, cap, pic, dem)
                     
                     if fo_viz < fo_viz_melhor:
                         fo_viz_melhor = fo_viz
                         sol_viz_melhor = deepcopy(sol_viz)
                     
                     sol_viz[i][j], sol_viz[i][l] = sol_viz[i][l], sol_viz[i][j]
    
    return sol_viz_melhor, fo_viz_melhor


def met_descida_interna2(sol, fo, cid, veic, c, d, ts, ti, tf, cap, pic, dem):
    
    fo_viz = fo
    sol_viz = deepcopy(sol)
        
    fo_viz_melhor = fo
    sol_viz_melhor = deepcopy(sol)
    
    # ESTRUTURA DE VIZINHANÇA - TROCA DA ORDEM DE VISITAÇÃO DE UM CLIENTE - MESMO VEÍCULO
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
    
    return sol_viz_melhor, fo_viz_melhor


def met_descida_externa(sol, fo, cid, veic, c, d, ts, ti, tf, cap, pic, dem):
    
    fo_viz = fo
    sol_viz = deepcopy(sol)
        
    fo_viz_melhor = fo
    sol_viz_melhor = deepcopy(sol)
    
    # ESTRUTURA DE VIZINHANÇA - TROCA DA ORDEM DE VISITAÇÃO DE DOIS CLIENTES - VEÍCULOS DIFERENTES
    for i in range(veic):
        
        if len(sol_viz[i]) > 0:
            
            for j in range(veic):
                
                if (len(sol_viz[j]) > 0) and (i != j):
                    
                    for k in range(len(sol_viz[i])):
                        for l in range(len(sol_viz[j])):
                    
                            sol_viz[i][k], sol_viz[j][l] = sol_viz[j][l], sol_viz[i][k]
                            
                            fo_viz = CFO.calc_fo(sol_viz, cid, veic, c, d, ts, ti, tf, cap, pic, dem)
                            
                            if fo_viz < fo_viz_melhor:
                                fo_viz_melhor = fo_viz
                                sol_viz_melhor = deepcopy(sol_viz)
                            
                            sol_viz[i][k], sol_viz[j][l] = sol_viz[j][l], sol_viz[i][k]
                               
    return sol_viz_melhor, fo_viz_melhor

def met_descida_externa2(sol, fo, cid, veic, c, d, ts, ti, tf, cap, pic, dem):
    
    fo_viz = fo
    sol_viz = deepcopy(sol)
        
    fo_viz_melhor = fo
    sol_viz_melhor = deepcopy(sol)
    
    # ESTRUTURA DE VIZINHANÇA - TROCA DA ORDEM DE VISITAÇÃO DE UM CLIENTE - VEÍCULOS DIFERENTES
    for i in range(veic):
        
        if len(sol_viz[i]) > 0:
            
            for j in range(veic):
                
                if (len(sol_viz[j]) > 0) and (i != j):
                    
                    for k in range(len(sol_viz[i])):
                        for l in range(len(sol_viz[j]) + 1):
                            
                            aux = sol_viz[i][k]
                            sol_viz[i].remove(aux)
                            sol_viz[j].insert(l, aux)
                            
                            fo_viz = CFO.calc_fo(sol_viz, cid, veic, c, d, ts, ti, tf, cap, pic, dem)
                     
                            if fo_viz < fo_viz_melhor:
                                fo_viz_melhor = fo_viz
                                sol_viz_melhor = deepcopy(sol_viz)
                            
                            sol_viz = deepcopy(sol)
        
    return sol_viz_melhor, fo_viz_melhor