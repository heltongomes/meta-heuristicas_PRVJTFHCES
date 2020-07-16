# -*- coding: utf-8 -*-
"""
VNS

@author: helton gomes
"""

from copy import deepcopy

import calcula_fo as CFO
import descida as MD

def met_vns(sol_corrente, fo_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap, pic, dem, r):
    
    k = 1
    
    while k <= r: 
    
        if k == 1:
            #sol_viz.clear()
            sol_viz, fo_viz = MD.met_descida_interna(sol_corrente, fo_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap, pic, dem)

            #print("k =", k, "Solução Vizinha:", sol_viz)
            #print("FO Vizinha:", fo_viz)
        
            if fo_viz < fo_corrente:
                fo_corrente = fo_viz
                sol_corrente = deepcopy(sol_viz)
            
                k = 1
            else:
                k += 1
            
        elif k == 2:
            #sol_viz.clear()
            sol_viz, fo_viz = MD.met_descida_interna2(sol_corrente, fo_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap, pic, dem)

            #print("k =", k, "Solução Vizinha:", sol_viz)
            #print("FO Vizinha:", fo_viz)
        
            if fo_viz < fo_corrente:
                fo_corrente = fo_viz
                sol_corrente = deepcopy(sol_viz)
            
                k = 1
            else:
                k += 1
                
        elif k == 3:
            #sol_viz.clear()
            sol_viz, fo_viz = MD.met_descida_externa(sol_corrente, fo_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap, pic, dem)

            #print("k =", k, "Solução Vizinha:", sol_viz)
            #print("FO Vizinha:", fo_viz)
        
            if fo_viz < fo_corrente:
                fo_corrente = fo_viz
                sol_corrente = deepcopy(sol_viz)
            
                k = 1
            else:
                k += 1
        
        elif k == 4:
            #sol_viz.clear()
            sol_viz, fo_viz = MD.met_descida_externa2(sol_corrente, fo_corrente, qtd_cid, qtd_veic, custo, dist, t_serv, t_ini, t_fim, cap, pic, dem)

            #print("k =", k, "Solução Vizinha:", sol_viz)
            #print("FO Vizinha:", fo_viz)
        
            if fo_viz < fo_corrente:
                fo_corrente = fo_viz
                sol_corrente = deepcopy(sol_viz)
            
                k = 1
            else:
                k += 1
            
    return sol_corrente, fo_corrente
    
    
