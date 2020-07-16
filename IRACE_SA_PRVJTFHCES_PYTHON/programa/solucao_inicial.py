# -*- coding: utf-8 -*-
"""
GERA SOLUÇÃO INICIAL PARA O PRVJTFHCES

@author: Helton Gomes
"""

# IMPORTANDO BIBLIOTECAS
import random
import time

time.process_time

# FUNÇÃO PARA A DETERMINAÇÃO DE UMA SOLUÇÃO INICIAL PARA O PRVJTFHCES
def sol_ini(cid, veic, cap, pic, dem):
    
    sol = []
    lista_C = []
    lista_aux = []
    lista_veic = []
    cap_rest = []    
    
    for i in range(1, cid+1):
        lista_C.append(i)
    
    for i in range(veic):
        cap_rest.append(cap[i])
    
    
    for i in range(veic):
        
        lista_veic.clear()
        
        for j in lista_C:
            if (cap_rest[i] - max(dem[j], pic[j])) >= 0:
                lista_aux.append(j)
        
        while len(lista_aux) > 0:
            
            x = random.choice(lista_aux)
            
            lista_veic.append(x)
            lista_aux.remove(x)
            lista_C.remove(x)
            
            cap_rest[i] = cap_rest[i] - max(dem[x], pic[x])
            
            lista_aux.clear()
            
            for j in lista_C:
                if cap_rest[i] - max(dem[j], pic[j]) >= 0:
                    lista_aux.append(j)
                   
        lista_aux.clear()
        sol.append(lista_veic[:])
        
    # TESTANDO A CAPACIDADE RESTANTE
    while len(lista_C) != 0:
        for i in lista_C:
            x = cap_rest.index(max(cap_rest))
            sol[x].append(i)
            cap_rest[x] = cap_rest[x] - max(dem[i], pic[i])
            lista_C.remove(i)
               
    return sol