# -*- coding: utf-8 -*-
"""
GERA SOLUÇÃO INICIAL

@author: helton gomes
"""

import random
import time

time.process_time

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
        
    #print('Capcidade Restante:', cap_rest)
    #print(cap_rest.index(max(cap_rest)))
    #print('Lista C: ', lista_C)
    #print(len(lista_C))
    
    # CASO ALGUMA CIDADE NA SEJA COLOCADA NA SOLUÇÃO, ELA É INSERIDA NA ROTA CUJO VEICULO TEM MAIOR
    # CAPACIDADE RESTANTE
    
    #if len(lista_C) != 0:
    while len(lista_C) != 0:
        for i in lista_C:
            x = cap_rest.index(max(cap_rest))
            sol[x].append(i)
            cap_rest[x] = cap_rest[x] - max(dem[i], pic[i])
            lista_C.remove(i)
    
    #print('Capcidade Restante:', cap_rest)
             
    #print('Lista C: ', lista_C)
    #print(len(lista_C))
               
    return sol
    